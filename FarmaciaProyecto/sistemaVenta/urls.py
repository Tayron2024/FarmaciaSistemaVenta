from django.urls import path
from . import views

app_name = 'sistemaVenta'  # Esto registra el namespace 'sistemaVenta'

urlpatterns = [
    path('', views.home, name='home'),
    path('gestion_inventario/', views.gestion_inventario, name='gestion_inventario'),
    path('venta_medicamentos/', views.venta_medicamentos, name='venta_medicamentos'),
    path('transferencia_sucursales/', views.transferencia_sucursales, name='transferencia_sucursales'),
    # Agrega más rutas según sea necesario
]
