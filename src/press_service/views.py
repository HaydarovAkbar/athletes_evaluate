from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .serializers import NewsSerializers
from .models import News


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetailViewSet(RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers

