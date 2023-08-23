from .settings import *
# SECURITY WARNING: don't run with debug turned on in production!

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'amdDom4kLm7e5nDxkEM1',
        'HOST': 'containers-us-west-106.railway.app',
        'PORT': '7741',
    }
}

DEBUG = True


ALLOWED_HOSTS = [
    'https://web-production-f94c.up.railway.app',
    'https://web-production-f94c.up.railway.app/',
    'web-production-f94c.up.railway.app',
]
