from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Perfil


class PerfilCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Perfil
        fields = UserCreationForm.Meta.fields + ('email', 'pais', 'fecha_de_nacimiento', 'direccion', 'avatar')


class PerfilChangeForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('first_name', 'last_name', 'pais', 'fecha_de_nacimiento', 'direccion', 'avatar')
        
        
        widgets = {
            'fecha_de_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'pais': 'País',
            'fecha_de_nacimiento': 'Fecha de Nacimiento',
            'avatar': 'Foto de Perfil',
        }