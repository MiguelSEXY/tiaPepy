from django.db import models
from promociones.models import Promocion
from django.contrib.auth.models import User  
from django.core.exceptions import ValidationError

class Reserva(models.Model):
    producto = models.ForeignKey(Promocion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Reserva de {self.cantidad} unidades de {self.producto.nombre}"

    def save(self, *args, **kwargs):
        # Verificar si hay suficiente stock
        if self.cantidad > self.producto.stock:
            raise ValidationError(
                f"No hay suficientes unidades disponibles. Stock disponible: {self.producto.stock}."
            )
        
        # Descontar stock y guardar la reserva
        self.producto.stock -= self.cantidad  
        self.producto.save()
        super().save(*args, **kwargs)

    def costo_total(self):
        return self.cantidad * self.producto.precio