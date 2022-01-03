import json

# go to: http://khmap.ise.bgu.ac.il/map/
# and import the output file

def main():
    create_json_file_for_viewer('../Files/json graphs/out1.json')
    # create_json_file_for_viewer('../Files/json graphs/out2.json', '../Files/json graphs for viewer/out2.json')
    # create_json_file_for_viewer('../Files/json graphs/out3.json', '../Files/json graphs for viewer/out3.json')

def create_json_file_for_viewer(json_file):
    f = open(json_file)
    data = json.load(f)
    f.close()

    vertices = parse_vertices(data["vertices"])
    edges = parse_edges(data["edges"])

    project_name = json_file.split('/')[-1]
    j2 = {}
    j2["class"] = "go.GraphLinksModel"
    j2["nodeDataArray"] = vertices
    j2["linkDataArray"] = edges
    save_to_file(j2, '../Files/json graphs for viewer/'+project_name)

def parse_vertices(vertices):
    new_vertices = []
    for v in vertices:
        new_v = {}
        new_v["category"] = v["type"]
        new_v["text"] = v["name"]
        new_v["fill"] = "#ffffff"
        new_v["stroke"] = "#000000"
        new_v["strokeWidth"] = 1
        new_v["key"] = v["key"]
        new_v["loc"] = ""
        new_v["refs"] = []
        new_v["ctxs"] = []
        new_v["comment"] = ''
        new_vertices.append(new_v)
    return new_vertices

def parse_edges(edges):
    new_edges = []
    for e in edges:
        new_e = {}
        new_e["category"] = e["type"]
        new_e["text"] = ''
        new_e["routing"] = {"yb": "Normal", "oE": 1}
        new_e["points"] = ''
        new_e["from"] = e["from"]
        new_e["to"] = e["to"]
        new_e["refs"] = []
        new_e["ctxs"] = []
        new_e["comment"] = ''
        new_edges.append(new_e)
    return new_edges

def save_to_file(json_object,output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(json_object, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
