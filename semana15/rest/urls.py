from rest_framework import routers
from .views import CarreraViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register('carrera',CarreraViewSet)

urlpatterns = [
    path('',include(router.urls))
]

