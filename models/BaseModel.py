from bson import ObjectId


class BaseModel:

    _collection = None

    def __init__(self, document):
        self._document = document
        self._id = document.get('id', None)

    @classmethod
    def collection(cls, db):
        return db[cls._collection]

    @classmethod
    async def get(cls, db, query):
        collection = cls.collection(db)

        return await collection.find_one(query)

    @classmethod
    async def find(cls, db, query):
        collection = cls.collection(db)

        cursor = collection.find(query)
        result = []

        while await cursor.fetch_next:
            user = cursor.next_object()
            user['_id'] = str(user['_id'])
            result.append(user)

        return result

    @classmethod
    async def insert(cls, db, document):
        collection = cls.collection(db)

        obj_id = await collection.insert_one(document)

        return obj_id

    @classmethod
    async def update(cls, db, query, document, **kwargs):
        collection = cls.collection(db)

        await collection.update(query, document, **kwargs)

    async def save(self, db):
        if not self._id:
            self._id = ObjectId()
            self._document['id'] = self._id

        await self.update(db, {'_id': self._id}, self._document, upsert=True)