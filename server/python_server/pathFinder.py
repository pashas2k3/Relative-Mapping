from collections import defaultdict
from heapq import heappush, heappop
from functools import reduce
import unittest


class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}
        self.relation = {}

    def add_node(self, id):
        self.nodes.add(id)

    def add_edge(self, from_id, to_id, distance, relation):
        self.edges[from_id].append(to_id)
        self.distances[(from_id, to_id)] = distance
        self.relation[(from_id, to_id)] = relation

    @classmethod
    def dijkstra(cls, graph, first, last, node_loader):
        queue = [(0, first, (), ())]
        visited = set()
        dist = {first: 0}

        while queue:
            (cost, src, path, relation) = heappop(queue)

            if src in visited:
                continue

            if src not in graph.nodes:
                node_loader(src)

            visited.add(src)
            path += (src,)

            # If at destination node and all its neighbors have been visited
            if src == last and reduce(lambda f, n: (n in visited) and f, graph.edges[src]):
                return path, relation

            # Look at all the neighbors of current node
            for dest in graph.edges[src]:
                if dest in visited:
                    continue
                # Update distance if not already in dist with smaller distance to node
                if dest not in dist or cost + graph.distances[(src, dest)] < dist[dest]:
                    dist[dest] = cost + graph.distances[(src, dest)]
                    relation += (graph.relation[(src, dest)],)
                    heappush(queue, (dist[dest], dest, path, relation))
        return (),()

# Enter the userId for multiple different user
if __name__ == '__main__':
    '''
    1 -- 2 ----5--6
    +----3   +-4
    '''
    graph = Graph()
    for num in range(6):
        graph.add_node(num+1)

    graph.add_edge(1, 2, 1, 'parent')
    graph.add_edge(2, 1, 1, 'child')
    graph.add_edge(1, 3, 1, 'parent')
    graph.add_edge(3, 1, 1, 'child')
    graph.add_edge(2, 4, 1, 'parent')
    graph.add_edge(4, 2, 1, 'child')
    graph.add_edge(2, 5, 1, 'parent')
    graph.add_edge(5, 2, 1, 'child')
    graph.add_edge(5, 6, 1, 'parent')
    graph.add_edge(6, 5, 1, 'parent')

    test = unittest.TestCase()

    def noop():
        pass
    p, r = Graph.dijkstra(graph, 3, 6, noop)
    print(r)
    test.assertEqual((3, 1, 2, 5, 6), p)

    p, r = Graph.dijkstra(graph, 3, 3, noop)
    print(r)
    test.assertEqual((3,), p)
