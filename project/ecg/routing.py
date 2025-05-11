from django.urls import re_path

from .consumers import EcgConsumer

websocket_urlpatterns = [
    re_path(r'ws/ecg/$', EcgConsumer.as_asgi()),
]