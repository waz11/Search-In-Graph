import string

class Query:

    def __init__(self, query):
        self.content = query.split(',')
        self.key = -1
        self.classes_vertex_map = {}
        self.methods_vertex_map = {}
        self.edges_map = {}
        self.special_words = set(["extends", "implements", "contains", "method","class","gets"])
        self.graph = {}

    def get_uniqe_key(self) -> int:
        self.key+=1
        return self.key

    def parse(self):
        q = self.content
        for sentence in q:
            print(sentence)
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    if word=='extends':
                        vertex1 = self.create_vertex(words[i-1],"class")
                        vertex2 = self.create_vertex(words[i+1],"class")
                        self.create_edge("extends", vertex2["name"], vertex1["name"])
                    elif word=='implements':
                        vertex1 = self.create_vertex(words[i-1],"class")
                        vertex2 = self.create_vertex(words[i+1],"class")
                        self.create_edge("implements", vertex2["name"], vertex1["name"])
                    # elif word=='gets':
                    #     vertex1 = self.create_vertex(words[i-1],"method")
                    #     vertex1["attributes"].append(words[i+1])


    def create_vertex(self, name:string, type:string, attributes:list=[]):
        if type == 'class':
            if name not in self.classes_vertex_map.keys():
                vertex = {}
                vertex["name"] = name
                vertex["key"] = self.get_uniqe_key()
                vertex["type"] = type
                if len(attributes) > 0:
                    vertex["attributes"]
                self.classes_vertex_map[name] = vertex
            return self.classes_vertex_map[name]
        if type == 'method':
            if name not in self.methods_vertex_map.keys():
                vertex = {}
                vertex["name"] = name
                vertex["key"] = self.get_uniqe_key()
                vertex["type"] = type
                if len(attributes) > 0:
                    vertex["attributes"]
                self.methods_vertex_map[name] = vertex
            return self.methods_vertex_map[name]



    def create_edge(self, type, source, to):
        edge = {}
        edge["type"] = type
        if source not in self.classes_vertex_map.keys():
            self.create_vertex(source)
        edge["from"] = source
        edge["to"] = to
        self.edges_map[source,to] = edge

    def build(self):
        list1 = list(self.classes_vertex_map.values())
        list2 = list(self.methods_vertex_map.values())
        vertices = list1+list2
        self.graph["vertices"] = vertices

        self.graph["edges"] = list(self.edges_map.values())
        print(self.graph)


def main():
    q1 = "c1 extends c2"
    q2 = "c3 implements c4"
    q3 = "m1 gets f1 and f2 and f3"
    q4 =  "c5 with m2 and m3 and m4"
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