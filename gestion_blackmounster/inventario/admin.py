from django.contrib import admin
from .models import Usuario, Pelicula, Transaccion
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'genero', 'precio_compra', 'precio_arriendo', 'stock')
    search_fields = ('titulo', 'director')

class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'pelicula', 'tipo', 'fecha_inicio', 'estado')
    list_filter = ('estado', 'tipo')

admin.site.register(Usuario)
admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Transaccion, TransaccionAdmin)




def crear_grupo():
    group_lectura, created = Group.objects.get_or_create(name='Lectura')
    if created:
        permisos_lectura = Permission.objects.filter(codename__in=['view_pelicula'])
        group_lectura.permissions.set(permisos_lectura)
    group_desarrolladores, created = Group.objects.get_or_create(name='Desarrolladores')
    if created:
        permisos_desarrolladores = Permission.objects.filter(codename__in=[
            'add_pelicula',
            'change_pelicula',
            'delete_pelicula',
            'view_pelicula'
        ])
        group_desarrolladores.permissions.set(permisos_desarrolladores)

crear_grupo()