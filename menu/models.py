from django.db import models
class Permisos(models.Model):
    llave = models.CharField(max_length=50, blank=True)
    descripcion = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.llave
    class Meta:
        permissions = [
            ("proceso_listado", "proceso_listado"),
            ("proceso_extender", "proceso_extender"),
            ("proceso_adicionar", "proceso_adicionar"),
            ("proceso_editar", "proceso_editar"),
            ("proceso_deshabilitar", "proceso_deshabilitar"),
            ("proceso_eliminar", "proceso_eliminar"),
            ("proceso_exportar", "proceso_exportar"),
            ("proceso_imprimir", "proceso_imprimir"),
            ("detalle_proceso_listado", "detalle_proceso_listado"),
            ("detalle_proceso_extender", "detalle_proceso_extender"),
            ("detalle_proceso_adicionar", "detalle_proceso_adicionar"),
            ("detalle_proceso_editar", "detalle_proceso_editar"),
            ("detalle_proceso_deshabilitar", "detalle_proceso_deshabilitar"),
            ("detalle_proceso_eliminar", "detalle_proceso_eliminar"),
            ("detalle_proceso_exportar", "detalle_proceso_exportar"),
            ("detalle_proceso_imprimir", "detalle_proceso_imprimir"),
        ]
