from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
import re
from datetime import date
from .models import Promocion, Usuario, Producto

class PromocionModelForm(forms.ModelForm):
    class Meta:
        model = Promocion
        fields = ['nombre', 'descripcion','productos', 'usuarios', 'descuento', 'fecha_fin']
        labels = {
            'nombre': 'Nombre de la Promoción',
            'descripcion': 'Descripción',
            'productos': 'Productos',
            'usuarios': 'Usuarios',
            'descuento': 'Descuento (%)',
            'fecha_fin': 'Fecha Fin',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre único'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Descripción de al menos 100 caracteres'}),
            'productos': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'usuarios': forms.Select(attrs={'class': 'form-select'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control', 'min': 0, 'max': 100}),
            'fecha_fin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Activa/Inactiva'}),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if Promocion.objects.filter(nombre=nombre).exists():
            raise ValidationError("El nombre de la promoción ya está en uso.")
        return nombre

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if len(descripcion) < 100:
            raise ValidationError("La descripción debe tener al menos 100 caracteres.")
        return descripcion

    def clean_descuento(self):
        descuento = self.cleaned_data.get('descuento')
        if not (0 <= descuento <= 100):
            raise ValidationError("El descuento debe ser un valor entre 0 y 100.")
        return descuento

    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')
        if fecha_fin and fecha_fin <= date.today():
            raise ValidationError("La fecha fin debe ser posterior a la fecha actual.")
        return fecha_fin

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado not in ['activa', 'inactiva']:
            raise ValidationError("El estado debe ser 'activa' o 'inactiva'.")
        return estado

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        usuarios = cleaned_data.get('usuarios')

        # validadcion para asegurar que un usuario no use la misma promoción dos veces
        if usuarios and nombre:
            for usuario in usuarios:
                if Promocion.objects.filter(usuarios=usuario, nombre=nombre).exists():
                    self.add_error('usuarios', f"El usuario {usuario} ya tiene asignada esta promoción.")
        return cleaned_data



class PromocionBusquedaForm(forms.Form):
    texto = forms.CharField(
        required=False,
        label="Texto (Nombre o Descripción)",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar texto'}),
    )
    fecha_inicio = forms.DateField(
        required=False,
        label="Fecha de Inicio",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    fecha_fin = forms.DateField(
        required=False,
        label="Fecha de Fin",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    )
    descuento_minimo = forms.IntegerField(
        required=False,
        label="Descuento Mínimo",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Descuento mínimo'}),
    )
    
    #estado = forms.TextInput(
    #   required=False,
    #   label="Activa/Inactiva",
    #   widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar estado'}),
    #)
    def clean_descuento_minimo(self):
        descuento_minimo = self.cleaned_data.get('descuento_minimo')
        if descuento_minimo is not None and descuento_minimo < 0:
            raise ValidationError("El descuento mínimo no puede ser menor que 0.")
        return descuento_minimo

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')

        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            self.add_error('fecha_fin', "La fecha de fin no puede ser anterior a la fecha de inicio.")
        return cleaned_data
