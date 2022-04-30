import string
from Graph.edge import Edge
from Graph.graph import Graph
from Graph.vertex import Vertex, VertexTypeEnum


class GraphFromQuery(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.classes_names: dict = {}  # name:vertex
        self.methods_names: dict = {}  # name:vertex
        self.interfaces_names: dict = {}  # name:vertex
        self.key = -1

    def get_key(self)->int:
        self.key += 1
        return self.key


    def add_edge(self, type: VertexTypeEnum, source_key: int, dest_key: int):
        edge = Edge(source_key, dest_key, type)
        super().add_edge(edge)

    def add_vertex(self, name :string, type: VertexTypeEnum):
        if(type == VertexTypeEnum.CLASS):
            return self.add_class(name)
        if(type==VertexTypeEnum.METHOD): return self.add_method(name)
        if(type == VertexTypeEnum.INTERFACE): return self.add_interface(name)

    def add_class(self, name: string) -> Vertex:
        vertex_key = self.classes_names.get(name)
        if vertex_key != None:
            return super().get_vertex(vertex_key)

        vertex = Vertex(self.get_key(), name, VertexTypeEnum.CLASS)
        super().add_vertex(vertex)
        self.classes_names[name] = vertex.key
        return vertex

    def add_method(self, name) -> Vertex:
        vertex_key = self.methods_names.get(name)
        if vertex_key != None:
            return super().get_vertex(vertex_key)

        vertex = Vertex(self.get_key(), name, VertexTypeEnum.METHOD)
        super().add_vertex(vertex)
        self.methods_names[name] = vertex.key
        return vertex

    def add_interface(self, name: string) -> Vertex:
        vertex_key = self.interfaces_names.get(name)
        if vertex_key != None:
            return super().get_vertex(vertex_key)

        vertex = Vertex(self.get_key(), name, VertexTypeEnum.INTERFACE)
        super().add_vertex(vertex)
        self.interfaces_names[name] = vertex.key
        return vertex
