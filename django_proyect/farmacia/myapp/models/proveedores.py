from django.db import models

class Proveedores(models.Model):
    
    nombreProveedor = models.CharField(max_length=100)
    direccionProveedor = models.CharField(max_length=200)
    correoProveedor = models.EmailField()
    
    def __str__(self):
        return self.nombreProveedor