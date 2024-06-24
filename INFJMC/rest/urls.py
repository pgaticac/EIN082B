from django.urls import path, include
from rest_framework import serializers, routers
from . import views
from .views import CarreraViewSet

router = routers.DefaultRouter()
router.register('carreras',views.CarreraViewSet)

urlpatterns = [
    path('',include(router.urls))
]