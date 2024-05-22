from django.shortcuts import render
from myapp.models import Proveedores

def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'myapp/lista_proveedores.html', {'proveedores': proveedores})

