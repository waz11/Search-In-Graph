import string
from Graph.vertex import Vertex


class Edge:
    def __init__(self, type, source:Vertex, to:Vertex):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def toJson(self):
        j = {}
        j["type"] = self.type
        j["from"] = self.source.key
        j["to"] = self.to.key
        return j

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)
