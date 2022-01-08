import re
from pathlib import Path
import javalang
from Graph.graph import Graph
from javalang.parse import parse
from Parser.codeToGraph.handlers import handle_class
from Parser.codeToGraph.types import typeof

primitive_variables = set(['String','boolean', 'byte', 'char', 'double','float', 'int', 'long', 'short'])
generice_variable = set(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
unwanted_types = primitive_variables.union(generice_variable)

class CodeParser:
    def __init__(self, path):
        self.directory_path = path
        self.graph = self.build_graph()

    def __concat_files(self,project_path):
        pathlist = Path(project_path).glob('**/*.java')
        result = ""
        for path in pathlist:
            path_in_str = str(path)
            with open(path_in_str, "r") as f:
                code_file = f.read()
                code_file = re.sub("package(.*?);", '', code_file)
                code_file = re.sub("import(.*?);", '', code_file)
            result += code_file
        return result

    def build_graph(self):
        code = self.__concat_files(self.directory_path)
        parsed_code = parse(code)
        graph = Graph()

        for x in parsed_code.types:
            if (typeof(x) == 'class' or typeof(x) == 'interface'):
                class_component = handle_class(x)
                name = class_component.name
                type = class_component.type
                modifiers = class_component.modifiers
                class_vertex = graph.add_class(name, modifiers)

                for attr in class_component.fields:
                    if attr.type not in unwanted_types:
                        class_vertex.add_attribute(attr.type)
                        field_type_vertex = graph.add_class(attr.type, 'class')
                        graph.add_edge('field', class_vertex, field_type_vertex)

                for method in class_component.methods:
                    name = method.name
                    arguments = []
                    for arg in method.arguments:
                        if arg not in unwanted_types:
                            arguments.append(arg)
                    return_type = method.return_type
                    method_vertex = graph.add_method(name, arguments, modifiers, return_type)
                    graph.add_edge('method', class_vertex, method_vertex)

                    for arg in arguments:
                        arg_vertex = graph.add_class(arg)
                        graph.add_edge('argument', method_vertex, arg_vertex)

                if class_component.extends:
                    name = class_component.extends
                    extended_class_vertex = graph.add_class(name, 'class')
                    graph.add_edge('extends', class_vertex, extended_class_vertex)

                for interface_name in class_component.implements:
                    interface_vertex = graph.add_interface(interface_name)
                    graph.add_edge('implements', class_vertex, interface_vertex)
            else:
                print(x)

        return graph

def main():
    c = CodeParser('../../Files/codes/src1')
    graph = c.build_graph()
    graph.print_vertices()
    graph.print_edges()
    print(graph.num_of_vertices(), "vertices")
    print(graph.num_of_edges(),"edges")
    graph.draw()

if __name__ == '__main__':
    main()

