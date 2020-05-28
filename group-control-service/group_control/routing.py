from . import consumers
from django.urls import re_path
websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room>.*)/', consumers.ChatConsumer)
]