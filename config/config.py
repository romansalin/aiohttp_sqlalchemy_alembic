import os
import pathlib

config = dict()

config['root_path'] = str(pathlib.Path(__file__).parent.parent)
config['log_path'] = 'logs'
config['sleep_sec'] = 3
config['secret'] = os.getenv('JWT_HASH_SECRET')
config['db'] = None
config['base_url'] = 'http://0.0.0.0'
config['timezone'] = 'UTC'
