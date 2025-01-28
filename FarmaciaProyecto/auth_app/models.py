from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo de Usuario (extendido de AbstractUser)
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
