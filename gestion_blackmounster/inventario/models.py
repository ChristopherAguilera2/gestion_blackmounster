from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    nombre_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    # Solucionar conflicto añadiendo el `related_name` para los campos `groups` y `user_permissions`
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_usuario_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='usuario'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_usuario_permissions_set',  
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='usuario'
    )

    def __str__(self):
        return self.nombre_completo

class Pelicula(models.Model):
    GENERO_CHOICES = [
        ('Ciencia Ficción', 'Ciencia Ficción'),
        ('Terror', 'Terror'),
        ('Suspenso', 'Suspenso'),
        ('Romantica', 'Romántica'),
        ('Comedia', 'Comedia'),
        ('Acción', 'Acción'),
        ('Drama', 'Drama'),
        ('Crimen', 'Crimen'),
        ('Animación', 'Animación'),
    ]
    titulo = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    genero = models.CharField(max_length=50, choices=GENERO_CHOICES)
    precio_compra = models.DecimalField(max_digits=5, decimal_places=2)
    precio_arriendo = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.titulo
    


class Transaccion(models.Model):
    ESTADO_CHOICES = [
        ('completada', 'Completada'),
        ('pendiente', 'Pendiente'),
    ]
    TIPO_CHOICES = [
        ('compra', 'Compra'),
        ('arriendo', 'Arriendo'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha_inicio = models.DateTimeField()
    fecha_termino = models.DateTimeField(null=True, blank=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.usuario.username} - {self.pelicula.titulo}"

