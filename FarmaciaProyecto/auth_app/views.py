from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm

# Vista para el login de usuarios
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Credenciales inválidas'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Vista para el registro de nuevos usuarios
def registro_cliente(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al login después de registrarse
    else:
        form = CustomUserCreationForm()
    return render(request, 'registro_cliente.html.html', {'form': form})
