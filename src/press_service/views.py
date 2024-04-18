from django.shortcuts import render
from .serializers import NewsSerializers
from .models import News
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView


# Create your views here.


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

