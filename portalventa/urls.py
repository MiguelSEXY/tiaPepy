from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf import settings
from notificaciones import views as viewsNotificaciones
from productos import views as viewsProductos
from promociones import views as viewPromociones
from reservas import views as viewReservas
from correo import views as viewCorreo

urlpatterns = [ 
    path('', include('core.urls')),
    path("admin/", admin.site.urls),
    path('', core_views.home, name='home'),
    path('aboutus/', core_views.aboutus, name='aboutus'),
    path('sobrenosotros/', core_views.aboutus, name='aboutus'),
    path('productos/',viewsProductos.productos,name="productos"),
    path('notificaciones/',viewsNotificaciones.notificaciones,name="notificaciones"),
    path('contacto/', include('contact.urls')),
    path('CrearNotificacion/', viewsNotificaciones.crearNotificacion,name="CrearNotificacion"),
    path('CrearProducto/',viewsProductos.AgregarProducto,name="CrearProducto"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('editar_producto/<int:producto_id>/', viewsProductos.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:producto_id>/', viewsProductos.eliminar_producto, name='eliminar_producto'),
    path('editar_notificacion/<int:id>/', viewsNotificaciones.editarNotificacion, name='editar_notificacion'),
    path('eliminar_notificacion/<int:id>/', viewsNotificaciones.eliminarNotificacion, name='eliminar_notificacion'),
    path('logout',core_views.cerrarSesion,name="logout"),
    path('promociones/',viewPromociones.promociones,name='Promociones'),
    path('crearPromocion/',viewPromociones.crearPromocion,name='crearPromocion'),
    path('editarPromocion/<int:promo_id>/',viewPromociones.editarPromocion,name='editarPromocion'),
    path('eliminarPromocion/<int:id>/',viewPromociones.eliminarPromocion,name='eliminarPromocion'),
    path('crearNotificacionEspecial/',viewsNotificaciones.crearNotificacionEspecial,name="crearNotificacionEspecial"),
    path('notificacionesEspeciales/',viewsNotificaciones.notificacionesEspeciales,name='notificacionesEspeciales'),
    path('editarNotificacionEspecial/<int:id>/',viewsNotificaciones.editarNotificacionEspecial,name='editarNotificacionEspecial'),
    path('eliminarNotificaionEspecial/<int:id>/',viewsNotificaciones.eliminarNotificacionEspecial,name='eliminarNotificacionEspecial'),
    path('crearReserva/',viewReservas.crearReserva,name="crearReserva"),
    path('misReservas/',viewReservas.misReservas, name='misReservas'),
    path('reserva/detalle/<int:reserva_id>/', viewReservas.detalleReserva, name='detalleReserva'),
    path('sinAcceso',core_views.sinAcceso,name="Sin Acceso"),
    path('cambiarPreferencias',core_views.cambiarPreferencias,name="cambiarPreferencias"),
    path('perfil/', core_views.perfil, name='perfil'),
    path('reservas/', viewReservas.listadoReservas, name='listadoReservas'),
    path('completarReserva/<int:reserva_id>/',viewReservas.completarReserva,name='completarReserva'),
    path('cancelarReserva/<int:reserva_id>/',viewReservas.cancelarReserva,name='cancelarReserva'),
    path('crearCorreo',viewCorreo.crearCorreo,name="crearCorreo"),
    path('enviarCorreo',viewCorreo.enviarCorreo,name="enviarCorreo"),

]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)