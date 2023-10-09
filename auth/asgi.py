
import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from home.consumers import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()

ws_patterns=[
  path('ws/<str:room_name>/<str:username>/',TestConsumer.as_asgi())
]

application=ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket':AuthMiddlewareStack(URLRouter(ws_patterns))
})
