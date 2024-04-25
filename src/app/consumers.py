# chat/consumers.py
import json

from channels.generic.websocket import WebsocketConsumer
from .serializers import MatchResultSerializer, CompetitionSerializer
from .models import MatchResult, Competition
from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin

class MatchResultConsumer(CreateModelMixin,UpdateModelMixin, GenericAsyncAPIConsumer):
    queryset=Competition.objects.all()
    serializer_class=CompetitionSerializer
    permission_classes=(permissions.AllowAny,)
