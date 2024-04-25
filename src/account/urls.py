from django.urls import path
from .views import LoginApi

urlpatterns = [
    path('login/', LoginApi.as_view(), name='login'),
]
