from django.contrib import admin
from .models import Usuario, Cliente, Sucursal, Medicamento, Inventario, Pedido, DetallePedido

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol')
    list_filter = ('rol',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'direccion', 'telefono')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio')
    search_fields = ('nombre',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'cantidad')
    list_filter = ('sucursal',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha_creacion', 'estado', 'sucursal_origen', 'sucursal_destino')
    list_filter = ('estado', 'fecha_creacion')

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'medicamento', 'cantidad')
