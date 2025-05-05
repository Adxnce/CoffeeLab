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
# Create your views here.

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated,])
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

        usuario = Usuario(username=username, email=email, direccion=direccion, ciudad=ciudad)
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

@api_view(['POST'])
def lista_productos_post(request):
    if request.method == 'POST':
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def vista_usuarios_mod(request, id):
    try:
        us = Usuario.objects.get(username=id)
    except Usuario.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UsuarioSerializer(us)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UsuarioSerializer(us, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        us.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def vista_carrito_usuario(request):
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
def borrar_producto_carrito(request, item_id):
    try:
        item = CarritoItems.objects.get(id=item_id, carrito__usuario=request.user)
        item.delete()
        return Response({"detail": "Producto eliminado del carrito"})
    except CarritoItems.DoesNotExist:
        return Response({"detail": "Producto no encontrado en el carrito"}, status=404)

