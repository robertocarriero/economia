from django.urls import path
from .views import noticias_economicas

urlpatterns = [
    path('noticias/',noticias_economicas , name='noticias')
]
