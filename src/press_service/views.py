from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters

from .serializers import NewsSerializers, CategorySerializers, HashtagSerializers
from .models import News, Category, Hashtag
from .paginition import TenPagination, TwentyPagination


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    pagination_class = TenPagination
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ('title', 'hashtag', 'published_at')


class NewsDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    pagination_class = TwentyPagination


class CategoryDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class HashtagViewSet(ListAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers
    pagination_class = TwentyPagination


class HashtagDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializers

