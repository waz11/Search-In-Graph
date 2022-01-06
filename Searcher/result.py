from Graph.graph import Graph
from Graph.vertex import Vertex


class Result:

    def __init__(self):
        self.graph = Graph()
        self.rank = 0.0

    def add_vertex(self, vertex:Vertex, rank):
        self.graph.add_vertex(vertex)
        self.rank += rank

    def add_edge(self, edge):
        self.graph.add_edge()

    def get_rank(self):
        return self.rank

    def __str__(self):
        s = ''
        for vertex in self.graph.get_vertices():
            s+=str(vertex)+' '
        return s
        # return str(self.graph.get_vertices())


def main():
    res = Result()
    res.get_rank()
    res.add_vertex(Vertex(1,'v1',''))
    res.add_vertex(Vertex(2, 'v2', ''))
    print(res)


if __name__ == '__main__':
    main()

