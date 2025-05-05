from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as auth_logout,  login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, ProductoForm, LoginForm
from .models import Usuario, Producto

# Create your views here.

def index(request):
    return render(request, 'coffeelab/index.html')

def aboutUs(request):
    return render(request, 'coffeelab/about-us.html')

@login_required
def adminPanel(request):
    usuarios = Usuario.objects.all()

    datos = {
        'usuarios': usuarios
    }

    return render(request, 'coffeelab/adminPanel.html')

@login_required
def adminPanelCreate(request):

    datos = {
        'form' : UsuarioForm()
    }

    return render(request, 'coffeelab/adminPanelCreate.html', datos)

@login_required
def adminPanelUpdate(request, id):

    usuario = Usuario.objects.get(username=id)


    datos = {
        'form': UsuarioForm(instance=usuario),
        'id': id
    }

    return render(request, 'coffeelab/adminPanelUpdate.html', datos)

@login_required
def adminPanelDelete(request, id):
    datos = {
        'id': id
    }
    usuario = Usuario.objects.get(username=id)
    usuario.delete()
    return redirect(to='adminPanel')

@login_required
def agregarProducto(request):
    
    datos = {
        'form' : ProductoForm()
    }

    return render(request, 'coffeelab/agregarProducto.html', datos)

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
                return redirect(to='adminPanel')
            else:
                formulario.add_error(None, "Usuario o contraseña incorrectos")

    return render(request, 'coffeelab/login.html', datos)

def logout(request):
    auth_logout(request)
    return redirect(to='log')

def user(request):
    datos = {
        'form' : UsuarioForm()
    }

    if request.method== 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.save(commit=False)
            usuario.set_password(formulario.cleaned_data['password'])
            usuario.is_active = True
            usuario.save()
            return redirect('log')

    return render(request, 'coffeelab/user.html', datos)
