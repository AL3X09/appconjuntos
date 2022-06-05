from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', PersonListView.as_view(), name = 'listar_persona'),
    path('api/crear/', PersonCreateView.as_view(), name = 'crear_persona'),
    path('api/actualiza/<int:pk>/', PersonaDetailView.as_view(), name = 'actualiza_persona'),
    path('api/borrar/<int:pk>/', PersonaDeleteView.as_view(), name = 'borrar_persona'),
]