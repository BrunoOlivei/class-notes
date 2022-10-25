"""Expressões regulares (Regular Expression - ReGex) são expressões encontradas, geralmente em strings que são padrão
exemplo são CEPs, onde sabe se que é um grupo de 8 números de 0 a 9 com ou sem hífen após os 5 primeiros números.
"""
# Importando a biblioteca de expressões regulares
import re

# Variável com string contendo endereço completo, inclusive CEP
endereco = "Rua Imperador Comodo, 459, Jardim Imperador, Americana-SP"

'''
O módulo compile compila um padrão de expressão regular que posteriormente pode ser utilizado para correspondência
com outros métodos.
Dentro do método compile utilizamos colchetes que recebem as informações que são padrão entre aspas como uma string
'''

# Variável padrão recebe a compilação dos conjuntos de caracteres que padrão em um CEP cada colchete é um conjunto.
# padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")

'''
Para não ficar repetitivo cada um dos conjuntos passados dentro do compile, podemos utilizar quantificadores.
Os quantificadores informam quantas vezes cada conjunto se repete, para isso basta inserir a quantidade dentro de chaves
logo após o conjunto em questão.
'''

# Compilando conjunto de números repetidos por 5 vezes antes do hífen e 3 vezes após o hífen
# padrao = re.compile("[0123456789]{5}[-][0123456789]{3}")

'''
Dentro do CEP, muitas vezes temos ou não o hífen, casos como esse podemos utilizar o ? para informar ao compilador que
aquele conjunto de caracteres são opcionais, ou seja, pode ou não conter. 
'''

# Ponto de interrogação informa que o conjunto de caracteres são opcionais, sendo assim caso o compile não o encontre
# não incorre em erro
# padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")

'''
Podemos simplificar ainda mais os conjuntos de caracteres utilizando um intervalo entre cada conjunto, como tempos 
algarismo de 0 a 9 podemos escrever [0-9] utilizando um hífen entre o primeiro e último número. Pode ser utilizado 
também para informar que um conjunto de caracteres vai de "a" até "z" por exemplo.
'''

# Simplificando mais os conjuntos de algarismos informando um intervalo, separados por hífen
# padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")

'''
Caracteres opcionais como o hífen no CEP podem ser informados utilizando também as chaves, passando dois valores 
separados por vírgula, o primeiro sendo 0 como nenhuma ocorrência e o segundo sendo 1 como uma ocorrência. 
Isso demonstra que poderiamos informar que determinados caracteres podem ocorrer, partindo de um N número de vezes até 
um limite de N + X por exemplo. 
'''

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

'''
O método search da biblioteca re retorna um objeto de memória do tipo Match, que indica que encontrou o padrão dentro da
variável informada
'''
busca = padrao.search(endereco)
print(busca)
# <re.Match object; span=(59, 68), match='13479-792'>

'''
Nos objetos de memória retornados pelo search como o Match, podemos utilizar um outro método para visualizar o que foi
encontrado, o método é o group e ele retorna uma simples string caso encontre 1 ocorrência do compile, mais de uma 
retornará uma tupla contendo cada ocorrência encontrada.
'''

cep = busca.group()
print(cep)
# 13479-792
