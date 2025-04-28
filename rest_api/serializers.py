from rest_framework import serializers
from coffeelab.models import Usuario, Producto 

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombreUsuario', 'email', 'contrasena', 'direccion', 'ciudad']
        
        