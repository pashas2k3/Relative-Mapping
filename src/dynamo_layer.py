import boto3
from boto3.dynamodb.conditions import Key, Attr
from relative import Relative
from relation import Relation
import unittest

def get_ddb():
    return boto3.resource('dynamodb', endpoint_url="http://localhost:8000", region_name='us-west-2')


def get_table(table_name):
    return get_ddb().Table(table_name)


def get_relative_table():
    return get_table('relative')


def get_relation_table():
    return get_table('relation')


# Assuming no pagination
# We need GSIs over the name and DOB
def get_relative_by_name(name):
    response = get_relative_table().scan(FilterExpression=Attr('name').contains(name))
    items = response['Items']
    if items:
        return [Relative.from_dict(item) for item in items]
    return None


def get_relative_by_id(id):
    response = get_relative_table().get_item(Key={'id': id})
    items = response['Item']
    if items:
        return [Relative.from_dict(item) for item in items]
    return None


def get_relatives(relative_id):
    response = get_relation_table().query(KeyConditionExpression=Key('src').eq(relative_id))
    relatives = {}

    # There can be only one direct relation
    # 1. Parent (Biological)
    # 2. Spouse
    for item in response['Items']:
        relatives[item['dest']] = item['relation']

    return relatives


def add_relative(relative):
    get_relative_table().put_item(
        Item=relative.asdict(),
        ConditionExpression='attribute_not_exists(id)')


def add_relation(relation):
    get_relation_table().put_item(
        Item=relation.asdict(),
        ConditionExpression='attribute_not_exists(src)')


if __name__ == '__main__':
    def create_relation_table(ddb):
        print('creating relation table ')
        ddb.create_table(TableName='relation', KeySchema=[{
            'AttributeName': 'src',
            'KeyType': 'HASH'
        }, {
            'AttributeName': 'dest',
            'KeyType': 'RANGE'
        }], AttributeDefinitions=[
            {
                'AttributeName': 'src',
                'AttributeType': 'S'
            }, {
                'AttributeName': 'dest',
                'AttributeType': 'S'
            }
        ], ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10})

    def create_relative_table(ddb):
        print('creating relative table ')
        ddb.create_table(TableName='relative', KeySchema=[{
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }], AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            }
        ], ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10})

    def delete_tables(ddb):
        print('deleting All tables ')
        for table in ddb.tables.all():
            table.delete()

    def relative_equality(one, other):
        return one.id == other.id and one.gender == other.gender \
               and one.nickname == other.nickname \
               and one.dob == other.dob and one.name == other.name

    # Create a relatives and relation table
    ddb = get_ddb()
    delete_tables(ddb)
    create_relative_table(ddb)
    create_relation_table(ddb)

    test = unittest.TestCase()

    # Add a relative
    write_relative = Relative('John Doe', '2016-01-01', 'Joe', 'male')
    add_relative(write_relative)

    # Read the relative back
    read_relative = get_relative_by_name(write_relative.name)[0]

    test.assertTrue(relative_equality(write_relative, read_relative))
    child = read_relative.id

    relative = Relative('Jane Doe', '1980-12-31', 'Jane', 'male')
    add_relative(relative)
    mother = relative.id

    # Add a relation
    add_relation(Relation(child, 'CHILD', mother, '2016-01-01'))
    add_relation(Relation(mother, 'PARENT', child, '2016-04-27'))

    # Get relation and verify
    child_relation = get_relatives(child)
    test.assertEqual(child_relation[mother], 'CHILD')
