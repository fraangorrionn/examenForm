# Generated by Django 5.1.3 on 2024-12-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examenApp', '0002_rename_producto_promocion_productos_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promocion',
            name='estado',
            field=models.CharField(default='activo', max_length=20),
        ),
    ]