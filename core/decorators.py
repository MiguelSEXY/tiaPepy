from django.shortcuts import redirect
from functools import wraps

def group_required(group_name):
    """
    Decorador que permite el acceso solo si el usuario pertenece al grupo especificado.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('Sin Acceso')
        return _wrapped_view
    return decorator
