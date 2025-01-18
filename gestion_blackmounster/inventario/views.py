from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Pelicula, Transaccion, Usuario
from .forms import PeliculaForm, TransaccionForm
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm

# Vista principal
def inicio(request):
    return render(request, 'inicio.html')

# Vista de inicio de sesión
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'auth_form.html', {'form': form, 'action': 'login'})

# Vista de cierre de sesión
def logout_view(request):
    logout(request)
    return redirect('inicio')

# Vista de registro
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            usuario = Usuario(nombre_completo=user)
            usuario.save()
            lectura_group = Group.objects.get(name='Lectura')
            user.groups.add(lectura_group)
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'auth_form.html', {'form': form, 'action': 'register'})

# Vista de listado de películas
def peliculas_lista(request):
    peliculas = Pelicula.objects.all()
    puede_agregar_pelicula = request.user.has_perm('inventario.add_pelicula')
    puede_editar_pelicula = request.user.has_perm('inventario.change_pelicula')
    puede_eliminar_pelicula = request.user.has_perm('inventario.delete_pelicula')
    context = {
        'items': peliculas,
        'item_type': 'pelicula',
        'puede_agregar_pelicula': puede_agregar_pelicula,
        'puede_editar_pelicula': puede_editar_pelicula,
        'puede_eliminar_pelicula': puede_eliminar_pelicula,
    }

    return render(request, 'listado_detalle.html', context)

# Vista de detalle de película
def pelicula_detalle(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    return render(request, 'listado_detalle.html', {'item': pelicula, 'item_type': 'pelicula'})

# Vista de listado de transacciones, solo accesible si el usuario está logeado
@login_required
def transacciones_lista(request):
    if request.user.is_superuser:
        transacciones = Transaccion.objects.all()  # Para admin, todas las transacciones
    else:
        usuario = Usuario.objects.get(nombre_completo=request.user)
        transacciones = Transaccion.objects.filter(usuario=usuario)
    return render(request, 'listado_detalle.html', {'items': transacciones, 'item_type': 'transaccion'})

# Vista de detalle de transacción, solo accesible si el usuario está logeado
@login_required
def transaccion_detalle(request, pk):
    transaccion = get_object_or_404(Transaccion, pk=pk)
    return render(request, 'listado_detalle.html', {'item': transaccion, 'item_type': 'transaccion'})

# Vista para agregar una nueva película
@permission_required('inventario.add_pelicula', raise_exception=True)
@login_required
def pelicula_nueva(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Película agregada exitosamente.")
            return redirect('peliculas_lista')
    else:
        form = PeliculaForm()
    return render(request, 'formulario.html', {'form': form, 'action': 'nueva', 'item_type': 'pelicula'})

# Vista para editar una película
@permission_required('inventario.change_pelicula', raise_exception=True)
@login_required
def pelicula_editar(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    if request.method == 'POST':
        form = PeliculaForm(request.POST, instance=pelicula)
        if form.is_valid():
            form.save()
            messages.success(request, "Película actualizada exitosamente.")
            return redirect('peliculas_lista')
    else:
        form = PeliculaForm(instance=pelicula)
    return render(request, 'formulario.html', {'form': form, 'action': 'editar', 'item_type': 'pelicula'})

# Vista para eliminar una película
@permission_required('inventario.delete_pelicula', raise_exception=True)
@login_required
def pelicula_eliminar(request, pk):
    pelicula = get_object_or_404(Pelicula, pk=pk)
    pelicula.delete()
    messages.success(request, "Película eliminada exitosamente.")
    return redirect('peliculas_lista')


# Vista para realizar una nueva transacción
@login_required
def transaccion_nueva(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST, user=request.user)
        if form.is_valid():
            transaccion = form.save(commit=False)  
            pelicula = transaccion.pelicula  
            transaccion.usuario = request.user 
            transaccion.save()
            if transaccion.tipo == 'compra' or transaccion.tipo == 'arriendo':
                if pelicula.stock > 0:
                    pelicula.stock -= 1  
                    pelicula.save()  
                    transaccion.save()  

                    messages.success(request, "Transacción realizada exitosamente.")
                else:
                    messages.error(request, "No hay suficiente stock para realizar esta transacción.")
                    return redirect('transacciones_lista')
            else:
                messages.error(request, "Tipo de transacción no válido.")
                return redirect('transacciones_lista')

            return redirect('transacciones_lista')
    else:
        form = TransaccionForm(user=request.user)

    return render(request, 'formulario.html', {'form': form, 'action': 'nueva', 'item_type': 'transaccion'})


