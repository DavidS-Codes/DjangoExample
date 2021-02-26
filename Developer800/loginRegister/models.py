from django.db import models

# Create your models here.
class UserApp(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    fecha_registro = models.DateTimeField(auto_now=True)

