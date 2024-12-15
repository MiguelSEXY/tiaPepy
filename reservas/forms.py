from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['producto', 'cantidad']
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        producto = self.cleaned_data['producto']

        if cantidad > producto.stock:
            raise forms.ValidationError(f"No hay suficientes unidades de {producto.nombre}.")
        return cantidad
