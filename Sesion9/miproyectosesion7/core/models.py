from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True, verbose_name="Codigo")
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    duracion = models.IntegerField(verbose_name="Duración (Semestres)")
    jefecarrera = models.CharField(max_length=200,  verbose_name="Nombre") 

    def __str__(self) -> str:
        return self.nombre
    
class Docente(models.Model):
    rut = models.CharField(max_length=20, verbose_name="RUT")
    nombre = models.CharField(max_length=20, verbose_name="Nombre")
    titulo = models.CharField(max_length=50, verbose_name="Titulo")

    def __str__(self) -> str:
        return self.rut