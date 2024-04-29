from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'core/home.html',data)


def carreras(request):
    #return HttpResponse('<h1>Carreras</h1>')
    title = "Carreras"

    carrerasList =[
        "Técnico Universitario en Informática",
        "Ingeniería en Informática",
        "Ingeniería de Ejecución en Software",
    ]

    data = {
        "title":title,
        "carreras":carrerasList
    }
    return render(request, 'core/carreras.html',data)


def docentes(request):
    #return HttpResponse('<h1>Docentes</h1>')
    title = "Profesores"

    data = {
        "title":title,
    }
    return render(request, 'core/docentes.html',data)