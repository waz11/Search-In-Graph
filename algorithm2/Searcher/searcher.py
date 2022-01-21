import string
import time
import snowballstemmer
from Graph.graph import Graph
from Graph.vertex import Vertex
from Parser.codeToGraph.code_to_graph import CodeParser
from algorithm2.Searcher.query import Query


class Searcher:
    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = []
        self.candidate_nodes = []

    def is_relevant(self,vertex:Vertex):
        stemmer = snowballstemmer.stemmer('english');
        # print(stemmer.stemWords("happines existing".split()))
        # stems = vertex.
        for q in self.query.tokens:
            for v in vertex.tokens:
                if q==v: return True
                # if stemmer.stemWords(v.split())

    def generating_candidate_nodes(self) ->set:
        vertices = self.graph.get_vertices()
        relevant = set()
        for v in vertices:
            if self.is_relevant(v):
                relevant.add(v)
        return relevant

    def measuring_candidates_weight(self):
        pass

    def generating_and_measuring_subgraph(self):
        pass

    def extending_and_recommending_subgraph(self):
        pass


    def search(self):
        start_time = time.time()

        end_time = time.time()
        total_time = end_time - start_time
        convert_second(total_time)
        print('total time:', convert_second(total_time))


def convert_second(seconds)->string:
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = Searcher(graph, query)

    # searcher.is_relevant()


    # stemmer = snowballstemmer.stemmer('english');
    # print(stemmer.stemWords("happines existing".split()))


if __name__ == '__main__':
    main()