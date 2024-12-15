from django.shortcuts import render,redirect,get_object_or_404
from .forms import NotificacionForm,NotificacionEspecialForm
from django.core.paginator import Paginator
from .models import Notificacion,NotificacionEspecial
from django.contrib.auth.decorators import login_required
from core.decorators import group_required

@group_required('Vendedor')
def crearNotificacion(request):
    if request.method == 'POST':
        form = NotificacionForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.autor=request.user
            item.save()
            return redirect('notificaciones')  
    else:
        form = NotificacionForm()

    return render(request, 'notificaciones/crearNotificacion.html', {'formNoti': form})


def notificaciones(request): 
    notificaciones = Notificacion.objects.all()
    paginator = Paginator(notificaciones, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notificaciones/notificaciones.html", {'page_obj': page_obj})



@group_required('Vendedor')
def editarNotificacion(request, id):
    notificacion = get_object_or_404(Notificacion, id=id)
    if request.method == 'POST':
        form = NotificacionForm(request.POST, request.FILES, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('notificaciones')
        else:
            print("Errores del formulario:", form.errors)  
    else:
        form = NotificacionForm(instance=notificacion)

    return render(request, 'notificaciones/editar_notificacion.html', {'formNoti': form, 'notificacion': notificacion})


@group_required('Vendedor')
def eliminarNotificacion(request, id):
    notificacion = get_object_or_404(Notificacion, id=id)

    if request.user != notificacion.autor:
        return redirect('notificaciones')

    if request.method == 'POST':
        notificacion.delete()
        return redirect('notificaciones')

    return render(request, 'notificaciones/eliminar_notificacion.html', {'notificacion': notificacion})

def notificacionesEspeciales(request): 
    notificaciones = NotificacionEspecial.objects.all()
    paginator = Paginator(notificaciones, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notificaciones/notificacionesEspeciales.html", {'page_obj': page_obj})

@group_required('Vendedor')
def crearNotificacionEspecial(request):
    if request.method == 'POST':
        form = NotificacionEspecialForm(request.POST, request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.autor=request.user
            item.save()
            form.save()  
            return redirect('notificacionesEspeciales')  
    else:
        form = NotificacionEspecialForm()

    return render(request, 'notificaciones/crearNotificacionEspecial.html', {'formNotiEspecial': form})

@group_required('Vendedor')
def editarNotificacionEspecial(request, id):
    notificacion = get_object_or_404(NotificacionEspecial, id=id)
    if request.method == 'POST':
        form = NotificacionEspecialForm(request.POST, request.FILES, instance=notificacion)
        if form.is_valid():
            form.save()
            return redirect('notificacionesEspeciales')
        else:
            print("Errores del formulario:", form.errors)  
    else:
        form = NotificacionEspecialForm(instance=notificacion)

    return render(request, 'notificaciones/editar_notificacionEspecial.html', {'formNoti': form, 'notificacion': notificacion})


@group_required('Vendedor')
def eliminarNotificacionEspecial(request, id):
    notificacion = get_object_or_404(NotificacionEspecial, id=id)

    if request.user != notificacion.autor:
        return redirect('notificacionesEspeciales')

    if request.method == 'POST':
        notificacion.delete()
        return redirect('notificacionesEspeciales')

    return render(request, 'notificaciones/eliminarNotificacionEspecial.html', {'notificacion': notificacion})
