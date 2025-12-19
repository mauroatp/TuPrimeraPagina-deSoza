from django import forms
from .models import Automotora, Vendedor, Auto

class AutomotoraForm(forms.ModelForm):
    class Meta:
        model = Automotora
        fields = ['nombre', 'direccion', 'email_contacto']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'apellido', 'documento']

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['modelo', 'marca', 'anio', 'precio']