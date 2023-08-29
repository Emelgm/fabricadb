from django.db import models

class LowerField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class UpperField(models.CharField):

    def get_prep_value(self, value):
        return str(value).upper()


class Cliente(models.Model):
    codigo = UpperField(max_length=10, unique=True, null=True, blank=True)
    nombre = LowerField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    direccion = LowerField(max_length=150, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    nombre = LowerField(max_length=50, null=True, blank=True)
    email = LowerField(max_length=100, null=True, blank=True)
    direccion = LowerField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=10, null=True, blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre