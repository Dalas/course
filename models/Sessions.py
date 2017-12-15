from bson import ObjectId
from uuid import uuid4


class Sessions:

    @staticmethod
    async def insert(db, data):
        data['_id'] = ObjectId()
        session_id = await db.Sessions.insert(data)
        return session_id

    @staticmethod
    async def update_or_create(db, user_id):
        session = {
            'token': str(uuid4()),
            'user_id': user_id
        }

        await db.Sessions.update({'user_id': user_id}, session, upsert=True)

        return session

    @staticmethod
    async def find_by_token(db, token):
        data = await db.Sessions.find_one({'token': token})
        return data
