from django.urls import path
from .views import circulacion_monetaria

urlpatterns = [
    path('circulacion/', circulacion_monetaria, name=('circulacion'))
]
