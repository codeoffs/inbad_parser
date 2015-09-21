import sqlite3
import time

class db():
    def __init__(self):
        self.con = sqlite3.connect('db_pars.sqlite3')
        try:
            self.create_tb()
        except Exception:
            print('Table Exists')

    def create_tb(self):
        cur = self.con.cursor()
        cur.execute("CREATE TABLE `inbad` (\
	        `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
	        `title`	TEXT,\
	        `descript`	TEXT,\
	        `img`	TEXT,\
	        `attr`	TEXT,\
	        `timestemp`	INTEGER\
        )")
        self.con.commit()

    def inser_data(self, array_data):
        #print(array_data)
        cur = self.con.cursor()

        cur.execute("INSERT INTO `inbad` (`title`, `descript`, `img`, `attr`, `timestemp`)\
                    VALUES ('"+array_data['title'][0]+"','"+array_data['descript'][0]+"','"+str(array_data['img'])+"','"+str(array_data['attr'])+"','"+str(round(time.time()))+"')")
        self.con.commit()
