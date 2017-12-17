from aiohttp_jinja2 import render_template
from aiohttp.web import HTTPFound

from models import Users, Sessions

import hashlib


async def login_handler(request):
    return render_template('LoginTemplate.html', request, {})


async def process_login(request):
    db = request.app['db']
    data = await request.post()

    user = await Users.find(db, {'login': data['login']})

    if not user:
        return render_template('LoginTemplate.html', request, {'error': 'Invalid login or password'})

    user = user[0]

    if user['password'] != hashlib.sha256(data['password'].encode('utf-8')).hexdigest():
        return render_template('LoginTemplate.html', request, {'error': 'Invalid login or password'})

    session = await Sessions.update_or_create_session(db, user['_id'])

    response = HTTPFound('/')
    response.set_cookie('token', session['token'])

    return response
