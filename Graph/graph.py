import string
import json
from Graph.edge import Edge
from Graph.vertex import Vertex
import networkx as nx
from matplotlib import pyplot as plt

from Utils.json_functions import list_to_json, save_json_to_file
from main import src1_path


class Graph:
    def __init__(self):
        self.vertices :dict = {}            # key:vertex
        self.edges :dict = {}               # key,key:edge
        self.classes_names :dict = {}       # name:vertex
        self.methods_names :dict = {}       # name:vertex
        self.interfaces_names :dict = {}    # name:vertex
        self.key = -1

    def __get_key(self)->int:
        self.key += 1
        return self.key

    def add_vertex(self,vertex:Vertex)->None:
        self.vertices[vertex.key] = vertex


    def add_class(self, name:string, modifiers=[])->Vertex:
        vertex = self.classes_names.get(name)
        if vertex:
            if len(modifiers) > len(vertex.modifiers):
                vertex.set_modifiers(modifiers)
            return vertex
        else:
            key = self.__get_key()
            vertex = Vertex(key ,name, 'class', [],modifiers)
            self.vertices[key] = vertex
            self.classes_names[name] = vertex
            return vertex

    def add_method(self, name, arguments=[], modifiers=[], return_type='')->Vertex:
        key = self.__get_key()
        vertex = Vertex(key, name, 'method', arguments, modifiers)
        self.vertices[key] = vertex
        self.methods_names[name] = vertex
        return vertex

    def add_interface(self, name:string)->Vertex:
        vertex = self.interfaces_names.get(name)
        if vertex:
            return vertex
        else:
            key = self.__get_key()
            vertex = Vertex(key ,name, 'interface')
            self.vertices[key] = vertex
            self.interfaces_names[name] = vertex
            return vertex

    def add_edge(self, type:string, source:Vertex, to:Vertex):
        edge = Edge(source, to, type)
        self.edges[edge.source.key, edge.to.key] = edge
        edge.source.add_neighbor(edge.to)

    def get_vertex(self,key:int)->Vertex:
        return self.vertices.get(key, None)

    def get_edge(self,source_key:int, to_key:int)->Edge:
        return self.edges.get((source_key, to_key),None)

    def get_vertices(self)->list:
        list = []
        for vertex in self.vertices.values():
            list.append(vertex)
        return list

    def get_edges(self)->list:
        list = self.edges.values()
        return list

    def num_of_vertices(self)->int:
        return len(self.vertices)

    def num_of_edges(self)->int:
        return len(self.edges)

    def print_vertices(self)->None:
        for v in self.vertices.values():
            print(v)

    def print_edges(self)->None:
        for e in self.edges.values():
            print(e)

    def toJson(self)->json:
        json = {}
        json["vertices"] = list_to_json(list(self.vertices.values()))
        json["edges"] = list_to_json(list(self.edges.values()))
        return json

    def save_to_json_file(self, path)->None:
        save_json_to_file(self.toJson(), path)

    def draw(self)->None:
        G = nx.DiGraph()
        ed = []
        edge_labels = dict()
        for edge in self.edges.values():
            v1 :string = edge.source.name
            v2 :string = edge.to.name
            ed.append((v1,v2))
            edge_labels[v1,v2] = edge.type
        G.add_edges_from(ed)

        if self.num_of_edges() == 0:
            for vertex in self.vertices.values():
                G.add_node(vertex.name)

        pos = nx.spring_layout(G, k=500)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=2000,node_color='#00b4d9')
        nx.draw_networkx_labels(G, pos, font_size=10, font_color='k')
        nx.draw_networkx_edges(G, pos, edge_color = 'b', arrowsize=20, arrowstyle='fancy')

        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()


def main():

    pass


    # g = Graph()
    # v1 = g.add_class('name1', 'type')
    # v2 = g.add_class('name2', 'kkk')
    # g.add_edge('extends',v1,v2)
    # g.draw()



if __name__ == '__main__':
    main()