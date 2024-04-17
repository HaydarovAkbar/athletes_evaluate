from django.urls import path
from .views import LoginApi, RefereeAPI

urlpatterns=[
    path('login/', LoginApi.as_view(), name='login'),
    path('ref_login/', RefereeAPI.as_view(), name='ref_login'),
]
