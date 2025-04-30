from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from .forms import UsuarioForm, ProductoForm, LoginForm
from .models import Usuario, Producto

# Create your views here.

def index(request):
    return render(request, 'coffeelab/index.html')

def aboutUs(request):
    return render(request, 'coffeelab/about-us.html')

def adminPanel(request):
    usuarios = Usuario.objects.all()

    datos = {
        'usuarios': usuarios
    }

    return render(request, 'coffeelab/adminPanel.html', datos)

def adminPanelCreate(request):

    datos = {
        'form': UsuarioForm()
    }

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario creado correctamente"
        else:
            datos['mensaje'] = "Error al crear el usuario"

    return render(request, 'coffeelab/adminPanelCreate.html', datos)

def adminPanelUpdate(request, id):

    usuario = Usuario.objects.get(nombreUsuario=id)

    datos = {
        'form': UsuarioForm(instance=usuario)
    }

    return render(request, 'coffeelab/adminPanelUpdate.html', datos)

def adminPanelDelete(request, id):

    usuario = Usuario.objects.get(nombreUsuario=id)
    usuario.delete()
    return redirect(to='adminPanel')


def catalogo(request):

    if request.method == 'GET':
        productos = Producto.objects.all()

    return render(request, 'coffeelab/catalogo.html', {'productos': productos})

def cart(request):
    return render(request, 'coffeelab/cart.html')

def login(request):

    datos = {
        'form': LoginForm()
    }

    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect(to='index')
            else:
                formulario.add_error(None, "Usuario o contraseña incorrectos")

    return render(request, 'coffeelab/login.html', datos)

def user(request):
    datos = {
        'form' : UsuarioForm()
    }

    if request.method== 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario creado correctamente"

    return render(request, 'coffeelab/user.html', datos)
