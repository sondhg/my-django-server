from django.urls import path
from .consumers import WebSocketDataConsumer

websocket_urlpatterns = [
    path("ws/data/", WebSocketDataConsumer.as_asgi()),
]
