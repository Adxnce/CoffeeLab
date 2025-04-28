from django.urls import path
from rest_api.views import lista_usuarios , vista_usuarios_mod
from rest_api.viewsLogin import login

urlpatterns = [

    path('lista_usuarios/', lista_usuarios, name='lista_usuarios'),
    path('datos_usuarios/<str:id>', vista_usuarios_mod, name='modif_usuario'),
    path('login/', login, name='login')
]