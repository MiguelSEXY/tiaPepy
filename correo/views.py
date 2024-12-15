from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .form import ContactForm,EnviarCorreoFormulario
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User

def crearCorreo(request):
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
                ['82b71db7a90955@inbox.mailtrap.io'],
                reply_to=[email],
            )
            try:
                email.send()
                return redirect(reverse('Contacto')+'?ok',{'form':contact_form})
            except:
                return redirect(reverse('Contacto')+'?error')

    return render(request,'contacto/contacto.html', {'form':contact_form})



def enviarCorreo(request):
    if request.method == 'POST':
        form = EnviarCorreoFormulario(request.POST)
        usuarios_con_notificaciones = User.objects.filter(perfil__recibir_notificaciones=True)
        correos = [usuario.email for usuario in usuarios_con_notificaciones]

        if form.is_valid():
            promocion = form.cleaned_data['promocion']
            mensaje_adicional = form.cleaned_data['mensaje_adicional']
            
            nombre_promocion = promocion.nombre
            stock = promocion.stock
            precio = promocion.precio

            # Contenido del correo
            subject = f"Promoción: {nombre_promocion}"
            message = f"""
            ¡No te pierdas esta oferta!
            
            Promoción: {nombre_promocion}
            Stock disponible: {stock}
            Precio: ${precio}
            
            {mensaje_adicional}
            """
            from_email = '82b71db7a90955@inbox.mailtrap.io'
            recipient_list = correos  # Lista de correos a los que enviar

            send_mail(subject, message, from_email, recipient_list)

            messages.success(request, 'Correo de promoción enviado con éxito.')
            return render(request, 'correo/confirmacion.html', {'promocion': promocion})
    else:
        form = EnviarCorreoFormulario()

    return render(request, 'correo/enviarPromocion.html', {'form': form})
