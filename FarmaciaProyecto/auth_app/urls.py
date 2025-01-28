from django.urls import path
from . import views

app_name = 'auth_app'  # Esto es importante para usar los namespaces en las URLs

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.register_view, name='registro_cliente'),
]
