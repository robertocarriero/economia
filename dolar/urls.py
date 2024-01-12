from django.urls import path
from .views import valor_usd

urlpatterns = [
    path('dolar/', valor_usd, name='dolar'),
]
