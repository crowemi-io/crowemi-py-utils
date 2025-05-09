import uuid
from pymongo import MongoClient, AsyncMongoClient


MAX_POOL_SIZE = 10
MIN_POOL_SIZE = 1
MAX_IDLE_TIME = 60000 # 60 seconds

class Base():
    def __init__(self, database: str, session_id: str = None):
        if not session_id:
            session_id = uuid.uuid4().hex
        self.session_id = session_id
        self.database = database

class AsyncMongoDBClient(Base):
    def __init__(self, uri: str, database: str, session_id: str = None):
        super().__init__(database, session_id)
        self.client: AsyncMongoClient = AsyncMongoClient(uri, maxPoolSize=MAX_POOL_SIZE, minPoolSize=MIN_POOL_SIZE, maxIdleTimeMS = MAX_IDLE_TIME)

    async def create(self, collection: str, data: dict) -> str:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = await collection.insert_one(data)
            return ret.inserted_id
        except Exception as e:
            raise e

    async def read(self, collection: str, query: dict, projection: dict) -> list:
        try:
            ret = list()
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = await collection.find(query, projection).to_list(length=None)
            return ret
        except Exception as e:
            raise e

    async def update(self, collection: str, query: dict, data: dict) -> int:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = await collection.update_one(filter=query, update=data)
            return ret.modified_count
        except Exception as e:
            raise e

    async def delete(self, collection: str, query: dict) -> int:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = await collection.delete_many(query)
            return ret.deleted_count
        except Exception as e:
            raise e


class MongoDBClient(Base):
    def __init__(self, uri: str, database: str, session_id: str = None):
        super().__init__(database, session_id)
        self.client: MongoClient = MongoClient(uri, maxPoolSize=MAX_POOL_SIZE, minPoolSize=MIN_POOL_SIZE, maxIdleTimeMS = MAX_IDLE_TIME)

    def create(self, collection: str, data: dict) -> str:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = collection.insert_one(data)
            return ret.inserted_id
        except Exception as e:
            raise e

    def read(self, collection: str, query: dict) -> list:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = collection.find(query).to_list(length=None)
            return ret
        except Exception as e:
            raise e

    def update(self, collection: str, query: dict, data: dict) -> int:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = collection.update_one(filter=query, update=data)
            return ret.modified_count
        except Exception as e:
            raise e

    def delete(self, collection: str, query: dict) -> int:
        try:
            database = self.client.get_database(self.database)
            collection = database.get_collection(collection)
            ret = collection.delete_many(query)
            return ret.deleted_count
        except Exception as e:
            raise e

