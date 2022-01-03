import json
import os
import string

from Preprocess.Parser.CodeFromFile import CodeFromFile


def code_to_graph(project_path, output_path, project_name=''):
    folder_name :string= os.path.basename(project_path)
    if project_name is '':
        project_name = folder_name
    code_from_file = CodeFromFile(project_path,project_name, output_path)
    code_from_file.concat_files()
    connect_between_classes(output_path)
    # code_from_file.test_new_file()

def connect_between_classes(json_file):
    f = open(json_file)
    data = json.load(f)
    f.close()
    map = {}
    vertices = data["vertices"]
    new_edges = []

    for v in vertices:
        name = v["name"]
        key = v["key"]
        type = v["type"]
        if type=="class":
            map[name] = key

    for v in vertices:
        key = v["key"]
        if "attributes" in v:
            attributes = v["attributes"]
            for attr in attributes:
                obj = attr.split(' ')[0]
                if obj in map.keys():
                    new_edge = {}
                    to = map[obj]
                    print(obj," ",to)
                    new_edge["type"] = "contains"
                    new_edge["from"] = key
                    new_edge["to"] = to
                    new_edges.append(new_edge)
    edges = data["edges"]
    edges= edges + new_edges
    new_json = {}
    new_json["vertices"] = vertices
    new_json["edges"] = edges
    save_to_file(new_json,json_file)


def save_to_file(json_object,output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)


def main():
    code_to_graph('../Files/codes/src', '../Files/json graphs/out1.json','iterable list practice')
    # code_to_graph('../Files/codes/src2','../Files/json graphs/out2.json')
    # code_to_graph('../Files/codes/src3','../Files/json graphs/out3.json')


if __name__ == '__main__':
    main()
