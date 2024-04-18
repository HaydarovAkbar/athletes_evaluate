from django.shortcuts import render
from .serializers import NewsSerializers, CategorySerializers, HashtagSerializers
from .models import News, Category, Hashtag
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters

# Create your views here.


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class HashtagViewSet(ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class CategoryDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    filter_backends = [filters.DjangoFilterBackend]


class HashtagDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers
    filter_backends = [filters.DjangoFilterBackend]


class NewsDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    filter_backends = [filters.DjangoFilterBackend]






