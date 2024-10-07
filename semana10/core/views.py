from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def carreras(request):
    titulo = "Carreras"
    carreras = Carrera.objects.all()
    data = {
        "titulo":titulo,
        "carreras": carreras
    }
    return render(request,'core/carreras.html',data)
    

def profesores(request):
    titulo = "Profesores"
    h1 = "<h1> "+ titulo + "</h1>"
    return HttpResponse(h1)
