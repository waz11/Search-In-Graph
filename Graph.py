import json


class Graph:

    def __init__(self, path):
        self.graph = {}
        self.vertex_info = {}
        self.vertex_type = {}
        self.edge_info = {}
        self.__build_graph(path)

    def __build_graph(self, path):
        f = open(path)
        data = json.load(f)
        for node in data['vertices']:
            self.graph[node["key"]] = []
            self.vertex_info[node["key"]] = node["name"]
            self.vertex_type[node["key"]] = node["type"]
        for edge in data['edges']:
            self.graph[edge["from"]].append(edge["to"])
            self.edge_info[(edge["from"], edge["to"])] = edge["type"]
        f.close()

        # print(self.graph)
        # print(self.vertex_info)
        # print(self.vertex_type)
        # print(self.edge_info)

    def num_of_vertices(self):
        return len(self.vertex_info)

    def neighbors(self, key):
        return self.graph[key]

    def edge_type(self, from_node, to_node):
        return self.edge_info[(from_node, to_node)]

    def vertex_text(self, key):
        return self.vertex_info[key]

    def get_first_node(self):
        return self.vertex_info[0]

    def get_type(self, id):
        return self.vertex_type[id]

    def bfs(self):
        print(str(self.vertex_info))
        print(str(self.graph))
        queue = [0]
        visited = {}
        for key in self.graph:
            visited[key] = False
        while queue:
            vertex = queue.pop(0)
            visited[vertex] = True
            print("ID:" + str(vertex) + " Text: " + self.vertex_info[vertex])
            print("My neighbor:")
            i = 0
            for key in self.graph[vertex]:
                i += 1
                if not visited[key]:
                    queue.append(key)
                print("ID:"+str(key)+" Text: "+self.vertex_info[key])