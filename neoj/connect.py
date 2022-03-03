from neo4j import GraphDatabase

# QUERIES:
# MATCH (n) DETACH DELETE n
# MATCH (n) RETURN (n)

class App:

    def __init__(self):
        uri = "neo4j+s://4a367a96.databases.neo4j.io"
        user = 'neoj'
        password = 'tOfwQzxEEpycCb4X2hL2VkUjMBp5W86lyhhoezAXJL0'
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        # Don't forget to close the driver connection when you are finished with it
        self.driver.close()

    def create_vertex(self, v1):
        with self.driver.session() as session:
            session.write_transaction(self.add_vertex, v1)

    def create_edge(self, source, to, type):
        with self.driver.session() as session:
            session.write_transaction(self.add_edge, source, to, type)

    @staticmethod
    def add_vertex(tx, vertex):
        query = (
            "CREATE (v:Vertex "
            "{ key: $key, name: $name, type: $type }) "
        )
        tx.run(query, key=vertex.key, name=vertex.name, type=vertex.type)

    @staticmethod
    def add_edge(tx, source, to, type):
        if type=='extends':
            query = """MATCH
              (a:Vertex),
              (b:Vertex)
            WHERE a.key = $key1 AND b.key = $key2
            CREATE (a)-[r:extends {key: a.key + 'extends' + b.key}]->(b)
            RETURN type(r)"""
        if type=='implements':
            query = """MATCH
              (a:Vertex),
              (b:Vertex)
            WHERE a.key = $key1 AND b.key = $key2
            CREATE (a)-[r:implements {key: a.key + ' implements ' + b.key}]->(b)
            RETURN type(r)"""
        tx.run(query, key1=source.key, key2=to.key, type=type)


if __name__ == "__main__":
    # Aura queries use an encrypted connection using the "neoj+s" URI scheme
    app = App()
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