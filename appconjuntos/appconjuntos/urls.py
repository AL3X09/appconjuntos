#from settings import PROJECT_ROOT
"""appconjuntos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
#from .settings.base import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('conjunto/', include('apps.conjunto.urls')),
    path('propiedad/', include('apps.propiedad.urls')),
    path('person/', include('apps.person.urls')),
    path('user/', include('apps.users.urls')),
    #re_path(r'^img/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT,}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
