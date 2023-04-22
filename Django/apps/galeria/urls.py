from django.urls import path
from apps.galeria import views

urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('busar/', views.buscar, name='buscar'),
    path('nova-imagem', views.nova_imagem, name='nova_imagem'),
    path('editar-imagem', views.editar_imagem, name='editar_imagem'),
    path('deletar-imagem', views.deletar_imagem, name='deletar_imagem'),
]