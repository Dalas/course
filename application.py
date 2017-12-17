from routes import register_routes
from db import setup_db
from middlewares import response_middleware

from aiohttp_swagger import setup_swagger
from aiohttp_jinja2 import setup as jinja2_setup, request_processor
from aiohttp import web, ClientSession

import jinja2
import asyncio
import os


def prepare_client(app):
    app['client'] = ClientSession(loop=app.loop)


def create_app():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop, middlewares=(response_middleware, ))

    register_routes(app)
    prepare_client(app)
    setup_db(app)

    jinja2_setup(app, loader=jinja2.FileSystemLoader('./templates'), context_processors=[request_processor])
    setup_swagger(app, swagger_from_file=os.path.join(os.path.dirname(__file__), 'api.yaml'))

    return app


def run_app(app):
    web.run_app(app, port=9000)