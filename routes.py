from controllers import web, api


def register_routes(app):
    app.router.add_static('/static', './static')

    app.router.add_get('/', web.main_handler, name='main-route')
    app.router.add_get('/storehouses', web.store_houses_handler, name='storehouses')
    app.router.add_get('/products', web.products_handler, name='products')
    app.router.add_get('/waybills', web.waybills_handler, name='waybills')

    # Auth
    # Web
    app.router.add_get('/register', web.registration_handler, name='registration-route')
    app.router.add_get('/login', web.login_handler, name='login-route')
    app.router.add_post('/login', web.process_login, name='process-login')
    # Api
    app.router.add_post('/api/v1/login', api.login_handler, name='login-api-route')
    app.router.add_post('/api/v1/user', api.registration_handler, name='registration-api-route')

    # Storehouses
    app.router.add_get('/api/v1/storehouses', api.get_store_houses_handler, name='get-storehouses')
    app.router.add_post('/api/v1/storehouse', api.create_store_house_handler, name='create-storehouse')
    app.router.add_delete('/api/v1/storehouse', api.delete_store_house_handler, name='delete-storehouse')

    # Storehouses
    app.router.add_get('/api/v1/products', api.get_products_handler, name='get-products')
    app.router.add_post('/api/v1/product', api.create_product_handler, name='create-product')
    app.router.add_delete('/api/v1/product', api.delete_product_handler, name='delete-product')

    # Waybills
    app.router.add_get('/api/v1/waybills', api.get_waybills_handler, name='get-waybills')
    app.router.add_post('/api/v1/waybill', api.create_waybill_handler, name='create-waybill')
    app.router.add_put('/api/v1/waybill', api.process_waybill_handler, name='process-waybill')
    app.router.add_delete('/api/v1/waybill', api.delete_waybill_handler, name='delete-waybill')
