from django.db import models

class Carrera(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
