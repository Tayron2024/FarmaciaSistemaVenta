from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistemaVenta.urls')),  # Asegúrate de que 'sistemaVenta.urls' esté aquí
]
