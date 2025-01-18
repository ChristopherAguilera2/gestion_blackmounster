from inventario.models import Pelicula

# Filtrar las películas cuyo género sea "Acción" y tengan stock mayor a 0
peliculas_accion_stock = Pelicula.objects.filter(genero="Acción", stock__gt=0)
for pelicula in peliculas_accion_stock:
    print(pelicula.titulo, pelicula.stock)
