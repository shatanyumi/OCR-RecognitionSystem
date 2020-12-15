# Database manager for controlling the database
import json
import time

import pandas as pd
from sqlalchemy import create_engine


class DatabaseManager(object):

    # init a database named db_name
    def __init__(self, db_name):
        # self.engine is used for the pandas
        sql = 'sqlite:///%s' % db_name
        self.engine = create_engine(sql)

    def set_tablename(self, tablename):
        self.table_name = tablename

    # store json data to the sql , and return true
    def store_json(self, data):
        data_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        tmp = json.loads(data)
        frame = pd.DataFrame([(tmp['name'][0], tmp['title'][0], tmp['mobile'][0], tmp['email'][0], tmp['comp'][0],
                               tmp['addr'][0], data_id)],
                             columns=['name', 'title', 'tel', 'email', 'comp', 'addr', 'id'])
        frame.to_sql(self.table_name, con=self.engine, index=False, if_exists='append')

        return True

    # stor dict data to the sql , and return true
    def store_dict(self, data):
        # print(data)
        data_id = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        frame = pd.DataFrame(
            [(data['name'], data['title'], data['mobile'], data['email'], data['comp'],
              data['addr'], data_id)],
            columns=['name', 'title', 'tel', 'email', 'comp', 'addr', 'id'])
        frame.to_sql(self.table_name, con=self.engine, index=False, if_exists='append')
        return data_id

    # update a data by id
    def update(self, data):
        sql = "update %s set name='%s' , title='%s', tel='%s', email='%s', comp='%s', addr='%s' where id=%s" % (
            self.table_name, data['name'], data['title'], data['mobile'], data['email'], data['comp'], data['addr'],
            data['id'])
        self.engine.execute(sql)

    # delete a data by id
    def delete(self, id):
        sql = "delete from %s where id = %s" % (self.table_name, id)
        self.engine.execute(sql)

    # fuzzy search
    def search(self, attrbute, s):
        sql = "select * from %s where ( %s like '%s')" % (self.table_name, attrbute, '%' + s + '%')
        lines = pd.read_sql_query(sql, con=self.engine, index_col=None)
        return lines

    def get_all(self):
        lines = pd.read_sql(self.table_name, self.engine,
                            columns=['name', 'title', 'tel', 'email', 'comp', 'addr', 'id'])
        return lines


if __name__ == '__main__':
    database = DatabaseManager('system.db')
    database.set_tablename('peoples')
    print(database.get_all())
    data = {'name': 'name', 'title': 'title', 'tel': 'tel', 'email': 'email', 'comp': 'comp', 'addr': 'addr',
            'id': '20201114223505'}
    print(database.search('name', 'aaa'))
    # print(database.get_all())
