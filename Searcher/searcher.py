from Graph.graph import Graph
from Ranker.ranker import Ranker
from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.graph = graph
        self.query = query
        self.heap = MaxHeap()
        self.ranker = Ranker()


    def calculate_similarity(self):
        for vertex1 in self.query.graph.get_vertex():
            for vertex2 in self.graph.get_vertex():
                sim = self.ranker.get_rank(vertex1, vertex2)
                print(sim)
                self.heap.insert(sim, vertex2)
        vertex, rank = self.heap.extractMax()
        print(rank, vertex)

# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):
        pass


def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = Graph('../Files/json graphs/src1.json')
    searcher = Searcher(graph, query)
    searcher.calculate_similarity()

if __name__ == '__main__':
    main()