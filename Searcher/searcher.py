from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.query = query
        print(self.query.graph.draw())
        self.ordered_similar_nodes = MaxHeap()
        pass


# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):

        pass


def main():
    query = "class list implements class iterable"
    q = Query(query)
    # searcher = Searcher('',q)


if __name__ == '__main__':
    main()