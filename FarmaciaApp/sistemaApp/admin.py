
from django.contrib import admin



from .models import (
    Estado, Stock, Categoria, Insumo,
    Producto, Proveedor, Pedido, Operacion,
    Historial, Sucursal, Cliente, Persona,
    Farmaceutico, Administrador, Alerta, Inventario,
)


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # Adjusted related fields for Persona model.
    list_display = ("nombre", "descripcion")
    search_fields = ("nombre",)


@admin.register(Insumo)
class InsumoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cantidadDisponible", "unidad_medida", "precio_unitario", "stock", "categoria")
    list_filter = ("stock", "fecha_vencimiento")
    search_fields = ("nombre", "ubicacion")


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "precio", "cantidad", "insumo")
    list_filter = ("insumo__categoria",)
    search_fields = ("nombre",)


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("email", "direccion", "contacto")
    search_fields = ("email", "contacto")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("fecha", "estado", "descripcion", "cliente", "sucursal", "retiroSucursal")
    list_filter = ("estado", "sucursal", "retiroSucursal")
    search_fields = ("descripcion", "cliente__nombre")


@admin.register(Operacion)
class OperacionAdmin(admin.ModelAdmin):
    list_display = ("fechaRegistro", "costoTotal", "motivoSalida", "sucursalOrigen", "sucursalDestino")
    list_filter = ("sucursalOrigen", "sucursalDestino")
    search_fields = ("motivoSalida",)


@admin.register(Historial)
class HistorialAdmin(admin.ModelAdmin):
    list_display = ("actualizacion", "tipoOperacion")
    search_fields = ("actualizacion", "tipoOperacion__motivoSalida")


@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ("nombre", "ubicacion", "horario", "estado")
    list_filter = ("estado",)
    search_fields = ("nombre", "ubicacion")


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "cedula", "email", "telefono")
    search_fields = ("nombre", "apellido", "cedula")


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ("username", "rol", "email", "is_staff", "is_superuser")
    list_filter = ("rol", "is_staff", "is_superuser")
    search_fields = ("username", "email")


@admin.register(Farmaceutico)
class FarmaceuticoAdmin(admin.ModelAdmin):
    list_display = ("username", "turno", "email")
    search_fields = ("username", "turno")


@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "revision", "control")
    search_fields = ("username", "email")


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ("mensaje", "fecha", "tipo", "inventario")
    list_filter = ("tipo", "fecha")
    search_fields = ("mensaje",)


@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ("almacenamiento", "sucursal")
    search_fields = ("almacenamiento", "sucursal__nombre")