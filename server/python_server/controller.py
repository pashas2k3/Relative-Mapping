from dynamo_layer import get_relative_by_name, get_relatives, add_relative, add_relation
from pathFinder import Graph
from relation import Relation
from relative import Relative
from util import reset_all_tables


def find_relation(param):
    src = param.src
    dest = param.dest
    graph = Graph()

    def loader(curr):
        # Intentionally load only current node and only one direction of edge
        # nodes absent from graph is trigger for loading the node in graph and
        # its neighbors
        graph.add_node(curr)
        for relative, relation in get_relatives(curr).items():
            graph.add_edge(curr, relative, Relation.get_distance(relation), relation)

    # We need relation along with the path of relatives
    return Graph.dijkstra(graph, src, dest, loader)


def get_relative_info(name):
    return map(lambda r: r.asdict_attr(), get_relative_by_name(name))

def add_individual(d):
    add_relative(Relative.from_dict(d))


def make_relation(d):
    r = Relation.from_dict(d)
    # Add relationship from both sides
    add_relation(r)
    add_relation(r.flip_relation())


if __name__=="__main__":
    from dynamo_layer import get_ddb, get_relative_by_id
    import unittest

    reset_all_tables(get_ddb())
    grandfather = Relative("Prescott Sheldon Bush", "05-15-1895", "Bush1m", "male")
    grandmother = Relative("Dorothy Walker", "07-01-1901", "Bush1f", "female")
    father = Relative("George Henry Walker Bush", "06-12-1924", "George Senior", "male")
    mother = Relative("Barbara Pierce", "06-08-1925", "Barbara", "female")
    aunt = Relative("Nancy Walker Bush", "02-04-1926", "Nancy", "female")
    uncle = Relative("William Henry Trotter Bush", "07-04-1938", "Bill", "male")
    child1 = Relative("George Walker Bush", "07-06-1946", "George", "male")
    child2 = Relative("Jeb Bush", "02-11-1953", "Jeb", "male")

    add_relative(grandfather); add_relative(grandmother); add_relative(father); add_relative(mother)
    add_relative(aunt); add_relative(uncle); add_relative(child1); add_relative(child2)

    # Since - each child can be child of 2 people but the two may not be associated any more, so better
    # The front end should send both requests for relation -> mother - child, father- child
    # Spousal relationship - should have entry for duration of marriage
    # Relative info should have field to update
    def get_relation_dict(src, dest, relation, date):
        return {'src': src.id, 'relation': relation, 'dest': dest.id, 'event_date': date}

    make_relation(get_relation_dict(grandmother, grandfather, 'SPOUSE', '08-06-1920'))
    make_relation(get_relation_dict(father, mother, 'SPOUSE', '01-06-1945'))
    make_relation(get_relation_dict(father, grandfather, 'PARENT', father.dob))
    make_relation(get_relation_dict(father, grandmother, 'PARENT', father.dob))
    make_relation(get_relation_dict(aunt, grandfather, 'CHILD', aunt.dob))
    make_relation(get_relation_dict(aunt, grandmother, 'CHILD', aunt.dob))
    make_relation(get_relation_dict(uncle, grandmother, 'CHILD', aunt.dob))
    make_relation(get_relation_dict(uncle, grandfather, 'CHILD', aunt.dob))
    make_relation(get_relation_dict(child1, father, 'CHILD', child1.dob))
    make_relation(get_relation_dict(child1, mother, 'CHILD', child1.dob))
    make_relation(get_relation_dict(child2, mother, 'CHILD', child2.dob))

    testCase = unittest.TestCase()

    def print_relation(path, relation, src, dest):
        print ('Relation between ' + src.name + ' and ' + dest.name)
        for relative, relation in zip(path, relation):
            print(get_relative_by_id(relative).name + '- is ' + relation + ' of ->')
        print(dest.name)

    path, relation = find_relation({'src':child1.id, 'dest':child2.id})
    testCase.assertEqual(relation, ('CHILD', 'PARENT'))
    print_relation(path, relation, child1, child2)

    path, relation = find_relation({'src':child2.id, 'dest':uncle.id})
    testCase.assertEqual(relation, ('CHILD', 'SPOUSE', 'PARENT', 'PARENT'))
    print_relation(path, relation, child2, uncle)
