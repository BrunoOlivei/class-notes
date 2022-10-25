import re

# url = https://www.bytebank.com.br/cambio

'''
Quando utilizamos os colchetes para compilar um padrão de caracteres nós estamos informando ao python que dentro do 
padrão podem ou não ter algum ou todos os caracteres informados. Utilizando o parênteses nós informamos que 
necessariamente os caracteres ali presentes precisam ser exatamente aqueles e dispostos da forma que informamos.
'''
# padrao_url = re.compile('(https://) [abc]')

'''
Da mesma forma que fizemos para o CEP podemos informar, com a interrogação, que determinado conjunto de caracteres é
opcional.
'''
# padrao_url = re.compile('(https://)?(www.)?')

'''
Textos padrões que não terão nenhuma instrução (opcional ou não, quantificador, etc) podem ser passados sem a 
necessidade de parenteses.
'''
# padrao_url = re.compile('(https://)?(www.)?bytebank.com(.br)?/cambio')

'''
No caso da URL do ByteBank, o HTTPS pode ou não conter o 'S', para determinar que um caractere que está inserido em um 
conjunto de caracteres já determinados como opcional ou não, podemos utilizar o parenteses ou os colchetes também
e informar utilizando a interrogação.
'''
# padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

'''
Para o CEP nós utilizamos o método search para buscar dentro de um endereço se havia ou não o CEP, para o caso do 
ByteBank onde necessariamente iremos apenas checar se a URL é exatamente o padrão e não procurar dentro de um texto
se a URL existe, utilizaremos o método match, caso o match não encontra ele retorna None.
'''
url = 'https://www.bytebank.com.br/cambio'
padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = padrao_url.match(url)

'''
Como o match retorna None podemos verificar se a função match encontrou uma url válida e caso retorne None envia uma 
mensagem ao usuário informando que a URL é inválida
'''
if not match:
    raise ValueError("A URL é inválida!")
else:
    print("A URL é válida!")
