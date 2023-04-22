from django.urls import path
from apps.usuarios import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout', views.logout, name='logout')
]