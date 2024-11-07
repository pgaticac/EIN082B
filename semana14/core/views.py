from django.shortcuts import render
from .models import Carrera, Profesor
import requests

# Create your views here.
def home(request):
    titulo = "Inicio"
    data = {
        "titulo": titulo
    }
    return render(request,'core/index.html', data)

def carreras(request):
    titulo = "Carreras"
        
    if (request.POST):
        #capturar los datos desde el form
        codigo = request.POST["codigo"]
        nombre = request.POST["nombre"]
        duracion = request.POST["duracion"]
        
        #Validaciones
        
        
        
        
        nueva = Carrera(codigo=codigo,nombre=nombre,duracion=duracion)
        nueva.save()    
    
    carreras = Carrera.objects.all()
    data = {
        "titulo":titulo,
        "carreras": carreras
    }
    return render(request,'core/carreras.html',data)
    

def profesores(request):
    titulo = "Profesores"
    
    info = requests.get("https://666da9297a3738f7caccf886.mockapi.io/inf/docentes")
    profesores = info.json()
    
    lista_profes = list()
    
    for p in profesores:
        profesor = Profesor(
            rut = p["id"],
            nombre = p["nombre"],
            titulo = p["especialidad"]
        )
        
        lista_profes.append(profesor)
    
    
    data = {
        "titulo":titulo,
        "profesores":lista_profes,
    
    }
    return render(request,'core/profesores.html',data)

