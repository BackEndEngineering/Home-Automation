from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'guitron_localdb',
        'USER': 'sc_user',
        'PASSWORD': 'raspberrypi',
        'HOST': '',
        'PORT': '',
    }
}
