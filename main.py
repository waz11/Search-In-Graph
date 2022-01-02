from Graph.graph import Graph
from Searcher.searcher import Searcher

def buildGraph(path):
    graph = Graph(path)
    # graph.draw()

def main():
    buildGraph('Files/json graphs/out1.json')
    buildGraph('Files/json graphs/out2.json')
    buildGraph('Files/json graphs/out3.json')
    query = []
    # searcher = Searcher(graph, query)


if __name__ == '__main__':
    main()
