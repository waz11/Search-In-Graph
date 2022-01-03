from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.query = query
        self.ordered_similar_nodes = MaxHeap()



# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):

        pass


def main():
    query = "class list implements class iterable"
    q = Query(query)
    q.graph.draw()
    searcher = Searcher('',q)


if __name__ == '__main__':
    main()