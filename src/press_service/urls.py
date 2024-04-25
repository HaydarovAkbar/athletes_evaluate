from django.urls import path

from .views import NewsViewSet, NewsDetailViewSet, CategoryViewSet, CategoryDetailViewSet, HashtagViewSet, HashtagDetailViewSet

urlpatterns = [
    path('news/', NewsViewSet.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailViewSet.as_view(), name='news_detail'),
    path('categories/', CategoryViewSet.as_view(), name='categories'),
    path('categories/<int:pk>/', CategoryDetailViewSet.as_view(), name='categories_detail'),
    path('hashtags/', HashtagViewSet.as_view(), name='hashtags'),
    path('hashtags/<int:pk>/', HashtagDetailViewSet.as_view(), name='hashtags_detail'),
]
