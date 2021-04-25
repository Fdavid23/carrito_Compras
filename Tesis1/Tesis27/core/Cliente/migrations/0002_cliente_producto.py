# Generated by Django 3.0.4 on 2021-04-19 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0002_producto_categoria_producto'),
        ('Cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='producto',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='Producto.Producto'),
            preserve_default=False,
        ),
    ]
