from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Producto)
admin.site.register(Usuario)
admin.site.register(CarritoItems)
admin.site.register(Carrito)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
