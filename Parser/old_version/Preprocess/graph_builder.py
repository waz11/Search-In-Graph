import os
import string
from Parser.old_version.Preprocess.Parser.CodeFromFile import CodeFromFile

def code_to_graph_in_json_file(project_path, project_name=None):
    folder_name :string= os.path.basename(project_path)
    if project_name is None:
        project_name = folder_name
    output_path = '../Files/json graphs/'+project_name+'.json'
    CodeFromFile(project_path,project_name, output_path)



def main():
    # code_to_graph_in_json_file('../Files/codes/src1', 'Project 1')
    code_to_graph_in_json_file('../../../Files/codes/maze', 'maze')
    # code_to_graph_in_json_file('../Files/codes/src3', 'Project 3')
    # code_to_graph_in_json_file('../../../Files/codes/poi/common/usermodel')

if __name__ == '__main__':
    main()
