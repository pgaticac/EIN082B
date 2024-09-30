from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def carreras(request):
    titulo = "Carreras"
    carreras = ("Técnico Universitario en Informática",
                "Ingeniería en Informática",
                "Ingeniería de Ejecución en Software",
                "Ingeniería Civil Informática")
    data = {
        "titulo":titulo,
        "carreras": carreras
    }
    return render(request,'core/carreras.html',data)
    

def profesores(request):
    titulo = "Profesores"
    h1 = "<h1> "+ titulo + "</h1>"
    return HttpResponse(h1)
