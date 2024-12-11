from django.contrib import admin
from .models import (
    Usuario, 
    Promocion, 
    PromocionUsuario, 
)

# Registro de modelos en el panel de administración
admin.site.register(Usuario)
admin.site.register(Promocion)
admin.site.register(PromocionUsuario)
