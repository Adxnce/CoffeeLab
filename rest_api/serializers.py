from rest_framework import serializers
from coffeelab.models import Usuario, Producto, CarritoItems, Carrito, Pedido, DetallePedido
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'email', 'password', 'direccion', 'ciudad']
        
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['SKU', 'nombreProducto', 'descripcion', 'precio', 'imagen']

class CarritoItemsSerializer(serializers.ModelSerializer):
    producto = serializers.StringRelatedField()
    precio_unitario = serializers.DecimalField(source='producto.precio', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CarritoItems
        fields = ['id', 'producto', 'cantidad', 'precio_unitario']

class CarritoSerializer(serializers.ModelSerializer):
    items = CarritoItemsSerializer(many=True, read_only=True)

    class Meta:
        model = Carrito
        fields = ['id', 'usuario', 'items']
