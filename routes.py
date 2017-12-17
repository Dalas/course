from controllers import web, api


def register_routes(app):
    app.router.add_static('/static', './static')

    app.router.add_get('/', web.main_handler, name='main-route')

    # Auth
    # Web
    app.router.add_get('/register', web.registration_handler, name='registration-route')
    app.router.add_get('/login', web.login_handler, name='login-route')
    # Api
    app.router.add_post('/api/v1/login', api.login_handler, name='login-api-route')
    app.router.add_post('/api/v1/user', api.registration_handler, name='registration-api-route')

    # Storehouses
    app.router.add_get('/api/v1/storehouses', api.get_store_houses_handler, name='get-storehouses')
    app.router.add_post('/api/v1/storehouse', api.create_store_house_handler, name='create-storehouses')
    app.router.add_delete('/api/v1/storehouse', api.delete_store_house_handler, name='delete-storehouses')
