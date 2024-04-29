# EIN082B

## Bienvenidos a **Taller de Lenguajes de Programación**!

Esta es la pagina de inicio de nuestro repositorio. Está escrita en un lenguaje llamado _Markdown_. Puedes encontrar más información al respecto [Acá](https://docs.github.com/es/get-started/writing-on-github)

## Material complementario

* [Introducción a HTML](https://developer.mozilla.org/es/docs/Web/HTML)
* [Comandos git](https://github.com/gdcodev/comandos-git)

## Apoyo Django

## Parte 1:  Configuración del entorno

1. Verificar que Python 3 esté instalado en el equipo

```console
c:\> python --version
```

> Si python no está instalado, instalar según instrucciones de clase
[Descargar instalador desde sitio oficial de Python](http://www.python.org)

1. Verificar que PIP esté instalado en el equipo

```console
c:\> py -m pip --version
```

>Si PIP está desactualizado, actualizar.

```console
c:\> py -m pip install --upgrade pip
```

3.Instalar Django

```console
c:\> pip install django
```

>Puedes verificar la instalación con:

```console
c:\> py -m django --version
```

> [!IMPORTANT]
> No olvidar verificar que Python esté agregado a las variables de entorno.



## Parte 2:  Crear proyecto Django

>Debes crear un directorio donde almacenarás el proyecto. Si trabajarás enlazado a un repo, éste es un buen momento para clonarlo.
En esta demo, se asumirá que los proyectos se almacenarán en

<code>__C:/ProyectosDjango__ </code>

### Para crear el directorio y acceder a él desde el cmd

```console
c:\>Users\yo> cd\
c:\>md ProyectosDjango
c:\>cd ProyectosDjango 

c:\ProyectosDjango>
```

### Para acceder al directorio desde el cmd

```console
c:\>cd c:\ProyectosDjango
c:\ProyectosDjango>
```

### Creando proyecto django

```console
c:\ProyectosDjango>django-admin startproject nombre_proyecto
```

> [!TIP]
> No olvidar verificar que el directorio Script esté agregado a las variables de entorno. De otra forma, el comando django-admin no será reconocido por la consola.

## Parte 3:  Enlazar proyecto django a Visual Studio Code

>Abrir directorio del proyecto django creado en el paso anterior con Visual Studio Code. Ésta será la raiz de nuestro proyecto.

## Parte 4:  Crear Aplicación

>Éste será nuestro sitio web. Desde el terminal de VSCODE, escribir:

```console
c:\ProyectosDjango\Proyecto>py manage.py startapp nombre_aplicacion
```

## Parte 5:  Agregar aplicación al proyecto

>En el archivo <code>settings.py </code> agregar el nombre de la aplicación a __INSTALLED_APPS__

```python
    INSTALLED_APPS = [
    #LIBRERIAS DJANGO
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #MI APP
    'nombre_app',
]
```

## Parte 6:  Iniciar servidor 

>En la terminal de VS CODE iniciar el servidor de pruebas. __No olvidar que el servidor debe mantenerse corriendo durante todo el uso de la aplicación__.

```console
c:\ProyectosDjango\Proyecto>py manage.py runserver
```

Puedes ver los resultados en <code>http://127.0.0.1:8000/</code>
