from Graph.graph import Graph
from Graph.vertex import Vertex


class Result:

    def __init__(self, graph=Graph()):
        self.graph = graph
        self.rank = 0.0

    def add_vertex(self, vertex:Vertex, rank):
        self.graph.add_vertex(vertex)
        self.rank += rank

    def get_rank(self):
        return self.rank

    def __str__(self):
        str = ''
        for vertex in self.graph.get_vertices():
            str+=vertex.name+' '
        return str


def main():
    res = Result()
    res.get_rank()
    res.add_vertex(Vertex(1,'v1',''))
    res.add_vertex(Vertex(2, 'v2', ''))
    print(res)


if __name__ == '__main__':
    main()

