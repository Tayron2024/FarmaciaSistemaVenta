from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario
class Usuario(AbstractUser):
    ROLES = [
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
        ('cliente', 'Cliente'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

# Modelo de Cliente (extendido de Usuario)
class Cliente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

# Modelo de Sucursal
class Sucursal(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre

# Modelo de Medicamento
class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo de Inventario
class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

# Modelo de Pedido
class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('en_transito', 'En Tránsito'),
        ('completado', 'Completado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    sucursal_origen = models.ForeignKey(Sucursal, related_name='pedidos_origen', on_delete=models.CASCADE)
    sucursal_destino = models.ForeignKey(Sucursal, related_name='pedidos_destino', on_delete=models.CASCADE)

# Modelo de Detalle de Pedido
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()

    def calcular_total(self):
        return self.medicamento.precio * self.cantidad
