from django.db import models

class RespuestaFormulario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    duda = models.TextField()
    fecha = models.DateTimeField()
    informacion = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre

# Create your models here.