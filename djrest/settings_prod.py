from .settings_common import *

DEBUG = True

ALLOWED_HOST = ['*']

CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://d19u3oyzhhez9d.cloudfront.net',
)

ATTEND_FRONT_ROOT = 'http://d19u3oyzhhez9d.cloudfront.net'