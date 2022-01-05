from Graph.graph import Graph
from Graph.vertex import Vertex


class Result:

    def __init__(self, graph=Graph(), rank=0.0):
        self.graph = graph
        self.rank = rank

    def add_vertex(self, vertex:Vertex, rank=0):
        self.graph.add_vertex(vertex)
        self.rank += rank

    def increase_rank(self, n):
        self.rank += n

    def get_rank(self):
        rank = 0
        if self.graph.num_of_vertices() > 0:
            rank = self.rank / self.graph.num_of_vertices()
        return rank

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

