
# myapp/urls.py
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.index, name='index'),  
    path('productos/', views.productos.lista_productos, name='lista_productos'),
    path('proveedores/', views.proveedores.lista_proveedores, name='lista_proveedores'),
]
