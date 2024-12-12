from django.contrib import admin
from .models import (
    Usuario,
    Producto, 
    Promocion, 
)

# Registro de modelos en el panel de administración
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Promocion)
