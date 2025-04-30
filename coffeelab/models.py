from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Email')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')

    REQUIRED_FIELDS = ['email', 'direccion', 'ciudad']

    def __str__(self):
        return self.username

class Producto(models.Model):

    SKU = models.IntegerField(primary_key=True, verbose_name='ID de Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    descripcion = models.TextField(verbose_name='Descripcion del Producto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    # imagen = models.ImageField(upload_to='productos/', verbose_name='Imagen del Producto', null=True, blank=True)
    imagen = models.CharField(max_length=100, null=True, blank=True, verbose_name="Nombre del archivo de imagen (en static/img/)")
    # stock = models.IntegerField(verbose_name='Stock')

    def __str__(self):
        return self.nombreProducto

class Inventario(models.Model):

    idInventario = models.AutoField(primary_key=True, verbose_name='ID de Inventario')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    stock = models.IntegerField(verbose_name='Stock en Inventario')

    def __str__(self):
        return f"{self.producto.nombreProducto} - {self.stock} unidades"

class Carrito(models.Model):

    idCarrito = models.AutoField(primary_key=True, verbose_name='ID de Carrito')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')

    def __str__(self):
        return f"{self.usuario} - {self.producto}"

class Pedido(models.Model):
    idPedido = models.AutoField(primary_key=True, verbose_name='ID de Pedido')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario')
    fecha_pedido = models.DateTimeField(auto_now_add=True, verbose_name='Fecha del Pedido')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total del Pedido')
    estado = models.CharField(max_length=20, choices=[
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado')
    ], default='pendiente', verbose_name='Estado')

    def __str__(self):
        return f"Pedido {self.idPedido} de {self.usuario}"

class DetallePedido(models.Model):
    idDetalle = models.AutoField(primary_key=True, verbose_name='ID de Detalle')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name='Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio Unitario')

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombreProducto} (Pedido {self.pedido.idPedido})"


