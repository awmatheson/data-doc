"""
WSGI config for gettingstarted project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

import os

if os.getenv("DJANGO-ENVIRONMENT") == 'development':
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings_dev")
else:
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")


from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
