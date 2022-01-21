import json
import string
from Parser.old_version.Graph.edge import Edge
from Parser.old_version.Graph.vertex import Vertex
from Parser.old_version.Utils.json_functions import read_json_file


class Graph:
    def __init__(self, json_path:string=''):
        self.__vertices :dict = {} #key:vertex
        self.edges :dict = {}
        self.__classes_names = set()
        self.__methods_names = set()
        if len(json_path) > 0:
            self.__loading_graph_file(json_path)

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
            # self.__vertices[vertex.key] = vertex
            self.add_vertex(vertex)

    def add_vertex(self,vertex:Vertex) -> None:
        # if vertex.key not in self.__vertices.keys():
        if (vertex.type == "class") and (vertex.name not in self.__classes_names):
            self.__vertices[vertex.key] = vertex
            self.__classes_names.add(vertex.name)
        elif (vertex.type == "method") and (vertex.name not in self.__methods_names):
            self.__vertices[vertex.key] = vertex
            self.__methods_names.add(vertex.name)
        else:
            self.__vertices[vertex.key] = vertex

    def __edges_builder_fron_json_obj(self, edges:json) -> None:
        for e in edges:
            source = self.__vertices[e['from']]
            to = self.__vertices[e['to']]
            edge = Edge(e["type"], source, to)
            self.add_edge(edge)

    def add_edge(self,edge:Edge) -> None:
        self.edges[edge.source.key,edge.to.key] = edge
        edge.source.add_neighbor(edge.to)

    def get_vertices(self) ->list:
        list = []
        for vertex in self.__vertices.values():
            list.append(vertex)
        return list

    def get_edges(self) ->list:
        list = self.edges.values()
        return list


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

    e=g.edges[v1.key, v2.key]
    print(e)
    # g.draw()
    print(g.edges)


if __name__ == '__main__':
    main()