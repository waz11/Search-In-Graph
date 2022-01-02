from graph.graph import Graph
from searcher import Searcher


def main():
    graph = Graph('Preprocess/Files/out.json')
    graph.draw()
    query = []
    searcher = Searcher(graph, query)


if __name__ == '__main__':
    main()
