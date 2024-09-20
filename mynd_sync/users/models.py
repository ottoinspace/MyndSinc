from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Usuario(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_medico = models.BooleanField(default=False)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    CPF = models.CharField(max_length=11, unique=True, null=True, blank=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )


class Medico(models.Model):
    user = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    DRT = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.user.username} - DRT: {self.DRT}'
