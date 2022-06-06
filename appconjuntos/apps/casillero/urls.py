from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', CasilleroListView.as_view(), name = 'listar_propiedad'),
    path('api/crear/', CasilleroCreateView.as_view(), name = 'crear_propiedad'),
    path('api/detalle/<int:pk>/', CasilleroDetailView.as_view(), name = 'detalle_conjunto'),
    path('api/actualiza/<int:pk>/', CasilleroUpdateView.as_view(), name = 'actualiza_propiedad'),
    path('api/borrar/<int:pk>/', CasilleroDetailView.as_view(), name = 'borrar_propiedad'),
]