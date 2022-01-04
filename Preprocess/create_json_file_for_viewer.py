import json

# go to: http://khmap.ise.bgu.ac.il/map/
# and import the output file

from Graph.graph import Graph
from Utils.json_functions import read_json_file, save_json_to_file


def main():
    g = Graph('../Files/json graphs/src1.json')
    create_json_file_for_viewer(g.get_vertex(), g.get_edges(), 'src1')

def create_json_file_for_viewer(vertices:list=[], edges:list=[],graph_name='src'):
    vertices = __parse_vertices(vertices)
    edges = __parse_edges(edges)
    json = {}
    json["class"] = "go.GraphLinksModel"
    json["nodeDataArray"] = vertices
    json["linkDataArray"] = edges
    save_json_to_file(json, '../Files/json graphs for viewer/'+graph_name+'.json')

def __parse_vertices(vertices):
    new_vertices = []
    for v in vertices:
        new_v = {}
        if v.type == "class":
            new_v["category"] = "Task"
            new_v["strokeWidth"] = 2
        elif v.type == "method":
            new_v["category"] = "Quality"
            new_v["stroke"] = "rgb(255, 0, 0"
            new_v["strokeWidth"] = 1
        new_v["text"] = v.name
        new_v["key"] = v.key
        new_vertices.append(new_v)
    return new_vertices

def __parse_edges(edges):
    new_edges = []
    for e in edges:
        new_e = {}
        new_e["category"] = e.type
        new_e["text"] = ''
        if e.type == "extends":
            new_e["category"] = "ExtendedBy"
            new_e["text"] = 'extends'
        elif e.type == "implements":
            new_e["category"] = "ExtendedBy"
            new_e["text"] = 'implements'
        elif e.type == "method":
            new_e["category"] = "Contribution"
            new_e["text"] = 'method'
        new_e["from"] = e.source.key
        new_e["to"] = e.to.key
        new_edges.append(new_e)
    return new_edges


if __name__ == '__main__':
    main()
