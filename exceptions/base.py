

class BaseResponseException(Exception):
    error = 'Can\'t parse response'
    status = 1
