import json
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import pylab

class Vertex:
    def __init__(self, key, name, type, attributes=[]):
        self.key = key
        self.name = name
        self.type = type
        self.attributes = attributes

    def __str__(self):
        return "[key:{}, name:{}, type:{}, attributes:{}]".format(self.key,self.name,self.type,self.attributes)


class Edge:
    def __init__(self, type, source, to):
        self.type = type
        self.source = source
        self.to = to

    def __str__(self):
        return "({},{}):{}".format(self.source, self.to, self.type)


class Graph:
    def __init__(self, path):
        self.graph = {}
        self.vertex_info = {}
        self.vertex_type = {}
        self.edge_info = {}
        self.vertices = {}
        self.edges = {}
        self.edges2 = {}
        self.__build_graph(path)

    def add_vertex(self, v):
        key = v['key']
        name = v['name']
        type = v['type']
        attributes = []
        if "attributes" in v:
            attributes = v['attributes']
            vertex = Vertex(key, name, type, attributes)
        else:
            vertex = Vertex(key, name, type)
        self.vertices[key] = vertex
        self.graph[key] = []
        self.vertex_info[key] = v["name"]
        self.vertex_type[key] = v["type"]
        return vertex

    def add_edge(self, e):
        type = e["type"]
        source = e["from"]
        to = e["to"]
        edge = Edge(type, source, to)
        self.edges2[(source,to)] = edge
        if source not in self.edges.keys():
            self.edges[source] = [edge]
        else:
            self.edges[source].append(edge)
        self.graph[source].append(to)
        self.edge_info[(source, to)] = type
        return edge

    def __build_graph(self, path):
        f = open(path)
        data = json.load(f)
        for v in data['vertices']:
            vertex = self.add_vertex(v)
        for e in data['edges']:
            edge = self.add_edge(e)
        f.close()

        # print(self.graph)
        # print(self.vertex_info)
        # print(self.vertex_type)
        # print(self.edge_info)


    def draw(self):
        G = nx.DiGraph()
        ed = []
        for e in self.edges.values():
            for element in e:
                v1 = self.vertices[element.source].name
                v2 = self.vertices[element.to].name
                ed.append((v1,v2))
        G.add_edges_from(ed)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=600)
        nx.draw_networkx_labels(G, pos, font_size=8, font_color='k')
        nx.draw_networkx_edges(G, pos,  edge_color='r', arrows=True)
        nx.draw_networkx_edges(G, pos,  arrows=False)

        plt.show()


    def num_of_vertices(self):
        return len(self.vertex_info)

    def neighbors(self, key):
        return self.graph[key]

    def edge_type(self, from_node, to_node):
        return self.edge_info[(from_node, to_node)]

    def vertex_text(self, key):
        return self.vertex_info[key]

    def get_first_node(self):
        return self.vertex_info[0]

    def get_type(self, id):
        return self.vertex_type[id]

    def bfs(self):
        print(str(self.vertex_info))
        print(str(self.graph))
        queue = [0]
        visited = {}
        for key in self.graph:
            visited[key] = False
        while queue:
            vertex = queue.pop(0)
            visited[vertex] = True
            print("ID:" + str(vertex) + " Text: " + self.vertex_info[vertex])
            print("My neighbor:")
            i = 0
            for key in self.graph[vertex]:
                i += 1
                if not visited[key]:
                    queue.append(key)
                print("ID:" + str(key) + " Text: " + self.vertex_info[key])
