from django.db import models
from django.contrib.auth.models import AbstractUser

"""
cuando se cambia la tabla de usuarios
antes de realizar la primer migracion, realizar los cambio y luego ejecutar
manage.py makemigrations
"""
class Usuario(AbstractUser):
    codigo_sala = models.CharField(max_length=6)
    nombre_sala = models.CharField(max_length=50)
    def __str__(self):
        return '{}:{}'.format(self.codigo_sala,self.nombre_sala)
