from django.db import models
from django.contrib.auth.models import User
from promociones.models import Promocion

class Notificacion(models.Model):
    titulo= models.CharField(max_length=30,verbose_name="Titulo Notificación")
    imagen=models.ImageField(upload_to="notificaciones", verbose_name="Imagen",default="notificaciones/noImagen.png",blank=True)
    contenido= models.TextField(max_length=200,verbose_name="Contenido de la notificación")
    importante= models.BooleanField(default=False, verbose_name="Es una notificación importante")
    creacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    modificacion= models.DateTimeField(auto_now=True,verbose_name="Fecha de Modificación")
    autor=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Notificacion"
        verbose_name_plural="Notificaciones"
    
    def __str__(self):
        return "Titulo: "+self.titulo
    
class NotificacionEspecial(models.Model):
    titulo= models.CharField(max_length=30,verbose_name="Titulo Notificación")
    imagen=models.ImageField(upload_to="notificacionesEspeciales", verbose_name="Imagen",default="notificaciones/noImagen.png",blank=True)
    contenido= models.TextField(max_length=200,verbose_name="Contenido de la notificación")
    creacion= models.DateTimeField(auto_now_add=True,verbose_name="Fecha de Creación")
    modificacion= models.DateTimeField(auto_now=True,verbose_name="Fecha de Modificación")
    promocion=models.ForeignKey(Promocion,on_delete=models.CASCADE,verbose_name="Promoción vinculada")
    autor=models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        verbose_name="Notificacion (Especial)"
        verbose_name_plural="Notificaciones (Especiales)"
    
    def __str__(self):
        return "Titulo: "+self.titulo