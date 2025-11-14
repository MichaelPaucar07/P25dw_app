from django.db import models
from core.apps.docentes.models import Docente

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    numero_creditos = models.IntegerField()
    nivel = models.CharField(max_length=20)
    horas_semana = models.IntegerField()
    jornada = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='cursos/')
    docentes = models.ManyToManyField(Docente, related_name='cursos')
    
    def __str__(self):
        return self.nombre
