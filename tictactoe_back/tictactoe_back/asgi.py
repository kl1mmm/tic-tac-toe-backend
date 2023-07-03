"""
ASGI config for tictactoe_back project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from users.consumers import OnlineStatusConsumer
from users.middleware import TokenAuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tictactoe_back.settings")

urlpatterns_websocket = [path('ws/online/', OnlineStatusConsumer.as_asgi())]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(TokenAuthMiddlewareStack(
        URLRouter(urlpatterns_websocket)
    ))
})
