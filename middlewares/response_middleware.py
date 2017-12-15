from exceptions import BaseApiException

from aiohttp.web import Response, FileResponse, json_response


async def response_middleware(app, handler):

    async def middleware_handler(request, *args, **kwargs):
        try:
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
