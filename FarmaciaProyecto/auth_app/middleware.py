# Archivo: auth_app/middleware.py
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware para redirigir a usuarios no autenticados a la página de login.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and not request.path.startswith(reverse('auth_app:login')):
            return redirect(settings.LOGIN_URL)
        return self.get_response(request)
