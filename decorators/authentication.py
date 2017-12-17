from bson import ObjectId

from models import Users, Sessions
from exceptions import LoginRequiredException


ROLE_STUDENT = "ROLE_STUDENT"
ROLE_LECTURER = "ROLE_LECTURER"
ROLE_ADMIN = "ROLE_ADMIN"


AVAILABLE_PATHS = {
    ROLE_STUDENT: '/vk',
    ROLE_LECTURER: '/journal',
    ROLE_ADMIN: '/admin'
}


def is_authenticated(available_role=None):
    def method_wrapper(func):
        async def wrapper(request, *args, **kwargs):
            token = request.headers.get('token', None)

            if token:
                db = request.app['db']

                session = await Sessions.get(db, {'token': token})

                if not session:
                    raise LoginRequiredException()

                user = await Users.get(db, {'_id': ObjectId(session['user_id'])})

                if not user:
                    raise LoginRequiredException()

                request.user = user
            else:
                raise LoginRequiredException()

            return await func(request, *args, **kwargs)

        return wrapper

    return method_wrapper
