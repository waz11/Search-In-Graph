from Graph.graph import Graph
from Searcher.searcher import Searcher


def main():
    graph = Graph('Preprocess/Files/out1.json')
    graph.draw()
    query = []
    searcher = Searcher(graph, query)


if __name__ == '__main__':
    main()
