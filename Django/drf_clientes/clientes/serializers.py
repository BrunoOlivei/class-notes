from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data: dict):
        """Valida os dados do cliente

        Args:
            data (dict): dados do cliente

        Raises:
            serializers.ValidationError: valida cada campo do cliente e retorna o erro caso algum campo não seja válido

        Returns:
            dict: dados do cliente
        """
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({"cpf": "Número de CPF inválido"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({"nome": "O nome deve conter apenas letras."})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({"rg": "O rg deve conter 9 dígitos."})

        if not celular_valido(data['celular']):
            raise serializers.ValidationError({"celular": "O celular deve conter no mínimo 11 dígitos e estar no formato 11 91234-1234."})
        
        return data
    

