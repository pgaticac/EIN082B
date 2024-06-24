from django.shortcuts import render
from rest_framework import serializers, viewsets
from core.models import Carrera
from .serializers import CarreraSerializer

class CarreraViewSet(viewsets.ModelViewSet):
    queryset = Carrera.objects.all()
    #Gestión de la información a mostrar por el API
    serializer_class = CarreraSerializer


