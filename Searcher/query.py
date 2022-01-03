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
        self.special_words = set(["extends", "implements", "method","class","in"])

    def get_uniqe_key(self) -> int:
        self.key += 1
        return self.key

    def parse(self):
        q = self.content
        for sentence in q:
            # print(sentence)
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    # print(word)
                    if word=='class':
                        self.create_vertex(words[i + 1], "class")
                    # if word =='method':
                    #     self.create_vertex(words[i + 1], "method")
                    if word=='extends':
                        vertex1 = self.create_vertex(words[i-1],"class")
                        vertex2 = self.create_vertex(words[i+1],"class")
                        self.create_edge("extends", vertex2, vertex1)
                    # if word=='implements':
                    #     vertex1 = self.create_vertex(words[i-1],"class")
                    #     vertex2 = self.create_vertex(words[i+1],"class")
                    #     self.create_edge("implements", vertex2["name"], vertex1["name"])
                    # if word=='in':
                    #     print("ron")
                    #     method = self.create_vertex(words[i + 1], "method")
                    #     vertex = self.create_vertex(words[i + 2], "class")
                    #     self.create_edge("method",vertex,method)
                    # elif word=='with'
                    # elif word=='gets':
                    #     vertex1 = self.create_vertex(words[i-1],"method")
                    #     vertex1["attributes"].append(words[i+1])


    def create_vertex(self, name:string, type:string, attributes:list=[]) -> Vertex:
        # print(name,type)
        if type == 'class':
            if name not in self.classes_vertex.keys():
                vertex = Vertex(self.get_uniqe_key(),name,"class",attributes)
                self.classes_vertex[name] = vertex
            return self.classes_vertex[name]
        #
        # if type == 'method':
        #     if name not in self.methods_vertex.keys():
        #         vertex = Vertex(self.get_uniqe_key(), name, "method", attributes)
        #         self.methods_vertex[name] = vertex
        #     return self.methods_vertex[name]

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

    def build(self):
        vertices = self.build_vertices_list()
        edges = self.build_edges_list()
        j={}
        j["vertices"] = vertices
        j["edges"] = edges
        save_json_to_file(j, 'query.json')


def main():
    q1 = "class c1 extends class c2"
    q2 = "class c3 implements c4"
    q6 = "method m5 in class c1"

    q3 = "m1 gets field1 and field2 and field3"
    q4 = "c5 with m2 and m3 and m4"
    q5 = "c6 contains c7"

    q = Query(q1)
    q.parse()
    q.build()




    # key = 0
    # for i,v in enumerate(q):
    #     if v == "extends":
    #         create_vertex(name=q[i-1], key=key, type="class")
    #         key+=1
    #         create_vertex(name=q[i+1], key=key, type="class")
    #         key+=1


if __name__ == '__main__':
    main()