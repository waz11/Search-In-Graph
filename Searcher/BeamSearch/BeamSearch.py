import math
import string

from Graph.graph import Graph
from Graph.vertex import Vertex
from Searcher.BeamSearch.group import Group
from Searcher.BeamSearch.model.WordEmbedding import WordEmbedding
from Searcher.ISearcher import ISearcher
from Parser.codeToGraph.code_to_graph import CodeParser
from Query.query import Query
from Searcher.BeamSearch.Ranker.ranker import Ranker
from utils.maxheap import MaxHeap

def top(k, weights_map: dict) -> list:
    heap = MaxHeap()
    for item in weights_map:
        heap.push(weights_map[item],item)
    res = []
    while(min(k,heap.size)>0):
        candidate = heap.pop()
        res.append(candidate[0])
        k-=1
    return res

def build_sub_graph(vertices, edges) ->Graph:
    g = Graph()
    for v in vertices:
        g.add_vertex(v)
    for e in edges:
        g.add_edge(e)
    return g

def top_groups(k, beam: list) -> list:
    heap = MaxHeap()
    for group in beam:
        heap.push(group.cost, group)
    res = []
    while(min(k,heap.size)>0):
        candidate = heap.pop()
        res.append(candidate[0])
        k-=1
    return res


class BeamSearch(ISearcher):
    def __init__(self, graph:Graph, query:Query, java_project_name:string):
        self.graph :Graph = graph
        self.query :Query = query
        self.model = WordEmbedding(self.graph, java_project_name)
        self.ranker = Ranker(self.model)


    def generate_subgraph(self, k, candidates_by_token, weights):
        beam = []
        for c in top(k, weights):
            beam.append(Group(c))

        for group in beam:
            for Ci in candidates_by_token.values():
                x = group.select_candidate(Ci, self.model)

        beam = top_groups(k, beam)
        return top_groups(1, beam)[0].vertices

    def search(self, k=2):
        candidates_by_token, weights = self.__get_candidates()
        vertices = self.generate_subgraph(k, candidates_by_token, weights)
        graph :Graph = self.extend_vertex_set_to_connected_subgraph(vertices)
        graph.draw()
        return graph

    def __get_candidates(self) ->tuple[dict, dict]:
        candidates_by_token = dict()
        weights = dict()
        for token in self.query.get_tokens():
            candidates_by_token[token] = set()
        for vertex in self.graph.get_vertices():
            for token in self.query.get_tokens():
                if self.ranker.is_candidate_node(token, vertex):
                    candidates_by_token[token].add(vertex)
                    if vertex not in weights:
                        weight = self.ranker.get_scores(self.query.tokens, list(vertex.tokens))
                        weights[vertex] = weight
        return candidates_by_token, weights

    def dist(self, vertex1, vertex2):
        return self.model.euclid(vertex1, vertex2)

    def findShortestPath(self, X :Vertex, Y :set):
        shortest_path = float('inf')
        path :list = None
        v = None
        for goal in Y:
            new_path :list = self.graph.bfs(goal, X)
            if new_path == None: new_path = self.graph.bfs(X, goal)
            if new_path != None and len(new_path) < shortest_path:
                shortest_path = len(new_path)
                path = new_path
                v = goal
        return v, path

    def extend_vertex_set_to_connected_subgraph(self, vertex_set) ->Graph:
        Y = vertex_set
        E = set()
        V = set()
        E = set()
        while(Y.__len__()>0):
            X = Y.pop()
            v, path = self.findShortestPath(X, Y)
            if path != None:
                for edge in path:
                    E.add(edge)
                    V.add(edge.source)
                    V.add(edge.to)

        graph: Graph = build_sub_graph(V, E)
        return graph


if __name__ == '__main__':
    query = Query("class list implements class iterable,class list contains class node")
    graph = CodeParser('../../Files/codes/src1').graph
    searcher = BeamSearch(graph, query, 'src1')
    searcher.search(50)
    # searcher.model.db.print_table('src1')
    # searcher.model.db.delete_db()