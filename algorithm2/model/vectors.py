import os
import fasttext
import sqlite3
import numpy as np
import io

from scipy import spatial
from scipy.spatial import distance
from Parser.codeToGraph.code_to_graph import CodeParser

class WordEmbedding:
    def __init__(self, graph, project_name):
        self.graph = graph
        self.table_name = project_name
        self.conn = self.build()
        self.crsr = self.conn.cursor()
        if not self.is_table_exist():
            self.create_table()
            self.build_table()

    def __del__(self):
        self.conn.close()

    def is_table_exist(self) ->bool:
        try:
            self.crsr.execute('SELECT key FROM %s' % self.table_name)
            return True
        except:
            return False


    def build_table(self):
        model = fasttext.load_model('model/cc.en.300.bin')
        for v in self.graph.get_vertices():
            key = v.key
            vector = model[v.name]
            self.insert_vector(key, vector)

    def adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def build(self):
        sqlite3.register_adapter(np.ndarray, self.adapt_array)
        sqlite3.register_converter("array", self.convert_array)
        conn = sqlite3.connect('vectors.db', detect_types=sqlite3.PARSE_DECLTYPES)
        return conn

    def drop_table(self):
        self.crsr.execute("DROP TABLE IF EXISTS %s;" % self.table_name)
        self.conn.commit()

    def create_table(self):
        self.crsr.execute("CREATE TABLE IF NOT EXISTS %s (key INT PRIMARY KEY NOT NULL, vector array NOT NULL);" % self.table_name)
        self.conn.commit()

    def insert_vector(self,key, x): # numpy.ndarray
        self.crsr.execute("INSERT INTO %s  VALUES (?,?)" % self.table_name, (key, x))
        self.conn.commit()

    def __getitem__(self, key):
        if isinstance(key, int):
            # crsr = conn.cursor()
            self.key = str(key)
            self.crsr.execute('SELECT * FROM %s where key=%s' % (self.table_name, key))
            vector = self.crsr.fetchall()
            res = vector[0][1]
        else:
            model = fasttext.load_model('cc.en.300.bin')
            res = model[key]
        return res




    def print_table(self):
        self.crsr.execute("SELECT * FROM %s" % self.table_name)
        ans = self.crsr.fetchall()
        for i in ans:
            key = i[0]
            vector = i[1]
            # print(key)
        print(len(ans))

    def delete_db(self):
        self.conn.close()
        os.remove('vectors.db')

    def euclid_distance(self, v1, v2):
        # distance.euclidean(v1, v2)
        return 1.0 - spatial.distance.cosine(v1, v2)

def main():
    g = CodeParser('../../Files/codes/src1').graph
    model = WordEmbedding(g, 'src1')
    # model.print_table()

    # g.print_vertices()
    v1 = model["list"]
    v1 = model["delete"]
    v2 = model["blue"]
    d = model.euclid_distance(v1, v2)
    # print(d)


if __name__ == '__main__':
    main()