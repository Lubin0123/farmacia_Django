# Generated by Django 5.0.6 on 2024-05-21 18:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProveedor', models.CharField(max_length=100)),
                ('direccionProveedor', models.CharField(max_length=200)),
                ('correoProveedor', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionProducto', models.CharField(max_length=100)),
                ('precioProducto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cantidadProducto', models.PositiveIntegerField(default=0)),
                ('proveedores', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.proveedores')),
            ],
        ),
    ]
