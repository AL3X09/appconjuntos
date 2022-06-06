from django.urls import path

from .views import *

urlpatterns = [
    path('api/listar/', VisitanteListView.as_view(), name = 'listar_all_conjunto'),
    path('api/crear/', VisitanteCreateView.as_view(), name = 'crear_conjunto'),
    path('api/detalle/<int:pk>/', VisitanteDetailView.as_view(), name = 'detalle_conjunto'),
    path('api/actualiza/<int:pk>/', VisitanteUpdateView.as_view(), name = 'update_conjunto'),
    path('api/borrar/<int:pk>/', VisitanteDeleteView.as_view(), name = 'borrar_conjunto'),
]