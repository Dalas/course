from .BaseModel import BaseModel

from bson import ObjectId


class Users(BaseModel):

    _collection = 'users'

    @classmethod
    async def get_or_create_user_by_gh_user(cls, db, document):
        user = await cls.get(db, {'gh_id': document['id']})

        if not user:
            user = cls.prepare_gh_data(document)
            await cls.insert(db, user)

        return user

    @staticmethod
    def prepare_gh_data(document):
        result = {
            '_id': ObjectId(),
            'nickname': document['login'],

            'gh_avatar': document['avatar_url'],
            'gh_id': document['id'],
            'gh_account': document['url']
        }

        # TODO: add prepare

        return result
