from Graph.graph import Graph
from Graph.vertex import Vertex
from Ranker.ranker import Ranker
from Searcher.maxheap import MaxHeap
from Searcher.query import Query
from Searcher.result import Result


class Searcher:
    def __init__(self, graph, query):
        self.graph = graph
        self.query = query
        self.heap = MaxHeap(graph.num_of_vertices() * query.graph.num_of_vertices())
        self.ranker = Ranker()
        self.results = MaxHeap()
        # self.similarities = {}
        self.similarities = {(1, 0): 0.05631370309339764, (1, 1): 1.0, (1, 2): 0.5, (1, 3): 0.6805555555555556, (1, 4): 0.5, (1, 5): 0.75, (1, 6): 0.5555555555555556, (1, 7): 0.6097727137234901, (1, 11): 0.75, (1, 12): 0.25, (1, 13): 0.3012596570051089, (1, 14): 0.3490199519692301, (1, 15): 0.3039324782817448, (1, 16): 0.4305555555555556, (1, 17): 0.27562982850255446, (1, 18): 0.25, (1, 19): 0.5, (1, 20): 0.27562982850255446, (1, 21): 0.25, (1, 22): 0.44813320144815283, (1, 23): 0.3055555555555556, (1, 24): 0.35977271372349007, (1, 25): 0.30553452859346225, (1, 26): 0.26885943649970134, (1, 27): 0.30884308642903857, (2, 0): 0.0, (2, 1): 0.5, (2, 2): 1.0, (2, 3): 0.5, (2, 4): 0.5, (2, 5): 0.5, (2, 6): 0.5, (2, 7): 0.5, (2, 11): 0.25, (2, 12): 0.25, (2, 13): 0.25, (2, 14): 0.25, (2, 15): 0.25, (2, 16): 0.25, (2, 17): 0.25, (2, 18): 0.25, (2, 19): 0.25, (2, 20): 0.25, (2, 21): 0.25, (2, 22): 0.25, (2, 23): 0.25, (2, 24): 0.25, (2, 25): 0.25, (2, 26): 0.25, (2, 27): 0.25, (3, 0): 0.051259657005108906, (3, 1): 0.6097727137234901, (3, 2): 0.5, (3, 3): 0.6004313363236333, (3, 4): 0.5, (3, 5): 0.554886356861745, (3, 6): 0.6286006380653804, (3, 7): 1.0, (3, 11): 0.35977271372349007, (3, 12): 0.25, (3, 13): 0.29703808016013306, (3, 14): 0.42516351262743685, (3, 15): 0.4266461500770891, (3, 16): 0.3504313363236334, (3, 17): 0.32397875137774945, (3, 18): 0.25, (3, 19): 0.30488635686174503, (3, 20): 0.32397875137774945, (3, 21): 0.25, (3, 22): 0.3322587599936632, (3, 23): 0.3786006380653803, (3, 24): 0.75, (3, 25): 0.3070289967419445, (3, 26): 0.2676911125768552, (3, 27): 0.30276415435889864}


    def class_based_similarity(self):
        pass

    def class_relationship_based_similarity(self, threshold, k):
        pass

    def calculate_similarity(self):
        for vertex1 in self.query.graph.get_vertices():
            for vertex2 in self.graph.get_vertices():
                sim = self.ranker.get_rank(vertex1, vertex2)
                self.heap.insert(sim, vertex2)
                self.similarities[vertex1.key, vertex2.key] = sim
        # print(self.similarities)


    def get_first_nodes(self):
        vertices = {}
        for vertex1 in self.query.graph.get_vertices():
            max_sim = 0
            vertex = None
            for vertex2 in self.graph.get_vertices():
                sim = self.similarities[vertex1.key, vertex2.key]
                if sim>max_sim:
                    max_sim=sim
                    vertex = vertex2
            if(vertex not in vertices.keys() or vertices[vertex] < max_sim):
                vertices[vertex] = max_sim
        return vertices

    def search(self):
        first_vertices = self.get_first_nodes()
        self.results = MaxHeap(len(first_vertices)*2+1)

        # first_vetex = list(first_vertices.keys())[0]
        # print(first_vetex)
        # result = Result()
        # result.add_vertex(first_vetex, first_vertices[first_vetex])
        # visited = set()
        # visited.add(first_vetex.key)
        # self.greedy_algorithm_recursive(result,2,0,visited)
        # # self.results.insert(r.get_rank() / self.query.graph.num_of_vertices(), result)
        # print(result.get_rank(), result)
        # result = Result()
        # print(result.get_rank(), result)

        for vertex in first_vertices.keys():
            rank = first_vertices[vertex]
            result = Result()
            result.add_vertex(vertex, rank)
            visited = set()
            visited.add(vertex.key)
            self.greedy_algorithm_recursive(result,2,0,visited)
            self.results.insert(result.get_rank() / self.query.graph.num_of_vertices(), result)

    def get_results(self):
        while self.results.size > 0:
            element = self.results.extractMax()
            print(element.rank, element.element)

    def greedy_algorithm_recursive(self, result:Result,k, th, visited:set) -> Result:
        # print(result)
        if k==0:
            return result
        max_sim = 0
        vertex = None
        for vertex1 in self.query.graph.get_vertices():
            for vertex2 in result.graph.get_vertices():
                for neighbor in vertex2.neighbors:
                    if neighbor.key not in visited:
                        sim = self.similarities[vertex1.key, neighbor.key]
                        if sim > max_sim:
                            max_sim = sim
                            vertex = neighbor
        if vertex is None:
            return result
        result.add_vertex(vertex, max_sim)
        visited.add(vertex.key)
        self.greedy_algorithm_recursive(result, k-1, 0, visited)

    def get_top(self,n):
        while n>0:
            max = self.heap.extractMax()
            print(max.rank, max.element)
            n-=1


def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = Graph('../Files/json graphs/src1.json')
    searcher = Searcher(graph, query)
    # searcher.calculate_similarity()
    searcher.search()
    # print(searcher.similarities[1,1])
    searcher.get_results()


if __name__ == '__main__':
    main()