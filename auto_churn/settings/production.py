from auto_churn.settings.base import *

__author__ = 'William'

DEBUG = False

DATABASES = {
    'default': SETTINGS['production']
}


