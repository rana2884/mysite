from .base import *

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATICFILES_DIRS = (
      os.path.abspath(os.path.join(BASE_DIR, '..', 'static')),
)

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, "../media")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'key'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mysitedb',
        'USER': 'grana',
        'PASSWORD': 'Wind@1774',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
