from django.urls import path
from . import views

app_name = 'vendedores'

urlpatterns = [
    path('lista/', views.VendedorListView.as_view(), name='lista'),
    path('alta', views.VendedorCreateView.as_view(), name='alta_vendedor'),
    path('<int:pk>/', views.VendedorDetailView.as_view(), name='detalle'),
    path('<int:pk>/editar/', views.VendedorUpdateView.as_view(), name='editar'),
    path('<int:pk>/eliminar/', views.VendedorDeleteView.as_view(), name='eliminar'),
]