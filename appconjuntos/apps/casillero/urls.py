from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', PropiedadListView.as_view(), name = 'listar_propiedad'),
    path('api/crear/', PropiedadCreateView.as_view(), name = 'crear_propiedad'),
    path('api/actualiza/<int:pk>/', PropiedadDetailView.as_view(), name = 'actualiza_propiedad'),
    path('api/borrar/<int:pk>/', PropiedadDeleteView.as_view(), name = 'borrar_propiedad'),
]