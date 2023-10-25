from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
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
            # 'codigo': 'Código',
            'fecha_despacho': 'Fecha de Despacho',
            'cliente_id': 'ID Cliente',
        }
        widgets = {
            # 'codigo': forms.TextInput(
            #     attrs = {
            #         'class': 'form-control',
            #         'placeholder': ''
            #     }
            # ),
            'fecha_despacho': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'value': date.today()
                }
            ),
            'cliente_id': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Ingrese el código del Cliente'
                }
            ),
        }
    
    # def clean(self):
    #     try:
    #         sc = Remisiones.objects.get(
    #             cliente_id=self.cleaned_data["cliente_id"]
    #         )
    #         if not sc.exists():
    #             raise forms.ValidationError('Registro no existe')
    #     except Remisiones.DoesNotExist:
    #         pass
    #     return self.cleaned_data


class CarritoForm(forms.ModelForm):
    class Meta:
        model = RemiProd
        fields = ['cantidad', 'remision_id', 'producto_id']


class DespacharForm(forms.ModelForm):
    class Meta:
        model = Remisiones
        fields = ['estado']