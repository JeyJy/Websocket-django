import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

# import room.routing
from room.consumers import ChatConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochat.settings')

application = ProtocolTypeRouter({
    # "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            # room.routing.websocket_urlpatterns
            [path('ws/<str:room_name>/', ChatConsumer)]
        )
    )
})