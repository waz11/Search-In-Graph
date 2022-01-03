import os
import string

from Preprocess.Parser.CodeFromFile import CodeFromFile


def code_to_graph(project_path, output_path, project_name=''):
    folder_name :string= os.path.basename(project_path)
    if project_name is '':
        project_name = folder_name
    code_from_file = CodeFromFile(project_path,project_name, output_path)
    code_from_file.concat_files()
    # code_from_file.test_new_file()


def main():
    code_to_graph('../Files/codes/src', '../Files/json graphs/out1.json','iterable list practice')
    code_to_graph('../Files/codes/src2','../Files/json graphs/out2.json')
    code_to_graph('../Files/codes/src3','../Files/json graphs/out3.json')


if __name__ == '__main__':
    main()
