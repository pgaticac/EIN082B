from django.db import models

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre
