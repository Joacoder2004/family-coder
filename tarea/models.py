from errno import EADDRNOTAVAIL
from unicodedata import name
from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=20)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(auto_now_add=True, null=True, blank=True)