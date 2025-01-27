from django.urls import path
from . import views
from django.urls import path, include
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('registro_cliente.html/', views.registro_cliente, name='registro_cliente.html'),
    path('', include('farmacia.urls')),
]
