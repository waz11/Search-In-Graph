import string

from Graph.graph import Graph
from Parser.tokenizer import Tokenizer

class Query:

    def __init__(self, query:string):
        self.content = query
        self.special_words = set(["extends", "implements", "method", "class", "contains","interface"])
        self.tokens = self.get_tokens()
        self.graph = self.build_graph()

    def __str__(self):
        return str(self.content)

    # for BeamSearch:
    def get_tokens(self):
        tokens = Tokenizer().get_tokens(self.content, rm_stopwords=True)
        filtered = list(filter(lambda t: t not in self.special_words, tokens))
        return filtered

    # for GreedySearch:
    def build_graph(self)->Graph:
        g = Graph()
        content = self.content.split(',')
        for sentence in content:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in self.special_words:
                    if word=='class':
                        g.add_class(words[i + 1])
                    elif word =='method':
                        g.add_method(words[i + 1])
                    elif word=='extends':
                        vertex1 = g.add_class(words[i - 1])
                        vertex2 = g.add_class(words[i + 2])
                        g.add_edge1("extends", vertex1, vertex2)
                    elif word=='implements':
                        vertex1 = g.add_class(words[i - 1])
                        vertex2 = g.add_interface(words[i + 1])
                        g.add_edge1("implements", vertex1, vertex2)
                    elif word == 'interface':
                        g.add_interface(words[i + 1])
                    elif word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = g.add_class(words[i - 1])
                        else:
                            vertex1 = g.add_class(words[i - 1])
                        if words[i+1]== 'method':
                            vertex2 = g.add_method(words[i + 2])
                            g.add_edge1("method", vertex1, vertex2)
                        elif words[i+1]== 'class':
                            vertex2 = g.add_class(words[i + 2])
                            g.add_edge1("contains", vertex1, vertex2)
        return g

def main():
    q = "class list implements class iterable,class list contains class node"
    query = Query(q)
    # print(query.tokens)
    g=query.graph
    g.draw()


if __name__ == '__main__':
    main()