from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('creacion','modificacion')

admin.site.register(Producto,ProductoAdmin)

