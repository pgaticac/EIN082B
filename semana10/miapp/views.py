from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    title = "Inicio"

    data = {
        "title": title,
    }

    return render(request,'miapp/index.html', data)

def carreras(request):
    title = "Carreras"
    total_carreras = 3
    data = {
        "title": title,
        "total_carreras":total_carreras
    }
    return render(request,'miapp/carreras.html',data)

def docentes(request):
    title = "Docentes"
    
    data = {
        "title": title,
    }
    return render(request,'miapp/docentes.html',data)