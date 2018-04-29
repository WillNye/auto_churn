"""
WSGI config for auto_churn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

app_level = os.environ.get('APPLEVEL')

if app_level:
    if app_level == 'PROD':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_churn.settings.production")
    elif app_level == 'STAGING':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_churn.settings.staging")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_churn.settings.development")
else:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "auto_churn.settings.staging")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()


