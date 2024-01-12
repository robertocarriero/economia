from django.urls import path
from .views import depositos

urlpatterns = [
    path('depositos/', depositos, name='deposito'),
]
