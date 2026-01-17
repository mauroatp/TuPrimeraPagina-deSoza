from django.urls import path
from concesionaria.views import *

urlpatterns = [
    path('', index, name='index'),
    path('alta-automotora/', alta_automotora, name='alta_automotora'),
    
    path('alta-auto/', alta_auto, name='alta_auto'),
    path('buscar/', buscar_automotora, name='buscar_automotora'),
    path('automotora/<int:id>/', detalle_automotora, name='detalle_automotora'),
    path('automotora/editar/<int:pk>/', editar_automotora, name='editar_automotora'),
    path('automotora/eliminar/<int:pk>/', eliminar_automotora, name='eliminar_automotora'),
    path('autos/', lista_autos, name='lista_autos'),
    path('about/', about_me, name='about'),
    path('vehiculo/<int:pk>/', vehiculo_detalle, name='vehiculo_detalle'),
    path('vehiculo/<int:pk>/editar/', vehiculo_editar, name='vehiculo_editar'),
    path('vehiculo/<int:pk>/eliminar/', vehiculo_eliminar, name='vehiculo_eliminar'),
    path('detalle/<int:pk>/', vehiculo_detalle, name='vehiculo_detalle'),

]