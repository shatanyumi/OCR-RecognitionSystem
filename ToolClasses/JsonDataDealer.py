# Json Data Dealer to deal the json, and return the data

from DatabaseManager import DatabaseManager as dm


class JsonDataDealer(object):

    def store(self, jsons):
        tmp = jsons.loads(jsons)
        dbs = dm.DatabaseManager('lab.db')
        dbs.store_json(tmp)
