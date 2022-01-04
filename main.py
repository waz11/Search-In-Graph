import string

from Graph.graph import Graph
from Preprocess.graph_builder import code_to_graph_in_json_file
from Searcher.searcher import Searcher

def buildGraph(path):
    graph = Graph(path)
    graph.draw()

def main():
    # [1] Preprocess:
    # a. code to graph in json file:
    code_to_graph_in_json_file('Files/codes/src1', 'Project 1')
    # b. load graph from json file to Graph objec    # graph_code.loading_graph_file('Files/json graphs/src1.json')t
    # graph_code = Graph()

    # buildGraph('Files/json graphs/out1.json')
    # buildGraph('Files/json graphs/out2.json')
    # buildGraph('Files/json graphs/out3.json')
    # query = []
    # searcher = Searcher(graph, query)



if __name__ == '__main__':
    main()
