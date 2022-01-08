import string
from Graph.edge import Edge
from Graph.vertex import Vertex
import networkx as nx
from matplotlib import pyplot as plt

class Graph:
    def __init__(self):
        self.vertices :dict = {}        # key:vertex
        self.edges :dict = {}           # key,key:edge
        self.classes_names = dict()     # name:vertex
        self.methods_names = dict()     # name:vertex
        self.interfaces_names = dict()  #name:vertex
        self.key = -1

    def __get_key(self):
        self.key += 1
        return self.key

    def add_vertex(self,vertex):
        self.vertices[vertex.key] = vertex


    def add_class(self, name, modifiers=[]):
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

    def add_method(self, name, arguments=[], modifiers=[], return_type=''):
        key = self.__get_key()
        vertex = Vertex(key, name, 'method', arguments, modifiers)
        self.vertices[key] = vertex
        self.methods_names[name] = vertex
        return vertex

    def add_interface(self, name):
        vertex = self.interfaces_names.get(name)
        if vertex:
            return vertex
        else:
            key = self.__get_key()
            vertex = Vertex(key ,name, 'interface')
            self.vertices[key] = vertex
            self.interfaces_names[name] = vertex
            return vertex

    def add_edge(self, type, source, to):
        edge = Edge(source, to, type)
        self.edges[edge.source.key, edge.to.key] = edge
        edge.source.add_neighbor(edge.to)

    def get_vertex(self,key):
        return self.vertices.get(key, None)

    def get_edge(self,source_key, to_key):
        return self.edges.get((source_key, to_key),None)

    def get_vertices(self) ->list:
        list = []
        for vertex in self.vertices.values():
            list.append(vertex)
        return list

    def get_edges(self) ->list:
        list = self.edges.values()
        return list

    def num_of_vertices(self) -> int:
        return len(self.vertices)

    def num_of_edges(self) -> int:
        return len(self.edges)

    def print_vertices(self):
        for v in self.vertices.values():
            print(v)

    def print_edges(self):
        for e in self.edges.values():
            print(e)

    # def toJson(self):
    #     json = {}
    #     json["vertices"] = list_to_json(list(self.__vertices.values()))
    #     json["edges"] = list_to_json(list(self.__edges.values()))
    #     return json

    def draw(self) -> None:
        G = nx.DiGraph()
        ed = []
        for edge in self.edges.values():
            v1 :string = edge.source.name
            v2 :string = edge.to.name
            ed.append((v1,v2))
        G.add_edges_from(ed)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=1000)
        nx.draw_networkx_labels(G, pos, font_size=10, font_color='k')
        nx.draw_networkx_edges(G, pos,  edge_color='r', arrows=True)
        nx.draw_networkx_edges(G, pos,  arrows=False)
        plt.show()


def main():
    # g1 = Graph('../Files/json graphs/src1.json')
    # g1.toJson()
    # g1.draw()
    # print(str(g1.num_of_vertices()))
    # print(str(g1.num_of_edges()))
    # g1.print_vertices()
    # print()
    # g1.print_edges()


    g = Graph()
    v1 = g.add_class('name1', 'type')
    v2 = g.add_class('name2', 'kkk')
    for v in g.get_vertices():
        print(v)


if __name__ == '__main__':
    main()