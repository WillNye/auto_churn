from auto_churn.settings.base import *

__author__ = 'William'

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': SETTINGS['staging']
}

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': SETTINGS['redisStaging'],
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
