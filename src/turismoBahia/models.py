from django.db import models



# Create your models here.
class Museos(models.Model):

    nombre = models.CharField(max_length=120)
    direccion = models.CharField(max_length=120)
    entrada = models.CharField(max_length=120)
    contacto = models.FloatField()

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



