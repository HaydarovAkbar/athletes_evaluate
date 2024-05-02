from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework import status
from rest_framework.response import Response

from .models import Competition, Ring, Match, MatchResult
from .serializers import CompetitionSerializer, RingSerializer, MatchSerializer, MatchResultSerializer, \
    ActiveCompetitionSerializer, ActiveMatchSerializer
from .pagination.base import TenPagination

from account.models import User


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

    def create(self, request, *args, **kwargs):
        ring = request.user.ring
        request_data = request.data
        request_data['ring'] = ring.id
        serializer = self.get_serializer(data=request_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        users = User.objects.filter(ring=serializer.instance.ring, is_active=True)
        for user in users:
            if 'referees' in user.groups.values_list('name', flat=True):
                MatchResult.objects.create(match=serializer.instance, referee=user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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


class PatchMatchResultApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['match']

    def get_queryset(self):
        user = self.request.user
        return MatchResult.objects.filter(referee=user, is_finished=False)


class GetMatchResultApi(generics.ListAPIView):
    queryset = MatchResult.objects.all()
    serializer_class = MatchResultSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['match']

    def get_queryset(self):
        user = self.request.user
        return MatchResult.objects.filter(referee=user, is_finished=False)


class GetActiveMatchApi(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = ActiveMatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Match.objects.filter(ring=user.ring, is_finished=False)


class ChangeMatchStatusApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        match_results = MatchResult.objects.filter(match=instance)
        for match_result in match_results:
            match_result.is_finished = True
            match_result.save()
        instance.is_finished = True
        instance.save()
        return Response(status=status.HTTP_200_OK)