from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', NoticiaListView.as_view(), name = 'listar_all_noticia'),
    path('api/crear/', NoticiaCreateView.as_view(), name = 'crear_noticia'),
    path('api/detalle/<int:pk>/', NoticiaDetailView.as_view(), name = 'detalle_noticia'),
    path('api/actualiza/<int:pk>/', NoticiaUpdateView.as_view(), name = 'update_noticia'),
    path('api/borrar/<int:pk>/', NoticiaDeleteView.as_view(), name = 'borrar_noticia'),
]