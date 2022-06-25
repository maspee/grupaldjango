from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

class Publicacion(models.Model):
    titulo= models.CharField(max_length=100)
    contenido= models.TextField()
    fecha_publicacion= models.DateTimeField(default= timezone.now)
    autor= models.ForeignKey(User, on_delete= models.CASCADE)

    #con esto nos retorna el titulo de la publicacion, no la ubicacion en memoria.
    def __str__(self): 
        return self.titulo


