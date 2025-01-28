from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistemaVenta.urls', namespace='sistemaVenta')),  # Asegúrate de usar namespace
    path('auth/', include('auth_app.urls', namespace='auth_app')),  # Opcional, si tienes auth_app
]
