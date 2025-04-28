from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from coffeelab.models import Usuario, Producto
from .serializers import UsuarioSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def lista_usuarios(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = UsuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = UsuarioSerializer(data = data)
        serializer = UsuarioSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def vista_usuarios_mod(request, id):
    try:
        us = Usuario.objects.get(nombreUsuario=id)
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