from django.shortcuts import render,redirect,get_object_or_404
from .form import PromocionForm
from .models import Promocion
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.decorators import group_required


def promociones(request): 
    promos=Promocion.objects.all()
    paginator = Paginator(promos, 3) 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"promociones/verPromociones.html",{'page_obj':page_obj})

@group_required('Vendedor')
def crearPromocion(request):
    if request.method=='GET':
        return render(request,'promociones/crearPromocion.html',{
            'formPromo':PromocionForm
        })
    else:
        try:
            form= PromocionForm(request.POST,request.FILES)
            if form.is_valid():
                item=form.save(commit=False)
                item.autor=request.user
                item.save()
                return redirect('/promociones')
            else:
                print("ERROR en el Formulario")

        except ValueError:
            return render(request,'promociones/crearPromocion.html',{
            'formPromo':PromocionForm,
            'error': "Error en los datos"
        })


@group_required('Vendedor')
def editarPromocion(request, promo_id):
    promo = get_object_or_404(Promocion, id=promo_id)
    if request.method == "POST":
        form = PromocionForm(request.POST, request.FILES, instance=promo)
        if form.is_valid():
            form.save()
            return redirect('/promociones')  
    else:
        form = PromocionForm(instance=promo)
    return render(request, 'promociones/editarPromocion.html', {'formPromo': form})


@group_required('Vendedor')
def eliminarPromocion(request, id):
    promocion = get_object_or_404(Promocion, id=id)
    if request.method == "POST":
        promocion.delete()
        messages.success(request, "Promoción eliminada correctamente.")
        return redirect('/promociones')  
    return render(request, 'promociones/eliminarPromocion.html', {'promo': promocion})
