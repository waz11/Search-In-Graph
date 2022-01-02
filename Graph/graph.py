import json
import networkx as nx
from matplotlib import pyplot as plt

from Graph.edge import Edge
from Graph.vertex import Vertex


class Graph:
    def __init__(self, path_to_json_file):
        self.vertices = dict()
        self.edges :dict = {}
        self.__build_graph(path_to_json_file)

    def __build_graph(self, path):
        f = open(path)
        data = json.load(f)
        for v in data['vertices']:
            if "attributes" in v:
                vertex = Vertex(v['key'], v['name'], v['type'],v['attributes'])
            else:
                vertex = Vertex(v['key'], v['name'], v['type'], [])
            self.vertices[vertex.key] = vertex

        for e in data['edges']:
            source = self.vertices[e["from"]]
            dest = self.vertices[e["to"]]
            edge = Edge(e["type"], source, dest)
            self.vertices[source.key].add_edge(edge)
            if source not in self.edges.keys():
                self.edges[source] = [edge]
            else:
                self.edges[source].append(edge)
        f.close()


    def draw(self):
        G = nx.DiGraph()
        ed = []
        print(len(self.edges))
        for edges_list in self.edges.values():
            for edge in edges_list:
                v1 = edge.source.name
                v2 = edge.to.name
                ed.append((v1,v2))
        G.add_edges_from(ed)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=600)
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='k')
        nx.draw_networkx_edges(G, pos,  edge_color='r', arrows=True)
        nx.draw_networkx_edges(G, pos,  arrows=False)
        plt.show()

    def num_of_vertices(self):
        return len(len(self.vertices))

    def get_first_node(self):
        return self.vertices[0]

    # def bfs(self):
    #     queue = [0]
    #     visited = {}
    #     for key in self.Graph:
    #         visited[key] = False
    #     while queue:
    #         vertex = queue.pop(0)
    #         visited[vertex] = True
    #         print("ID:" + str(vertex) + " Text: " + self.vertex_info[vertex])
    #         print("My neighbor:")
    #         i = 0
    #         for key in self.Graph[vertex]:
    #             i += 1
    #             if not visited[key]:
    #                 queue.append(key)
    #             print("ID:" + str(key) + " Text: " + self.vertex_info[key])
