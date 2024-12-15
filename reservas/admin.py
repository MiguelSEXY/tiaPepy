from django.contrib import admin
from .models import Reserva

class ReservaAdmin(admin.ModelAdmin):
    readonly_field=('fecha_reserva')

admin.site.register(Reserva,ReservaAdmin)