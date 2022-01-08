import json
import string
from Graph.vertex import Vertex

class Edge():

    def __init__(self, source:Vertex, to:Vertex, type):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def toJson(self) -> json:
        json = {}
        json["type"] = self.type
        json["from"] = self.source.key
        json["to"] = self.to.key
        return json

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)