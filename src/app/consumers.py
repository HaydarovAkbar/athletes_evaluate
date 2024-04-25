import json

from django.db.models import QuerySet

from .serializers import MatchResultSerializer
from .models import MatchResult

from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from djangochannelsrestframework.observer import model_observer

class MatchResultConsumer(CreateModelMixin,UpdateModelMixin, GenericAsyncAPIConsumer):
    
    def get_queryset(self, **kwargs) -> QuerySet:
        qs= super().get_queryset(**kwargs)
        return qs.filter(referee=self.scope['user'])
    
    serializer_class=MatchResultSerializer
    permission_classes=(permissions.AllowAny,)
    


class MainRefereeMatchResultConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    def get_queryset(self, **kwargs) -> QuerySet:
        qs=super().get_queryset(**kwargs)
        return qs.filter(referee=self.scope['user'])
    
    serializer_class=MatchResultSerializer
    permission_classes=(permissions.AllowAny)
    
    async def connect(self):
        self.model_change.subscribe()
        await super().connect()

    @model_observer(MatchResult)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    @model_change.serialize
    def model_serialize(self, instance, action,**kwargs):
        return dict(data=MatchResultSerializer(instance=instance).data, action=action.value)
