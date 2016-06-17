"""
WSGI config for raspberry project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
import socketio
from whitenoise.django import DjangoWhiteNoise

from .sockets import serv

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "raspberry.settings")

application = get_wsgi_application()
application = socketio.Middleware(serv, application)
application = DjangoWhiteNoise(application)
