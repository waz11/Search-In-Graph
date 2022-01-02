import string


class Vertex:
    def __init__(self, key:int, name:string, type:string, attributes:list=[]):
        self.key :int = key
        self.name :string = name
        self.type :string = type
        self.attributes :list = attributes
        self.edges :dict = {}
        self.neighbors :set = set()

    def add_edge(self, edge):
        self.edges[edge.to.key] = edge
        self.neighbors.add(edge.to)


    def __str__(self):
        return "[key:{}, name:{}, type:{}, attributes:{}]".format(self.key, self.name, self.type, self.attributes)
