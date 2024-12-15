from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recibir_notificaciones = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
