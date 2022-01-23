from Graph.graph import Graph
from Graph.vertex import Vertex
from Interfaces import ISearcher
from Parser.codeToGraph.code_to_graph import CodeParser
from algorithm2.Searcher.query import Query

class BeamSearch(ISearcher):
    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = []
        self.candidate_nodes = []


    def __is_relevant(self,vertex:Vertex):
        stemmer = snowballstemmer.stemmer('english');
        # print(stemmer.stemWords("happines existing".split()))
        # stems = vertex.
        for q in self.query.tokens:
            if q == v: return self.matrix['full_name']
            else:
                for v in vertex.tokens:
                    if q==v: return self.matrix['part_name']
                    elif stemmer.stemWord(v) == stemmer.stemWord(q): return self.matrix['stemming']



    def generating_candidate_nodes(self) ->set:
        vertices = self.graph.get_vertices()
        relevant = set()
        for v in vertices:
            if self.__is_relevant(v):
                relevant.add(v)
        return relevant

    def measuring_candidates_weight(self):
        pass

    def generating_and_measuring_subgraph(self):
        pass

    def extending_and_recommending_subgraph(self):
        pass


    def search(self):
        candidate_nodes = self.generating_candidate_nodes()
        print([v.name for v in candidate_nodes])




def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = BeamSearch(graph, query)
    searcher.search()

    # searcher.is_relevant()


    # stemmer = snowballstemmer.stemmer('english');
    # print(stemmer.stemWords("happines existing".split()))


if __name__ == '__main__':
    main()