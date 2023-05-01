from rest_framework import viewsets, filters
from clientes.serializers import ClienteSerializer
from clientes.models import Cliente
from django_filters.rest_framework import DjangoFilterBackend # importando o filtro

class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter] # adicionando o filtro
    ordering_fields = ['nome'] # ordena por nome 
    search_fields = ['nome', 'cpf'] # adicionando o filtro
    filterset_fields = ['ativo'] # adicionando o filtro

