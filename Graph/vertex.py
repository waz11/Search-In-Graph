import string
from Ranker.similarity import sim_vertics
from Parser.tokenizer import Tokenizer


class Vertex:
    def __init__(self, key:int, name:string, type:string, attributes:list=[]):
        self.key :int = key
        self.name :string = name
        self.type :string = type
        self.attributes :list = attributes
        self.edges :dict = {}
        self.neighbors :set = set()
        self.labels = Tokenizer(name).synonyms

    def add_edge(self, edge):
        self.edges[edge.to] = edge
        self.neighbors.add(edge.to)

    def get_neighbors(self):
        return self.neighbors

    def sim(self, other_vertex):
        return sim_vertics(self.tokens, other_vertex.tokens)

    def __str__(self):
        return "[key:{}, name:{}, type:{}, attributes:{}, labels:{}]".format(self.key, self.name, self.type, self.attributes, self.labels)
