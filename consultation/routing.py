from django.urls import re_path

from consultation import consumers

websocket_urlpatterns = [
    re_path(r'ws/consultation/new/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]