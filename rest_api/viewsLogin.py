from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from coffeelab.models import Usuario, Producto
from .serializers import UsuarioSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login(request):
    data = request.data  # Utiliza request.data para obtener los datos
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return Response({'detail': 'Username y password son requeridos.'}, status=400)

    user = authenticate(request, username=username, password=password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'rol': user.rol,
            'username': user.username,
            })
    else:
        return Response({'detail': 'Usuario o contraseña incorrectos.'}, status=401)
