import copy
import decimal
import functools
import json
import logging

import jsonschema

from utils import schemas
from exceptions import ValidationError


logger = logging.getLogger(__name__)


def is_num(val):
    try:
        decimal.Decimal(val)
    except (decimal.InvalidOperation, TypeError, ValueError):
        return False
    return True


def validate_schema(obj, schema):
    errors = []
    for e in jsonschema.Draft4Validator(schema, format_checker=jsonschema.FormatChecker()).iter_errors(obj):
        path = e.path.pop() if e.path else ''
        if path:
            errors.append('{0}: {1}'.format(path, e.message))
        else:
            errors.append(e.message)
    return ', '.join(errors)


async def validate(request, schema, required_all=True):
    try:
        body = await request.json()
        if schema:
            if not required_all:
                schema = copy.deepcopy(schema)
                schema.pop('required', None)
                body = {k: v for k, v in body.items() if k in schema['properties'] and v is not None}

            errors = validate_schema(body, schema)
            if errors:
                raise ValidationError()
        return body
    except json.JSONDecodeError as e:
        logger.exception('Bad json, got exception %s', e)
        raise ValidationError()


create_user_request_validator = functools.partial(validate, schema=schemas.create_user_request_schema)
login_request_validator = functools.partial(validate, schema=schemas.login_request_schema)
create_storehouse_request_validator = functools.partial(validate, schema=schemas.create_storehouse_request_schema)
delete_storehouse_request_validator = functools.partial(validate, schema=schemas.delete_storehouse_request_schema)
create_product_request_validator = functools.partial(validate, schema=schemas.create_product_request_schema)
delete_product_request_validator = functools.partial(validate, schema=schemas.delete_product_request_schema)
create_waybill_request_validator = functools.partial(validate, schema=schemas.create_waybill_request_schema)
process_waybill_request_validator = functools.partial(validate, schema=schemas.process_waybill_request_schema)
