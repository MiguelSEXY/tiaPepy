from django import template

register = template.Library()

@register.filter
def pertenece_a_grupo(user, group_name):
    """
    Verifica si un usuario pertenece a un grupo.
    """
    return user.groups.filter(name=group_name).exists()
