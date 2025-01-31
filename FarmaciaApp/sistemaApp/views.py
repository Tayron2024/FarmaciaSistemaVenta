from django.shortcuts import render, redirect
from django.contrib import messages

# Home page
def inicio(request):
    return render(request, "inicio.html")
def home(request):
    return render(request, "home.html")
def farmaceutico(request):
    return render(request, "farmaceutico.html")
def cliente(request):
    return render(request, "gestion_cliente.html")
def inventario(request):
    return render(request, "gestion_inventario.html")
def pedido(request):
    return render(request, "pedido.html")
def reporte(request):
    return render(request, "reporte.html")
def sucursal(request):
    return render(request, "gestion_sucursal.html")
def compra(request):
    return render(request, "gestion_compra.html")
def confirmacion_pago(request):
    return render(request, 'compra/confirmacion_pago.html')
def gestion_inventario(request):
    return render(request, 'gestion_inventario.html')

def gestion_sucursal(request):
    return render(request, 'gestion_sucursal.html')

def transferir_producto(request):
    if request.method == 'POST':
        sucursal_origen = request.POST['sucursal_origen']
        sucursal_destino = request.POST['sucursal_destino']
        producto = request.POST['producto']
        cantidad = request.POST['cantidad']

        # Aquí iría la lógica de transferencia (actualización en la base de datos)
        messages.success(request, f"Se ha transferido {cantidad} unidades de {producto} de {sucursal_origen} a {sucursal_destino}.")

        return redirect('gestion_sucursal')  # Redirigir de nuevo a gestión de sucursales

    return render(request, 'transferir_producto.html')