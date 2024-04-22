from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics

from .serializers import LogInSerializer
from .models import *


class LoginApi(TokenObtainPairView):
    serializer_class = LogInSerializer