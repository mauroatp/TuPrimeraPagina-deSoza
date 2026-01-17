from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Automotora, Auto
from .forms import AutomotoraForm, VendedorForm, AutoForm
from django.contrib.auth.decorators import login_required
from .models import Auto
from .forms import AutoForm

def index(request):
    return render(request, 'concesionaria/index.html')

@login_required
def alta_automotora(request):
    form = AutomotoraForm()
    if request.method == "POST":
        form = AutomotoraForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Sede de Automotora registrada con éxito!')
            form = AutomotoraForm()
    return render(request, 'concesionaria/alta_automotora.html', {'form': form})

@login_required
def editar_automotora(request, pk):
    automotora = get_object_or_404(Automotora, pk=pk)
    if request.method == 'POST':
        form = AutomotoraForm(request.POST, instance=automotora)
        if form.is_valid():
            form.save()
            return redirect('buscar_automotora')
    else:
        form = AutomotoraForm(instance=automotora)
    return render(request, 'concesionaria/automotora_form.html', {
        'form': form, 
        'editando': True,
        'automotora': automotora
    })

@login_required
def eliminar_automotora(request, pk):
    automotora = get_object_or_404(Automotora, pk=pk)
    if request.method == 'POST':
        automotora.delete()
        return redirect('buscar_automotora')
    return render(request, 'concesionaria/automotora_confirm_delete.html', {'automotora': automotora})
@login_required
def alta_vendedor(request):
    form = VendedorForm()
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vendedor dado de alta correctamente!')
            form = VendedorForm()
    return render(request, 'concesionaria/alta_vendedor.html', {'form': form})

@login_required
def alta_auto(request):
    form = AutoForm()
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Vehículo ingresado al inventario!')
            form = AutoForm()
    return render(request, 'concesionaria/alta_auto.html', {'form': form})
@login_required
def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'concesionaria/lista_autos.html', {'autos': autos})

@login_required
def buscar_automotora(request):
    query = request.GET.get('nombre', '')
    
    if query:
        automotoras = Automotora.objects.filter(nombre__icontains=query)
    else:
        automotoras = Automotora.objects.none() 
    
    return render(request, 'concesionaria/buscar_automotora.html', {
        'automotoras': automotoras,
        'query': query
    })
@login_required
def detalle_automotora(request, id):
    automotora = get_object_or_404(Automotora, id=id)
    return render(request, 'concesionaria/detalle_automotora.html', {'automotora': automotora})

def about_me(request):
    return render(request, 'concesionaria/about.html')

@login_required
def vehiculo_detalle(request, pk):
    vehiculo = get_object_or_404(Auto, pk=pk)
    return render(request, 'concesionaria/vehiculo_detalle.html', {'vehiculo': vehiculo})


@login_required
def vehiculo_editar(request, pk):
    vehiculo = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=vehiculo)
        if form.is_valid():
            form.save()
            return redirect('vehiculo_detalle', pk=vehiculo.pk)
    else:
        form = AutoForm(instance=vehiculo)
    return render(request, 'concesionaria/vehiculo_form.html', {'form': form, 'editando': True})


@login_required
def vehiculo_eliminar(request, pk):
    vehiculo = get_object_or_404(Auto, pk=pk)
    if request.method == 'POST':
        vehiculo.delete()
        return redirect('lista_autos')
    return render(request, 'concesionaria/vehiculo_confirm_delete.html', {'vehiculo': vehiculo})