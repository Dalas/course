

class BaseApiException(Exception):
    error = 'Can\'t parse response.'
    status = 1


class PasswordMissMatchException(BaseApiException):
    error = 'Passwords missmatch.'
    status = 2

