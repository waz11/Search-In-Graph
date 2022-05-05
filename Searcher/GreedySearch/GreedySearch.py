import Graph.graph
from Graph.graph import Graph
from Query.query import Query
from Searcher.GreedySearch.Ranker.VectorsDB import VectorsDB
from Searcher.GreedySearch.Ranker.ranker import Ranker
from Searcher.GreedySearch.Result.result import Result
from utils.heap import Heap


class GreedySearch():

    def __init__(self, graph:Graph, database=False):
        self.graph :Graph = graph
        self.ranker :Ranker = Ranker()
        self.results :Heap = Heap()
        self.similarities = dict()
        self.database = database
        if database:
            self.db = VectorsDB()
            self.db.create_table("sim")

    def get_sim(self, vertex1_key, vertex2_key):
        if self.database:
            return self.db.get("sim", vertex1_key, vertex2_key)
        return self.similarities[vertex1_key, vertex2_key]

    def calculate_similarities(self, query :Query) -> None:
        graphV = self.graph.get_vertices()
        queryV = query.graph.get_vertices()

        for v1 in queryV:
            for v2 in graphV:
                sim = self.ranker.get_vertices_rank(v1, v2)
                self.similarities[v1.key, v2.key] = sim
                if self.database: self.db.add("sim",v1.key,v2.key,sim)

        if self.database: self.db.print_table("sim")


    def get_first_nodes(self, query)->list:
        vertices = {}
        for vertex1 in query.graph.get_vertices():
            max_sim = 0
            v_key = None
            for vertex2 in self.graph.get_vertices():

                if self.database: sim = self.db.get("sim", vertex1.key, vertex2.key)
                else: sim = self.similarities[vertex1.key, vertex2.key]

                if sim>max_sim:
                    max_sim=sim
                    v_key = vertex2.key
            if(v_key not in vertices.keys() or vertices[v_key] < max_sim):
                vertices[v_key] = max_sim
        return vertices

    def search(self, query ,k=2, threshold = 1):
        self.results: Heap = Heap()
        self.calculate_similarities(query)
        first_vertices = self.get_first_nodes(query)

        results = Heap()
        for v_key in first_vertices.keys():
            rank = first_vertices[v_key]
            result = Result()
            result.add_vertex(self.graph.get_vertex(v_key), rank)
            visited = set()
            visited.add(v_key)
            self.greedy_algorithm_recursive(query, result, k, threshold, visited)
            rank = result.get_rank() / max(query.graph.num_of_vertices(), len(result.graph))
            results.push(rank, result)
        return results.pop()[0]

    def get_results(self, result_heap):
        results = []
        while result_heap.size > 0:
            result, rank = result_heap.pop()
            results.append(result)
            print(rank, result.graph)
            # result.graph.draw()
        return results

    def greedy_algorithm_recursive(self, query, result, k, th, visited:set) :
        if k==0:
            return result
        max_sim = 0
        _edge = None
        vertex = None

        graphV = self.graph.get_vertices()
        queryV = query.graph.get_vertices()

        for v1 in graphV:
            for v2 in queryV:
                for edge in self.graph.edges_dict[v1.key]:
                    if edge.to not in visited:
                        sim = self.get_sim(v2.key, edge.to)
                        if sim > max_sim:
                            max_sim = sim
                            vertex = edge.to
                            _edge = edge

        if vertex is None:
            return result
        result.add_vertex(self.graph.get_vertex(vertex), max_sim)
        result.add_edge(_edge)
        visited.add(vertex)
        self.greedy_algorithm_recursive(query, result, k - 1, 0, visited)
