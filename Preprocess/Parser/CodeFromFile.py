import json
import os
from pathlib import Path
import re

from Preprocess.Parser.CodeWrapper import CodeWrapper
from Preprocess.Parser.MapCreator import MapCreator
from Preprocess.Parser.CodeParser import codeParser

class CodeFromFile:
    def __init__(self, file_path, name, output_path=""):
        self.file_path = file_path
        self.directory = os.fsencode(self.file_path)
        self.name = name
        self.output_path = output_path
        self.full_code_text = ""
        self.code_parser = codeParser()


    def concat_files(self):
        pathlist = Path(self.file_path).glob('**/*.java')
        for path in pathlist:
            path_in_str = str(path)
            with open(path_in_str, "r") as f:
                self.full_code_text += f.read()
                self.full_code_text = re.sub("package(.*?);", '', self.full_code_text)
                self.full_code_text = re.sub("import(.*?);", '', self.full_code_text)
                self.create_parse_and_map()


    def create_parse_and_map(self):
        code_file = CodeWrapper(self.name, self.name)

        mapped_code = self.code_parser.parse_post(self.full_code_text, code_file)

        map_code = MapCreator(mapped_code)
        task_dict = map_code.create_dictionary(code_file)
        if not self.output_path:
            self.output_path = "output_json.json"
        with open(self.output_path, 'w') as fp:
            json.dump(task_dict, fp)


    def test_new_file(self):
        pathlist = Path(self.file_path).glob('**/*.java')
        for path in pathlist:
            # because path is object not string
            path_in_str = str(path)
            # print(path_in_str)
            self.full_code_text = ""
            with open(path_in_str, "r") as f:
                print(path_in_str.split('/')[-1].split('.')[0])
                self.full_code_text += f.read()
                self.full_code_text = re.sub("package(.*?);", '', self.full_code_text)
                self.full_code_text = re.sub("import(.*?);", '', self.full_code_text)

            current_query = CodeWrapper(self.name, self.name)
            mapped_code = self.code_parser.parse_post(self.full_code_text, current_query)