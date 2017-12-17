from utils import validators
from models import StoreHouses
from decorators import is_authenticated

from bson import ObjectId


@is_authenticated()
async def get_store_houses_handler(request):
    data = await StoreHouses.find(request.app['db'], {})

    return data, 200


@is_authenticated()
async def create_store_house_handler(request):
    data = await validators.create_storehouse_request_validator(request)

    await StoreHouses.insert(request.app['db'], data)

    return {}, 201


@is_authenticated()
async def delete_store_house_handler(request):
    data = await validators.delete_storehouse_request_validator(request)

    await StoreHouses.delete(request.app['db'], {'_id': ObjectId(data['storehouse_id'])})

    return {}, 204
