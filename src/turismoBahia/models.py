from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Museos(models.Model):

    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    entrada = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

class CentroHistorico(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
   
    def __str__(self):
        return f"{self.nombre} - {self.direccion}"


class Parques(models.Model):
    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    
    def __str__(self):
        return f"{self.nombre} - {self.direccion}"


class Avatar(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True)

