from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', TipoAvisoListView.as_view(), name = 'listar_tipo_aviso'),
    path('api/crear/', TipoAvisoCreateView.as_view(), name = 'crear_tipo_aviso'),
    path('api/detalle/<int:pk>/', TipoAvisoDetailView.as_view(), name = 'detalle_tipo_aviso'),
    path('api/actualiza/<int:pk>/', TipoAvisoUpdateView.as_view(), name = 'actualiza_tipo_aviso'),
    path('api/borrar/<int:pk>/', TipoAvisoDeleteView.as_view(), name = 'borrar_tipo_aviso'),
]