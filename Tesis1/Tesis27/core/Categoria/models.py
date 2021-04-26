from django.db import models
from core.sexoLD import gender_choices
# Create your models here.
class Categoria(models.Model):
 name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
 def __str__(self):
      return 'Nombre: {}'.format(self.name)
      class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']