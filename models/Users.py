from bson import ObjectId
from .Sessions import Sessions


class Users:

    @staticmethod
    async def find_one(db, query):
        user = await db.Users.find_one(query)

        if not user:
            return {}

        user['_id'] = str(user['_id'])
        return user

    @staticmethod
    async def insert(db, data):
        data['_id'] = ObjectId()

        user = await db.Users.insert_one(data)
        return user.inserted_id

    @staticmethod
    async def get(db, user_id):
        user = await db.Users.find_one({'_id': ObjectId(user_id)})
        return user

    @staticmethod
    async def find_by_session_token(db, token):
        session = await Sessions.find_by_token(token)

        if not session:
            return None

        user = await db.Users.find_one({'_id': ObjectId(session['user_id'])})

        if not user:
            return None

        user['_id'] = str(user['_id'])
        return user

    @staticmethod
    async def find(db, query, exclude=None):
        result = []
        cursor = db.Users.find(query, exclude)

        while (await cursor.fetch_next):
            user = cursor.next_object()

            result.append(
                Users.prepare(user)
            )

        return result

    @staticmethod
    def prepare(obj):
        obj['_id'] = str(obj['_id'])

        return obj

    @staticmethod
    async def update(db, query, user):
        await db.Users.update(query, user)

    @staticmethod
    async def delete(db, query):
        await db.Users.remove(query)
