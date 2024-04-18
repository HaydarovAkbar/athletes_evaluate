from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from django.shortcuts import render
from django.contrib.auth import hashers
from rest_framework import generics
from .serializers import LogInSerializer
from .models import *

# Create your views here.


class LoginApi(TokenObtainPairView):
    serializer_class = LogInSerializer


# class RefereeAPI(TokenObtainPairView):
#     serializer_class = RefereeUserSerializers

#     def post(self, request: Request, *args, **kwargs):
#         username = request.POST['username']
#         password = request.POST['password']
#         try:
#             referee = RefereeUser.objects.get(username=username)
#         except:
#             raise Exception("Referee not found")
#         if referee.check_password(password):
#             response = {
#                 'username': referee.username,
#                 'password': referee.password,
#                 'ring': referee.ring,
#                 'main': referee.main,
#                 'groups': [group.name for group in referee.groups.all()],
#                 'permissions': [permission.name for permission in referee.user_permissions.all()]
#             }
#             return Response(response, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_404_NOT_FOUND)
