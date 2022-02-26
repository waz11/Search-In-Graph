import os
import fasttext
import sqlite3
import numpy as np
import io
from Parser.codeToGraph.code_to_graph import CodeParser

class VecDB:
    def __init__(self, table_name="src"):
        self.table_name = table_name
        self.conn = self.build()
        self.crsr = self.conn.cursor()
        # if not self.is_table_exist():
        #     self.create_table()

    def __del__(self):
        self.conn.close()

    def is_table_exist(self) ->bool:
        try:
            self.crsr.execute('SELECT key FROM %s' % self.table_name)
            return True
        except:
            return False

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
        if not self.db.is_table_exist():
            self.crsr.execute("CREATE TABLE IF NOT EXISTS %s (key INT PRIMARY KEY NOT NULL, vector array NOT NULL);" % self.table_name)
            self.conn.commit()

    def insert_vector(self,key, vector): # numpy.ndarray
        self.crsr.execute("INSERT INTO %s  VALUES (?,?)" % self.table_name, (key, vector))
        self.conn.commit()

    def get(self, key):
        self.crsr.execute('SELECT * FROM %s where key=%s' % (self.table_name, str(key)))
        vector = self.crsr.fetchall()
        res = vector[0][1]
        return res

    def print_table(self):
        self.crsr.execute("SELECT * FROM %s" % self.table_name)
        ans = self.crsr.fetchall()
        for i in ans:
            key = i[0]
            vector = i[1]
            print(key, vector[0])

    def delete_db(self):
        self.conn.close()
        os.remove('vectors.db')



def main():
    db = VecDB('src1')
    g = CodeParser('../../../Files/codes/src1').graph
    # model = VecDB(g, 'src1')
    # model.print_table()

    # g.print_vertices()
    # v1 = model[2]
    # v2 = model[1]
    # d = model.euclid_distance(v1, v2)
    # print(d)
    pass


if __name__ == '__main__':
    main()