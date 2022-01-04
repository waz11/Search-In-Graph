from Graph.graph import Graph
from Ranker.similarity import sim_vertics
from Searcher.maxheap import MaxHeap
from Searcher.query import Query


class Searcher:
    def __init__(self, graph, query):
        self.query = query
        self.ordered_similar_nodes = MaxHeap()
        self.query_graph = query.graph
        self.graph = graph


    def calculate_similarity(self):
        for vertex1 in self.query.graph.vertices.values():
            print('v1:',vertex1)
            for vertex2 in self.graph.vertices.values():
                print(vertex2)
                sim = sim_vertics(vertex1,vertex1)
                # print(sim)
                # self.ordered_similar_nodes.insert(sim, vertex2)


# first_similar_node -> next_similar_node -> greedy_algorithm_recursive
    def greedy_algorithm_recursive(self):
        self.calculate_similarity()
        # print(self.ordered_similar_nodes.size)
        # pass


def main():
    query = "class list implements class iterable"
    q = Query(query)
    g = Graph()
    g.loading_graph_file('../Files/json graphs/src1.json')
    # searcher = Searcher(g,q)
    # searcher.greedy_algorithm_recursive()


if __name__ == '__main__':
    main()