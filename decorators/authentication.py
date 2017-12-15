from models import Users, Sessions

from aiohttp.web import HTTPFound


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
            token = request.cookies.get('token', None)

            if token:
                session = await Sessions.get(request.app['db'], {'token': token})
                # TODO: refactor this
                if session:
                    request.session = session
                else:
                    return HTTPFound('/')
            else:
                return HTTPFound('/')

            return await func(request, *args, **kwargs)

        return wrapper

    return method_wrapper
