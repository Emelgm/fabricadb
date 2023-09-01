from django.db import models
from clientes.models import Cliente
from datetime import date


class LowerField(models.CharField):

    def get_prep_value(self, value):
        return str(value).lower()


class UpperField(models.CharField):

    def get_prep_value(self, value):
        return str(value).upper()


class Remisiones(models.Model):
    codigo = UpperField(max_length=10, unique=True, null=False, blank=False)
    fecha_despacho = models.DateField(default=date.today(),null=False, blank=False)
    estado = models.BooleanField(default=True)
    orden = models.BooleanField(default=False)
    usuario = LowerField(max_length=15, null=True, default='')
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # def make_id(*args, **kwargs):
    #     # time = timezone.now().strftime('%H%M%S')
    #     count = Remisiones.objects.all().count()
    #     key = Remisiones.objects.order_by('id').last().id
    #     if count > 0:
    #         new_id = 'D' + str(key+1).zfill(3)
    #     else:
    #         new_id = 'D' + str(1).zfill(3)
        
    #     codigo = str(new_id)
    #     return codigo
    
    def __str__(self):
        return self.codigo
