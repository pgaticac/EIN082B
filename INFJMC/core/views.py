from django.shortcuts import render
from django.http import HttpResponse

def home(request):
   # return HttpResponse('<h1>Hola Mundo</h1>')
    return render(request, 'core/home.html')
def carreras(request):
    #return HttpResponse('<h1>Carreras</h1>')
    return render(request, 'core/carreras.html')


def docentes(request):
    #return HttpResponse('<h1>Docentes</h1>')
    return render(request, 'core/docentes.html')