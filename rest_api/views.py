from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt
from coffeelab.models import Usuario, Producto, Carrito, CarritoItems
from .serializers import UsuarioSerializer, ProductoSerializer, CarritoSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
import json

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
# Create your views here.

@api_view(['GET', 'POST'])
@permission_classes([AllowAny,])
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        direccion = request.data.get('direccion')
        ciudad = request.data.get('ciudad')
        rol = request.data.get('rol')

        usuario = Usuario(username=username, email=email, direccion=direccion, ciudad=ciudad, rol=rol)
        usuario.set_password(password)  # Encriptar la contraseña
        usuario.save()
        # Crear el carrito para el nuevo usuario
        carrito = Carrito(usuario=usuario)
        carrito.save()

        return Response({"detail": "Usuario creado exitosamente"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def lista_productos(request):
    if request.method == 'GET':
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def lista_productos_id(request, id):
    try:
        producto = Producto.objects.get(SKU=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated,])
def lista_productos_post(request):
    if request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','DELETE'])
@permission_classes([IsAuthenticated,])
def lista_productos_mod(request, id):
    try:
        producto = Producto.objects.get(SKU=id)
    except Producto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        print(request.data)
        serializer = ProductoSerializer(producto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated,])
def vista_usuarios_mod(request, id):
    try:
        us = Usuario.objects.get(username=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(us)
        return Response(serializer.data)

    elif request.method == 'PUT':
        
        newPassword = request.data.get('password')
        us.set_password(newPassword)  # Encriptar la nueva contraseña
        newData = {
            'username': request.data.get('username'),
            'email': request.data.get('email'),
            'direccion': request.data.get('direccion'),
            'ciudad': request.data.get('ciudad'),
            'password': us.password,
            'rol': request.data.get('rol'),
        }
        serializer = UsuarioSerializer(us, data=newData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        us.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated,])
def vista_carrito_usuario(request):
    print("hola")
    try:
        carrito = Carrito.objects.get(usuario=request.user)
    except Carrito.DoesNotExist:
        return Response({"detail": "Carrito no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CarritoSerializer(carrito)
        return Response(serializer.data)

    elif request.method == 'POST':
        usuario = request.user
        producto_nombre = request.data.get('producto')
        cantidad = request.data.get('cantidad', 1)
        print(usuario, request.data, cantidad)


        try:
            carrito = Carrito.objects.get(usuario=usuario)
        except Carrito.DoesNotExist:
            carrito = Carrito(usuario=usuario)
            carrito.save()

        try:
            producto = Producto.objects.get(nombreProducto=producto_nombre)
        except Producto.DoesNotExist:
            return Response({"detail": "Producto no encontrado."}, status=status.HTTP_400_BAD_REQUEST)    



        item, created = CarritoItems.objects.get_or_create(carrito=carrito, producto=producto, defaults={'cantidad': 0})
        if not created:
            item.cantidad += cantidad
            item.save()
        else:
            item.cantidad = cantidad
            item.save()

        return Response({"detail": "Item agregado al carrito"})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated,])
def borrar_producto_carrito(request, item_id):
    try:
        item = CarritoItems.objects.get(id=item_id, carrito__usuario=request.user)
        item.delete()
        return Response({"detail": "Producto eliminado del carrito"})
    except CarritoItems.DoesNotExist:
        return Response({"detail": "Producto no encontrado en el carrito"}, status=404)


def api_productos(request):
        productos = Producto.objects.all()
        data = ProductoSerializer(productos, many=True).data
        return JsonResponse(data, safe=False)

def api_usuarios(request):
        usuarios = Usuario.objects.all()
        data = UsuarioSerializer(usuarios, many=True).data
        return JsonResponse(data, safe=False)

@csrf_exempt
def recuperar_clave(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        print(email)
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuario no encontrado'}, status=404)

        uidb64 = urlsafe_base64_encode(force_bytes(usuario.pk))

        reset_url = f'http://127.0.1:8000/recuperar_clave_form/{uidb64}/'
        send_mail(
            'Restablecimiento de contraseña',
            f'Para restablecer tu contraseña, haz clic en el siguiente enlace: {reset_url}',
            'no-reply@tudominio.com',
            [email],
        )

        return JsonResponse({'mensaje': 'Correo enviado con instrucciones para restablecer la contraseña'})
    return render(request, 'recuperar_clave_form.html')
    

    