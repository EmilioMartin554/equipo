from django.db import models

class Plantel(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.CharField(max_length=50)
    posicion = models.CharField(max_length=50)
    peso = models.CharField(max_length=50)
    goles = models.CharField(max_length=50)
# Create your models here.
