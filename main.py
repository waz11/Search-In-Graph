from Parser.codeToGraph.code_to_graph import CodeParser
from Searcher.query import Query
from Searcher.searcher import Searcher


def main():
    query = Query("class list implements class iterable,class list contains class node")
    graph = CodeParser('Files/codes/src1').graph
    j = query.graph.toJson()

    searcher = Searcher(graph, query)
    searcher.search()
    searcher.get_results()


if __name__ == '__main__':
    main()
