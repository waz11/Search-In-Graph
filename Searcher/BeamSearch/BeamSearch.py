import string
import sys

from Graph.graph import Graph
from Graph.vertex import Vertex
from Result.result import Result
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
        self.model = WordEmbedding(Graph, 'src1')
        self.ranker = Ranker(self.model)

    def get_candidates_by_token(self, token:string) ->set:
        candidates = set()
        for vertex in self.graph.get_vertices():
            if self.ranker.is_candidate_node(token, vertex):
                candidates.add(vertex)
        return candidates

    def generating_candidate_nodes(self)->set:
        candidates_by_token = {}
        for token in self.query.tokens:
            curr_candidates = self.get_candidates_by_token(token)
            heap = self.sort_candidates(curr_candidates)
            candidates_by_token[token] = heap.pop()
        return candidates_by_token

    def sort_candidates(self, candidates) ->float:
        weights_heap = MaxHeap()
        for candidate in candidates:
            weight = self.ranker.get_scores(self.query.tokens, list(candidate.tokens))
            if(weight > 0):
                weights_heap.insert_item(weight, candidate)
        return weights_heap

    def union_candidates(self, candidates_by_token:dict):
        candidates = set()
        for token in self.query.tokens:
            candidates |= candidates_by_token[token]
        return candidates

    def generating_and_measuring_subgraph(self, candidates, candidates_by_token):
        weights_heap = self.sort_candidates(candidates)
        candidate, rank = weights_heap.pop()
        pass

    def extending_and_recommending_subgraph(self):
        pass

    def top(self, k:int, C:MaxHeap):
        result = []
        k = min(k, C.size)
        while(k>0):
            result.append(C.pop())
            k-=1
        return result

    def dist(self, vertex1, vertex2):
        return self.model.euclid(vertex1, vertex2)

    def findShortestPath(self, X :Vertex, Y :set):
        path_len = float('inf')
        path = None
        for goal in Y:
            new_path = self.graph.bfs(goal, X)
            if new_path == None:
                new_path = self.graph.bfs(X, goal)
            elif new_path != None and len(new_path) < path_len:
                path = new_path
        return path

    def extend_vertex_set_to_connected_subgraph(self, vertex_set):
        Y = vertex_set
        E = set()
        # print(Y)
        res = Result()
        while(Y.__len__()>0):
            X = Y.pop()
            z = self.findShortestPath(X, Y)
            if z != None:
                for vertex in z.get_vertices():
                    res.add_vertex(vertex)
                for edge in z.get_edges():
                    res.add_edge(edge)

        return res


    def search(self, k=1):
        Ci :dict = self.generating_candidate_nodes()
        vertex_set = []
        for c in Ci.values():
            vertex_set.append(c[0])
        result = self.extend_vertex_set_to_connected_subgraph(vertex_set)
        result.graph.draw()



def main():
    query = Query("class list implements class iterable,class list contains class node")
    # query.graph.draw()
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = BeamSearch(graph, query)
    searcher.search()
    # searcher.model.db.print_table('src1')
    # searcher.model.db.delete_db()


if __name__ == '__main__':
    main()





# C :set = self.union_candidates(Ci)
# C :MaxHeap = self.sort_candidates(C)
# a =  list((item,rank) for item, rank in C)
# beam = self.top(k,C)
# for v in beam:
#     Wv = v[1]
#     vi = v[0]
#     delta = 0
# dist = self.dist(v,c) / Wc*Wv
# delta += self.dist(v,c)
# self.generating_and_measuring_subgraph(candidates, candidate_Q)