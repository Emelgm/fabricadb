from django.contrib import admin
from .models import Producto, RemiProd, Recepcion

admin.site.register([Producto, RemiProd, Recepcion])