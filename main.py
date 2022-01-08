from Parser.codeToGraph.code_to_graph import CodeParser
from Searcher.query import Query
from Searcher.searcher import Searcher
from Utils.create_json_file_for_viewer import create_json_file_for_viewer


def main():
    query = Query("class list implements iterable,class list contains class node")
    print(query.graph.toJson())
    # query.graph.draw()

    graph = CodeParser('Files/codes/src1').graph
    # graph.draw()
    print(graph.num_of_vertices(),"vertices")
    print(graph.num_of_edges(),"edges")
    # create_json_file_for_viewer(graph, 'src1')

    searcher = Searcher(graph, query)
    # searcher.search()
    # searcher.get_results()


if __name__ == '__main__':
    main()
