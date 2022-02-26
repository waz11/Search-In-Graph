import re
import string
from pathlib import Path
import javalang
from Graph.graph import Graph
from javalang.parse import parse
from Parser.codeToGraph.handlers import component_handler
from Parser.codeToGraph.types import typeof
from main import src1_path

primitive_variables = set(['String','boolean', 'byte', 'char', 'double','float', 'int', 'long', 'short'])
generic_types = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
unwanted_types = primitive_variables.union(generic_types)

class CodeParser:
    def __init__(self, path:string):
        self.directory_path = path
        self.graph = Graph()
        self.build_graph(self.graph)

    def concat_files(self, project_path:string)->string:
        pathlist = Path(project_path).glob('**/*.java')
        result = ""
        for path in pathlist:
            path_in_str = str(path)
            with open(path_in_str, "r") as f:
                code_file = f.read()
                code_file = re.sub("package(.*?);", '', code_file)
                code_file = re.sub("import(.*?);", '', code_file)
            try:
                parsed_code = parse(code_file)
                result += code_file
            except:
                pass
        return result

    def build_graph(self, graph:Graph) ->None:
        code = self.concat_files(self.directory_path)
        parsed_code = parse(code)
        for x in parsed_code.types:
            if (typeof(x) == 'class' or typeof(x) == 'interface'):
                component_handler(self.graph, x)
            # else:
            #     print(x)


def main():
    from pathlib import Path
    font_path = Path(__file__).parent / "files" / "resources" / "COMIC.TTF"
    font_absolute_path = font_path.absolute()
    print(font_absolute_path)


    print(src1_path)
    g = CodeParser(src1_path).graph
    g.draw()
    x=g.num_of_vertices()
    print(x)


if __name__ == '__main__':
    main()

