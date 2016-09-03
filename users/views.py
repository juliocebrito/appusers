from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .models import DatastoreUser
from .serializers import UserSerializer, GroupSerializer
from djangae.contrib.gauth.datastore.models import Group

class UserViewSet(viewsets.ModelViewSet):
    queryset = DatastoreUser.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [AllowAny]

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [AllowAny]
