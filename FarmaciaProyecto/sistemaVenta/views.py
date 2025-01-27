from django.shortcuts import render, redirect
from .models import Cliente, Inventario, Pedido, DetallePedido, Medicamento, Sucursal
from .forms import PedidoForm, DetallePedidoForm, InventarioForm, ClienteForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def gestion_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'gestion_cliente.html', {'clientes': clientes})

@login_required
def gestion_inventario(request):
    inventarios = Inventario.objects.all()
    return render(request, 'gestion_inventario.html', {'inventarios': inventarios})

@login_required
def registro_pedidos(request):
    if request.method == 'POST':
        pedido_form = PedidoForm(request.POST)
        if pedido_form.is_valid():
            pedido = pedido_form.save()
            return redirect('transferencia_sucursales')
    else:
        pedido_form = PedidoForm()
    return render(request, 'registro_pedidos.html', {'pedido_form': pedido_form})

@login_required
def transferencia_sucursales(request):
    if request.method == 'POST':
        detalle_form = DetallePedidoForm(request.POST)
        if detalle_form.is_valid():
            detalle_form.save()
            return redirect('venta_medicamentos')
    else:
        detalle_form = DetallePedidoForm()
    return render(request, 'transferencia_sucursales.html', {'detalle_form': detalle_form})

@login_required
def venta_medicamentos(request):
    if request.method == 'POST':
        inventario_form = InventarioForm(request.POST)
        if inventario_form.is_valid():
            inventario_form.save()
            return redirect('home')
    else:
        inventario_form = InventarioForm()
    return render(request, 'venta_medicamentos.html', {'inventario_form': inventario_form})
