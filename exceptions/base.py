

class BaseApiException(Exception):
    error = 'Can\'t parse response.'
    status = 500


class PasswordMissMatchException(BaseApiException):
    error = 'Passwords missmatch.'
    status = 400


class LoginException(BaseApiException):
    error = 'Invalid login or password.'
    status = 403


class LoginRequiredException(BaseApiException):
    error = 'Login required'
    status = 403


class ValidationError(BaseApiException):
    error = 'Invalid json format.'
    status = 400
