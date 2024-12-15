from django.shortcuts import render,redirect,get_object_or_404
from .form import ProductoForm
from .models import Producto
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.decorators import group_required


@group_required('Vendedor')
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        producto.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return redirect('productos')  
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})


@group_required('Vendedor')
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')  
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'productos/editar_producto.html', {'form': form})

@group_required('Vendedor')
def AgregarProducto(request):
    if request.method=='GET':
        return render(request,'productos/agregarProducto.html',{
            'formProducto':ProductoForm
        })
    else:
        try:
            form= ProductoForm(request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                print("ERROR en el Formulario")

        except ValueError:
            return render(request,'productos/agregarProducto.html',{
            'formProducto':ProductoForm,
            'error': "Error en los datos"
        })

def productos(request): 
    ventas=Producto.objects.all()
    paginator = Paginator(ventas, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"productos/productos.html",{'page_obj':page_obj})