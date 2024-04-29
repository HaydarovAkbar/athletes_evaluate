from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters

from .models import Competition, Ring, Match, MatchResult
from .serializers import CompetitionSerializer, RingSerializer, MatchSerializer, MatchResultSerializer, \
    ActiveCompetitionSerializer
from .pagination.base import TenPagination


class CompetitionCreateApi(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated, ]
    pagination_class = TenPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return serializer


class RingCreateApi(generics.ListCreateAPIView):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAuthenticated, ]


class MatchCreateApi(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated, ]


class MatchResultCreateApi(generics.ListCreateAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = [IsAuthenticated, ]


class CompetitionUpdateDeleteRetrieveAPi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = ['uuid']


class RingUpdateDeleteRetieveApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['competition']


class GetRingApi(generics.ListAPIView):
    queryset = Ring.objects.all()
    serializer_class = RingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['competition']


class MatchUpdateDeleteRetriveAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['ring']


class MatchResultUpdateDeleteRetriveApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['match']


class ActiveCompetitionApi(generics.ListAPIView):
    queryset = Ring.objects.all()
    serializer_class = ActiveCompetitionSerializer
    permission_classes = [IsAuthenticated]


class GetMatchResultApi(generics.ListAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['match']

    def get_queryset(self):
        user = self.request.user
        return MatchResult.objects.filter(referee=user, is_finished=False)
