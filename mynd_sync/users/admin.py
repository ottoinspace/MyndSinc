from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Medico
# Register your models here.


class UsuarioAdmin(UserAdmin):
    model = Usuario
    list_display = ['username', 'is_cliente', 'is_medico']


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Medico)
