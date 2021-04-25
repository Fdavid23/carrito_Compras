from django.db import models
from core.Producto.models import Producto
from datetime import datetime
# Create your models here.
class Cliente(models.Model):
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150, verbose_name='Nombres')
    dni = models.CharField(max_length=10, unique=True, verbose_name='Dni')
    fecha_nacimiento= models.DateField(auto_now=True)
    edad=models.PositiveIntegerField(default=0)
    salario=models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    sexo=models.CharField(max_length=50, verbose_name='Sexo')
    estado=models.BooleanField(default=True)
    avatar=models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    curriculum_Vitae=models.FileField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)

	
    def __str__(self):
     return self.nombre
    
class Meta:
    verbose_name=' Empleado'
    verbose_name_prural='Empleados'
    db_table='empleado'
    ordering='[id]'
    


    