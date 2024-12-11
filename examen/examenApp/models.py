from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class Promocion(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la promoción")
    descripcion = models.TextField(verbose_name="Descripción de la promoción")
    usuarios = models.ManyToManyField(
        Usuario, 
        through="PromocionUsuario", 
        related_name="promociones", 
        verbose_name="Usuarios asignados"
    )
    descuento = models.IntegerField(verbose_name="Descuento (%)")
    fecha_fin = models.DateField(verbose_name="Fecha fin de la promoción")

    def __str__(self):
        return self.nombre


class PromocionUsuario(models.Model):
    promocion = models.ForeignKey(Promocion, on_delete=models.CASCADE, related_name="uso_promociones")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="uso_promociones")
    fecha_aplicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.nombre} - {self.promocion.nombre}"
