import json


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

    def set_modifiers(self,modifiers):
        self.modifiers=modifiers

    def add_attribute(self, type):
        self.attributes.add(type)

    def add_neighbor(self, vertex):
        self.neighbors.add(vertex)

    def toJson(self) -> json:
        j = {}
        j["key"] = self.key
        j["type"] = self.type
        j["name"] = self.name
        j["modifiers"] = self.modifiers
        j["attributes"] = self.attributes

    def __str__(self):
        neighbors = []
        if self.neighbors:
            for neighbor in self.neighbors:
                neighbors.append(neighbor.name)
        if len(self.attributes) > 0:
            return "[key:{}, type:{}, name:{}, attributes:{}, neighbors:{}]".format(self.key, self.type, self.name, self.attributes, neighbors)
        return "[key:{}, type:{}, name:{}]".format(self.key, self.type, self.name, neighbors)
