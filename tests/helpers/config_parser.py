import os
import functools
import configparser

from io import StringIO


def parse_config(raw):
    config = configparser.ConfigParser()
    if raw.strip().startswith('['):
        config.readfp(StringIO(raw))
    else:
        config.readfp(StringIO('\n[environment]\n' + raw))
        config.get = functools.partial(config.get, 'environment')
    return config


def get_config():
    if os.path.isfile('.env'):
        raw_config = open('.env').read()
        config = parse_config(raw_config)
    else:
        config = os.environ

    return config
