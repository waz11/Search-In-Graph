import string

from Graph.graph import Graph
from Utils.Interfaces import ISearcher
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

    def get_candidates_for_query_token(self, token:string):
        candidates = set()
        for v in self.graph.get_vertices():
            if self.ranker.is_candidate_node(token, v):
                candidates.add(v)
        return candidates

    def generating_candidate_nodes(self)->set:
        candidates = {}
        for token in self.query.tokens:
            candidates[token] = self.get_candidates_for_query_token(token)
        return candidates

    def measuring_candidates_weight(self):
        score_relevant = 0
        score_irrelevant = 0

    def get_node_weight(self, score_relevant, score_irrelevant) ->float:
        numerator  = 2 * score_relevant * score_irrelevant
        denominator = score_relevant + score_irrelevant
        return numerator / denominator

    def generating_and_measuring_subgraph(self):
        pass

    def extending_and_recommending_subgraph(self):
        pass


    def search(self):
        candidate_nodes = self.generating_candidate_nodes()
        for key in candidate_nodes.keys():
            c = []
            for i in candidate_nodes[key]:
                c.append(i.name)
            print('key:', key, c)



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