import hashlib

from utils import validators
from models import Users
from exceptions import PasswordMissMatchException


async def registration_handler(request):
    data = await validators.create_user_request_validator(request)

    if data['password'] != data['confirm_password']:
        raise PasswordMissMatchException()

    del data['confirm_password']
    data['password'] = hashlib.sha256(data['password'].encode('utf-8')).hexdigest()

    await Users.insert(request.app['db'], data)

    return {}, 201
