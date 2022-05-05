import os
import sqlite3

class VectorsDB:
    def __init__(self):
        self.conn = self.__connect()
        self.crsr = self.conn.cursor()

    # def __del__(self):
    #     self.conn.close()

    def __connect(self):
        conn = sqlite3.connect('./Ranker/database.db', detect_types=sqlite3.PARSE_DECLTYPES)
        # print("db - connected")
        return conn

    def is_table_exist(self, table_name) ->bool:
        try:
            c=self.crsr.execute('SELECT key1 FROM %s' % table_name)
            # print("table already exist")
            return True
        except:
            return False

    def drop_table(self, table_name):
        self.crsr.execute("DROP TABLE IF EXISTS %s;" % table_name)
        self.conn.commit()

    def create_table(self, table_name):
        self.crsr.execute("CREATE TABLE IF NOT EXISTS %s (key1 INT NOT NULL, key2 INT NOT NULL, sim FLOAT NOT NULL);" % table_name)
        self.conn.commit()
        print("table was created")

    def add(self, table_name, key1, key2, sim):
        self.crsr.execute("INSERT INTO %s  VALUES (?,?,?)" % table_name, (key1, key2, sim))
        self.conn.commit()


    def get(self, table_name, key1, key2):
        self.crsr.execute('SELECT sim FROM %s where key1=%s and key2=%s' % (table_name, str(key1), str(key2)))
        sim = self.crsr.fetchall()
        return sim[0][0]

    def print_table(self, table_name):
        print("printingggg")
        self.crsr.execute("SELECT * FROM %s" % table_name)
        ans = self.crsr.fetchall()
        for i in ans:
            key1 = i[0]
            key2 = i[1]
            sim = i[2]
            print(key1,key2,sim)

    def delete_db(self):
        self.conn.close()
        os.remove('./model/vectors.db')
