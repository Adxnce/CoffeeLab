from django.db import models

# Create your models here.

class Usuario(models.Model):
    # nombre usuario, email, contraseña, direccion, ciudad
    # nombreUsuario = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre de Usuario')
    nombreUsuario = models.CharField(max_length=50, verbose_name='Nombre de Usuario')
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
