import json
from Parser.tokenizer import Tokenizer


class Vertex:

    def __init__(self,key:int, name, type, attributes=[], modifiers=[]):
        self.key = key
        self.type = type
        if 'abstract' in modifiers:
            self.type = 'abstract'
        self.name = name
        self.modifiers = []
        self.attributes = set()
        for att in attributes:
            self.attributes.add(att)
        self.neighbors = set()
        self.tokens = Tokenizer().get_tokens(name)

    def set_modifiers(self,modifiers)->None:
        self.modifiers=modifiers

    def add_attribute(self, type)->None:
        self.attributes.add(type)

    def add_neighbor(self, vertex)->None:
        self.neighbors.add(vertex)

    def toJson(self)->json:
        json = {}
        json["key"] = self.key
        json["type"] = self.type
        json["name"] = self.name
        # json["modifiers"] = self.modifiers
        json["attributes"] = list(self.attributes)
        return json

    def __str__(self):
        neighbors = []
        if self.neighbors:
            for neighbor in self.neighbors:
                neighbors.append(neighbor.name)
        return "[{},{},{}]".format(self.key, self.type, self.name)
