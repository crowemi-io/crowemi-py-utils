import os
import unittest
from datetime import datetime

from bson import ObjectId

from crowemi.data.mongo import AsyncMongoDBClient, MongoDBClient


class TestAsyncMongoDBClient(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.client = AsyncMongoDBClient(uri="mongodb://root:example@localhost:27017/", database="test_db")

    async def test_create(self):
        ret = await self.client.create(collection="test_collection", data={"test": "test"})
        self.assertTrue(type(ret) == ObjectId)
        return ret

    async def test_create_many(self):
        ret = await self.client.create(collection="test_collection", data=[{"test": "test"}, {"test": "test2"}, {"test": "test3"}], batch=True)
        ids = ret["inserted_ids"]
        self.assertTrue(len(ids) == 3)
        return ret

    async def test_read(self):
        object_id = await self.test_create()
        ret = await self.client.read(collection="test_collection", query={"_id": object_id})
        self.assertTrue(len(ret) > 0)

    async def test_read_projection(self):
        object_id = await self.test_create()
        ret = await self.client.read(collection="test_collection", query={"_id": object_id}, projection={"test": 1})
        # tests that "test" is in the projection
        self.assertTrue("test" in ret[0])
        ret = await self.client.read(collection="test_collection", query={"_id": object_id}, projection={"test": 0})
        # tests that "test" is not in the projection
        self.assertTrue("test" not in ret[0])

    async def test_read_sort(self):
        object_id = await self.test_create()
        ret = await self.client.read(collection="test_collection", query={"_id": object_id}, projection={}, sort=[("test", 1)])
        # tests that the result is sorted by "test" in ascending order
        self.assertTrue(ret[0]["test"] == "test")

    async def test_delete(self):
        object_id = await self.test_create()
        ret = await self.client.delete(collection="test_collection", query={"_id": object_id})
        self.assertTrue(ret > 0)

    async def test_update(self):
        object_id = await self.test_create()
        ret = await self.client.update(collection="test_collection", query={"_id": object_id}, data={'$set': {"test": "updated_test"}})
        self.assertTrue(ret > 0)

    async def test_updsert(self):
        ret = await self.client.update(collection="test_collection", query={"test": "upsert_test22"}, data={'$set': {"test": "updated"}}, upsert=True)
        self.assertTrue(ret > 0)

class TestMongoDBClient(unittest.TestCase):
    def setUp(self):
        self.client = MongoDBClient(uri="mongodb://root:example@localhost:27017/", database="test_db")

    def test_create(self):
        ret = self.client.create(collection="test_collection", data={"test": "test"})
        self.assertTrue(type(ret) == ObjectId)
        return ret

    def test_read(self):
        object_id = self.test_create()
        ret = self.client.read(collection="test_collection", query={"_id": object_id})
        self.assertTrue(len(ret) > 0)

    def test_delete(self):
        object_id = self.test_create()
        ret = self.client.delete(collection="test_collection", query={"_id": object_id})
        self.assertTrue(ret > 0)

    def test_update(self):
        object_id = self.test_create()
        ret = self.client.update(collection="test_collection", query={"_id": object_id}, data={'$set': {"test": "updated_test"}})
        self.assertTrue(ret > 0)


if __name__ == '__main__':
    unittest.main()