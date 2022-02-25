import string
from Graph.graph import Graph
from Searcher.BeamSearch.model.WordEmbedding import WordEmbedding
from Searcher.ISearcher import ISearcher
from Parser.codeToGraph.code_to_graph import CodeParser
from Query.query import Query
from Searcher.BeamSearch.Ranker.ranker import Ranker
from Utils.maxheap import MaxHeap


class BeamSearch(ISearcher):

    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = []
        self.candidate_nodes = []
        self.model = WordEmbedding(Graph)
        self.ranker = Ranker(self.model)

    def get_candidates_by_token(self, token:string) ->set:
        candidates = set()
        for vertex in self.graph.get_vertices():
            if self.ranker.is_candidate_node(token, vertex):
                candidates.add(vertex)
        return candidates

    def generating_candidate_nodes(self)->set:
        candidates = set()
        candidates_by_token = {}
        for token in self.query.tokens:
            curr_candidates = self.get_candidates_by_token(token)
            candidates_by_token[token] = [curr_candidates]
            candidates |= curr_candidates
        return candidates, candidates_by_token

    def measuring_candidates_weight(self, candidates) ->float:
        weights_heap = MaxHeap()
        for candidate in candidates:
            weight = self.ranker.get_scores(self.query.tokens, list(candidate.tokens))
            weights_heap.insert_item(weight, candidate)
        return weights_heap

    def generating_and_measuring_subgraph(self, candidates, candidates_by_token):
        weights_heap = self.measuring_candidates_weight(candidates)
        candidate, rank = weights_heap.pop()


        pass

    def extending_and_recommending_subgraph(self):
        pass


    def search(self):
        candidates, candidates_by_token = self.generating_candidate_nodes()
        self.generating_and_measuring_subgraph(candidates, candidates_by_token)










def main():
    query = Query("class list implements class iterable,class list contains class node")
    query.graph.draw()
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = BeamSearch(graph, query)
    searcher.search()


if __name__ == '__main__':
    main()