from django.urls import path
from .views import valor_usd_of

urlpatterns = [
    path('dolar_of/', valor_usd_of, name='dolar_of'),
]
