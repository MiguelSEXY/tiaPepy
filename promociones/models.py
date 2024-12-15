from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Promocion(models.Model):
    nombre= models.CharField(max_length=30,verbose_name="Nombre de la promoción")
    imagen=models.ImageField(upload_to="promociones", verbose_name="Imagen de la promoción",default="promociones/default.jpg",blank=True)
    precio= models.IntegerField(validators=[
        MinValueValidator(0)
    ], verbose_name="Precio")
    stock= models.IntegerField(validators=[MinValueValidator(0,message='el stock de la promoción no puede ser inferior a 0')])
    creacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    modificacion= models.DateTimeField(auto_now=True,verbose_name="Fecha de Modificación")
    autor=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Promocion"
        verbose_name_plural="Promociones"
    
    def __str__(self):
        return "Promo: "+self.nombre
    
    def reservar(self, cantidad):

        if cantidad > self.stock:
            raise ValueError("No hay suficientes unidades disponibles para reservar.")
        self.stock -= cantidad
        self.save()

    def aumentar_disponibilidad(self, cantidad):
        self.stock += cantidad
        self.save()