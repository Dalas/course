from models import Users


ROLE_STUDENT = "ROLE_STUDENT"
ROLE_LECTURER = "ROLE_LECTURER"
ROLE_ADMIN = "ROLE_ADMIN"


AVAILABLE_PATHS = {
    ROLE_STUDENT: '/vk',
    ROLE_LECTURER: '/journal',
    ROLE_ADMIN: '/admin'
}


def is_authenticated(available_role=None):
    def method_wrapper(method):
        async def wrapper(self, *args, **kwargs):
            token = self.get_secure_cookie('token')

            if not token:
                return self.redirect('/login')

            self.current_user = await Users.find_by_session_token(token.decode('utf-8'))

            if not self.current_user:
                return self.redirect('/login')

            if available_role and  self.current_user['role'] != available_role:
                return self.redirect(AVAILABLE_PATHS[self.current_user['role']])

            return method(self, *args, **kwargs)

        return wrapper

    return method_wrapper
