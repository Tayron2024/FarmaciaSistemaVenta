from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gestion_cliente/', views.gestion_cliente, name='gestion_cliente'),
    path('gestion_inventario/', views.gestion_inventario, name='gestion_inventario'),
    path('registro_pedidos/', views.registro_pedidos, name='registro_pedidos'),
    path('transferencia_sucursales/', views.transferencia_sucursales, name='transferencia_sucursales'),
    path('venta_medicamentos/', views.venta_medicamentos, name='venta_medicamentos'),
]
