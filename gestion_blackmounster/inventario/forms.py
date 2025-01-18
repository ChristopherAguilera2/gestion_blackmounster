from django import forms
from .models import Pelicula, Transaccion, Usuario
from django.forms import DateInput
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'director', 'genero', 'precio_compra', 'precio_arriendo', 'stock']
        widgets = {
            'precio_compra': forms.NumberInput(attrs={'step': 0.01}),
            'precio_arriendo': forms.NumberInput(attrs={'step': 0.01}),
        }

    def clean_precio_compra(self):
        precio_compra = self.cleaned_data.get('precio_compra')
        if precio_compra < 0:
            raise forms.ValidationError("El precio de compra debe ser 0 o mayor.")
        return precio_compra

    def clean_precio_arriendo(self):
        precio_arriendo = self.cleaned_data.get('precio_arriendo')
        if precio_arriendo < 0:
            raise forms.ValidationError("El precio de arriendo debe ser 0 o mayor.")
        return precio_arriendo

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock < 0:
            raise forms.ValidationError("El stock debe ser 0 o mayor.")
        return stock

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = ['usuario', 'pelicula', 'tipo', 'fecha_inicio', 'fecha_termino', 'estado']
    
    fecha_inicio = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(), 
        required=True,  
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  
        super().__init__(*args, **kwargs)
        if self.user and not self.user.is_superuser:
            self.fields['usuario'].queryset = Usuario.objects.filter(nombre_completo=self.user)
            self.fields['usuario'].initial = self.user  
            self.fields['usuario'].empty_label = None
            self.fields['usuario'].disabled = True 
            self.fields['estado'].initial = 'pendiente'
            self.fields['estado'].disabled = True  
        else:
            self.fields['usuario'].queryset = Usuario.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        tipo = cleaned_data.get('tipo')
        fecha_termino = cleaned_data.get('fecha_termino')

        if tipo == 'arriendo' and not fecha_termino:
            self.add_error('fecha_termino', 'Este campo es obligatorio cuando el tipo es arriendo.')

        if tipo == 'compra' and fecha_termino:
            self.add_error('fecha_termino', 'El campo fecha de término no debe ser completado cuando el tipo es compra.')

        return cleaned_data
    
    def clean_fecha_termino(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_termino = self.cleaned_data.get('fecha_termino')
        if isinstance(fecha_inicio, datetime):
            fecha_inicio = fecha_inicio.date()  
        if isinstance(fecha_termino, datetime):
            fecha_termino = fecha_termino.date()  
        if fecha_termino:
            if fecha_termino < fecha_inicio:
                raise forms.ValidationError("La fecha de término no puede ser anterior a la fecha de inicio.")
        return fecha_termino
    
    def clean_pelicula(self):
        pelicula = self.cleaned_data.get('pelicula')
        if pelicula.stock <= 0:
            raise forms.ValidationError(f"La película '{pelicula.titulo}' no tiene stock disponible.")
        return pelicula
    



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']