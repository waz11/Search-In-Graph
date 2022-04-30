import string

from Graph.edge import EdgeTypeEnum
from Graph.graph import Graph
from Graph.graphFromQuery import GraphFromQuery
from Graph.vertex import VertexTypeEnum
from Parser.tokenizer import Tokenizer


special_words = ["extends", "implements", "method", "class", "contains","interface"]

class Query:

    def __init__(self, query:string):
        self.content = query
        self.tokens = self.get_tokens()
        self.graph = self.build_graph()

    def __str__(self):
        return str(self.content)

    # for BeamSearch:
    def get_tokens(self):
        tokens = Tokenizer().get_tokens(self.content, rm_stopwords=True)
        filtered = list(filter(lambda t: t not in special_words, tokens))
        return filtered

    # for GreedySearch:
    def build_graph(self)->Graph:
        g = GraphFromQuery()
        content = self.content.split(',')
        for sentence in content:
            words = list(sentence.split(' '))
            for i, word in enumerate(words):
                if word in special_words:
                    if word=='class':
                        name = words[i + 1]
                        v = g.add_vertex(name, VertexTypeEnum.CLASS)

                    elif word =='method':
                        g.add_vertex(words[i + 1], VertexTypeEnum.METHOD)

                    elif word=='extends':
                        vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.CLASS)
                        g.add_edge(EdgeTypeEnum.EXTENDS, vertex1.key, vertex2.key)

                    elif word=='implements':
                        vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        vertex2 = g.add_vertex(words[i + 1], VertexTypeEnum.INTERFACE)
                        g.add_edge(EdgeTypeEnum.IMPLEMENTS, vertex1.key, vertex2.key)

                    elif word == 'interface':
                        name = words[i + 1]
                        g.add_vertex(name, VertexTypeEnum.INTERFACE)

                    elif word=='contains':
                        if words[i-2] == 'class':
                            vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)
                        else:
                            vertex1 = g.add_vertex(words[i - 1], VertexTypeEnum.CLASS)

                        if words[i+1]== 'method':
                            vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.METHOD)
                            g.add_edge(EdgeTypeEnum.METHOD, vertex1.key, vertex2.key)

                        elif words[i+1]== 'class':
                            vertex2 = g.add_vertex(words[i + 2], VertexTypeEnum.CLASS)
                            g.add_edge(EdgeTypeEnum.CONTAINS, vertex1.key, vertex2.key)
        return g

