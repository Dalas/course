from controllers import web, api


def register_routes(app):
    app.router.add_static('/static', './static')

    app.router.add_get('/', web.main_handler, name='main-route')

    # Auth
    app.router.add_get('/register', web.registration_handler, name='registration-route')
    app.router.add_get('/login', web.login_handler, name='login-route')


    #
    # # Repositories
    # app.router.add_get('/api/repositories', views.my_repositories, name='my-repositories')
    #
    # # Users
    # app.router.add_get('/api/users/me', views.get_me, name='my-profile')
