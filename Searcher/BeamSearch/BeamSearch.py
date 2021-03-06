import copy
from Graph.graph import Graph
from Query.query import Query
from Searcher.BeamSearch.Ranker.ranker import Ranker
from Searcher.BeamSearch.group import Group
from Searcher.BeamSearch.model.WordEmbedding import WordEmbedding
from utils.heap import Heap


def top(k, weights_map: dict) -> list:
    heap = Heap() # MAX HEAP
    for item in weights_map:
        heap.push(weights_map[item],item)
    res = []
    while(min(k,heap.size)>0):
        candidate = heap.pop()
        res.append(candidate[0])
        k-=1
    return res

def top_groups(k, beam: list) -> list:
    heap = Heap(key=lambda x: -x) # MIN HEAP
    for group in beam:
        heap.push(group.cost, group)
    res = []
    while(min(k,heap.size)>0):
        candidate = heap.pop()
        res.append(candidate[0])
        k-=1
    return res


class BeamSearch():
    def __init__(self, graph:Graph):
        self.graph :Graph = graph
        self.model = WordEmbedding(self.graph)
        self.ranker = Ranker(self.model)

    def getDelta(self, c_key: int, v_key: int) -> float:
        delta = self.model.euclid(c_key, v_key)
        return delta

    def generate_subgraph(self, k :int, candidates_by_token :dict, weights :dict) ->set:
        beam = []
        for c in top(k, weights):
            beam.append(Group(c))

        for Ci in candidates_by_token.values():
            new_beam = []
            for group in beam:
                for c_key in Ci:
                    delta = 0
                    for v_key in group.vertices:
                        delta += self.getDelta(c_key,v_key)
                    cpy_group = copy.deepcopy(group)
                    cpy_group.add_vertex_key(c_key)
                    cpy_group.set_cost(cpy_group.cost + delta)
                    new_beam.append(cpy_group)
            beam = top_groups(k, new_beam)
        return top_groups(1, beam)[0].vertices

    def search(self, query:Query, k :int=2) ->Graph:
        candidates_by_token, weights = self.__get_candidates(query)
        # print(candidates_by_token)
        # print(weights)
        vertices_keys = self.generate_subgraph(k, candidates_by_token, weights)
        graph :Graph = self.extend_vertex_set_to_connected_subgraph(vertices_keys)
        return graph

    def __get_candidates(self, query:Query):
        candidates_by_token = dict()
        weights = dict()
        for token in query.get_tokens():
            candidates_by_token[token] = set()
        for vertex in self.graph.get_vertices():
            for token in query.get_tokens():
                if self.ranker.is_candidate_node(token, vertex):
                    candidates_by_token[token].add(vertex.key)
                    if vertex not in weights:
                        weight = self.ranker.get_scores(query.tokens, list(vertex.tokens))
                        weights[vertex.key] = weight
        return candidates_by_token, weights

    def dist(self, vertex1, vertex2) ->float:
        return self.model.euclid(vertex1, vertex2)

    def extend_vertex_set_to_connected_subgraph(self, vertices_keys) ->Graph:
        Y = vertices_keys
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
        graph: Graph = self.build_sub_graph(V, E)
        return graph

    def findShortestPath(self, X_key :int, Y :int):
        shortest_path = float('inf')
        path :list = None
        v :int = None

        for goal_key in Y:
            dir1 :list = self.graph.bfs(goal_key, X_key)
            dir2: list = self.graph.bfs(X_key, goal_key)
            new_path = []
            if dir1!=None and dir2!=None:
                if len(dir1) < len(dir2):
                    new_path = dir1
                else:
                    new_path = dir2
            elif dir1!=None:
                new_path = dir1
            else:
                new_path = dir2

            if new_path != None and len(new_path) < shortest_path:
                shortest_path = len(new_path)
                path = new_path
                v = goal_key
        return v, path

    def build_sub_graph(self, vertices :set, edges :set) -> Graph:
        g = Graph()
        for v_key in vertices:
            g.add_vertex(self.graph.get_vertex(v_key))
        for e in edges:
            g.add_edge(e)
        return g

