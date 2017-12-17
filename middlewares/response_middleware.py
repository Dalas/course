from exceptions import BaseApiException
from models import Users, Sessions

from aiohttp.web import Response, FileResponse, json_response
from bson import ObjectId


async def response_middleware(app, handler):

    async def middleware_handler(request, *args, **kwargs):
        try:
            token = request.headers.get('token', None) or request.cookies.get('token', None)
            if token:
                db = request.app['db']
                session = await Sessions.get(db, {'token': token})
                if session:
                    user = await Users.get(db, {'_id': ObjectId(session['user_id'])})

                    if user:
                        request.user = user

            response = await handler(request, *args, **kwargs)

            if isinstance(response, Response) or isinstance(response, FileResponse):
                return response
            else:
                data, status = response
                return json_response({'data': data, 'error': {}}, status=status)

        except BaseApiException as e:
            return json_response({'data': {}, 'error': e.error}, status=e.status)

        # TODO: use only for debug
        # except Exception as e:
        #     print(e)  # TODO: add normal logger
        #     return json_response({'data': {}, 'error': {'code': 1000, 'message': 'Internal server error!'}}, status=500)

    return middleware_handler
