from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    nombre = "Pame"
    mensaje = "<h1>Hola "+ nombre + "</h1>"
    return HttpResponse(mensaje)
