from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mysite',
        'USER': 'grana',
        'PASSWORD': 'usha1234',
        'HOST': 'mysite.chekrprgdtfv.ap-southeast-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
