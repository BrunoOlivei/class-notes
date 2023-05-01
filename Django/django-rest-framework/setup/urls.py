# Django REST Framework
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter() # Cria uma rota padrão
router.register('alunos', AlunosViewSet, basename='Alunos') # Registra a rota alunos
router.register('cursos', CursosViewSet, basename='Cursos') # Registra a rota cursos
router.register('matriculas', MatriculaViewSet, basename='Matriculas') # Registra a rota matriculas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), # Inclui as rotas do router
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
