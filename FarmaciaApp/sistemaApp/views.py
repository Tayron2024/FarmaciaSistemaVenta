from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import Transferencia, Sucursal, Insumo, Venta, DetalleVenta, Persona
from django.http import JsonResponse
import json

def gestion_compra(request):
    return render(request, 'gestion_compra.html')

def factura(request):
    ventas = Venta.objects.all()
    return render(request, 'factura.html', {'ventas': ventas})
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

# Vista para la página de inicio
def home(request):
    return render(request, "home.html")

# Vista para el registro de usuarios
def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        # Crear un nuevo usuario
        try:
            user = Persona.objects.create_user(username=username, password=password, rol=role)
            user.save()
            messages.success(request, "Registro exitoso. Por favor, inicia sesión.")
            return redirect('home')
        except Exception as e:
            messages.error(request, f"Error al registrar: {str(e)}")
            return redirect('registro')

    return render(request, "registro.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)
        if user is not None and user.rol == role:
            login(request, user)
            if role == 'ADMIN':
                return redirect('admin')  # Redirigir a la página de administrador
            elif role == 'EMPLEADO':
                return redirect('farmaceutico')  # Redirigir a la página de farmacéutico
            elif role == 'CLIENTE':
                return redirect('gestion_cliente')  # Redirigir a la página de cliente
        else:
            messages.error(request, "Credenciales incorrectas o rol no válido.")
            return redirect('home')

    return render(request, "home.html")

def transferir_medicamento(request):
    if request.method == 'POST':
        sucursal_origen_id = request.POST['sucursal_origen']
        sucursal_destino_id = request.POST['sucursal_destino']
        insumo_id = request.POST['insumo']
        cantidad = int(request.POST['cantidad'])

        sucursal_origen = Sucursal.objects.get(id=sucursal_origen_id)
        sucursal_destino = Sucursal.objects.get(id=sucursal_destino_id)
        insumo = Insumo.objects.get(id=insumo_id)

        # Verificar si hay suficiente stock en la sucursal de origen
        if insumo.cantidadDisponible >= cantidad:
            # Crear la transferencia
            Transferencia.objects.create(
                sucursal_origen=sucursal_origen,
                sucursal_destino=sucursal_destino,
                insumo=insumo,
                cantidad=cantidad
            )

            # Actualizar el stock en ambas sucursales
            insumo.cantidadDisponible -= cantidad
            insumo.save()

            # Aquí podrías agregar lógica para actualizar el stock en la sucursal de destino
            # (dependiendo de cómo manejes el inventario en cada sucursal).

            messages.success(request, "Transferencia realizada con éxito.")
            return redirect('gestion_cliente')  # Redirigir a la página de gestión de cliente
        else:
            messages.error(request, "No hay suficiente stock en la sucursal de origen.")
            return redirect('transferir_medicamento')

    # Obtener todas las sucursales e insumos para el formulario
    sucursales = Sucursal.objects.all()
    insumos = Insumo.objects.all()
    return render(request, 'transferir_medicamento.html', {'sucursales': sucursales, 'insumos': insumos})

def procesar_pago(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            nombre = request.POST.get('nombre')
            correo = request.POST.get('correo')
            direccion = request.POST.get('direccion')
            carrito = json.loads(request.POST.get('carrito'))
            total = float(request.POST.get('total'))

            # Validar que el carrito no esté vacío
            if not carrito:
                return JsonResponse({'error': 'El carrito está vacío.'}, status=400)

            # Validar que cada ítem tenga las claves necesarias
            for item in carrito:
                if not all(key in item for key in ['producto', 'cantidad', 'precio', 'subtotal']):
                    return JsonResponse({'error': 'Faltan claves en los datos del carrito.'}, status=400)

            # Guardar la venta en la base de datos
            venta = Venta.objects.create(
                nombre_cliente=nombre,
                correo_cliente=correo,
                direccion_cliente=direccion,
                total=total
            )

            # Guardar los detalles de la venta
            for item in carrito:
                DetalleVenta.objects.create(
                    venta=venta,
                    producto=item['producto'],
                    cantidad=item['cantidad'],
                    precio_unitario=item['precio'],
                    subtotal=item['subtotal']
                )

            # Limpiar el carrito en localStorage (desde el frontend)
            # Redirigir a la página de factura
            return redirect('factura', venta_id=venta.id)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar el carrito.'}, status=400)
        except KeyError as e:
            return JsonResponse({'error': f'Falta la clave {str(e)} en los datos del carrito.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Método no permitido'}, status=405)

def factura(request, venta_id):
    # Obtener la venta y sus detalles
    venta = get_object_or_404(Venta, id=venta_id)
    detalles = DetalleVenta.objects.filter(venta=venta)

    # Pasar los datos al template
    context = {
        'nombre': venta.nombre_cliente,
        'correo': venta.correo_cliente,
        'direccion': venta.direccion_cliente,
        'carrito': [{
            'producto': detalle.producto,
            'cantidad': detalle.cantidad,
            'precio': detalle.precio_unitario,
            'subtotal': detalle.subtotal
        } for detalle in detalles],
        'total': venta.total
    }

    return render(request, 'factura.html', context)

def transferir_medicamento(request):
    return render(request, 'transferir_medicamento.html')
