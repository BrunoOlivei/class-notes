from rest_framework import serializers # Importa o módulo serializers do rest_framework
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer): # Cria uma classe AlunoSerializer que herda de serializers.ModelSerializer
    class Meta: 
        model = Aluno # Aluno é o model que será serializado
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'foto'] # Campos que serão serializados


class CursoSerializer(serializers.ModelSerializer): # Cria uma classe CursoSerializer que herda de serializers.ModelSerializer
    class Meta:
        model = Curso # Curso é o model que será serializado
        fields = '__all__' # Todos os campos serão serializados

class MatriculaSerializer(serializers.ModelSerializer): # Cria uma classe MatriculaSerializer que herda de serializers.ModelSerializer
    class Meta:
        model = Matricula # Matricula é o model que será serializado
        exclude = [] # Todos os campos serão serializados

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao') # Cria um campo somente leitura para o curso e exibe a descrição
    periodo = serializers.SerializerMethodField() # Cria um campo para o período e exibe o valor do método get_periodo
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome') # Cria um campo somente leitura para o aluno_nome e exibe o nome do aluno
    class Meta:
        model = Matricula
        fields = ['aluno_nome']

class AlunoSerializerV2(serializers.ModelSerializer): # Cria uma classe AlunoSerializer que herda de serializers.ModelSerializer
    class Meta: 
        model = Aluno # Aluno é o model que será serializado
        fields = ['id', 'nome', 'celular', 'rg', 'cpf', 'data_nascimento', 'foto'] # Campos que serão serializados

