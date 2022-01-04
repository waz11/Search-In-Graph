import os
import string
from Preprocess.Parser.CodeFromFile import CodeFromFile

# building graph from java project to json file
def code_to_graph(project_path, project_name=''):
    folder_name :string= os.path.basename(project_path)
    if project_name is '':
        project_name = folder_name
    output_path = '../Files/json graphs/'+folder_name+'.json'
    CodeFromFile(project_path,project_name, output_path)


def main():
    code_to_graph('../Files/codes/src1','Project 1')
    code_to_graph('../Files/codes/src2','Project 2')
    code_to_graph('../Files/codes/src3','Project 3')

if __name__ == '__main__':
    main()
