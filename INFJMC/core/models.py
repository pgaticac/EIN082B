from django.db import models

#Class Carrera
class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    duracion = models.IntegerField()

    def __str__(self) -> str:
       return self.nombre



#Class Profesor
class Profesor(models.Model):
    nombre = models.CharField(max_length=80)
    imagen_url = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre




tipo_mensajes = [
   ("0" , "sugerencia"),
   ("1" , "consulta"),
   ("2" , "oferta laboral"),
   ("3" ,  "oferta práctica"),
]


class Mensaje(models.Model):
    nombre = models.CharField(max_length=50)
    email = models.EmailField()
    tipo = models.CharField(max_length=20, choices=tipo_mensajes)
    asunto = models.CharField(max_length=50)
    texto = models.TextField()

    def __str__(self) -> str:
        return self.asunto