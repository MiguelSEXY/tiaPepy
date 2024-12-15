from django import template
from django.contrib.auth.models import Group
from django.shortcuts import render

register = template.Library()

@register.filter
def pertenece_a_grupo(user, grupo_name):
    """Filtro para comprobar si el usuario pertenece a un grupo determinado."""
    return user.groups.filter(name=grupo_name).exists()

def vista_con_reservas(request):
    # Verificar si el usuario pertenece al grupo 'Vendedor'
    es_vendedor = request.user.groups.filter(name="Vendedor").exists()

    # Pasar la variable al template
    return render(request, 'reservas/listado_reservas.html', {'es_vendedor': es_vendedor})