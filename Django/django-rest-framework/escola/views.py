from rest_framework import viewsets, generics, status # Importa o módulo viewsets do rest_framework
from escola.models import Aluno, Curso, Matricula # Importa os models Aluno e Curso do app escola
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer, \
    AlunoSerializerV2 # Importa os serializers AlunoSerializer e CursoSerializer do app escola
from rest_framework.response import Response # Importa o módulo Response do rest_framework
from django.utils.decorators import method_decorator # Importa o módulo method_decorator do django.utils.decorators
from django.views.decorators.cache import cache_page # Importa o módulo cache_page do django.views.decorators.cache


class AlunosViewSet(viewsets.ModelViewSet): 
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all() # Consulta todos os objetos do model Aluno
    def get_serializer_class(self):
        if self.request.version == 'v2': # Se a versão da requisição for v2
            return AlunoSerializerV2 # Retorna a classe AlunoSerializerV2
        else:
            return AlunoSerializer # Classe que serializa os dados do model Aluno

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all() # Consulta todos os objetos do model Curso
    serializer_class = CursoSerializer # Classe que serializa os dados do model Curso

    def create(self, request):
        '''Cria um curso e retorna a URL para acessar o curso criado tornando a API mais auto descritiva'''
        serializer = self.serializer_class(data=request.data) # Cria um objeto serializer com os dados da requisição
        if serializer.is_valid(): # Se os dados forem válidos
            serializer.save() # Salva os dados
            response = Response(serializer.data, status=status.HTTP_201_CREATED) # Cria uma resposta com os dados e o status 201
            object_id = str(serializer.data['id']) # Pega o id do objeto criado
            response['location'] = request.build_absolute_uri() + object_id # Cria a URL para acessar o objeto criado
            return response # Retorna a resposta

class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all() # Consulta todos os objetos do model Matricula
    serializer_class = MatriculaSerializer # Classe que serializa os dados do model Matricula
    http_method_names = ['get', 'post', 'put', 'path'] # Define os métodos HTTP que serão aceitos

    @method_decorator(cache_page(20)) # Define o tempo de cache da página em segundos
    def dispatch(self, *args, **kwargs):
        return super(MatriculaViewSet, self).dispatch(*args, **kwargs)

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk']) # Consulta todos os objetos do model Matricula que possuem o aluno_id igual ao id passado na URL
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer # Classe que serializa os dados do model Matricula

class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']) # Consulta todos os objetos do model Matricula que possuem o curso_id igual ao id passado na URL
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer # Classe que serializa os dados do model Matricula