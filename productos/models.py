from django.db import models
from remisiones.models import Remisiones
from clientes.models import Proveedor
from datetime import date


class LowerField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class UpperField(models.CharField):

    def get_prep_value(self, value):
        return str(value).upper()


class Producto(models.Model):
    codigo = UpperField(max_length=10, unique=True, null=False, blank=False)
    nombre = LowerField(max_length=150, null=False, blank=False)
    marca = LowerField(max_length=150, null=True, blank=True)
    cantidad = models.IntegerField()
    peso = models.FloatField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    

class RemiProd(models.Model):
    cantidad = models.IntegerField()
    peso = models.FloatField()
    remision_id = models.ForeignKey(Remisiones, on_delete=models.CASCADE)
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Recepcion(models.Model):
    fecha_recepcion = models.DateField(default=date.today(),null=False, blank=False)
    orden = models.BooleanField(default=False)
    usuario = LowerField(max_length=15, null=True, default='')
    proveedor_id = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class ReceProd(models.Model):
    cantidad = models.IntegerField()
    producto_id = models.ForeignKey(Producto, on_delete=models.CASCADE)
    recepcion_id = models.ForeignKey(Recepcion, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)