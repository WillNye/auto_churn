import sys

from auto_churn.settings.base import *

__author__ = 'William'

CORS_ORIGIN_ALLOW_ALL = False
ALLOWED_HOSTS = ['*']

PYLINT_LOAD_PLUGIN = (
    'pylint_django',
)

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_sloccount',
    'django_jenkins.tasks.run_flake8',
)

DATABASES = {
    'default': SETTINGS['development'],
    'TEST': {
        'MIRROR': 'default',
    }
}





