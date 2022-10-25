"""
Definindo atributos próprios da linguagem dentro de uma classe criada.
Suponhamos que queremos ter um método dentro da nossa classe "extrator_url" que retorne o tamanho da url informada.
Para isso poderiamos utilizar o método len()
"""
from extrator_url import ExtratorUrl

url = "bytebank.com/cambio?quantidade=100&moedaDestino=dolar&moedaOrigem=real"
extrair_url = ExtratorUrl(url)  # Criando um objeto com a url

'''
Utilizando o método len() com o nosso objeto extrair_url
'''
# print("O tamanho da URL é: ", len(extrair_url))
'''
Não foi possível e o python retornou um erro:
    print("O tamanho da URL é: ", len(extrair_url))
TypeError: object of type 'ExtratorUrl' has no len()
O erro diz que o objeto da classe ExtratorUrl não possui o atributo len()

Na linguagem python existe o atributo, porém não podemos utilizar ele sem o definirmos dentro da nossa classe.

Para isso basta definirmos um método (def) utilizando __len__(self), passando self como argumento, e como desejamos que 
ele retorne apenas o tamanho da url informada no objeto, colocamos return len(self.url).
Dessa forma podemos utilizar a própria função built-in do python
'''

print("O tamanho da URL é: ", len(extrair_url))
# O tamanho da URL é:  70

'''
Dessa forma vimos que podemos definir métodos da própria linguagem para as nossas classes e assim usufruir das suas
funcionalidades sempre que necessário basta utilizar a função passando como argumento o próprio objeto.
'''

'''
Outro método que podemos utilizar dentro da classe extrator url é o __str__, se utilizarmos a função built-in print 
sem instancia-la dentro da classe nós teremos como resultado o objeto de memória, o que não seria interessante.
'''
# print(extrair_url)
# <extrator_url.ExtratorUrl object at 0x00000146CCE4B1C0>

'''
Instanciando o __str__ ele irá retornar para nós o objeto que está dentro dessa memória em formato string, para isso
basta definir um novo método com __str__ passando como argumento a propria classe e como retorno a mesma classe chamando
a url
'''
# def __str__(self):
#     return self.url

print(extrair_url)

'''
Igualdade vs. Indentidade
Ao descrevermos um expressão para comparar dois valores, utilizamos o == para essa finalidade, por exemplo compararmos
dois objetos distintos extrair_url e extrair_url_2, sendo os dois objetos contendo a mesma url, o resultado dessa 
comparação será False, isso por que o python executa o método __eq__() onde, extrair_url__eq__(extrair_url_2).
Na verdade o que esse método realiza não é a comparação dos valores em si (URL) mas o endereço de memória em que cada
objeto se encontra, como criamos dois objetos, será utilizado dois endereços de memória.
'''
# extrair_url_2 = ExtratorUrl(url)
# print(extrair_url == extrair_url_2)
# False

'''
Para usufruirmos do método __eq__ de forma que caso tenhamos dois objetos com a mesma url, isso pode ser útil caso para
evitar utilização desnecessária de memória, podemos construir um método dentro da nossa classe, utilizando novamente o
def __eq__(self, other), aqui temos uma diferença, já que o método eq recebe um argumento, que no caso dele é o segundo
valor a ser comparado, por padrão o chamamos de other. 
Em seguida retornamos com return self.url == other.url
'''
# def __eq__(self, other):
#     return self.url == other.url

extrair_url_2 = ExtratorUrl(url)
print(extrair_url == extrair_url_2)
# True

'''
Aqui precisamos deixar algo muito claro que o método __eq__ compara os valores dos objetos, mas em nenhum momento os 
objetos possuem o mesmo endereço de memória, eles continuam diferentes, podemos verificar isso utilizando o método id()
'''
print(id(extrair_url))
print(id(extrair_url_2))
# 2509265969104
# 2509265968912

print(id(extrair_url) == id(extrair_url_2))
# False

'''
Outra forma de comparar os endereços de memória é utilizando o is
'''
print(extrair_url is extrair_url_2)
# False