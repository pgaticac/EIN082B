from django.contrib import admin
from .models import Carrera
from .models import Profesor

# Register your models here.
admin.site.register(Carrera)
admin.site.register(Profesor)