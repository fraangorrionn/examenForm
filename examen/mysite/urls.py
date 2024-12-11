"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
    path('promociones/', include('examenApp.urls')),
    path('', lambda request: redirect('lista_promociones')),  # Redirige al listado de promociones
]
from django.conf.urls import handler404, handler500, handler403, handler400

handler404 = 'examenApp.views.handler_404'
handler500 = 'examenApp.views.handler_500'
handler403 = 'examenApp.views.handler_403'
handler400 = 'examenApp.views.handler_400'