# Database manager for controlling the database
import sqlite3
import pandas as pd
import json

class DatabaseManager(object):

    # init a database named db_name
    # 不知道这个函数会不会先自动执行
    def __init__(self, db_name):
        # self.db is a connection
        self.db = sqlite3.connect(db_name)

    def store(self, jsonstr):
        state = False

        self.jsonstr = jsonstr
        data_map = json.loads(self.jsonstr)
        data_tmp = [[d['name'][0], d['title'][0], d['tel'][0], d['email'][0], d['comp'][0],
                          d['addr'][0]] for d in data_map]
        df = pd.DataFrame(data_tmp, columns=['name', 'title', 'tel', 'email', 'comp', 'addr'])

        #不确定这里的state是否有用，能不能收到返回值
        state = df.to_sql('datas', con=self.db, if_exists='append')

        self.db.commit()
        self.db.close()

        return state

    def get(self, str):
        cur = self.db.cursor()

        # 模糊查找
        line = cur.execute("select * from datas where (name like'%" & str & "%') or (title like'%" & str & "%') or (tel like'%" & str & "%') or (email like'%" & str & "%') or (comp like'%" & str & "%') or (addr like'%" & str & "%')")

        self.db.commit()
        self.db.close()

        return line

    def get_all(self):
        cur = self.db.cursor()

        tables = cur.execute("select name,title,telephone,email,company,address from datas")

        self.db.commit()
        self.db.close()

        return tables
