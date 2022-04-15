import string
import json


from Graph.edge import Edge
from Graph.vertex import Vertex
import networkx as nx
from matplotlib import pyplot as plt
from Parser.old_version.Graph.graph import Graph
from Graph.utils.json_functions import list_to_json, save_json_to_file


class Graph:
    def __init__(self):
        self.vertices :dict = {}            # key:vertex
        self.edges :dict = {}               # key,key:edge
        self.classes_names :dict = {}       # name:vertex
        self.methods_names :dict = {}       # name:vertex
        self.interfaces_names :dict = {}    # name:vertex
        self.key = -1

    def __len__(self):
        return len(self.vertices)

    def __get_key(self)->int:
        self.key += 1
        return self.key

    def add_vertex(self,vertex:Vertex)->None:
        self.vertices[vertex.key] = vertex

    def add_edge(self, edge: Edge):
        self.edges[edge.source.key, edge.to.key] = edge
        edge.source.add_neighbor(edge.to)

    def copy_vertex(self, other:Vertex):
        vertex = Vertex(other.key, other.name, other.type)
        self.vertices[other.key] = vertex
        return vertex

    def copy_edge(self, other :Edge):
        source = self.get_vertex(other.source.key)
        to = self.get_vertex(other.to.key)
        self.add_edge1(other.type, source, to)

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



    def add_edge1(self, type:string, source:Vertex, to:Vertex):
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
        nx.draw_networkx_edges(G, pos, edge_color = 'b')

        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

    def get_path(self, dic, first, last):
        queue = []
        parent = dic[last]
        while(last != first):
            queue.append(last)
            parent = dic[last]
            last = parent
        queue.append(parent)
        queue.reverse()
        sub_graph = Graph()
        for v in queue:
            sub_graph.copy_vertex(v)
        for i,k in enumerate(queue):
            if(i+1<len(queue)):
                edge = self.get_edge(queue[i].key, queue[i+1].key)
                sub_graph.copy_edge(edge)
        return sub_graph



    def bfs(self, source :Vertex, goal :Vertex) -> list:
        queue1 = []
        queue2 = []
        visited = set()
        queue2.append(source)
        dic = dict()
        while(len(queue2) > 0):
            queue1 = queue2
            queue2 = []
            while(len(queue1)>0):
                curr = queue1.pop()
                visited.add(curr.key)
                if(curr==goal):
                    return self.get_path(dic, source, goal).get_edges()
                else:
                    for neighbor in curr.neighbors:
                        if not visited.__contains__(neighbor.key):
                            queue2.append(neighbor)
                            dic[neighbor] = curr
        return None


def main():



    g = Graph()
    v1 = g.add_class('name1', 'type')
    v2 = g.add_class('name2', 'kkk')
    v3 = g.add_class('name3', 'kkk')

    g.add_edge1('extends', v1, v3)
    g.add_edge1('extends', v3, v2)
    # g.draw()
    sub_g :Graph= g.bfs(v1,v2)
    print(len(sub_g))


if __name__ == '__main__':
    main()