from django.urls import reverse
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Pelicula, Transaccion, Usuario
from .forms import TransaccionForm

class TestUrls(TestCase):
    def test_home_url(self):
        url = reverse('inicio') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_login_url(self):
        url = reverse('login') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_register_url(self):
        url = reverse('register') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_peliculas_url(self):
        url = reverse('peliculas_lista')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#    def test_transacciones_url(self):

#    def test_transaccion_nueva_url(self):


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        cls.pelicula = Pelicula.objects.create(
            titulo="Inception", 
            genero="Sci-Fi", 
            director="Christopher Nolan", 
            precio_compra=15.99, 
            precio_arriendo=4.99, 
            stock=10
        )
        
        fecha_inicio = timezone.now()
        fecha_termino = fecha_inicio + timezone.timedelta(days=7)
        cls.transaccion = Transaccion.objects.create(
            usuario=cls.user, 
            pelicula=cls.pelicula, 
            tipo="Arriendo", 
            fecha_inicio=fecha_inicio, 
            fecha_termino=fecha_termino, 
            estado="Completada"
        )

    def test_home_view(self):
        url = reverse('inicio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_peliculas_view(self):
        url = reverse('peliculas_lista')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

#    def test_transaccion_nueva_view(self):


#    def test_transaccion_create_view(self):


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.pelicula = Pelicula.objects.create(
            titulo="Inception", 
            genero="Sci-Fi", 
            director="Christopher Nolan", 
            precio_compra=15.99, 
            precio_arriendo=4.99, 
            stock=10
        )

#    def test_transaccion_form_valid(self):

#    def test_transaccion_form_invalid(self):


class TestModels(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        cls.pelicula = Pelicula.objects.create(
            titulo="Inception", 
            genero="Sci-Fi", 
            director="Christopher Nolan", 
            precio_compra=15.99, 
            precio_arriendo=4.99, 
            stock=10
        )
        
        fecha_inicio = timezone.now()
        fecha_termino = fecha_inicio + timezone.timedelta(days=7)
        cls.transaccion = Transaccion.objects.create(
            usuario=cls.user, 
            pelicula=cls.pelicula, 
            tipo="Arriendo", 
            fecha_inicio=fecha_inicio, 
            fecha_termino=fecha_termino, 
            estado="Completada"
        )

    def test_pelicula_model(self):
        pelicula = self.pelicula
        self.assertEqual(pelicula.titulo, 'Inception')
        self.assertEqual(pelicula.stock, 10)

    def test_transaccion_model(self):
        transaccion = self.transaccion
        self.assertEqual(transaccion.estado, 'Completada')
        self.assertEqual(transaccion.pelicula.titulo, 'Inception')



class TestTemplateRendering(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = Usuario.objects.create_user(username='testuser', password='testpassword')
        cls.pelicula = Pelicula.objects.create(
            titulo="Inception", 
            genero="Sci-Fi", 
            director="Christopher Nolan", 
            precio_compra=15.99, 
            precio_arriendo=4.99, 
            stock=10
        )

    def test_home_template(self):
        url = reverse('inicio')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'inicio.html')

    def test_peliculas_template(self):
        url = reverse('peliculas_lista')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'listado_detalle.html')

#    def test_transaccion_nueva_template(self):


    def test_home_url(self):
        url = reverse('inicio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Bienvenido")

    #    def test_register_url(self):

    def test_login_url(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {'username': 'testuser', 'password': 'password123'}
        response = self.client.post(url, data)
        self.assertRedirects(response, reverse('inicio'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)


    def test_logout_url(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.login(username='testuser', password='password123')
        self.assertTrue(self.client.session['_auth_user_id'])
        url = reverse('logout')
        response = self.client.get(url)
        self.assertRedirects(response, reverse('inicio'))
        self.assertFalse('_auth_user_id' in self.client.session)


#    def test_pelicula_editar_url(self):

def test_pelicula_eliminar_url(self):
    self.user = User.objects.create_user(username='testuser', password='password123')
    self.client.login(username='testuser', password='password123')
    pelicula = Pelicula.objects.create(titulo="Pelicula 1", descripcion="Descripción", fecha_lanzamiento="2025-01-01")
    self.assertTrue(Pelicula.objects.filter(pk=pelicula.pk).exists())
    url = reverse('pelicula_eliminar', kwargs={'pk': pelicula.pk})
    response = self.client.post(url)
    self.assertRedirects(response, reverse('peliculas_lista'))
    self.assertFalse(Pelicula.objects.filter(pk=pelicula.pk).exists())


def test_transacciones_url(self):
    self.user = User.objects.create_user(username='testuser', password='password123')
    self.client.login(username='testuser', password='password123')
    transaccion = Transaccion.objects.create(cantidad=5, descripcion="Compra de película", usuario=self.user)
    url = reverse('transacciones_lista')
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "Compra de película")
