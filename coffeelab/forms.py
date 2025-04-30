from django import forms
from django.forms import ModelForm
from .models import Usuario, Producto

class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'direccion', 'ciudad']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['nombreProducto', 'descripcion', 'precio']

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=50)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)