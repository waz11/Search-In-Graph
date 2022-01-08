from Graph.graph import Graph


class Query:

    def __init__(self, query):
        self.query = query
        self.graph = Graph()
        self.content = query.split(',')
        self.special_words = set(["extends", "implements", "method", "class", "contains"])
        self.__parse()

    def build_json_obj(self):
        self.__parse()

    def __str__(self):
        return str(self.content)

    def __parse(self):
        g = Graph()
        for sentence in self.content:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    if word=='class':
                        g.add_class(words[i + 1])
                    if word =='method':
                        g.add_method(words[i + 1])
                    if word=='extends':
                        vertex1 = g.add_class(words[i - 1])
                        vertex2 = g.add_class(words[i + 2])
                        g.add_edge("extends", vertex1, vertex2)
                    if word=='implements':
                        vertex1 = g.add_class(words[i - 1])
                        vertex2 = g.add_interface(words[i + 1])
                        g.add_edge("implements", vertex1, vertex2)
                    if word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = g.add_class(words[i - 1])
                        else:
                            vertex1 = g.add_class(words[i - 1])
                        if words[i+1]== 'method':
                            vertex2 = g.add_method(words[i + 2])
                            g.add_edge("method", vertex1, vertex2)
                        elif words[i+1]== 'class':
                            vertex2 = g.add_class(words[i + 2])
                            g.add_edge("contains", vertex1, vertex2)
        self.graph = g

def main():
    q1 = "class c2 extends class c1"
    q2 = "class c2 implements class c3"
    q3 = "class c1 contains method m1"
    q = q1+','+q2+','+q3

    query = Query("class list implements class iterable,class list contains class node")
    query.graph.print_vertices()
    query.graph.print_edges()
    query.graph.draw()


if __name__ == '__main__':
    main()