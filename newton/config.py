import os
import configparser
from os import environ as env
from newton.errors import NewtonError


# for trade_api
def set_keys(key, secret):
    env['NEWTON_KEY'] = key
    env['NEWTON_SECRET'] = secret


def get_keys():
    if env.get('NEWTON_KEY') and env.get('NEWTON_SECRET'):
        return env['NEWTON_KEY'], env['NEWTON_SECRET']

    home = os.path.expanduser('~')
    config_file = os.path.join(home, '.newton')
    if os.path.isfile(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        return config['api_keys']['key'], config['api_keys']['secret']

    raise NewtonError('api keys are not set')
