import json

from django.db.models import QuerySet

from .serializers import MatchResultSerializer
from .models import MatchResult

from djangochannelsrestframework import permissions
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import CreateModelMixin, ListModelMixin, UpdateModelMixin
from djangochannelsrestframework.observer import model_observer


class MatchResultConsumer(CreateModelMixin, UpdateModelMixin, GenericAsyncAPIConsumer):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self, **kwargs) -> QuerySet:
        qs = super().get_queryset(**kwargs)
        user = self.scope['user']
        return qs.filter(referee=user, is_finished=False)


class MainRefereeMatchResultConsumer(ListModelMixin, GenericAsyncAPIConsumer):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = (permissions.AllowAny)

    def get_queryset(self, **kwargs) -> QuerySet:
        qs = super().get_queryset(**kwargs)
        user = self.scope['user']
        return qs.filter(is_finished=False, match__ring = user.ring)

    async def connect(self):
        self.model_change.subscribe()
        await super().connect()

    @model_observer(MatchResult)
    async def model_change(self, message, observer=None, **kwargs):
        await self.send_json(message)

    # @model_change.serialize
    # def model_serialize(self, instance, action, **kwargs):
    #     return dict(data=MatchResultSerializer(instance=instance).data, action=action.value)
