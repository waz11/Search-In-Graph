from Graph.graphFromJson import GraphFromJson
from Query.query import Query
from Searcher.BeamSearch.BeamSearch import BeamSearch
from Searcher.GreedySearch.GreedySearch import GreedySearch


def testGreedySearch():
    graph = GraphFromJson('./Files/graphs/src1.json')
    query = Query("class list implements iterable,class list contains class node")
    searcher = GreedySearch(graph)
    result = searcher.search(query)
    print(result.get_rank(), result.graph)
    result.graph.draw()


def testBeamSearch():
    graph = GraphFromJson('./Files/graphs/src1.json')
    query = Query("list iterable node")
    searcher = BeamSearch(graph)
    result = searcher.search(query, 2)

    print(result)
    result.draw()

def main():
    # testGreedySearch()
    testBeamSearch()



if __name__ == '__main__':
    main()
