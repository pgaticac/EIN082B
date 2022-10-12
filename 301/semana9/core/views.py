from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    html = "<h1>Hola Mundo!</h1>"
    return HttpResponse(html)

def servicios(request):
    html = "<h1>Servicios</h1>"
    return HttpResponse(html)

