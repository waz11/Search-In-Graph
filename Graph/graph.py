import json
import string

import networkx as nx
from matplotlib import pyplot as plt
from Graph.edge import Edge
from Graph.vertex import Vertex
from Utils.json_functions import read_json_file


class Graph:
    def __init__(self, json_path:string='', vertices:list=[], edges:list=[]):
        self.__vertices :dict = {} #key:vertex
        self.__edges :dict = {}
        if len(json_path) > 0:
            self.__loading_graph_file(json_path)
        elif len(vertices)>0 or len(edges)>0:
            self.__build(vertices, edges)
        self.__classes_vertices_names = set()
        self.__methods_vertices_names = set()


    def __loading_graph_file(self, path) -> None:
        data :json = read_json_file(path)
        vertices :list = data['vertices']
        edges :list = data['edges']
        self.__build(vertices, edges)
        # self.vertices[0].name = "PROJECT-DIRECTORY"

    def __build(self, vertices: list, edges: list) -> None:
        self.__vertices_builder_fron_json_obj(vertices)
        self.__edges_builder_fron_json_obj(edges)

    def __vertices_builder_fron_json_obj(self, vertices:json) -> None:
        for v in vertices:
            if "attributes" in v:
                vertex = Vertex(v['key'], v['name'], v['type'], v['attributes'])
            else:
                vertex = Vertex(v['key'], v['name'], v['type'], [])
            self.__vertices[vertex.key] = vertex

    def __edges_builder_fron_json_obj(self, edges:json) -> None:
        for e in edges:
            source = self.__vertices[e["from"]]
            dest = self.__vertices[e["to"]]
            edge = Edge(e["type"], source, dest)
            self.__vertices[source.key].add_edge(edge)
            if source not in self.__edges.keys():
                self.__edges[source] = [edge]
            else:
                self.__edges[source].append(edge)


    def draw(self) -> None:
        G = nx.DiGraph()
        ed = []
        for edges_list in self.__edges.values():
            for edge in edges_list:
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

    def num_of_vertices(self) -> int:
        return len(self.__vertices)

    def num_of_edges(self) -> int:
        return len(self.__edges)

    def get_root(self) -> Vertex:
        return self.__vertices[0]

    def add_vertex(self,vertex:Vertex) -> None:
        if vertex.key not in self.__vertices.keys():
            if (vertex.type == "class") and (vertex.name not in self.__classes_vertices_names):
                self.__vertices[vertex.key] = vertex
                self.__classes_vertices_names.add(vertex.name)
            elif (vertex.type == "method") and (vertex.name not in self.__methods_vertices_names):
                self.__vertices[vertex.key] = vertex
                self.__methods_vertices_names.add(vertex.name)


    def add_edge(self,edge:Edge) -> None:
        self.__edges[edge.source] = edge

    def print_vertices(self) -> None:
        for vertex in self.__vertices.values():
            print(vertex)

    def print_edges(self) -> None:
        for list in self.__edges.values():
            for edge in list:
                print(edge)

    def get_vertices(self) ->list:
        list = []
        for vertex in self.__vertices.values():
            list.append(vertex)
        return list

    def get_edges(self) ->list:
        list = []
        for l in self.__edges.values():
            for edge in l:
                list.append(edge)
        return list

    def list_to_json(self, list):
        json = []
        for element in list:
            json.append(element.toJson)

    def toJson(self):
        json = {}
        vertices = []
        for vertex in self.get_vertices():
            vertices.append(vertex.toJson())
        edges = []
        for edge in self.get_edges():
            edges.append(edge.toJson())
        json["vertices"] = vertices
        json["edges"] = edges
        return json

    def get_vertex(self,key):
        return self.vertices[key]

def main():
    g1 = Graph('../Files/json graphs/src1.json')
    g1.toJson()
    # # g1.graph_builder_from_json_file('../Files/query.json')
    # g1.draw()`
    # print(str(g1.num_of_vertices()))
    # print(str(g1.num_of_edges()))
    # g1.print_vertices()
    # print()
    # g1.print_edges()



if __name__ == '__main__':
    main()