from django.urls import path
from .views import *

urlpatterns = [
    path('api/listar/', AvisoSinAprobarListView.as_view(), name = 'listar_avisos_sin_aprobar'),
    path('api/listar/aprobados/', AvisoAprobadosListView.as_view(), name = 'listar_avisos_aprobados'),
    path('api/listar/vantas/', AvisoVentaListView.as_view(), name = 'listar_avisos_venta_inmueble'),
    path('api/listar/arriendos/', AvisoArriendoListView.as_view(), name = 'listar_avisos_arriendo_inmueble'),
    path('api/listar/productos/', AvisoPortafolioListView.as_view(), name = 'listar_avisos_productos_ofrecidos'),
    path('api/crear/', AvisoCreateView.as_view(), name = 'crear_propiedad'),
    path('api/actualiza/<int:pk>/', AvisoUpdateView.as_view(), name = 'actualiza_propiedad'),
    path('api/borrar/<int:pk>/', AvisoDeleteView.as_view(), name = 'borrar_propiedad'),
]

"""no funcional por requerimiento del aplicativo
path('api/detalle/<int:pk>/', AvisoDetailView.as_view(), name = 'detalle_conjunto'),
"""