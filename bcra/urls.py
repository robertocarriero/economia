from django.urls import path
from .views import obtener_cotizacion

urlpatterns = [
    path('bcra/', obtener_cotizacion, name='inflacion'),
]
