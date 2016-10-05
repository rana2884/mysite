from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, '../static')

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db-name',
        'USER': 'db-user',
        'PASSWORD': 'db-pwd',
        'HOST': 'db-host',
        'PORT': 'db-port',
    }
}
