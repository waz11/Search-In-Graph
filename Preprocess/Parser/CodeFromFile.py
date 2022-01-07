import json
import os
from pathlib import Path
import re

from Preprocess.Parser.CodeWrapper import CodeWrapper
from Preprocess.Parser.MapCreator import MapCreator
from Preprocess.Parser.CodeParser import codeParser
from Utils.json_functions import save_json_to_file, get_data_from_json_file


class CodeFromFile:
    def __init__(self, file_path, name, output_path=""):
        self.file_path = file_path
        self.directory = os.fsencode(self.file_path)
        self.name = name
        self.output_path = output_path
        self.full_code_text = ""
        self.code_parser = codeParser()
        self.concat_files()
        self.connect_between_classes()


    def concat_files(self):
        pathlist = Path(self.file_path).glob('**/*.java')
        for path in pathlist:
            path_in_str = str(path)
            with open(path_in_str, "r") as f:
                self.full_code_text += f.read()
                self.full_code_text = re.sub("package(.*?);", '', self.full_code_text)
                self.full_code_text = re.sub("import(.*?);", '', self.full_code_text)
                self.create_parse_and_map()

    def connect_between_classes(self):
        data = get_data_from_json_file(self.output_path)
        map = {}
        vertices = data["vertices"]
        new_edges = []

        for v in vertices:
            print(v)
            name = v["name"]
            key = v["key"]
            type = v["type"]
            if type == "class":
                map[name] = key

        for v in vertices:
            key = v["key"]
            attributes_types = set()
            if "attributes" in v:
                attributes = v["attributes"]
                for attr in attributes:
                    obj = attr.split(' ')[0]
                    if obj in map.keys():
                        new_edge = {}
                        to = map[obj]
                        new_edge["type"] = "contains"
                        new_edge["from"] = key
                        new_edge["to"] = to
                        if not to in attributes_types:
                            attributes_types.add(to)
                            new_edges.append(new_edge)
        edges = data["edges"]
        edges = edges + new_edges
        new_json = {}
        new_json["vertices"] = vertices
        new_json["edges"] = edges
        save_json_to_file(new_json, self.output_path)


    def create_parse_and_map(self):
        code_file = CodeWrapper(self.name, self.name)
        mapped_code = self.code_parser.parse_post(self.full_code_text, code_file)
        map_code = MapCreator(mapped_code)
        task_dict = map_code.create_dictionary(code_file)
        if not self.output_path:
            self.output_path = "output_json.json"
        with open(self.output_path, 'w') as fp:
            json.dump(task_dict, fp)


    # def test_new_file(self):
    #     pathlist = Path(self.file_path).glob('**/*.java')
    #     for path in pathlist:
    #         path_in_str = str(path)
    #         self.full_code_text = ""
    #         with open(path_in_str, "r") as f:
    #             print(path_in_str.split('/')[-1].split('.')[0])
    #             self.full_code_text += f.read()
    #             self.full_code_text = re.sub("package(.*?);", '', self.full_code_text)
    #             self.full_code_text = re.sub("import(.*?);", '', self.full_code_text)