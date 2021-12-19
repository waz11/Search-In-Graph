import os

from Parser.CodeFromFile import CodeFromFile


def code_to_graph(project_path, output_path):
    folder_name = os.path.basename(project_path)
    code_from_file = CodeFromFile(project_path,folder_name, output_path)
    code_from_file.concat_files()
    code_from_file.test_new_file()


def main():
    # code_to_graph('Files/src', 'Files/out.json')
    code_to_graph('Files/src2','Files/out2.json')

if __name__ == '__main__':
    main()
