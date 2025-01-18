# BlackMounster

## Descripción general del proyecto

BlackMounster es una aplicación web que gestiona un inventario de películas y permite realizar transacciones de compra y arriendo. Está diseñada para ser utilizada tanto por administradores como por usuarios regulares. Los administradores tienen la capacidad de agregar, editar y eliminar películas, mientras que los usuarios pueden realizar transacciones (compra o arriendo) de las películas disponibles.

El sistema está basado en Django, un framework web de alto nivel que promueve un desarrollo rápido y limpio. La aplicación incluye autenticación de usuarios, gestión de permisos y roles, y una interfaz de usuario amigable basada en Bootstrap.

### Características principales

- **Gestión de películas**: Los administradores pueden gestionar el inventario de películas, agregar nuevas, editarlas o eliminarlas.
- **Gestión de transacciones**: Los usuarios pueden realizar transacciones para comprar o arrendar películas.
- **Roles y permisos**: Existen roles de administrador y usuario regular, con permisos diferenciados para gestionar las películas y realizar transacciones.
- **Interfaz intuitiva**: Basada en Bootstrap y `crispy_forms`, la interfaz es responsiva y fácil de usar.
- **CRUD de películas**: Los administradores pueden realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre las películas.
- **Autenticación de usuarios**: Sistema de login y registro para gestionar las cuentas de los usuarios.

---

## Requerimientos

crispy-bootstrap5==0.7
Django==4.1.1
django-bootstrap5==24.1  (para el diseño de la interfaz)
django-crispy-forms==2.0 (para la estilización de los formularios)
psycopg2==2.9.10

---

## Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/BlackMounster.git


2.Crear BD
psql -U postgres
psql -U blackmounster_user -d db_blackmounster

3.Ejecutar este SQL desde el comando "psql -U blackmounster_user -d db_blackmounster"
comandos iniciales\crearBD.sql

4.crear proyecto y entorno
django-admin startproject gestion_blackmounster
cd gestion_blackmounster
python -m venv venv
venv\Scripts\actívate

5.instalar librerías
pip install django==4.1.1
pip install psycopg2
pip install django-crispy-forms crispy-bootstrap5 django-bootstrap5
pip freeze > requerimient.txt
pip install -r requerimient.txt

6.configurar BD con DJANGO
python manage.py migrate

7.aplicacion del proyecto y crear super usuario
python manage.py createsuperuser
python manage.py startapp inventario

8.inserta datos con el terminal "python manage.py Shell" que están en el archivo
comandos iniciales\insertardatos.py


9.ejectar aplicacion
python manage.py runserver


               **info DB**
        'USER': 'blackmounster_user',
        'PASSWORD': 'blackmounster_pass',




Uso
Iniciar sesión: Los usuarios pueden iniciar sesión utilizando el formulario de inicio de sesión en /login/. Los administradores tienen acceso completo, mientras que los usuarios regulares pueden realizar transacciones.
Agregar películas: Solo los administradores pueden agregar películas desde la vista de administración.
Realizar transacciones: Los usuarios pueden comprar o arrendar películas desde la vista de detalles de cada película.

