import os
import fasttext
import sqlite3
import numpy as np
import io
from Parser.codeToGraph.code_to_graph import CodeParser

class VectorsDB:
    def __init__(self):
        self.conn = self.__connect()
        self.crsr = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def __adapt_array(self, arr):
        out = io.BytesIO()
        np.save(out, arr)
        out.seek(0)
        return sqlite3.Binary(out.read())

    def __convert_array(self, text):
        out = io.BytesIO(text)
        out.seek(0)
        return np.load(out)

    def __connect(self):
        sqlite3.register_adapter(np.ndarray, self.__adapt_array)
        sqlite3.register_converter("array", self.__convert_array)
        conn = sqlite3.connect('vectors.db', detect_types=sqlite3.PARSE_DECLTYPES)
        print("db - connected")
        return conn



    def is_table_exist(self, table_name) ->bool:
        try:
            self.crsr.execute('SELECT key FROM %s' % table_name)
            print("table already exist")
            return True
        except:
            return False

    def drop_table(self, table_name):
        self.crsr.execute("DROP TABLE IF EXISTS %s;" % table_name)
        self.conn.commit()

    def create_table(self, table_name):
        self.crsr.execute("CREATE TABLE IF NOT EXISTS %s (key INT PRIMARY KEY NOT NULL, vector array NOT NULL);" % table_name)
        self.conn.commit()
        print("table was created")

    def insert_vector(self,table_name, key, vector): # numpy.ndarray
        self.crsr.execute("INSERT INTO %s  VALUES (?,?)" % table_name, (key, vector))
        self.conn.commit()

    def get(self, table_name, key):
        self.crsr.execute('SELECT * FROM %s where key=%s' % (table_name, str(key)))
        vector = self.crsr.fetchall()
        if len(vector) >0:
            return vector[0][1]
        return 0

    def print_table(self, table_name):
        self.crsr.execute("SELECT * FROM %s" % table_name)
        ans = self.crsr.fetchall()
        for i in ans:
            key = i[0]
            vector = i[1]
            print(key, vector[0])

    def delete_db(self):
        self.conn.close()
        os.remove('./model/vectors.db')



def main():
    db = VectorsDB()
    res = db.is_table_exist("src1")
    print(res)
    db.print_table("src1")


if __name__ == '__main__':
    main()
