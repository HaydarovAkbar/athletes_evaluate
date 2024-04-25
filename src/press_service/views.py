from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .serializers import NewsSerializers, CategorySerializers, HashtagSerializers
from .models import News, Category, Hashtag


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class HashtagViewSet(ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers


class HashtagDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers


