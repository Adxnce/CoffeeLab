from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from coffeelab.models import Usuario, Producto
from .serializers import UsuarioSerializer

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def login(request):
    data = JSONParser().parse(request)
    User = get_user_model()

    username = data['username']
    password = data['password']

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response('Usuario Incorrecto')

    #validamos la password
    pass_valido = check_password(password, user.password)
    if not pass_valido:
        return Response('Contraseña Incorrecta')

    #permitir crear o recuperar el token
    token, created = Token.objects.get_or_create(user=user)
    return Response(token.key)