import string
from Parser.tokenizer import Tokenizer


class Vertex:
    def __init__(self, key:int, name:string, type:string, attributes:list=[]):
        self.key :int = key
        self.name :string = name
        self.type :string = type
        self.attributes :list = attributes
        self.edges :dict = {}
        self.neighbors :set = set()
        self.tokens = Tokenizer(name).tokens #added the tokens here for time complexity consideration

    def add_edge(self, edge) -> None:
        self.edges[edge.to.key] = edge
        self.neighbors.add(edge.to)


    def __str__(self):
        return "[key:{}, name:{}, type:{}, attributes:{}, tokens:{}]".format(self.key, self.name, self.type, self.attributes, self.tokens)
