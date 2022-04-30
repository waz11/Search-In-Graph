import json
import os
import string
from Graph.edge import Edge, EdgeTypeEnum
from Graph.graph import Graph
from Graph.utils.json_functions import get_data_from_json_file
from Graph.vertex import Vertex, VertexTypeEnum


def get_project_name(path: string) ->string:
    projectName = os.path.basename(path)
    projectName = projectName[0:projectName.rindex('.')]
    return projectName

class GraphFromJson(Graph):
    def __init__(self, path :string):
        Graph.__init__(self)
        self.build_graph_from_json(path)
        self.name: string = get_project_name(path)

    def build_graph_from_json(self, path :string):
        data :json = get_data_from_json_file(path)
        self.add_vertices_from_json(data['vertices'])
        self.add_edges_from_json(data['edges'])

    def add_vertices_from_json(self, vertices :json):
        for v in vertices:
            key = v['key']
            name = v['name']
            type = v['type']
            try:
                attributes = v['attributes']
                vertex = Vertex(key, name, VertexTypeEnum(type), attributes)
            except:
                vertex = Vertex(key, name, VertexTypeEnum(type))
            super().add_vertex(vertex)

    def add_edges_from_json(self, edges :json):
        for e in edges:
            type = e['type']
            source = e['from']
            to = e['to']
            edge = Edge(source, to, EdgeTypeEnum(type))
            super().add_edge(edge)

if __name__ == '__main__':
    path = '../Files/graphs/src1.json'
    g = GraphFromJson(path)
    print(len(g))
    print(g.num_of_vertices(),'vertices',g.num_of_edges(),'edges')
    for v in g.get_vertices():
        print(v)
    for e in g.get_edges():
        print(e)
    g.draw()
