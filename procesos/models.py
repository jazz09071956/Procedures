from django.db import models
from tablabase.models import TablaBase

# Create your models here.
class Proceso(TablaBase):
    codigo_proceso = models.CharField(max_length=50, blank=True)
    nombre_proceso = models.CharField(max_length=200)
    descripcion_proceso = models.TextField(blank=True)
    def __str__(self):
        return self.nombre_proceso
    class Meta:
        verbose_name_plural = "Procesos"
        verbose_name = "Proceso"
class Detalle_Proceso(TablaBase):
    proceso = models.ForeignKey(Proceso,on_delete=models.PROTECT)
    correlativo = models.CharField(max_length=10, blank=True)
    nombre_detalle_proceso = models.CharField(max_length=200, blank=True)
    descripcion_detalle_proceso = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='procesos/detalles/', blank=True, null=True)
    def __str__(self):
        return self.nombre_detalle_proceso
    class Meta:
        verbose_name_plural = "Detalles de Proceso"
        verbose_name = "Detalle de Proceso"
