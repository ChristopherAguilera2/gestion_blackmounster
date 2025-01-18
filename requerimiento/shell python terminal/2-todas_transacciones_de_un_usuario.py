from inventario.models import Usuario, Transaccion

# Obtener al usuario específico
datos="Juan Pérez"
juan = Usuario.objects.get(nombre_completo=datos)

# Obtener todas las transacciones realizadas por Juan Pérez
transacciones_juan = Transaccion.objects.filter(usuario=juan)
for transaccion in transacciones_juan:
    print(transaccion.pelicula.titulo, transaccion.tipo, transaccion.fecha_inicio)
