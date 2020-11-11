# Database manager for controlling the database
import json

import pandas as pd
from sqlalchemy import create_engine


class DatabaseManager(object):

    # init a database named db_name
    def __init__(self, db_name):
        # self.engine is used for the pandas
        sql = 'sqlite:///%s' % db_name
        self.engine = create_engine(sql)

    # store json data to the sql , and return true
    def store_json(self, data):
        tmp = json.loads(data)
        frame = pd.DataFrame([(tmp['name'][0], tmp['title'][0], tmp['tel'][0], tmp['email'][0], tmp['comp'][0],
                               tmp['addr'][0])], columns=['name', 'title', 'telephone', 'email', 'company', 'address'])
        frame.to_sql('datas', con=self.engine, index=False, if_exists='append')

        return True

    # stor dict data to the sql , and return true
    def store_dict(self, data):
        print(data)
        frame = pd.DataFrame(
            [(data['name'], data['title'], data['telephone'], data['email'], data['company'], data['address'])],
            columns=['name', 'title', 'telephone', 'email', 'company', 'address'])
        frame.to_sql('datas', con=self.engine, index=False, if_exists='append')
        return True

    # fuzzy search
    def search(self, s):
        sql = "select * from datas where (name like '%s') or (title like '%s') or (telephone like '%s') or (email like '%s') or (company like '%s') or (address like '%s')" % (
            '%' + s + '%', '%' + s + '%', '%' + s + '%', '%' + s + '%', '%' + s + '%', '%' + s + '%')
        lines = pd.read_sql_query(sql, con=self.engine, index_col=None)

        return lines

    def get_all(self):
        lines = pd.read_sql('datas', self.engine, columns=['name', 'title', 'telephone', 'email', 'company', 'address'])
        return lines
