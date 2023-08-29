from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
from productos.models import RemiProd
from .models import Remisiones


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']

class RemisionForm(forms.ModelForm):
    class Meta:
        model = Remisiones
        fields = ['fecha_despacho', 'cliente_id']
        labels = {
            'fecha_despacho': 'Fecha de Despacho',
            'cliente_id': 'ID Cliente',
        }
        widgets = {
            'fecha_despacho': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'value': date.today()
                }
            ),
            'cliente_id': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }


class CarritoForm(forms.ModelForm):
    class Meta:
        model = RemiProd
        fields = ['cantidad', 'peso', 'remision_id', 'producto_id']


class DespacharForm(forms.ModelForm):
    class Meta:
        model = Remisiones
        fields = ['estado']