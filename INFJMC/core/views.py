from django.shortcuts import render
from django.http import HttpResponse
from .models import Mensaje, Profesor
import requests  #pip install requests
import json

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
    
    # #obtener la data desde API
    # response = requests.get('https://666da9297a3738f7caccf886.mockapi.io/inf/docentes')

    # #transformar data a JSON
    # profesoresJSON = response.json()

    # #Crear lista de profesores desde la data JSON
    # profesores = list()

    # for p in profesoresJSON:
    #     profesor = Profesor()
    #     profesor.nombre = p['nombre']
    #     profesor.imagen_url = p['avatar']
    #     profesor.especialidad = p['especialidad']
    #     profesor.save()
    #     profesores.append(profesor)


    data = {
        "title":title,
        # "profesores" : profesores
    }
    return render(request, 'core/docentes.html',data)

def contacto(request):
    if(request.POST):
        #capturar datos desde el formulario
        nombre = request.POST['txtNombre']
        email = request.POST['txtEmail']
        tipo = request.POST['cboTipo']
        asunto = request.POST['txtAsunto']
        texto = request.POST['txtMensaje']

        #validaciones de reglas de negocio

        #construir y cargar el objeto con los datos del form
        mensaje = Mensaje()
        mensaje.nombre = nombre
        mensaje.email = email
        mensaje.tipo = tipo
        mensaje.asunto = asunto
        mensaje.texto = texto

        #guardar cambios en la base de datos
        mensaje.save()
    return render(request, 'core/contacto.html')

def nuevo_mensaje(request):
    if(request.POST):
        #capturar datos desde el formulario
        nombre = request.POST["txtNombre"]
        email = request.POST['txtEmail']
        tipo = request.POST['cboTipo']
        asunto = request.POST['txtAsunto']
        texto = request.POST['txtMensaje']

        #validaciones de reglas de negocio

        #construir y cargar el objeto con los datos del form
        mensaje = Mensaje()
        mensaje.nombre = nombre
        mensaje.email = email
        mensaje.tipo = tipo
        mensaje.asunto = asunto
        mensaje.texto = texto

        #guardar cambios en la base de datos
        mensaje.save()
        
    return render(request, 'core/contacto.html')
        
   
   