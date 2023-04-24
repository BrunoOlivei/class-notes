from django.urls import path
from apps.usuarios import views

urlpatterns = [
    path('login', views.login, name='login'), # Rota para a página de login
    path('cadastro', views.cadastro, name='cadastro'), # Rota para a página de cadastro 
    path('logout', views.logout, name='logout') # Rota para a página de logout
]