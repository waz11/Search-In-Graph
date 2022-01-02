import string

from Ranker.similarity import sim_edges
from graph.vertex import Vertex


class Edge:
    def __init__(self, type, source, to):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def sim(self, other_edge):
        return sim_edges(self, other_edge)

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)
