import json


def create_json_file_for_viewer(json_file):
    f = open(json_file)
    data = json.load(f)
    f.close()
    map = {}
    vertices = data["vertices"]
    new_edges = []

    for v in vertices:
        name = v["name"]
        key = v["key"]
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
                    new_edge["type"] = "contains"
                    new_edge["from"] = key
                    new_edge["to"] = to
                    new_edges.append(new_edge)
    edges = data["edges"]
    edges= edges + new_edges

    j2 = {}
    j2["vertices"] = vertices
    j2["edges"] = edges
    save_to_file(j2,json_file)


def save_to_file(json_object,output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)


def main():
    create_json_file_for_viewer('../Files/json graphs/out1.json')

if __name__ == '__main__':
    main()