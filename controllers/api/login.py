import hashlib

from aiohttp.web import json_response

from utils import validators
from models import Users, Sessions
from exceptions import LoginException


async def login_handler(request):
    db = request.app['db']
    data = await validators.login_request_validator(request)

    user = await Users.find(db, {'login': data['login']})

    if not user:
        raise LoginException()

    user = user[0]

    if user['password'] != hashlib.sha256(data['password'].encode('utf-8')).hexdigest():
        raise LoginException()

    session = await Sessions.update_or_create_session(db, user['_id'])

    # response = json_response({'token': })
    # response.set_cookie('token', session['token'])

    return {'token': session['token']}, 200
