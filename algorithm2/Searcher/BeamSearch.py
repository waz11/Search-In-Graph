import string

from Graph.graph import Graph
from Utils.Interfaces import ISearcher
from Parser.codeToGraph.code_to_graph import CodeParser
from Query.query import Query
from algorithm2.Ranker.ranker import Ranker


class BeamSearch(ISearcher):

    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = []
        self.candidate_nodes = []
        self.ranker = Ranker()

    def get_candidates_token(self, token:string):
        candidates = set()
        for v in self.graph.get_vertices():
            if self.ranker.is_candidate_node(token, v):
                candidates.add(v)
        return candidates

    def generating_candidate_nodes(self)->set:
        candidates = {}
        for token in self.query.tokens:
            candidates[token] = self.get_candidates_token(token)
        return candidates

    def measuring_candidates_weight(self, vertex) ->float:
        weight = self.ranker.get_scores(self.query.tokens, list(vertex.tokens))
        return weight

    def generating_and_measuring_subgraph(self):
        pass

    def extending_and_recommending_subgraph(self):
        pass


    def search(self):
        candidate_nodes = self.generating_candidate_nodes()
        for key in candidate_nodes.keys():
            c = []
            for i in candidate_nodes[key]:
                w = self.measuring_candidates_weight(i)
                c.append((i.name,w))
            print(key, c)





def main():
    query = Query("class list implements class iterable,class list contains class node")
    query.graph.draw()
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = BeamSearch(graph, query)
    searcher.search()


if __name__ == '__main__':
    main()