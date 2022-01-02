import string

from Graph.vertex import Vertex
from Ranker.similarity import sim_edges


class Edge:
    def __init__(self, type, source:Vertex, to:Vertex):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)
