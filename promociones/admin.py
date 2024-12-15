from django.contrib import admin
from .models import Promocion

class PromocionAdmin(admin.ModelAdmin):
    readonly_fields=('creacion','modificacion')

admin.site.register(Promocion,PromocionAdmin)

