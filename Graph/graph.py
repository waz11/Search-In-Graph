import json
import string

import networkx as nx
from matplotlib import pyplot as plt
from Graph.edge import Edge
from Graph.vertex import Vertex
from Utils.json_functions import read_json_file


class Graph:
    def __init__(self):
        self.vertices :dict = {}
        self.edges :dict = {}

    def graph_builder_from_json_file(self, path) -> None:
        data :json = read_json_file(path)
        vertices :json = data['vertices']
        edges :json = data['edges']
        self.__vertices_builder_fron_json_obj(vertices)
        self.__edges_builder_fron_json_obj(edges)
        self.vertices[0].name = "PROJECT-DIRECTORY"


    def __vertices_builder_fron_json_obj(self, vertices:json) -> None:
        for v in vertices:
            if "attributes" in v:
                vertex = Vertex(v['key'], v['name'], v['type'], v['attributes'])
            else:
                vertex = Vertex(v['key'], v['name'], v['type'], [])
            self.vertices[vertex.key] = vertex

    def __edges_builder_fron_json_obj(self, edges:json) -> None:
        for e in edges:
            source = self.vertices[e["from"]]
            dest = self.vertices[e["to"]]
            edge = Edge(e["type"], source, dest)
            self.vertices[source.key].add_edge(edge)
            if source not in self.edges.keys():
                self.edges[source] = [edge]
            else:
                self.edges[source].append(edge)


    def draw(self) -> None:
        G = nx.DiGraph()
        ed = []
        for edges_list in self.edges.values():
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
        return len(self.vertices)

    def num_of_edges(self) -> int:
        return len(self.edges)

    def get_root(self) -> Vertex:
        return self.vertices[0]

    def print_vertices(self):
        for list in self.edges.values():
            for e in list:
                print(e)

    def print_edges(self):
        for list in self.edges.values():
            for e in list:
                print(e)


def main():
    g1 = Graph()
    g1.graph_builder_from_json_file('../Files/json graphs/src1.json')
    g1.draw()
    print(str(g1.num_of_vertices()))
    print(str(g1.num_of_edges()))
    g1.print_vertices()
    print()
    g1.print_edges()


if __name__ == '__main__':
    main()