from django.db import models

#Class Carrera
#Class Profesor

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