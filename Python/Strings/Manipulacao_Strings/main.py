url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"

# Sanitização da URL
url = url.strip()

# Validação da URL
if url == "":
    raise ValueError("A URL está vazia!")

# Buscar parâmetros
indice_interrogacao = url.find("?")  # Encontra o indice do ? e armazena a variável
url_base = url[:indice_interrogacao]  # Fatia a url do começo até o ? exclusivo
url_parametros = url[indice_interrogacao+1:]  # Fatia a url a partir do caractere após o ? até o final
print(url_base)  # retorna a url base (bytebank.com/cambio)
print(url_parametros)  # retorna os parâmetros passados a URL (quantidade, moeda destino, moeda origem etc.)

# Separar os parâmetros e buscar seus valores

parametro_busca = "quantidade"
indice_parametro = url_parametros.find(parametro_busca)  # Encontra o indice do parâmetro de busca dentro da URL
indice_valor = indice_parametro + len(parametro_busca) + 1  # Encontra o indice do valor a partir do indice do
# parâmetro somado ao tamanho dos carácteres do parrots de busca, somado a 1 para indicar o indice do valor do
# parâmetro
indice_e_comercial = url_parametros.find("&", indice_valor)  # Encontra o indice do "&" a partir do indice do valor
# solicitado

# Verificar se consta na URL o & comercial para evitar erros
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)
