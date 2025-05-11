from django.urls import path, include
from rest_api.views import lista_usuarios , vista_usuarios_mod, lista_productos, lista_productos_post, vista_carrito_usuario, borrar_producto_carrito, lista_productos_mod, lista_productos_id, api_productos, api_usuarios, recuperar_clave
from rest_api.viewsLogin import login
# from rest_framework.authtoken import obtain_auth_token

urlpatterns = [

    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('lista_productos_post/', lista_productos_post, name='lista_productos_post'),
    path('datos_usuarios/<str:id>', vista_usuarios_mod, name='modif_usuario'),
    path('vista_carrito_usuario/', vista_carrito_usuario, name='vista_carrito_usuario'),
    path('borrar_producto_carrito/<int:item_id>', borrar_producto_carrito, name='borrar_producto_carrito'),
    path('login/', login, name='login'),
    path('lista_productos_mod/<int:id>', lista_productos_mod, name='lista_productos_mod'),
    path('lista_productos_id/<int:id>', lista_productos_id, name='lista_productos_id'),
    path('recuperar_clave/', recuperar_clave, name='recuperar_clave'),
    # mis apis

    path('usuarios/', api_usuarios, name='api_usuarios'),
    path('productos/', api_productos, name='api_productos'),

]