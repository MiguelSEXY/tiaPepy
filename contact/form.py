from django import forms

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
    max_length=20,
    widget=forms.EmailInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Correo'}))

    mensaje=forms.CharField(label='mensaje',
    required=True,
    min_length=5,
    max_length=50,
    widget=forms.TextInput(attrs={'class': 'form-control',
    'placeholder':'Ingrese su Mensaje','row':5}))
