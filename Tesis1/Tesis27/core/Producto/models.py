from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre_Producto=models.CharField(max_length=50, unique=True, verbose_name='Producto')
    categoria_Producto= models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_Producto


class Meta:
    verbose_name='Producto'
    verbose_name_prural='Productos'
    db_table='producto'
    ordering='[id]'
