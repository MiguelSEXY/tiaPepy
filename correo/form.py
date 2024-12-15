from django import forms
from promociones.models import Promocion

class ContactForm(forms.Form):
    name=forms.CharField(label='Nombre y apellido',
    required=True,
    min_length=5,
    max_length=25,
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Nombre y Apellido'}))

    email=forms.EmailField(label='Correo',
    required=True,
    min_length=5,
    max_length=40,
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Correo'}))

    mensaje=forms.CharField(label='mensaje',
    required=True,
    min_length=5,
    max_length=50,
    widget=forms.Textarea(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Mensaje','row':5}))


class EnviarCorreoFormulario(forms.Form):
    promocion = forms.ModelChoiceField(queryset=Promocion.objects.all(), required=True, label='Selecciona una promoción')
    mensaje_adicional = forms.CharField(widget=forms.Textarea, required=False, label='Mensaje')
