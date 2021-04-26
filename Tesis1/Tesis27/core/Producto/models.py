from django.db import models
from core.Categoria.models import Categoria
# Create your models here.
class Producto(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']
