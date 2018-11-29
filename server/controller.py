from dynamo_layer import get_relative_by_name, get_relative_by_id, get_relatives
from pathFinder import Graph
from relation import Relation

def find_relation(src, dest):
    graph = Graph()
    def loader(curr):
        # Intentionally load only current node and only one direction of edge
        # nodes absent from graph is trigger for loading the node in graph and
        # its neighbors
        graph.add_node(curr)
        for relative, relation in get_relatives(curr):
            graph.add_edge(curr, relative, Relation.get_distance(relation))

    # We need relation along with the path of relatives
    return Graph.dijkstra(graph, src, dest, loader)


def get_relative_info(name):
    return map(lambda r: r.asdict_attr(), get_relative_by_name(name))

# TODO
def add_relative_info():
    pass


if __name__=="__main__":
    pass