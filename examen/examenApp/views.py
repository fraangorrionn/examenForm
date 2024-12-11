from .forms import PromocionModelForm  # Corrige la importación del formulario
from django.db.models import Q  # Para realizar búsquedas avanzadas
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Promocion

# Vista para listar promociones
def lista_promociones(request):
    promociones = Promocion.objects.all()
    return render(request, 'promociones/lista_promociones.html', {'promociones': promociones})

# Vista para crear una promoción
def crear_promocion(request):
    if request.method == 'POST':
        formulario = PromocionModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Promoción creada con éxito.')
            return redirect('lista_promociones')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        formulario = PromocionModelForm()
    return render(request, 'promociones/crear_promocion.html', {'formulario': formulario})

# Vista para editar una promoción
def editar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        formulario = PromocionModelForm(request.POST, instance=promocion)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Promoción actualizada con éxito.')
            return redirect('lista_promociones')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        formulario = PromocionModelForm(instance=promocion)
    return render(request, 'promociones/editar_promocion.html', {'formulario': formulario, 'promocion': promocion})

# Vista para eliminar una promoción
def eliminar_promocion(request, pk):
    promocion = get_object_or_404(Promocion, pk=pk)
    if request.method == 'POST':
        promocion.delete()
        messages.success(request, 'Promoción eliminada con éxito.')
        return redirect('lista_promociones')
    return render(request, 'promociones/eliminar_promocion.html', {'promocion': promocion})

# Vista para buscar promociones
def buscar_promociones(request):
    query = request.GET.get('q', '')
    fecha_inicio = request.GET.get('fecha_inicio', '')
    fecha_fin = request.GET.get('fecha_fin', '')
    descuento_min = request.GET.get('descuento_min', '')

    promociones = Promocion.objects.all()

    if query:
        promociones = promociones.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
    if fecha_inicio:
        promociones = promociones.filter(fecha_fin__gte=fecha_inicio)
    if fecha_fin:
        promociones = promociones.filter(fecha_fin__lte=fecha_fin)
    if descuento_min:
        promociones = promociones.filter(descuento__gte=descuento_min)

    return render(request, 'promociones/buscar_promociones.html', {
        'promociones': promociones,
        'query': query,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'descuento_min': descuento_min,
    })

# Errores
def handler_404(request, exception):
    """Muestra una página personalizada para el error 404 (página no encontrada)."""
    return render(request, '404.html', status=404)

def handler_500(request):
    """Muestra una página personalizada para el error 500 (error interno del servidor)."""
    return render(request, '500.html', status=500)

def handler_403(request, exception):
    """Muestra una página personalizada para el error 403 (prohibido)."""
    return render(request, '403.html', status=403)

def handler_400(request, exception):
    """Muestra una página personalizada para el error 400 (solicitud incorrecta)."""
    return render(request, '400.html', status=400)

