import string
from Graph.edge import Edge
from Graph.vertex import Vertex
import networkx as nx
from matplotlib import pyplot as plt


class Graph:
    def __init__(self, directed=False):
        self.vertices :dict = {}    # key:vertex
        self.edges_dict :dict = {}  # key,key:edge
        self.edges :list = []
        self.directed :bool = directed
##################################################################################3
    def num_of_vertices(self):
        return len(self.vertices)
    def num_of_edges(self):
        return len(self.edges_dict)
##################################################################################3
    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.key] = vertex
        self.edges_dict[vertex.key] = []

    def add_edge(self, edge :Edge):
        self.add_edge_aux(edge)

    def add_edge_aux(self, edge: Edge, directed :bool = False):
        if(edge.source not in self.edges_dict):
            self.edges_dict[edge.source] = []
        self.edges_dict[edge.source].append(edge)
        self.edges.append(edge)
        if not directed:
            edge2 = Edge(edge.to, edge.source, edge.type)
            self.add_edge_aux(edge2, True)
##################################################################################3
    def get_vertices(self) ->list:
        return list(self.vertices.values())

    def get_edges(self) ->list:
        return list(self.edges)

    def get_vertex(self, key :int) ->Vertex:
        return self.vertices[key]

    def get_edge(self,source_key :int, dest_key :int) ->Edge:
        return self.edges_dict[source_key, dest_key]
##################################################################################
    def draw(self) ->None:
        G = nx.DiGraph()
        edges = []
        edge_labels = dict()
        for edges_list in self.edges_dict.values():
            for edge in edges_list:
                v1 :string = self.get_vertex(edge.source).name
                v2 :string = self.get_vertex(edge.to).name
                edges.append((v1,v2))
                edge_labels[v1,v2] = edge.type.value
        G.add_edges_from(edges)
        pos = nx.spring_layout(G, k=500)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=2000,node_color='#00b4d9')
        nx.draw_networkx_labels(G, pos, font_size=10, font_color='k')
        nx.draw_networkx_edges(G, pos, edge_color = 'b')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()
##################################################################################3
    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        s = ''
        for vertex in self.get_vertices():
            s += str(vertex) + ' '
        for edge in self.get_edges():
            s += str(edge) + ' '
        return s
##################################################################################3
    def bfs(self, source: int, goal: int) -> list:
        visited = set()
        queue = [source]
        edges = {source:[]}
        while (len(queue) > 0):
            size = len(queue)
            while (size > 0):
                curr = queue.pop()
                visited.add(curr)
                if (curr == goal):
                    res = []
                    for list in edges.values():
                        for edge in list:
                            res.append(edge)
                    return res
                else:
                    for edge in self.edges_dict[curr]:
                        if not visited.__contains__(edge.to):
                            queue.append(edge.to)
                            edges[curr].append(edge)
                            edges[edge.to] = []
                size-=1
        return None


