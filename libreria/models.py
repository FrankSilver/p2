from django.db import models
from django.utils import timezone

class Articulo(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()

#    def publish(self):
#        self.published_date = timezone.now()
#        self.save()

    def __str__(self):
        return self.nombre
