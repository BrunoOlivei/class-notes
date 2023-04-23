from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls), # Rota para a página de administração
    path('', include('apps.galeria.urls')), # Rota para a página de galeria
    path('', include('apps.usuarios.urls')), # Rota para a página de usuários
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Rota para a página de mídia
