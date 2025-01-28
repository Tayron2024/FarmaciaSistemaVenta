from django.contrib import admin
from django.urls import path
from sistemaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio),
    path('home/', views.home),
    path('farmaceutico/',views.farmaceutico),
    path('gestion_cliente/', views.cliente),
    path('gestion_inventario/',views.inventario),
    path('pedido/',views.pedido),
    path('reporte/',views.reporte),
    path('gestion_sucursal/',views.sucursal),
    path('gestion_compra/',views.compra),
    path('cliente/', views.cliente, name='cliente'),
    path('compra/', views.compra, name='compra'),
]