import string

from Graph.edge import Edge
from Graph.graph import Graph
from Graph.vertex import Vertex
from Utils.json_functions import save_json_to_file


class Query:

    def __init__(self, query):
        self.query = query

        # objects for parser:
        self.content = query.split(',')
        self.special_words = set(["extends", "implements", "method", "class", "contains"])
        self.key = 0
        self.__classes_vertex = {}
        self.__methods_vertex = {}
        self.__edges_map = {}
        self.parse()

        # objects for graph builder:
        self.vertices :list = self.__build_vertices_list()
        self.edges :list = self.__build_edges_list()
        self.graph = Graph(vertices=self.vertices, edges=self.edges)
        self.graph.draw()



    def build_json_obj(self):
        self.parse()

    def get_uniqe_key(self) -> int:
        self.key += 1
        return self.key


    def parse(self):
        q = self.content
        self.__create_vertex("QUERY",0,'query')
        for sentence in q:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    if word=='class':
                        self.__create_vertex(words[i + 1], "class")
                    if word =='method':
                        self.__create_vertex(words[i + 1], "method")
                    if word=='extends':
                        vertex1 = self.__create_vertex(words[i-1],"class")
                        vertex2 = self.__create_vertex(words[i+2],"class")
                        self.__create_edge("extends", vertex2, vertex1)
                    if word=='implements':
                        vertex1 = self.__create_vertex(words[i-1],"class")
                        vertex2 = self.__create_vertex(words[i+2],"class")
                        self.__create_edge("implements", vertex2, vertex1)
                    if word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = self.__create_vertex(words[i-1], "class")
                        else:
                            vertex1 = self.__create_vertex(words[i - 1], "method")
                        if words[i+1]== 'method':
                            vertex2 = self.__create_vertex(words[i + 2], "method")
                            self.__create_edge("method",vertex1,vertex2)
                        elif words[i+1]== 'class':
                            vertex2 = self.__create_vertex(words[i + 2], "class")
                            self.__create_edge("contains",vertex1,vertex2)
        self.vertices = self.__build_vertices_list()
        self.edges = self.__build_edges_list()


    def __create_vertex(self, name:string, type:string, attributes:list=[]) -> Vertex:
        if type == 'class':
            if name not in self.__classes_vertex.keys():
                vertex = Vertex(self.get_uniqe_key(),name,"class",attributes)
                self.__classes_vertex[name] = vertex
            return self.__classes_vertex[name]
        if type == 'method':
            if name not in self.__methods_vertex.keys():
                vertex = Vertex(self.get_uniqe_key(), name, "method", attributes)
                self.__methods_vertex[name] = vertex
            return self.__methods_vertex[name]

    def __create_edge(self, type, source, to):
        edge = Edge(type, source, to)
        if source not in self.__edges_map.keys():
            self.__edges_map[source] = [edge]
        else:
            self.__edges_map[source].append(edge)

    def __build_vertices_list(self):
        vertices = []
        for v in self.__classes_vertex.values():
            vertices.append(v.toJson())
        for v in self.__methods_vertex.values():
            vertices.append(v.toJson())
        return vertices

    def __build_edges_list(self):
        edges = []
        for list in self.__edges_map.values():
            for e in list:
                edges.append(e.toJson())
        return edges

    def toJson(self, out_path):
        vertices = self.__build_vertices_list()
        edges = self.__build_edges_list()
        json = {}
        json["vertices"] = vertices
        json["edges"] = edges
        save_json_to_file(json, '../Files/query.json')

    def __str__(self):
        return str(self.content)


def main():
    q1 = "class c2 extends class c1"
    q2 = "class c2 implements class c3"
    q3 = "class c1 contains method m1"
    q = q1+','+q2+','+q3

    query = Query("class list implements class iterable,class list contains class node")
    print(query)
    # print(query.json)
    # query.graph
    # save_json_to_file(query.json, 'query.json')


    # key = 0
    # for i,v in enumerate(q):
    #     if v == "extends":
    #         create_vertex(name=q[i-1], key=key, type="class")
    #         key+=1
    #         create_vertex(name=q[i+1], key=key, type="class")
    #         key+=1


if __name__ == '__main__':
    main()