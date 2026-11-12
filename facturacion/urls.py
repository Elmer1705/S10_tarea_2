from django.urls import path
from .views import (
    MarcaListView, MarcaCreateView, MarcaUpdateView, MarcaDeleteView,
    ProductoListView, ProductoCreateView, ProductoUpdateView, ProductoDeleteView
)

urlpatterns = [
    # URLs para Marcas
    path('marcas/', MarcaListView.as_view(), name='marca_list'),
    path('marcas/nueva/', MarcaCreateView.as_view(), name='marca_create'),
    path('marcas/editar/<int:pk>/', MarcaUpdateView.as_view(), name='marca_update'),
    path('marcas/eliminar/<int:pk>/', MarcaDeleteView.as_view(), name='marca_delete'),

    # URLs para Productos
    path('productos/', ProductoListView.as_view(), name='producto_list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto_create'),
    path('productos/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_update'),
    path('productos/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_delete'),
]