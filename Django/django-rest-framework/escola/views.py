from rest_framework import viewsets, generics # Importa o módulo viewsets do rest_framework
from escola.models import Aluno, Curso, Matricula # Importa os models Aluno e Curso do app escola
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer # Importa os serializers AlunoSerializer e CursoSerializer do app escola
from rest_framework.authentication import BasicAuthentication # Importa o módulo BasicAuthentication do rest_framework
from rest_framework.permissions import IsAuthenticated # Importa o módulo IsAuthenticated do rest_framework


class AlunosViewSet(viewsets.ModelViewSet): 
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all() # Consulta todos os objetos do model Aluno
    serializer_class = AlunoSerializer # Classe que serializa os dados do model Aluno
    authentication_classes = [BasicAuthentication] # Autenticação básica
    permission_classes = [IsAuthenticated] # Permissão de autenticação


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all() # Consulta todos os objetos do model Curso
    serializer_class = CursoSerializer # Classe que serializa os dados do model Curso
    authentication_classes = [BasicAuthentication] # Autenticação básica
    permission_classes = [IsAuthenticated] # Permissão de autenticação

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all() # Consulta todos os objetos do model Matricula
    serializer_class = MatriculaSerializer # Classe que serializa os dados do model Matricula
    authentication_classes = [BasicAuthentication] # Autenticação básica
    permission_classes = [IsAuthenticated] # Permissão de autenticação

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']) # Consulta todos os objetos do model Matricula que possuem o aluno_id igual ao id passado na URL
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer # Classe que serializa os dados do model Matricula
    authentication_classes = [BasicAuthentication] # Autenticação básica
    permission_classes = [IsAuthenticated] # Permissão de autenticação

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']) # Consulta todos os objetos do model Matricula que possuem o curso_id igual ao id passado na URL
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer # Classe que serializa os dados do model Matricula
    authentication_classes = [BasicAuthentication] # Autenticação básica
    permission_classes = [IsAuthenticated] # Permissão de autenticação