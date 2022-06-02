from django.urls import path
from .views import *

urlpatterns = [
    path('api/', Conjunto_all_data, name = 'conjunto_all'),
    path('api/<int:pk>/', Conjunto_list, name = 'listar_conjunto'),
    path('api/<int:pk>/', Conjunto_detail, name = 'detalle_conjunto'),
    #path('api/<string:name>/', Conjunto_insert, name = 'insertar_conjunto'),
    path('api/<int:pk>/', Conjunto_update, name = 'actualizar_conjunto'),
    path('api/<int:pk>/', Conjunto_update_patch, name = 'conjunto_patch'),
    path('api/<int:pk>/', Conjunto_delete, name = 'borrar_conjunto'),
]
