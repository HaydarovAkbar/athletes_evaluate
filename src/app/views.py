from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Competition, Ring, Match, MatchResult
from .serializers import CompetitionSerializer, RingSerializer, MatchSerializer, MatchResultSerializer

class CompetitionCreateApi(generics.ListCreateAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionSerializer
    permission_classes=[IsAuthenticated,] 

class RingCreateApi(generics.ListCreateAPIView):
    queryset=Ring.objects.all()
    serializer_class=RingSerializer
    permission_classes=[IsAuthenticated,]

class MatchCreateApi(generics.ListCreateAPIView):
    queryset=Match.objects.all()
    serializer_class=MatchSerializer
    permission_classes=[IsAuthenticated,]

class MatchResultCreateApi(generics.ListCreateAPIView):
    queryset=MatchResult.objects.all()
    serializer_class=MatchResultSerializer
    permission_classes=[IsAuthenticated,]

class CompetitionUpdateDeleteRetrieveAPi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Competition.objects.all()
    serializer_class=CompetitionSerializer
    permission_classes=[IsAuthenticated]

class  RingUpdateDeleteRetieveApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Ring.objects.all()
    serializer_class=RingSerializer
    permission_classes=[IsAuthenticated]

class MatchUpdateDeleteRetriveAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset=Match.objects.all()
    serializer_class=MatchSerializer
    permission_classes=[IsAuthenticated]

class MatchResultUpdateDeleteRetriveApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=MatchResult.objects.all()
    serializer_class=MatchResultSerializer
    permission_classes=[IsAuthenticated]

