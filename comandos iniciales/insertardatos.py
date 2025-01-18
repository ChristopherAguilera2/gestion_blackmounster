# Crear los usuarios
from inventario.models import Usuario

admin_user = Usuario.objects.create_user(username='admin', email='Admin@email.com', password='admin', nombre_completo='Admin')
juan_perez = Usuario.objects.create_user(username='juanperez', email='juan.perez@email.com', password='juan123', nombre_completo='Juan Pérez')
ana_gonzalez = Usuario.objects.create_user(username='anagonzalez', email='ana.gonzalez@email.com', password='ana123', nombre_completo='Ana González')
pedro_rojas = Usuario.objects.create_user(username='pedrorojas', email='pedro.rojas@email.com', password='pedro123', nombre_completo='Pedro Rojas')



# Crear las películas
from inventario.models import Pelicula

interstellar = Pelicula.objects.create(titulo='Interstellar', director='Cristopher Nolan', genero='Ciencia Ficción', precio_compra=19.99, precio_arriendo=4.99, stock=10)
dark_knight = Pelicula.objects.create(titulo='The Dark Knight', director='Christopher Nolan', genero='Acción', precio_compra=14.99, precio_arriendo=3.99, stock=8)
godfather = Pelicula.objects.create(titulo='The Godfather', director='Francis Ford Coppola', genero='Drama', precio_compra=12.99, precio_arriendo=3.49, stock=5)
shawshank = Pelicula.objects.create(titulo='The Shawshank Redemption', director='Frank Darabont', genero='Drama', precio_compra=11.99, precio_arriendo=2.99, stock=4)
pulp_fiction = Pelicula.objects.create(titulo='Pulp Fiction', director='Quentin Tarantino', genero='Crimen', precio_compra=16.99, precio_arriendo=4.49, stock=6)
avengers_endgame = Pelicula.objects.create(titulo='Avengers: Endgame', director='Anthony y Joe Russo', genero='Acción', precio_compra=22.99, precio_arriendo=6.99, stock=9)
matrix = Pelicula.objects.create(titulo='The Matrix', director='Lana y Lilly Wachowski', genero='Ciencia Ficción', precio_compra=17.99, precio_arriendo=4.99, stock=8)
parasite = Pelicula.objects.create(titulo='Parasite', director='Bong Joon-ho', genero='Drama', precio_compra=14.99, precio_arriendo=3.99, stock=5)
lion_king = Pelicula.objects.create(titulo='The Lion King', director='Rob Minkoff y Roger Allers', genero='Animación', precio_compra=13.99, precio_arriendo=3.49, stock=10)
spiderman = Pelicula.objects.create(titulo='Spider-Man: No Way Home', director='Jon Watts', genero='Acción', precio_compra=20.99, precio_arriendo=5.99, stock=6)




#agregar al grupo admin lso usuarios de models agregados de forma manual
# En el shell de Django (usando el script de administración o directamente en el shell)
from django.contrib.auth.models import User, Group
from inventario.models import Usuario

# Obtener el grupo de lectura
lectura_group = Group.objects.get(name='Lectura')

# Recorrer todos los usuarios en el modelo Usuario
usuarios = Usuario.objects.all()

for usuario in usuarios:
    if usuario.username != 'admin':  # Excluir al usuario 'admin'
        # Crear un usuario en el modelo User
        user = User.objects.create_user(
            username=usuario.username,
            email=usuario.email,
            password=usuario.password  # Si estás utilizando password en Usuario, se pasa directamente
        )
        
        # Asignar al grupo 'Lectura'
        user.groups.add(lectura_group)
        user.save()

        print(f"Usuario {usuario.username} creado y asignado al grupo 'Lectura'")
    else:
        print("El usuario 'admin' ya existe, no se creará nuevamente.")
