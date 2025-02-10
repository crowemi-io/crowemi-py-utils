from pymongo import MongoClient


class MongoClient():
    def __init__(self, uri: str, database: str):
        self.client: MongoClient = MongoClient(uri)
        self.db = self.client.get_database(database)

    def read(self, collection: str, query: dict):
        try:
            ret = list()
            res = self.db.get_collection(collection).find(query)
            [ret.append(doc) for doc in res]
            return ret
        except Exception as e:
            raise e

    def create(self, collection: str, data: dict):
        try:
            return self.db.get_collection(collection).insert_one(data).inserted_id
        except Exception as e:
            raise e
        
    def update(self, collection: str, query: dict, data: dict):
        try:
            return self.db.get_collection(collection).update_one(filter=query, update=data)
        except Exception as e:
            raise e
        
    def delete(self, collection: str, query: dict):
        try:
            return self.db.get_collection(collection).delete_many(query)
        except Exception as e:
            raise e
