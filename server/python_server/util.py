import boto3
from boto3.dynamodb.conditions import Key, Attr

def reset_all_tables(ddb):
    delete_tables(ddb)
    create_relative_table(ddb)
    create_relation_table(ddb)

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