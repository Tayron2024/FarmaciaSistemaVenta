from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class Venta(models.Model):
    nombre = models.CharField(max_length=255)
    correo = models.EmailField()
    direccion = models.TextField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

class Estado(models.TextChoices):
    ABIERTO = "ABIERTO", "Abierto"
    CERRADO = "CERRADO", "Cerrado"

class Stock(models.TextChoices):
    LLENO = "LLENO", "Lleno"
    NORMAL = "NORMAL", "Normal"
    BAJO = "BAJO", "Bajo"
    CRITICO = "CRITICO", "Critico"
    VACIO = "VACIO", "Vacio"
    REORDEN = "REORDEN", "Reorden"
    INACTIVO = "INACTIVO", "Inactivo"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def registrarCategoria(self):
        pass

    def actualizarCategoria(self):
        pass

    def consultarCategoria(self):
        pass

class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    cantidadDisponible = models.IntegerField()
    unidad_medida = models.CharField(max_length=50)
    precio_unitario = models.FloatField()
    nivelReorden = models.IntegerField()
    fecha_vencimiento = models.DateField()
    ubicacion = models.CharField(max_length=100)
    stock = models.CharField(max_length=10, choices= Stock.choices)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="insumos")

    def registrarInsumo(self):
        pass

    def actualizarCantidad(self):
        pass

    def verificarVencimiento(self):
        pass

    def verificarReorden(self):
        pass

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE, related_name="productos")

    def calcularCosto(self):
        pass

    def calcularCantidad(self):
        pass

class Proveedor(models.Model):
    email = models.EmailField()
    direccion = models.TextField()
    contacto = models.CharField(max_length=100)

    def registrarProducto(self):
        pass

    def consultarProveedor(self):
        pass

    def actualizarProductos(self):
        pass

class Pedido(models.Model):
    fecha = models.DateField()
    estado = models.CharField(max_length=50)
    descripcion = models.TextField()
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE, related_name='pedidos')
    sucursal = models.ForeignKey('Sucursal', on_delete=models.CASCADE, related_name='pedidos')
    retiroSucursal = models.BooleanField(default=True)

    def realizarPedido(self):
        pass

    def anularPedido(self):
        pass

class Operacion(models.Model):
    fechaRegistro = models.DateField()
    costoTotal = models.FloatField()
    motivoSalida = models.TextField()
    sucursalOrigen = models.ForeignKey('Sucursal', on_delete=models.CASCADE, related_name='operaciones_origen')
    sucursalDestino = models.ForeignKey('Sucursal', on_delete=models.CASCADE, related_name='operaciones_destino', null=True, blank=True)

    def registrarEntrada(self):
        pass

    def registrarSalida(self):
        pass

class Historial(models.Model):
    actualizacion = models.TextField()
    tipoOperacion = models.ForeignKey(Operacion, on_delete=models.CASCADE, related_name="historiales")

    def consultarHistorial(self):
        pass

    def registrarEntrada(self):
        pass

    def registrarSalida(self):
        pass

class Sucursal(models.Model):
    ubicacion = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    estado = models.CharField(max_length=10, choices=Estado.choices)

    def transferirMedicamento(self, producto, cantidad, sucursal_destino):
        pass

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cedula = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

class Persona(AbstractUser):
    ROLES = (
        ('ADMIN', 'Administrador'),
        ('EMPLEADO', 'Empleado de sucursal'),
        ('CLIENTE', 'Cliente'),
    )
    rol = models.CharField(max_length=10, choices=ROLES, default='CLIENTE')
    groups = models.ManyToManyField(
        Group,
        related_name="persona_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="persona_permissions",
        blank=True,
    )

class Farmaceutico(Persona):
    turno = models.CharField(max_length=50)

    def atender(self):
        pass

    def buscarProducto(self):
        pass

class Administrador(Persona):
    revision = models.TextField()
    control = models.TextField()

    def crearReporte(self):
        pass

class Alerta(models.Model):
    mensaje = models.TextField()
    fecha = models.DateField()
    tipo = models.CharField(max_length=100)
    inventario = models.ForeignKey('Inventario', on_delete=models.CASCADE, related_name="alertas")

    def enviarNotificacion(self):
        pass

    def generarAlertaStock(self):
        pass

    def generarAlertaVencimiento(self):
        pass

class Inventario(models.Model):
    almacenamiento = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name="inventarios")

    def agregarInsumo(self):
        pass

    def eliminarInsumo(self):
        pass

    def actualizarInventario(self):
        pass

    def generarAlertas(self):
        pass

    def obtenerValorTotalInventario(self):
        pass

    def revisarBodega(self):
        pass

class Transferencia(models.Model):
    sucursal_origen = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_origen')
    sucursal_destino = models.ForeignKey(Sucursal, on_delete=models.CASCADE, related_name='transferencias_destino')
    insumo = models.ForeignKey(Insumo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_transferencia = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transferencia de {self.insumo.nombre} desde {self.sucursal_origen.nombre} a {self.sucursal_destino.nombre}"

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    nombre_cliente = models.CharField(max_length=100, default='Cliente Anónimo')
    correo_cliente = models.EmailField(default='cliente@example.com')
    direccion_cliente = models.CharField(max_length=200, default='Dirección no especificada')
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"Venta #{self.id} - {self.nombre_cliente}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.producto} - {self.cantidad} unidades"