import json
import string
from Graph.vertex import Vertex

class Edge():
    def __init__(self, type, source:Vertex, to:Vertex):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def toJson(self):
        json = {}
        json["type"] = self.type
        json["from"] = self.source.key
        json["to"] = self.to.key
        return json

    def __str__(self):
        return "({},{}):{}".format(self.source.key, self.to.key, self.type)


def main():
    v1 = Vertex(1,'','')
    v2 = Vertex(2, '', '')
    e = Edge('',v1,v2)
    print(e)

if __name__ == '__main__':
    main()
