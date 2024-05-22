from django.shortcuts import render
from myapp.models import  Productos

def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'myapp/lista_productos.html', {'productos': productos})

