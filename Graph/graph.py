import json
import string
import networkx as nx
from matplotlib import pyplot as plt
from Graph.edge import Edge
from Graph.vertex import Vertex
from Utils.json_functions import get_data_from_json_file, list_to_json


class Graph:
    def __init__(self, json_path:string='', vertices:list=[], edges:list=[]):
        self.__vertices :dict = {} #key:vertex
        self.__edges :dict = {}
        self.__classes_names = set()
        self.__methods_names = set()
        if len(json_path) > 0:
            self.__loading_graph_file(json_path)
        elif len(vertices)>0 or len(edges)>0:
            self.__build(vertices, edges)

    def __loading_graph_file(self, path) -> None:
        data :json = get_data_from_json_file(path)
        vertices :list = data['vertices']
        edges :list = data['edges']
        self.__build(vertices, edges)
        # self.vertices[0].name = "PROJECT-DIRECTORY"

    def __build(self, vertices: list, edges: list) -> None:
        self.__vertices_builder_fron_json_obj(vertices)
        self.__edges_builder_fron_json_obj(edges)
        if 0 in self.__vertices.keys():
            del self.__vertices[0]

    def __vertices_builder_fron_json_obj(self, vertices:json) -> None:
        for v in vertices:
            if "attributes" in v:
                vertex = Vertex(v['key'], v['name'], v['type'], v['attributes'])
            else:
                vertex = Vertex(v['key'], v['name'], v['type'], [])
            # self.__vertices[vertex.key] = vertex
            self.add_vertex(vertex)

    def __edges_builder_fron_json_obj(self, edges:json) -> None:
        for e in edges:
            source = self.__vertices[e['from']]
            to = self.__vertices[e['to']]
            edge = Edge(e["type"], source, to)
            self.add_edge(edge)

    def add_vertex(self,vertex:Vertex) -> None:
        if (vertex.type == "class") and (vertex.name not in self.__classes_names):
            self.__vertices[vertex.key] = vertex
            self.__classes_names.add(vertex.name)
        elif (vertex.type == "method") and (vertex.name not in self.__methods_names):
            self.__vertices[vertex.key] = vertex
            self.__methods_names.add(vertex.name)
        else:
            self.__vertices[vertex.key] = vertex

    def add_edge(self,edge:Edge) -> None:
        self.__edges[edge.source.key, edge.to.key] = edge
        edge.source.add_neighbor(edge.to)

    def get_vertices(self) ->list:
        list = []
        for vertex in self.__vertices.values():
            list.append(vertex)
        return list

    def get_edges(self) ->list:
        list = self.__edges.values()
        return list

    def get_vertex(self,key):
        return self.__vertices.get(key, None)

    def get_edge(self,source_key, to_key):
        return self.__edges.get((source_key, to_key),None)

    def num_of_vertices(self) -> int:
        return len(self.__vertices)

    def num_of_edges(self) -> int:
        return len(self.__edges)

    def toJson(self):
        json = {}
        json["vertices"] = list_to_json(list(self.__vertices.values()))
        json["edges"] = list_to_json(list(self.__edges.values()))
        return json

    def draw(self) -> None:
        G = nx.DiGraph()
        ed = []
        for edge in self.__edges.values():
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
    v1 = Vertex(1,'v1','class')
    v2 = Vertex(2, 'v2', 'class')
    e = Edge('extends',v1,v2)
    g.add_vertex(v1)
    g.add_vertex(v2)
    g.add_edge(e)

if __name__ == '__main__':
    main()