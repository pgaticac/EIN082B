from django.shortcuts import render
from django.http import HttpResponse

menu = "<hr><ul>"
menu +=   " <li><a href=''>Inicio</a>"
menu +=   " <li><a href='carreras/'>Carreras</a>"
menu +=   " <li><a href='docentes/'>Docentes</a>"
menu += "</ul>"


def home(request):
    
   # titulo = "<h1>Informática USM</h1>"
   # contenido = "<hr><p>Lorem ipsum dolor sit amet."
   # html = titulo + menu + contenido
   # return HttpResponse(html)
   return render(request,'core/home.html')

def carreras(request):
    titulo = "<h1>Carreras</h1>"
    contenido = "<hr><p>Lorem ipsum dolor sit amet."
    html = titulo + menu + contenido
    return HttpResponse(html)

def docentes(request):
    titulo = "<h1>Docentes</h1>"
    return HttpResponse(titulo)