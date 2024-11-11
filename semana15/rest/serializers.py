from core.models import Carrera
from rest_framework import routers, serializers

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model= Carrera
        #fields = '__all__'
        fields = ["nombre", "duracion", "jefe_carrera"]
        #exclude = ['codigo']