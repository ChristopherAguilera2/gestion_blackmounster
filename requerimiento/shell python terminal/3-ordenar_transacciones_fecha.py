from inventario.models import Transaccion

# Obtener todas las transacciones ordenadas por fecha (fecha_inicio)
transacciones_ordenadas = Transaccion.objects.all().order_by('fecha_inicio')
for transaccion in transacciones_ordenadas:
    print(transaccion.pelicula.titulo, transaccion.tipo, transaccion.fecha_inicio)
