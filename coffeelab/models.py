from django.db import models

# Create your models here.

class Usuario(models.Model):
    # nombre usuario, email, contraseña, direccion, ciudad
    nombreUsuario = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre de Usuario')
    # nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
    email = models.EmailField(max_length=100, verbose_name='Email')
    contrasena = models.CharField(max_length=50, verbose_name='Contraseña')
    direccion = models.CharField(max_length=100, verbose_name='Direccion')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')

    def __str__(self):
        return self.nombreUsuario

class Producto(models.Model):

    idProducto = models.AutoField(primary_key=True, verbose_name='ID de Producto')
    nombreProducto = models.CharField(max_length=50, verbose_name='Nombre de Producto')
    descripcion = models.TextField(verbose_name='Descripcion del Producto')
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')

    def __str__(self):
        return self.nombreProducto

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


class CategoriaProducto(models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name='ID de Categoria')
    nombre = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombre

