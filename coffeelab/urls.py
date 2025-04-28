from django.urls import path
from .views import index, adminPanel, adminPanelCreate, adminPanelUpdate, adminPanelDelete ,cafeHonduras, cafePeru, cafeEtiopia, cart, login, user, aboutUs

urlpatterns = [
    path('', index, name='index'),
    path('adminPanel/', adminPanel, name='adminPanel'),
    path('adminPanelCreate/', adminPanelCreate, name='adminPanelCreate'),
    path('adminPanelUpdate/<id>/', adminPanelUpdate, name='adminPanelUpdate'),
    path('adminPanelDelete/<id>/', adminPanelDelete, name='adminPanelDelete'),
    path('about-us/', aboutUs, name='about_us'),
    path('cafe-honduras/', cafeHonduras, name='cafe_honduras'),
    path('cafe-peru/', cafePeru, name='cafe_peru'),
    path('cafe.etiopia/', cafeEtiopia, name='cafe_etiopia'),
    path('cart/', cart, name='cart'),
    path('login/', login, name='login'),
    path('user/', user, name='user'),
]