import string
import time
from Graph.graph import Graph
from Utils.Interfaces import ISearcher
from algorithm1.Ranker.ranker import Ranker
from Utils.maxheap import MaxHeap
from algorithm1.Searcher.query import Query
from Result.result import Result
import threading
from Parser.codeToGraph.code_to_graph import CodeParser


class GreedySearch(ISearcher):
    def __init__(self, graph:Graph, query:Query):
        self.graph :Graph = graph
        self.query :Query = query
        self.__ranker :Ranker = Ranker()
        self.__results :MaxHeap = MaxHeap()
        self.similarities = dict()

    def class_based_similarity(self):
        pass

    def class_relationship_based_similarity(self, threshold, k):
        pass

    def __calculate_similarities(self, vertices = []) -> None:
        if len(vertices) == 0:
            vertices = self.graph.get_vertices()
        for vertex1 in self.query.graph.get_vertices():
            for vertex2 in vertices:
                # for multithreaed:
                # print(threading.get_ident())
                # sim = Ranker().get_rank(vertex1, vertex2)

                # for single-threaded:
                sim = self.__ranker.get_rank(vertex1, vertex2)

                self.similarities[vertex1.key, vertex2.key] = sim


    def calculate_similarities_multi_threaded(self) -> None:
        vertices_list = self.graph.get_vertices()
        length = len(vertices_list)
        middle_index = length // 3

        first = vertices_list[:middle_index]
        second = vertices_list[middle_index:2*middle_index]
        third = vertices_list[2*middle_index:3*middle_index]

        t1 = threading.Thread(target=self.__calculate_similarities, args = (first,))
        t2 = threading.Thread(target=self.__calculate_similarities, args = (second,))
        t3 = threading.Thread(target=self.__calculate_similarities, args = (third,))
        t1.start()
        t2.start()
        t3.start()
        t1.join()
        t2.join()
        t3.join()

    def __get_first_nodes(self)->list:
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

    def search(self, k=2, threshold = 1):
        start_time = time.time()

        self.__calculate_similarities()
        # self.calculate_similarities_multi_threaded()

        first_vertices = self.__get_first_nodes()
        self.__results = MaxHeap(len(first_vertices) * 2 + 1)
        for vertex in first_vertices.keys():
            rank = first_vertices[vertex]
            result = Result()
            result.add_vertex(vertex, rank)
            visited = set()
            visited.add(vertex.key)
            self.__greedy_algorithm_recursive(result, k, threshold, visited)
            rank = result.get_rank() / self.query.graph.num_of_vertices()
            self.__results.insert(rank, result)
        end_time = time.time()
        total_time = end_time - start_time
        convert_second(total_time)
        print('total time:', convert_second(total_time))

        # # TESTING:
        # vertex = list(first_vertices)[0]
        # result = Result()
        # result.add_vertex(vertex, 1)
        # visited = set()
        # visited.add(vertex.key)
        # self.__greedy_algorithm_recursive(result, 2, threshold, visited)
        # print(result.graph.toJson())
        # # END

    def get_results(self):
        results = []
        while self.__results.size > 0:
            element = self.__results.extractMax()
            results.append(element)
            print(element.rank, element.item.graph.toJson())
            element.item.graph.draw()
        return self.__results

    def __greedy_algorithm_recursive(self, result:Result, k, th, visited:set) -> Result:
        if k==0:
            return result
        max_sim = 0
        edge = None
        vertex = None
        for vertex1 in self.query.graph.get_vertices():
            for vertex2 in result.graph.get_vertices():
                for neighbor in vertex2.neighbors:
                    if neighbor.key not in visited:
                        sim = self.similarities[vertex1.key, neighbor.key]
                        if sim > max_sim:
                            max_sim = sim
                            vertex = neighbor
                            edge = self.graph.get_edge(vertex2.key, vertex.key)

        if vertex is None:
            return result
        result.add_vertex(vertex, max_sim)
        result.add_edge(edge)
        visited.add(vertex.key)
        self.__greedy_algorithm_recursive(result, k - 1, 0, visited)


def convert_second(seconds)->string:
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def main():
    query = Query("class list implements iterable,class list contains class node")
    graph = CodeParser('../../Files/codes/src2').graph

    searcher = GreedySearch(graph, query)
    searcher.search()
    searcher.get_results()
    # searcher.calculate_similarities_multi_threaded()


if __name__ == '__main__':
    main()