from Parser.CodeFromFile import CodeFromFile


def code_to_graph(project_path, project_name, output_path):
    code_from_file = CodeFromFile(project_path,project_name, output_path)
    code_from_file.concat_files()
    code_from_file.test_new_file()

def main():
    code_to_graph('Files/src','Iterator_Practice', 'Files/out.json')


if __name__ == '__main__':
    main()
