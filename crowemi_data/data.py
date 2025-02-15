import uuid
from pymongo import MongoClient, AsyncMongoClient


class MongoDBClient():
    def __init__(self, uri: str, database: str = "crowemi-trades", session_id: str = None):

        if not session_id:
            session_id = uuid.uuid4().hex
        self.session_id = session_id

        self.client: MongoClient = MongoClient(uri)
        self.async_client: AsyncMongoClient = AsyncMongoClient(uri)

        self.db = self.client.get_database(database)

    def read(self, collection: str, query: dict):
        try:
            ret = list()
            res = self.db.get_collection(collection).find(query)
            [ret.append(doc) for doc in res]
            return ret
        except Exception as e:
            raise e

    async def read(self, collection: str, query: dict):
        try:
            ret = list()
            database = self.async_client.get_database(self.db)
            collection = database.get_collection(collection)
            res = await collection.find(query)
            [ret.append(doc) for doc in res]
            return ret
        except Exception as e:
            raise e

    def create(self, collection: str, data: dict):
        try:
            database = self.client.get_database(self.db)
            collection = database.get_collection(collection)
            return collection.insert_one(data).inserted_id
        except Exception as e:
            raise e

    async def create(self, collection: str, data: dict):
        try:
            database = self.async_client.get_database(self.db)
            collection = database.get_collection(collection)
            return await collection.insert_one(data).inserted_id
        except Exception as e:
            raise e

    def update(self, collection: str, query: dict, data: dict):
        try:
            database = self.client.get_database(self.db)
            collection = database.get_collection(collection)
            return collection.update_one(filter=query, update=data)
        except Exception as e:
            raise e

    async def update(self, collection: str, query: dict, data: dict):
        try:
            database = self.async_client.get_database(self.db)
            collection = database.get_collection(collection)
            return await collection.update_one(filter=query, update=data)
        except Exception as e:
            raise e
        
    def delete(self, collection: str, query: dict):
        try:
            database = self.client.get_database(self.db)
            collection = database.get_collection(collection)
            return collection.delete_many(query)
        except Exception as e:
            raise e

    async def delete(self, collection: str, query: dict):
        try:
            database = self.async_client.get_database(self.db)
            collection = database.get_collection(collection)
            return await collection.delete_many(query)
        except Exception as e:
            raise e
