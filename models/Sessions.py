from .BaseModel import BaseModel

from uuid import uuid4


class Sessions(BaseModel):

    _collection = 'sessions'

    @classmethod
    async def update_or_create_session(cls, db, user_id):
        session = {
            'token': str(uuid4()),
            'user_id': user_id
        }

        await cls.update(db, {'user_id': user_id}, session, upsert=True)

        return session

