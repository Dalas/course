from motor.motor_asyncio import AsyncIOMotorClient


def setup_db(app):
    # TODO: move all variables to some file
    client = AsyncIOMotorClient('127.0.0.1:27017', io_loop=app.loop)
    app['db'] = client['ChatDB']
