from .base import *

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