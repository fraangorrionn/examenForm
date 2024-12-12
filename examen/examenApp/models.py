from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario(models.Model):    
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    puede_tener_promociones = models.BooleanField()

    def __str__(self):
        return self.nombre

class Promocion(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(max_length=100)
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE)
    usuarios = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    descuento = models.IntegerField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=20, default='activo') 

    def __str__(self):
        return f"{self.usuarios.nombre} - {self.productos.nombre}"

