from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Usuario

class UsuarioAdmin(UserAdmin):
    list_display = ['id', 'username', 'codigo_sala', 'nombre_sala', 'email']
    list_display_links = ('id', 'username','codigo_sala')
    search_fields = ('username', 'codigo_sala', 'nombre_sala')
    list_per_page = 10
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Additional info', {
            'fields': ('codigo_sala', 'nombre_sala')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Additional info', {
            'fields': ('codigo_sala', 'nombre_sala')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(Usuario, UsuarioAdmin)

