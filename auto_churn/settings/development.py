from auto_churn.settings.base import *

__author__ = 'William'

DEBUG = True
CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS.append('rest_framework_swagger')

DATABASES = {
    'default': SETTINGS['development'],
    'TEST': {
        'MIRROR': 'default',
    }
}

SWAGGER_SETTINGS = {
        "USE_SESSION_AUTH": False,
        "LOGIN_URL": "/",
        "LOGOUT_URL": "/",
        "SUPPORTED_SUBMIT_METHOD": ['get', 'post', 'put', 'delete', 'patch'],
        "APIS_SORTER": "alpha",
        "VALIDATOR_URL": None,
        'SECURITY_DEFINITIONS': {
            "api_key": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            },
        }
     }
LOGIN_URL = 'rest_framework:login'
LOGOUT_URL = 'rest_framework:logout'



