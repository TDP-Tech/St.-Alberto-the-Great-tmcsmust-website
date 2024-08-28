"""
ASGI config for tmcsmust project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from channels.auth import AuthMiddlewareStack

# Correct environment variable for settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tmcsmust.settings')

# Initialize Django ASGI application early to ensure the AppRegistry is populated correctly.
django_asgi_app = get_asgi_application()

from ChatApp import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))
    ),
})
