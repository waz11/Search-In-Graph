import json


def list_to_json(list:list) -> json:
    json = []
    for element in list:
        json.append(element.toJson())
    return json

def get_data_from_json_file(path) -> json:
    f = open(path)
    data = json.load(f)
    f.close()
    return data

def save_json_to_file(json_object, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)