# coding: utf-8
import yaml
import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def get_api_yaml_path():
    return os.path.join(BASE_DIR, '../api.yaml')


def load_schema(api_doc=get_api_yaml_path()):
    s = yaml.load(open(api_doc))
    return s.get('definitions', {})


SCHEMA = load_schema()


def get_schema(name):
    return SCHEMA.get(name)


create_user_request_schema = get_schema('CreateUserRequest')
