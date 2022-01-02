import os
from Preprocess.Parser.CodeFromFile import CodeFromFile
from graph.graph import Graph
from searcher import Searcher


def code_to_graph(project_path, output_path):
    folder_name = os.path.basename(project_path)
    code_from_file = CodeFromFile(project_path,folder_name, output_path)
    code_from_file.concat_files()
    code_from_file.test_new_file()


def main():
    graph = Graph('Preprocess/Files/out.json')
    graph.draw()
    # query = []
    # searcher = Searcher(graph, query)


if __name__ == '__main__':
    main()
