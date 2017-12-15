from utils import validators
from exceptions import PasswordMissMatchException


async def registration_handler(request):
    data = await validators.create_user_request_validator(request)

    if data['password'] != data['confirm_password']:
        raise PasswordMissMatchException()

    return {}
