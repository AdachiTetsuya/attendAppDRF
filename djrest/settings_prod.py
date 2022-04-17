from .settings_common import *

DEBUG = True

ALLOWED_HOSTS = ['35.72.215.229']

# DATABASES = {
#      'default': {
#          'ENGINE': 'django.db.backends.postgresql',
#          'NAME': 'demiattend',
#          'USER': 'adachitetsuya',
#          'PASSWORD': '1019born',
#          'HOST': 'localhost',
#          'PORT': '5432',
#      }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


CORS_ORIGIN_WHITELIST = (
    'http://localhost:3000',
    'http://d19u3oyzhhez9d.cloudfront.net',
)

ATTEND_FRONT_ROOT = 'http://d19u3oyzhhez9d.cloudfront.net'
