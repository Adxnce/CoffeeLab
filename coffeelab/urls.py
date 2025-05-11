from django.urls import path
from django.contrib.auth.views import LoginView 
from coffeelab.views import index, adminPanel, adminPanelCreate, adminPanelUpdate, adminPanelDelete ,catalogo , cart, login, user, aboutUs, logout, agregarProducto, userPanel, administrarProductos, administrarProductoModificar, recuperar, recuperar_clave_form

urlpatterns = [
    path('', index, name='index'),
    path('adminPanel/', adminPanel, name='adminPanel'),
    path('adminPanelCreate/', adminPanelCreate, name='adminPanelCreate'),
    path('adminPanelUpdate/<str:id>/', adminPanelUpdate, name='adminPanelUpdate'),
    path('adminPanelDelete/<str:id>/', adminPanelDelete, name='adminPanelDelete'),
    path('about-us/', aboutUs, name='about_us'),
    path('catalogo/', catalogo, name='catalogo'),
    path('agregarProducto/', agregarProducto, name='agregarProducto'),
    path('cart/', cart, name='cart'),
    path('login/', LoginView.as_view(template_name='coffeelab/login.html'), name='log'),
    path('logout/', logout, name='logout'),
    path('user/', user, name='user'),
    path('userPanel/', userPanel, name='userPanel'),
    path('administrarProductos/', administrarProductos, name='administrarProductos'),
    path('administrarProductoModificar/<str:id>/', administrarProductoModificar, name='administrarProductoModificar'),
    path('recuperar/', recuperar, name='recuperar'),
    path('recuperar_clave_form/', recuperar_clave_form, name='recuperar_clave_form')
]
