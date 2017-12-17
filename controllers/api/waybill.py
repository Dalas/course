from utils import validators
from models import Waybill
from decorators import is_authenticated

from bson import ObjectId


@is_authenticated()
async def get_waybill_handler(request):
    data = await Waybill.find(request.app['db'], {})

    return data, 200


@is_authenticated()
async def create_waybill_handler(request):
    data = await validators.create_waybill_request_validator(request)

    await Waybill.insert(request.app['db'], data)

    return {}, 201


@is_authenticated()
async def delete_waybill_handler(request):
    data = await validators.process_waybill_request_validator(request)

    await Waybill.delete(request.app['db'], {'_id': ObjectId(data['waybill_id'])})

    return {}, 204


@is_authenticated()
async def process_waybill_handler(request):
    data = await validators.process_waybill_request_validator(request)

    waybill = await Waybill.get(request.app['db'], {'_id': ObjectId(data['waybill_id'])})

    return {}, 200
