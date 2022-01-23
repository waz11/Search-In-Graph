from Graph.graph import Graph
from Graph.vertex import Vertex
from Interfaces import ISearcher
from Parser.codeToGraph.code_to_graph import CodeParser
from algorithm2.Searcher.query import Query
from algorithm2.Ranker.ranker import Ranker


class BeamSearch(ISearcher):

    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = []
        self.candidate_nodes = []
        self.ranker = Ranker()

    def get_candidate(self, query_Vertex):
        candidates = set()
        for v in self.graph.get_vertices():
            sim = self.ranker.matching(query_Vertex, v)
            if(sim>0):
                candidates.add(v.key)
        return candidates

    def generating_candidate_nodes(self) ->set:
        candidates = []
        for v in self.query.graph.get_vertices():
            candidates[v.key] = self.get_candidate(v)
        return candidates

    def measuring_candidates_weight(self):
        score_relevant = 0
        score_irrelevant = 0

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