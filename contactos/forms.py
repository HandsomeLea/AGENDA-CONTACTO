from django import forms
from .models import Contacto

#Requerimientos para rellenar el contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'telefono', 'correo', 'direccion']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'telefono': forms.TextInput(attrs={'placeholder': '+56 9 1234 5678'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'ejemplo@correo.com'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Dirección'}),
        }                                       #placeholder = nada o espacio
