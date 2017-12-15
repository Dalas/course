from utils import validators
from models import StoreHouses
from exceptions import PasswordMissMatchException
from decorators import is_authenticated


@is_authenticated()
async def get_store_houses_handler(request):
    data = await StoreHouses.find(request.app['db'], {})

    return data, 201


@is_authenticated()
async def create_store_house_handler(request):
    data = await validators.create_user_request_validator(request)

    if data['password'] != data['confirm_password']:
        raise PasswordMissMatchException()

    del data['confirm_password']
    data['password'] = hashlib.sha3_256(data['password'].encode('utf-8')).hexdigest()

    await Users.insert(request.app['db'], data)

    return {}, 201


@is_authenticated()
async def delete_store_house_handler(request):
    data = await validators.create_user_request_validator(request)

    if data['password'] != data['confirm_password']:
        raise PasswordMissMatchException()

    del data['confirm_password']
    data['password'] = hashlib.sha3_256(data['password'].encode('utf-8')).hexdigest()

    await Users.insert(request.app['db'], data)

    return {}, 201
