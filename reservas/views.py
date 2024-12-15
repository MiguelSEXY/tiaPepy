from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservaForm
from .models import Promocion, Reserva
from core.decorators import group_required
from django.contrib import messages


@group_required('Comprador')
def crearReserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            # Guardar la reserva
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('misReservas')
    else:
        form = ReservaForm()

    return render(request, 'reservas/crearReserva.html', {'form': form})

@group_required('Comprador')
def misReservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)  # Obtener las reservas del usuario
    return render(request, 'reservas/misReservas.html', {'reservas': reservas})

@group_required('Comprador')
def detalleReserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    producto = reserva.producto

    # Si el método es POST, el usuario ha confirmado la eliminación

    if request.method == 'POST':
        # Devolvemos la cantidad al stock y guardamos el cambio
        producto.stock += reserva.cantidad
        producto.save()
        # Eliminar la reserva
        reserva.delete()
        # Redirigir a la lista de reservas después de eliminar
        return redirect('misReservas')
    return render(request, 'reservas/detalleReserva.html', {'reserva': reserva})


@group_required('Vendedor')
def listadoReservas(request):
    reservas = Reserva.objects.select_related('usuario', 'producto').all()

    return render(request, 'reservas/listadoReservas.html', {'reservas': reservas})


@group_required('Vendedor')
def completarReserva(request,reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    if request.method == "POST":
        reserva.delete()
        messages.success(request, "Reserva completada efectivamente.")
        return redirect('/reservas')  
    return render(request, 'reservas/completarReserva.html', {'promo': reserva})


def cancelarReserva(request,reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    producto = reserva.producto

    if request.method == "POST":
        producto = reserva.producto
        producto.stock += reserva.cantidad
        producto.save()

        reserva.delete()
        messages.success(request, "Reserva Cancelada.")

        return redirect('/reservas')  
    return render(request, 'reservas/cancelarReserva.html', {'promo': reserva})


def filtrarReservas(request):
    pass