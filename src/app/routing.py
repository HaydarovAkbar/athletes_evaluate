from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/referee/$", consumers.MatchResultConsumer.as_asgi()),
    re_path(r"ws/main/$", consumers.MainRefereeMatchResultConsumer.as_asgi()),
]
