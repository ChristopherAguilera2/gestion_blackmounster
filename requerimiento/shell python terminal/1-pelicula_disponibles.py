from inventario.models import Pelicula

peliculas = Pelicula.objects.all()
for pelicula in peliculas:
    print(pelicula.titulo)
