from Searcher.BeamSearch.BeamSearch import BeamSearch

from Graph.graphFromJson import GraphFromJson
from Query.query import Query
from Searcher.GreedySearch.GreedySearch import GreedySearch


def testGreedySearch(graph, query):
    searcher = GreedySearch(graph)
    result = searcher.search(query)
    print("Greedy Search Results:")
    print(result.get_rank(), result.graph)
    # result.graph.draw()

def testBeamSearch(graph, query):
    searcher = BeamSearch(graph)
    result = searcher.search(query, 2)
    print("Beam Search Results:")
    print(result)
    # result.draw()


def main():
    graph = GraphFromJson('./Files/graphs/src1.json')
    query1 = Query("class list implements iterable,class list contains class node")
    query2 = Query("list iterable node")
    print("Query:", query1)
    print("Query:", query2)
    testBeamSearch(graph, query2)
    testGreedySearch(graph, query1)


if __name__ == '__main__':
    main()
