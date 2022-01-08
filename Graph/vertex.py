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

    def set_modifiers(self,modifiers):
        self.modifiers=modifiers

    def add_attribute(self, type):
        self.attributes.add(type)

    def add_neighbor(self, vertex):
        self.neighbors.add(vertex)

    def toJson(self) -> json:
        json = {}
        json["key"] = self.key
        json["type"] = self.type
        json["name"] = self.name
        # json["modifiers"] = self.modifiers
        json["attributes"] = []
        if len(self.attributes) > 0:
            json["attributes"] = self.attributes
        return json

    def __str__(self):
        neighbors = []
        if self.neighbors:
            for neighbor in self.neighbors:
                neighbors.append(neighbor.name)
        if len(self.attributes) > 0:
            return "[key:{}, type:{}, name:{}, attributes:{}, neighbors:{}]".format(self.key, self.type, self.name, self.attributes, neighbors)
        return "[key:{}, type:{}, name:{}]".format(self.key, self.type, self.name, neighbors)
