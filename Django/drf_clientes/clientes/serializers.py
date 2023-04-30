from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate_cpf(self, cpf: str):
        """Valida o cpf

        Args:
            cpf (str): número do cpf

        Raises:
            serializers.ValidationError: O cpf deve conter 11 dígitos.

        Returns:
            str: número do cpf
        """
        if len(cpf) != 11:
            raise serializers.ValidationError("O cpf deve conter 11 dígitos.")
        return cpf
    