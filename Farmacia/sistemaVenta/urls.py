from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    # Rutas de autenticación
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/login/'), name='logout'),
    path('register/', views.registrar_usuario, name='register'),

    # Rutas de funcionalidades del sistema
    path('', views.home, name='home'),
    path('clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('inventario/', views.gestion_inventario, name='gestion_inventario'),
    path('pedidos/', views.registro_pedidos, name='registro_pedidos'),
    path('transferencias/', views.transferencia_sucursales, name='transferencia_sucursales'),
    path('ventas/', views.venta_medicamentos, name='venta_medicamentos'),
]
