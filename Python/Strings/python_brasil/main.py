from cpf_cnpj import Documento
from telefonesbr import TelefonesBr
from datasbr import DatasBr
from acessocep import BuscaEnereco


exemplo = "09361031678"  # CPF Correto
exemplo2 = "09361031677"  # CPF Incorreto
exemplo3 = "28132093000127"  # CNPJ Correto
exemplo4 = "28132093000129"  # CNPJ Incorreto
exemplo5 = "1111111111"  # CNS
# documento = Documento.cria_documento(exemplo)

tel_exemplo = "55(19)934575359"
# telefone_objeto = TelefonesBr(tel_exemplo)

cadastro = DatasBr()
# print(cadastro)

hoje = DatasBr()
# print(hoje.tempo_cadastro())

cep = 13479792
objeto = BuscaEnereco(cep)
# print(objeto)

a = objeto.acesso_viacep()
bairro, cidade, uf = objeto.acesso_viacep()
print(bairro, cidade, uf)