from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, permissions


class ClientsView(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAdminUser,)


class EstablishmentView(viewsets.ModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)


class AdminView(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = (permissions.IsAdminUser,)