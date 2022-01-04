from Graph.graph import Graph
from Ranker.similarity import sim_vertics
from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.graph = graph
        self.query = query
        self.ordered_similar_nodes = MaxHeap()


    def calculate_similarity(self):
        for vertex1 in self.query.graph.get_vertex():
            for vertex2 in self.graph.get_vertex():
                sim = sim_vertics(vertex1,vertex2)
                self.ordered_similar_nodes.insert(sim, vertex2)


# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):
        self.calculate_similarity()
        # print(self.ordered_similar_nodes.size)
        # pass


def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = Graph('../Files/json graphs/src1.json')
    searcher = Searcher(graph, query)
    searcher.calculate_similarity()
    # graph.print_vertices()
    # for v in graph.get_vertex():
    #    print(v)

if __name__ == '__main__':
    main()