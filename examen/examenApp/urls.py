from django.urls import path
from . import views

urlpatterns = [
    # Promociones
    path('promociones/', views.lista_promociones, name='lista_promociones'),  # Lista de promociones
    path('promociones/crear/', views.crear_promocion, name='crear_promocion'),  # Crear promoción
    path('promociones/editar/<int:pk>/', views.editar_promocion, name='editar_promocion'),  # Editar promoción
    path('promociones/eliminar/<int:pk>/', views.eliminar_promocion, name='eliminar_promocion'),  # Eliminar promoción

    # Busqueda avanzada de promociones
    path('promociones/buscar/', views.buscar_promociones, name='buscar_promociones'),
]
