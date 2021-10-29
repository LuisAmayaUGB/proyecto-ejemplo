from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Mascota(models.Model):
    nombre=models.CharField(max_length=25)
    apellidos = models.CharField(max_length=25)
    edad = models.CharField(max_length=25)

    def __str__(self):
      return self.nombre


class Persona(models.Model):   #Heredamos de la clase models de django

  # Campo nombre de tipo texto con un máximo de 30 caracteres
  nombre = models.CharField(max_length=30)
  # Campo apellidos de tipo texto con un máximo de 30 caracteres
  apellidos = models.CharField(max_length=30)

  def __str__(self):
    return self.nombre+" "+self.apellidos
