from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from .models import Cliente, Inventario, Pedido


# Vista de inicio
@login_required
def home(request):
    return render(request, 'home.html')


# Vista para cerrar sesión
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


# Gestión de clientes
class ClienteListView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'gestion_clientes.html'
    context_object_name = 'clientes'


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model = Cliente
    fields = ['usuario', 'direccion', 'telefono']
    template_name = 'form_cliente.html'
    success_url = '/clientes/'


class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model = Cliente
    fields = ['usuario', 'direccion', 'telefono']
    template_name = 'form_cliente.html'
    success_url = '/clientes/'


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    template_name = 'confirm_delete.html'
    success_url = '/clientes/'


# Gestión de inventario
class InventarioListView(LoginRequiredMixin, ListView):
    model = Inventario
    template_name = 'gestion_inventario.html'
    context_object_name = 'inventarios'


# Gestión de pedidos
class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'gestion_pedidos.html'
    context_object_name = 'pedidos'


class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    fields = ['cliente', 'estado', 'sucursal_origen', 'sucursal_destino']
    template_name = 'form_pedido.html'
    success_url = '/pedidos/'


# Transferencia entre sucursales
@login_required
def transferencia_sucursales(request):
    return render(request, 'transferencia_sucursales.html')


# Venta de medicamentos
@login_required
def venta_medicamentos(request):
    return render(request, 'venta_medicamentos.html')
