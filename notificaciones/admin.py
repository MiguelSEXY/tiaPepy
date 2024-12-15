from django.contrib import admin
from .models import Notificacion,NotificacionEspecial

class NotificacionAdmin(admin.ModelAdmin):
    readonly_fields=('creacion','modificacion')

admin.site.register(Notificacion,NotificacionAdmin)

class NotificacionEspecialAdmin(admin.ModelAdmin):
    readonly_fields=('creacion','modificacion')

admin.site.register(NotificacionEspecial,NotificacionEspecialAdmin)