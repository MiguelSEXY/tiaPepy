from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm,PreferenciasNotificacionForm
from django.contrib.auth import authenticate, login
from notificaciones.models import Notificacion
from django.contrib.auth.models import Group
from .models import Perfil
from django.core.paginator import Paginator
from notificaciones.models import NotificacionEspecial
from core.decorators import group_required


def home(request): 
    notificaciones = Notificacion.objects.all()
    paginator = Paginator(notificaciones, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notificaciones/notificaciones.html", {'page_obj': page_obj})


def aboutus(request): 
    return render(request,"core/sobrenosotros.html")

def contacto(request): 
    return render(request,"core/contacto.html")

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user=user_creation_form.save()
            perfil = Perfil.objects.create(user=user)
            group_name = 'Comprador'  # Nombre del grupo al que debe pertenecer el usuario
            group = Group.objects.get(name=group_name)  # Buscamos el grupo
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            user.groups.add(group)

            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


@login_required
def cerrarSesion(request):
    logout(request)
    return redirect('/')

def sinAcceso(request):
    return render(request,'core/sinAcceso.html',)

def cambiarPreferencias(request):
    perfil = Perfil.objects.get(user=request.user)
    if request.method == 'POST':
        form = PreferenciasNotificacionForm(request.POST, instance=perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')  # Redirige a una página de perfil
    else:
        form = PreferenciasNotificacionForm(instance=perfil)
    
    return render(request, 'core/cambiarPreferencia.html', {'form': form})

def perfil(request):
    try:
        perfil = Perfil.objects.get(user=request.user)

    except Perfil.DoesNotExist:
        perfil = None

    return render(request, 'core/perfil.html', {'perfil': perfil})

def notificacionesEspeciales(request): 
    notificaciones = NotificacionEspecial.objects.all()
    paginator = Paginator(notificaciones, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "notificaciones/notificacionesEspeciales.html", {'page_obj': page_obj})