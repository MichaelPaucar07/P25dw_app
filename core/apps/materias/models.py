from django.db import models
from apps.docentes.models import Docente

class Materias(models.Model):
    nombre = models.CharField(max_length=100)
    numero_creditos = models.IntegerField()
    nivel = models.CharField(max_length=20)
    horas_semana = models.IntegerField()
    jornada = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='materias/')
    docentes = models.ManyToManyField(Docente, related_name='materias')
    
    def __str__(self):
        return self.nombre
