import string

from Graph.edge import Edge
from Utils.json_functions import save_json_to_file
from Graph.vertex import Vertex

class Query:

    def __init__(self, query):
        self.content = query.split(',')
        self.key = -1
        self.graph = {}
        self.classes_vertex = {}
        self.methods_vertex = {}
        self.edges = {}
        self.special_words = set(["extends", "implements", "method","class","contains"])
        self.json = {}
        self.parse()
        self.toJson()

    def get_uniqe_key(self) -> int:
        self.key += 1
        return self.key

    def parse(self):
        q = self.content
        for sentence in q:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    # print(word)
                    if word=='class':
                        self.create_vertex(words[i + 1], "class")
                    if word =='method':
                        self.create_vertex(words[i + 1], "method")
                    if word=='extends':
                        vertex1 = self.create_vertex(words[i-1],"class")
                        vertex2 = self.create_vertex(words[i+2],"class")
                        self.create_edge("extends", vertex1, vertex1)
                    if word=='implements':
                        vertex1 = self.create_vertex(words[i-1],"class")
                        vertex2 = self.create_vertex(words[i+2],"class")
                        self.create_edge("implements", vertex2, vertex1)
                    if word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = self.create_vertex(words[i-1], "class")
                        else:
                            vertex1 = self.create_vertex(words[i - 1], "method")
                        if words[i+1]== 'method':
                            vertex2 = self.create_vertex(words[i + 2], "method")
                            self.create_edge("method",vertex1,vertex2)


    def create_vertex(self, name:string, type:string, attributes:list=[]) -> Vertex:
        # print(name,type)
        if type == 'class':
            if name not in self.classes_vertex.keys():
                vertex = Vertex(self.get_uniqe_key(),name,"class",attributes)
                self.classes_vertex[name] = vertex
            return self.classes_vertex[name]

        if type == 'method':
            if name not in self.methods_vertex.keys():
                vertex = Vertex(self.get_uniqe_key(), name, "method", attributes)
                self.methods_vertex[name] = vertex
            return self.methods_vertex[name]

    def create_edge(self, type, source, to):
        edge = Edge(type, source, to)
        if source not in self.edges.keys():
            self.edges[source] = [edge]
        else:
            self.edges[source].append(edge)

    def build_vertices_list(self):
        vertices = []
        for v in self.classes_vertex.values():
            vertices.append(v.toJson())
        for v in self.methods_vertex.values():
            vertices.append(v.toJson())
        return vertices

    def build_edges_list(self):
        edges = []
        for list in self.edges.values():
            for e in list:
                edges.append(e.toJson())
        return edges

    def toJson(self):
        vertices = self.build_vertices_list()
        edges = self.build_edges_list()
        self.json["vertices"] = vertices
        self.json["edges"] = edges


def main():
    q1 = "class c2 extends class c1"
    q2 = "class c4 implements class c3"
    q3 = "class c1 contains method m1"
    q = q1+','+q2+','+q3

    query = Query(q)
    print(query.json)
    save_json_to_file(query.json, 'query.json')


    # key = 0
    # for i,v in enumerate(q):
    #     if v == "extends":
    #         create_vertex(name=q[i-1], key=key, type="class")
    #         key+=1
    #         create_vertex(name=q[i+1], key=key, type="class")
    #         key+=1


if __name__ == '__main__':
    main()