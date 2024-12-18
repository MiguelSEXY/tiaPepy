from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['producto', 'cantidad']
    
    def clean_cantidad(self):
        cantidad = self.cleaned_data.get('cantidad')
        producto = self.cleaned_data.get('producto')

        if producto and cantidad > producto.stock:
            raise forms.ValidationError(
                f"Superas el stock disponible de {producto.nombre}. \nCant. Disponible= {producto.stock} unidades."
            )
        return cantidad
