from django.db import models

class Profesor(models.Model):
    rut = models.CharField(max_length=10,primary_key=True)
    nombre=models.CharField(max_length=60)
    titulo=models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name_plural = "Profesores"

class Carrera(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True)
    nombre = models.CharField(max_length=60)
    duracion = models.IntegerField()
    jefe_carrera = models.ForeignKey(Profesor, on_delete=models.SET_NULL, null=True, blank=True, related_name="carreras")
    
    def __str__(self) -> str:
        return self.nombre