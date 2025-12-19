from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Automotora
from .forms import AutomotoraForm, VendedorForm, AutoForm


def index(request):
    return render(request, 'concesionaria/index.html')


def alta_automotora(request):
    form = AutomotoraForm()
    if request.method == "POST":
        form = AutomotoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Sede de Automotora registrada con éxito!')
            form = AutomotoraForm()
    return render(request, 'concesionaria/alta_automotora.html', {'form': form})


def alta_vendedor(request):
    form = VendedorForm()
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vendedor dado de alta correctamente!')
            form = VendedorForm()
    return render(request, 'concesionaria/alta_vendedor.html', {'form': form})


def alta_auto(request):
    form = AutoForm()
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vehículo ingresado al inventario!')
            form = AutoForm()
    return render(request, 'concesionaria/alta_auto.html', {'form': form})


def buscar_automotora(request):
    query = request.GET.get('nombre', '')
    if query:
        resultados = Automotora.objects.filter(nombre__icontains=query)
    else:
        resultados = []
    return render(request, 'concesionaria/buscar_automotora.html', {
        'resultados': resultados, 
        'query': query
    })

def detalle_automotora(request, id):
    automotora = get_object_or_404(Automotora, id=id)
    return render(request, 'concesionaria/detalle_automotora.html', {'automotora': automotora})