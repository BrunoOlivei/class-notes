from django.urls import path
from apps.galeria import views

urlpatterns = [
    path('', views.index, name='index'), # Rota para a página inicial
    path('imagem/<int:foto_id>', views.imagem, name='imagem'), # Rota para a página de imagem
    path('busar/', views.buscar, name='buscar'), # Rota para a página de busca
    path('nova-imagem', views.nova_imagem, name='nova_imagem'), # Rota para a página de nova imagem
    path('editar-imagem/<int:foto_id>', views.editar_imagem, name='editar_imagem'), # Rota para a página de editar imagem
    path('deletar-imagem/<int:foto_id>', views.deletar_imagem, name='deletar_imagem'), # Rota para a página de deletar imagem
    path('filtro/<str:categoria>', views.filtro, name='filtro') # Rota para a página de filtro
]