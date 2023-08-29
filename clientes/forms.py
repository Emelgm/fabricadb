from django import forms 
from .models import Cliente, Proveedor


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['codigo', 'nombre', 'telefono', 'direccion']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }
        widgets = {
            'codigo': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el código del cliente'
                }
            ),
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del cliente'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el número de contacto del cliente'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el domicilio del cliente'
                }
            ),
        }


class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'email', 'telefono', 'direccion']
        labels = {
            'nombre': 'Nombre',
            'email': 'Correo Electróncio',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del proveedor'
                }
            ),
            'email': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el correo electrónico del proveedor'
                }
            ),
            'telefono': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el número de contacto del proveedor'
                }
            ),
            'direccion': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el domicilio del proveedor'
                }
            ),
        }