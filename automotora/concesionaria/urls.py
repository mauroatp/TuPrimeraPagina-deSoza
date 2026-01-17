from django.urls import path
from concesionaria.views import *

urlpatterns = [
    path('', index, name='index'),
    path('alta-automotora/', alta_automotora, name='alta_automotora'),
    path('alta-vendedor/', alta_vendedor, name='alta_vendedor'),
    path('alta-auto/', alta_auto, name='alta_auto'),
    path('buscar/', buscar_automotora, name='buscar_automotora'),
    path('automotora/<int:id>/', detalle_automotora, name='detalle_automotora'),
]