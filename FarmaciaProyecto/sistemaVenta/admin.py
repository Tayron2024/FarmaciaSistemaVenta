from django.contrib import admin
from .models import Usuario, Cliente, Sucursal, Medicamento, Inventario, Pedido, DetallePedido

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'rol')
    search_fields = ('username',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'direccion', 'telefono')
    search_fields = ('usuario__username',)

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'telefono')
    search_fields = ('nombre', 'direccion')

@admin.register(Medicamento)
class MedicamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('sucursal', 'medicamento', 'cantidad')

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'estado', 'fecha_creacion', 'sucursal_origen', 'sucursal_destino')
    list_filter = ('estado', 'sucursal_origen', 'sucursal_destino')

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'medicamento', 'cantidad')
