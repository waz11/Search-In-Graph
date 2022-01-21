import string
from Parser.old_version.Graph.vertex import Vertex


class Edge:
    def __init__(self, type, source:Vertex, to:Vertex):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to
