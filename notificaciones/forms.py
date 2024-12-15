from django import forms
from .models import Notificacion,NotificacionEspecial
from promociones.models import Promocion

class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = ['titulo', 'imagen', 'contenido', 'importante']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la notificación'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Ingrese el contenido de la notificación'
            }),
            'importante': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class NotificacionEspecialForm(forms.ModelForm):
    class Meta:
        model = NotificacionEspecial
        fields = ['titulo', 'imagen', 'contenido', 'promocion']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el título de la notificación'
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Ingrese el contenido de la notificación'
            }),
        }
        promocion=forms.ModelChoiceField(
            queryset=Promocion.objects.all(),
            empty_label="Selecciona una promoción",
            widget=forms.Select(attrs={'class': 'form-control'})
        )
        