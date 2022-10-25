# importando a classe ExtratorURL
from extrator_url import ExtratorUrl

# URL a ser utilizada pela classe
url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
# Criando um objeto com a url
extrair_url = ExtratorUrl(url)
# Definindo uma variável que receberá o resultado do método que extrai o valor (quantidade) de dentro da url
valor_quantidade = extrair_url.get_valor_parametro("quantidade")
# Imprimindo o resultado
print(valor_quantidade)

valor_dolar = 5.50
valor_total = valor_dolar * valor_quantidade
print(valor_total)
