import requests
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as auth_logout,  login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm, ProductoForm, LoginForm
from .models import Usuario, Producto
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.http import JsonResponse



# Create your views here.

def index(request):

    return render(request, 'coffeelab/index.html')

def aboutUs(request):
    
    try:
        cafe_response = requests.get("https://coffee.alexflipnote.dev/random.json")
        if cafe_response.status_code == 200:
            imagen_cafe = cafe_response.json()['file']
    except Exception as e:
        print("Error: ", e)
        imagen_cafe = 'static/coffeelab/img/default.jpeg'    

    try:
        frase_response = requests.get("https://api.adviceslip.com/advice")
        if frase_response.status_code == 200:
            frase = frase_response.json()['slip']['advice']
            print("yeah")
    except Exception as e:
        print("Error: ", e)
        frase = 'No hay frase disponible en este momento'


    return render(request, 'coffeelab/about-us.html', {
        'imagen_cafe': imagen_cafe,
        'frase': frase
    })



@permission_classes([IsAuthenticated,])
def administrarProductoModificar(request, id):

    producto = Producto.objects.get(SKU=id)
    datos = {
        'form': ProductoForm(instance=producto),
        'id': id
    }

    return render(request, 'coffeelab/administrarProductoModificar.html', datos)


@permission_classes([IsAuthenticated,])
def administrarProductos(request):

    return render(request, 'coffeelab/administrarProductos.html')

@permission_classes([IsAuthenticated,])
def adminPanel(request):
    usuarios = Usuario.objects.all()

    datos = {
        'usuarios': usuarios
    }

    return render(request, 'coffeelab/adminPanel.html')

@permission_classes([IsAuthenticated,])
def adminPanelCreate(request):

    datos = {
        'form' : UsuarioForm()
    }

    return render(request, 'coffeelab/adminPanelCreate.html', datos)

@permission_classes([IsAuthenticated,])
def adminPanelUpdate(request, id):

    usuario = Usuario.objects.get(username=id)


    datos = {
        'form': UsuarioForm(instance=usuario),
        'id': id
    }

    return render(request, 'coffeelab/adminPanelUpdate.html', datos)

@permission_classes([IsAuthenticated,])
def adminPanelDelete(request, id):
    datos = {
        'id': id
    }
    usuario = Usuario.objects.get(username=id)
    usuario.delete()
    return redirect(to='adminPanel')

@permission_classes([IsAuthenticated,])
def agregarProducto(request):
    
    datos = {
        'form' : ProductoForm()
    }

    return render(request, 'coffeelab/agregarProducto.html', datos)

def catalogo(request):

    return render(request, 'coffeelab/catalogo.html')

def cart(request):
    return render(request, 'coffeelab/cart.html')

def login(request):

    datos = {
        'form': LoginForm()
    }

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


@permission_classes([IsAuthenticated,])
def userPanel(request):
    datos = {
        'form' : UsuarioForm()
    }

    return render(request, 'coffeelab/userPanel.html', datos)

def recuperar(request):

    return render(request, 'coffeelab/recuperar.html')

def recuperar_clave_form(request):

    return render(request, 'coffeelab/recuperar_clave_form.html')