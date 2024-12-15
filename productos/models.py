from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre= models.CharField(max_length=30,verbose_name="Nombre del Producto")
    imagen=models.ImageField(upload_to="productos", verbose_name="Imagen",default="productos/default.png",blank=True)
    precio= models.IntegerField(validators=[
        MinValueValidator(0)
    ], verbose_name="Precio")
    creacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    modificacion= models.DateTimeField(auto_now=True,verbose_name="Fecha de Modificación")
    autor=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Producto"
        verbose_name_plural="Productos"
    
    def __str__(self):
        return "Producto: "+self.nombre