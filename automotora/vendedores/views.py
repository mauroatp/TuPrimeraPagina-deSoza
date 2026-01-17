from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Vendedor


class VendedorListView(ListView):
    model = Vendedor
    template_name = 'vendedores/lista_vendedores.html' 
    context_object_name = 'vendedores'


class VendedorDetailView(DetailView):
    model = Vendedor
    template_name = 'vendedores/detalle_vendedor.html'
    context_object_name = 'vendedor'


class VendedorCreateView(CreateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'email', 'dni']
    template_name = 'vendedores/alta_vendedor.html'
    success_url = reverse_lazy('vendedores:lista')


class VendedorUpdateView(UpdateView):
    model = Vendedor
    fields = ['nombre', 'apellido', 'email', 'dni']
    template_name = 'vendedores/editar_vendedor.html'
    success_url = reverse_lazy('vendedores:lista')


class VendedorDeleteView(DeleteView):
    model = Vendedor
    success_url = reverse_lazy('vendedores:lista')


    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)