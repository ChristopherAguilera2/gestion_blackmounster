from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Vista principal de bienvenida
    path('login/', views.login_view, name='login'),  # Vista para iniciar sesión
    path('logout/', views.logout_view, name='logout'),  # Vista para cerrar sesión
    path('register/', views.register_view, name='register'),  # Vista para registrar usuario
    path('peliculas/', views.peliculas_lista, name='peliculas_lista'),  # Vista de listado de películas
    path('peliculas/<int:pk>/', views.pelicula_detalle, name='pelicula_detalle'),  # Detalle de película
    path('peliculas/nueva/', views.pelicula_nueva, name='pelicula_nueva'),  # Vista para crear nueva película
    path('peliculas/<int:pk>/editar/', views.pelicula_editar, name='pelicula_editar'),  # Editar película
    path('peliculas/<int:pk>/eliminar/', views.pelicula_eliminar, name='pelicula_eliminar'),  # Eliminar película
    path('transacciones/', views.transacciones_lista, name='transacciones_lista'),  # Listado de transacciones
    path('transacciones/<int:pk>/', views.transaccion_detalle, name='transaccion_detalle'),  # Detalle de transacción
    path('transacciones/nueva/', views.transaccion_nueva, name='transaccion_nueva'),  # Realizar nueva transacción
]