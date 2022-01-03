import json
import string

import networkx as nx
from matplotlib import pyplot as plt
from Graph.edge import Edge
from Graph.vertex import Vertex


class Graph:
    def __init__(self, path_to_json_file):
        self.vertices :dict = {}
        self.edges :dict = {}

        self.__graph_builder(path_to_json_file)

    def __graph_builder(self, path):
        f = open(path)
        data :json = json.load(f)
        f.close()
        vertices :json = data['vertices']
        edges :json = data['edges']
        self.__vertices_builder(vertices)
        self.__edges_builder(edges)
        self.vertices[0].name = "PROJECT-DIRECTORY"


    def __vertices_builder(self, vertices:json):
        for v in vertices:
            if "attributes" in v:
                vertex = Vertex(v['key'], v['name'], v['type'], v['attributes'])
            else:
                vertex = Vertex(v['key'], v['name'], v['type'], [])
            self.vertices[vertex.key] = vertex

    def __edges_builder(self, edges:json):
        for e in edges:
            source = self.vertices[e["from"]]
            dest = self.vertices[e["to"]]
            edge = Edge(e["type"], source, dest)
            self.vertices[source.key].add_edge(edge)
            if source not in self.edges.keys():
                self.edges[source] = [edge]
            else:
                self.edges[source].append(edge)


    def draw(self):
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

    def num_of_vertices(self):
        return len(self.vertices)

    def num_of_edges(self):
        return len(self.edges)

    def get_root(self):
        return self.vertices[0]


def main():
    g = Graph("../Files/json graphs/out1.json")
    g.draw()
    print(str(g.num_of_vertices()))
    print(str(g.num_of_edges()))
    for v in g.vertices.values():
        print(v)
    print()
    for list in g.edges.values():
        for e in list:
            print(e)


if __name__ == '__main__':
    main()