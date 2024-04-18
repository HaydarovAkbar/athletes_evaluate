from django.urls import path
from .views import (NewsViewSet, CategoryViewSet, HashtagViewSet, NewsDetailViewSet, CategoryDetailViewSet,
                    HashtagDetailViewSet)


urlpatterns = [
    path('news/', NewsViewSet.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailViewSet.as_view(), name='news_detail'),
    path('category/', CategoryViewSet.as_view(), name='category'),
    path('category/<int:pk>/', CategoryDetailViewSet.as_view(), name='category_detail'),
    path('hashtag/', HashtagViewSet.as_view(), name='hashtag'),
    path('hashtag/<int:pk>/', HashtagDetailViewSet.as_view(), name='hashtag_detail'),
]
