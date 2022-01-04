from Graph.graph import Graph


class Result:

    def __init__(self, graph:Graph, rank=0.0):
        self.graph = graph
        self.rank = rank

    def inc_rank(self, n):
        self.rank += n

