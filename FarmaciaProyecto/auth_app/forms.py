from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

# Formulario para la creación de usuarios (registro)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password1', 'password2', 'rol']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
        }

# Formulario para el login de usuarios
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
