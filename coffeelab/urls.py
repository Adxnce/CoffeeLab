from django.urls import path
from coffeelab.views import index, adminPanel, adminPanelCreate, adminPanelUpdate, adminPanelDelete ,catalogo , cart, login, user, aboutUs

urlpatterns = [
    path('', index, name='index'),
    path('adminPanel/', adminPanel, name='adminPanel'),
    path('adminPanelCreate/', adminPanelCreate, name='adminPanelCreate'),
    path('adminPanelUpdate/<id>/', adminPanelUpdate, name='adminPanelUpdate'),
    path('adminPanelDelete/<id>/', adminPanelDelete, name='adminPanelDelete'),
    path('about-us/', aboutUs, name='about_us'),
    path('catalogo/', catalogo, name='catalogo'),
    path('cart/', cart, name='cart'),
    path('login/', login, name='log'),
    path('user/', user, name='user'),
]