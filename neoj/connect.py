import json

from neo4j import GraphDatabase

# QUERIES:
# MATCH (n) DETACH DELETE n
# MATCH (n) RETURN (n)
from Parser.old_version.Utils.json_functions import read_json_file


class App:

    def __init__(self):
        uri = "neo4j://localhost:7687"
        user = "neo4j"
        password = "1234"

        self.driver = GraphDatabase.driver(uri, auth=(user, password))
        self.session = self.driver.session()

    # def close(self):
    #     self.driver.close()


    def executeQuery(self, query):
        tx = self.session.begin_transaction()
        result = tx.run(query)
        tx.commit()
        return result

    def build_vertices(self, vertices, edges):

        query='CREATE '
        for v in vertices:
            key = v['key']
            name = v['name']
            type = v['type']
            attributes = v['attributes']
            obj = 'Class'
            if type=='method': obj='Method'
            elif type=='interface': obj='Interface'
            query = query + "(v{}:{} ".format(key,obj) + '{' + "key:'{}', name:'{}', type:'{}'".format(key,name,type,attributes) + '}),'

        for e in edges:
            type = e['type']
            source = e['from']
            to = e['to']
            query = query + "((v{})-[:{}]->(v{})),".format(source, type, to)

        query = query[:-1]
        self.executeQuery(query)


def loading_graph_file(path) -> None:
    data :json = read_json_file(path)
    vertices :list = data['vertices']
    edges :list = data['edges']
    return vertices, edges

def main():
    vertices, edges = loading_graph_file('./src1.json')
    app = App()
    app.executeQuery('MATCH (n) DETACH DELETE n')
    app.build_vertices(vertices,edges)
    # app.executeQuery()
    # app.vert(edges)


if __name__ == "__main__":
    main()

    # Aura queries use an encrypted connection using the "neoj+s" URI scheme
    # app = App()
    #
    # g = Graph()
    # v1 = g.add_class('name1', 'type')
    # v2 = g.add_class('name2', 'type2')
    # g.add_edge('extends', v1, v2)
    #
    # app.create_vertex(v1)
    # app.create_vertex(v2)
    # app.create_edge(v1,v2, 'extends')
    #
    # app.close()