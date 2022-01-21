import os
import string
from Parser.old_version.Preprocess.Parser.CodeFromFile import CodeFromFile

def code_to_graph_in_json_file(project_path, project_name=''):
    folder_name :string= os.path.basename(project_path)
    if project_name is '':
        project_name = folder_name
    output_path = '../Files/json graphs/'+folder_name+'.json'
    CodeFromFile(project_path,project_name, output_path)


def main():
    code_to_graph_in_json_file('../Files/codes/src1', 'Project 1')
    # code_to_graph_in_json_file('../Files/codes/src2', 'Project 2')
    # code_to_graph_in_json_file('../Files/codes/src3', 'Project 3')

if __name__ == '__main__':
    main()
