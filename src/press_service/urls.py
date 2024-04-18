from django.urls import path
from .views import NewsViewSet, NewsDetailViewSet


urlpatterns = [
    path('news/', NewsViewSet.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailViewSet.as_view(), name='news_detail'),
]
