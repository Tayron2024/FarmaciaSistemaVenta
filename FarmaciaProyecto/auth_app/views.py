from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm, RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.shortcuts import redirect

def register_view(request):
    # Si el formulario fue enviado y es válido, puedes crear el usuario
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda el formulario, creando el nuevo usuario
            return redirect('auth_app:login')  # Redirige al login o a otra página después del registro
    else:
        form = RegisterForm()

    return render(request, 'auth_app/register.html', {'form': form})
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

def logout_view(request):
    logout(request)
    return redirect('auth_app:login')

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
