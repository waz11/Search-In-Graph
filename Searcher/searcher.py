from Graph.graph import Graph
from Ranker.ranker import Ranker
from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.graph = graph
        self.query = query
        self.heap = MaxHeap(graph.num_of_vertices() * query.graph.num_of_vertices())
        self.ranker = Ranker()


    def class_based_similarity(self):
        pass

    def class_relationship_based_similarity(self, threshold, k):
        pass


    def calculate_similarity(self):
        for vertex1 in self.query.graph.get_vertices():
            for vertex2 in self.graph.get_vertices():
                sim = self.ranker.get_rank(vertex1, vertex2)
                # print(sim)
                self.heap.insert(sim, vertex2)

# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):
        pass

    def get_top(self,n):
        while n>0:
            max = self.heap.extractMax()
            print(max.rank, max.element)
            n-=1


def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = Graph('../Files/json graphs/src1.json')
    searcher = Searcher(graph, query)
    searcher.calculate_similarity()
    searcher.get_top(10)
    # json = query.graph.toJson()
    # print(json)


if __name__ == '__main__':
    main()