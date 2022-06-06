from django.urls import path

from .views import *

urlpatterns = [
    path('api/listar/', AuditoriaPedidoListView.as_view(), name = 'listar_all_conjunto'),
    path('api/crear/', AuditoriaPedidoCreateView.as_view(), name = 'crear_conjunto'),
    path('api/detalle/<int:pk>/', AuditoriaPedidoDetailView.as_view(), name = 'detalle_conjunto'),
    path('api/actualiza/<int:pk>/', AuditoriaPedidoUpdateView.as_view(), name = 'update_conjunto'),
    path('api/borrar/<int:pk>/', AuditoriaPedidoDeleteView.as_view(), name = 'borrar_conjunto'),
]