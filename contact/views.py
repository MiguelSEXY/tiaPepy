from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .form import ContactForm
from django.core.mail import send_mail
from core.models import Perfil


def contact(request):
    contact_form=ContactForm()
    if request.method == 'POST':
        contact_form=ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('mensaje', '')

            email=EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>:\n\n{}'.format(name,email,message),
                email,
                ['de1f08f28c915c@inbox.mailtrap.io'],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse('contact')+'?ok')
            except:
                return redirect(reverse('contact')+'?error')

    return render(request,'contact/contact.html', {'form':contact_form})

def enviar_notificacion(usuario, asunto, mensaje):
    perfil = Perfil.objects.get(user=usuario)

    # Verificar si el usuario desea recibir notificaciones
    if perfil.recibir_notificaciones:
        send_mail(
            asunto,
            mensaje,
            'from@example.com',  # Dirección del remitente
            [usuario.email],  # Dirección del destinatario
            fail_silently=False,
        )