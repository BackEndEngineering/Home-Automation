from .settings import *
import dj_database_url

#DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'guitron.herokuapp.com', 'gui-tron.com', 'www.gui-tron.com']
DEBUG = False
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY="y0e#_a&wvn&&ps24p10sg&r66=@2mv2rlh@e*nhpcqltu(0m4#"')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}
