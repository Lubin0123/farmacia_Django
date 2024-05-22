from django.db import models


class Productos(models.Model):
    
    descripcionProducto = models.CharField(max_length=100)
    precioProducto = models.DecimalField(max_digits=10, decimal_places=2)
    cantidadProducto = models.PositiveIntegerField(default=0)
    proveedores = models.ForeignKey('myapp.Proveedores', on_delete=models.SET_NULL, null=True) #relacion con la tabla proveedores 

    def __str__(self):
        return self.descripcionProducto
