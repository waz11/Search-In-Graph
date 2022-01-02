import os
from Preprocess.Parser.CodeFromFile import CodeFromFile


def code_to_graph(project_path, output_path, project_name=''):
    folder_name = os.path.basename(project_path)
    if project_name is '':
        project_name = folder_name
    code_from_file = CodeFromFile(project_path,project_name, output_path)
    code_from_file.concat_files()
    code_from_file.test_new_file()


def main():
    code_to_graph('Files/src', 'Files/out.json','iterable list practice')
    # code_to_graph('Files/src2','Files/out2.json')
    # code_to_graph('Files/src3', 'Files/out3.json')


if __name__ == '__main__':
    main()
