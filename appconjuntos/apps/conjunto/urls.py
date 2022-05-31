from django.urls import path
from .views import *

urlpatterns = [
    path('api/', Conjunto_list, name = 'lista_conjunto'),
    path('api/<int:pk>/', Conjunto_detail, name = 'detalle_conjunto')
]
