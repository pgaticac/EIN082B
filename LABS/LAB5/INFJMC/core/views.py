from django.shortcuts import render
from django.http import HttpResponse

menu = "<hr><ul>"
menu +=   " <li><a href=''>Inicio</a>"
menu +=   " <li><a href='carreras/'>Carreras</a>"
menu +=   " <li><a href='docentes/'>Docentes</a>"
menu += "</ul>"


def home(request):
    return render(request,'core/index.html')

def carreras(request):
    return render(request,'core/carreras.html')

def docentes(request):
    return render(request,'core/docentes.html')