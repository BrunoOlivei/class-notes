import pytest
from pytest import mark
from codigo.bytebank import Funcionario


class TestClass:
    def test_quando_idade_recebe_13_03_2000_retorna_22(self):
        entrada = '13/03/2000' # Given - Contexto
        esperado = 23

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        resultado = funcionario_teste.idade() # When - Ação

        assert resultado == esperado # Then - Asserção

    def test_quando_sobrenome_Lucas_Carvalho_retorna_Carvalho(self):
        entrada = " Lucas Carvalho " # Given - Contexto
        esperado = "Carvalho"

        funcionario_teste = Funcionario(entrada, '13/03/2000', 1111)

        resultado = funcionario_teste.sobrenome() # When - Ação

        assert resultado == esperado # Then - Asserção

    
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given - Contexto
        entrada_nome = "Paulo Bragança"
        esperado = 90000

        funcionario_teste = Funcionario(entrada_nome, '13/03/2000', entrada_salario)

        funcionario_teste.decrescimo_salario() # When - Ação
        resultado = funcionario_teste.salario

        assert resultado == esperado # Then - Asserção

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada_salario = 1000 # Given - Contexto
        esperado = 100

        funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
        resultado = funcionario_teste.calcular_bonus() # When - Ação

        assert resultado == esperado # Then - Asserção

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada_salario = 100000
            funcionario_teste = Funcionario('Teste', '13/03/2000', entrada_salario)
            resultado = funcionario_teste.calcular_bonus() # When - Ação

            assert resultado # Then - Asserção


    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = "Teste", "12/03/2000", 1000 # Given - Contexto
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

    #     funcionario_teste = Funcionario(nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() # When - Ação

    #     assert resultado == esperado # Then - Asserção