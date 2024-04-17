from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from rest_framework import generics
from .serializers import LogInSerializer
from .models import *

# Create your views here.

class LoginApi(TokenObtainPairView):
    serializer_class=LogInSerializer
    
