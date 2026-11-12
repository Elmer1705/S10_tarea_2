from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Marca, Producto

# ==========================================
# VISTAS PARA MARCA
# ==========================================

class MarcaListView(ListView):
    model = Marca
    template_name = 'facturacion/marca_list.html'
    context_object_name = 'marcas'

class MarcaCreateView(CreateView):
    model = Marca
    fields = ['nombre', 'pais_origen', 'activo']
    template_name = 'facturacion/marca_form.html'
    success_url = reverse_lazy('marca_list')

class MarcaUpdateView(UpdateView):
    model = Marca
    fields = ['nombre', 'pais_origen', 'activo']
    template_name = 'facturacion/marca_form.html'
    success_url = reverse_lazy('marca_list')

class MarcaDeleteView(DeleteView):
    model = Marca
    template_name = 'facturacion/marca_confirm_delete.html'
    success_url = reverse_lazy('marca_list')


# ==========================================
# VISTAS PARA PRODUCTO
# ==========================================

class ProductoListView(ListView):
    model = Producto
    template_name = 'facturacion/producto_list.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock', 'marca', 'activo']
    template_name = 'facturacion/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ['nombre', 'precio', 'stock', 'marca', 'activo']
    template_name = 'facturacion/producto_form.html'
    success_url = reverse_lazy('producto_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'facturacion/producto_confirm_delete.html'
    success_url = reverse_lazy('producto_list')