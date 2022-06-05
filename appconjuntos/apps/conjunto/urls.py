from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', ConjuntoListView.as_view(), name = 'listar_all_conjunto'),
    path('api/crear/', ConjuntoCreateView.as_view(), name = 'crear_conjunto'),
    path('api/detalle/<int:pk>/', ConjuntoDetailView.as_view(), name = 'detalle_conjunto'),
    path('api/actualiza/<int:pk>/', ConjuntoUpdateView.as_view(), name = 'update_conjunto'),
    path('api/borrar/<int:pk>/', ConjuntoDeleteView.as_view(), name = 'borrar_conjunto'),
]

"""urlpatterns = [
    #path('api/', Conjunto_all, name = 'conjunto_total'), se quita porque es una función que tare de todo y yo lo estoy dividiendo
    path('api/', Conjunto_view, name = 'listar_conjunto'),
    #path('api/insertar_c/', Conjunto_insert, name = 'insertar_conjunto'),
    path('api/detalle_c/<int:pk>/', Conjunto_detail, name = 'detalle_conjunto'),
    path('api/actualizar_c/<int:pk>/', Conjunto_update, name = 'actualizar_conjunto'),
    path('api/c_patch/<int:pk>/', Conjunto_update_patch, name = 'conjunto_patch'),
    path('api/borrar_c/<int:pk>/', Conjunto_delete, name = 'borrar_conjunto'),
]"""
