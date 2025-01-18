from inventario.models import Usuario, Pelicula, Transaccion

usuarios = Usuario.objects.all()
print(usuarios)

peliculas = Pelicula.objects.all()
print(peliculas)

transacciones = Transaccion.objects.all()
print(transacciones)
