from django.db import models

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    cedula = models.CharField(max_length=10, unique=True)
    tipo_sangre = models.CharField(max_length=5)
    direccion = models.TextField()
    imagen = models.ImageField(upload_to='docentes/')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"