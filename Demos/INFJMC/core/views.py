from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

def home(request):
    #return HttpResponse("<h1>Hola Mundo</h1>")
    return render(request,'core/home.html')

def carrera(request):
    carreras = Carrera.objects.all()
    
    return render(request,'core/carreras.html',{'carreras':carreras})

def docente(request):
    return render(request,'core/docentes.html')
