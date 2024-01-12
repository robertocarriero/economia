from django.urls import path
from .views import tasa_mensual

urlpatterns = [
    path('tasa_mensual/', tasa_mensual, name='valor'),
]
