# Generated by Django 3.0.4 on 2021-04-18 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria_Producto',
            field=models.CharField(default=5, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
