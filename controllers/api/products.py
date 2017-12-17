from utils import validators
from models import Products
from decorators import is_authenticated

from bson import ObjectId


@is_authenticated()
async def get_products_handler(request):
    data = await Products.find(request.app['db'], {})

    return data, 200


@is_authenticated()
async def create_product_handler(request):
    data = await validators.create_product_request_validator(request)

    await Products.insert(request.app['db'], data)

    return {}, 201


@is_authenticated()
async def delete_product_handler(request):
    data = await validators.delete_product_request_validator(request)

    await Products.delete(request.app['db'], {'_id': ObjectId(data['product_id'])})

    return {}, 204
