from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UsuarioForm, ProductoForm, LoginForm
from .models import Usuario

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

def cafeHonduras(request):
    return render(request, 'coffeelab/cafe-honduras.html')

def cafePeru(request):
    return render(request, 'coffeelab/cafe-peru.html')

def cafeEtiopia(request):
    return render(request, 'coffeelab/cafe.etiopia.html')

def cart(request):
    return render(request, 'coffeelab/cart.html')

def login(request):

    datos = {
        'form' : LoginForm()
    }

    if request.method == 'POST':
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']

            try:

                usuario = Usuario.objects.get(nombreUsuario__iexact=username)
                if usuario.nombreUsuario.lower() == 'admin':
                    if usuario.contrasena == password:
                        return redirect('adminPanel')
                    else:
                        datos['mensaje'] = "Contraseña incorrecta"
                else:
                    if usuario.contrasena == password:
                        return redirect('index')
                    else:
                        datos['mensaje'] = "Contraseña incorrecta"
            except Usuario.DoesNotExist:
                datos['mensaje'] = "Usuario no encontrado"
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
