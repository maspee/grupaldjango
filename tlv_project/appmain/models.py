from django.db import models
# Create your models here.
class Cliente(models.Model):
    rut=models.CharField(max_length=10, unique=True)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=100)
    correo=models.CharField(max_length=50)
    telefono=models.IntegerField()
