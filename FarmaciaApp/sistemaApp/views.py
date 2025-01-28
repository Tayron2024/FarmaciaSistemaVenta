from django.shortcuts import render


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