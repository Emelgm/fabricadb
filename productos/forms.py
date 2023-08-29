from django import forms
from .models import Producto, Recepcion
from datetime import date


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo','nombre', 'marca', 'cantidad', 'peso']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'marca': 'Marca',
            'cantidad': 'Cantidad',
            'peso': 'Peso (kg)',
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el código del producto'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'marca': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la marca del producto'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad del producto'
                }
            ),
            'peso': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el peso del producto'
                }
            ),
        }

class RecepcionForm(forms.ModelForm):
    class Meta:
        model = Recepcion
        fields = ['fecha_recepcion', 'proveedor_id']
        labels = {
            'fecha_recepcion': 'Fecha de Recepción',
            'proveedor_id': 'Nombre Proveedor',
        }
        widgets = {
            'fecha_recepcion': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control', 
                    'type': 'date',
                    'value': date.today()
                }
            ),
            'proveedor_id': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }