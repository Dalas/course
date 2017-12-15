

class BaseApiException(Exception):
    error = 'Can\'t parse response.'
    status = 500


class PasswordMissMatchException(BaseApiException):
    error = 'Passwords missmatch.'
    status = 400


class LoginException(BaseApiException):
    error = 'Invalid login or password.'
    status = 403
