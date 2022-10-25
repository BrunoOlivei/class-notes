# Tuple (Tupla)

## Introdução

-   Tuplas são representadas por parênteses ()
-   Tuplas são imutáveis, não é possível alterar os itens que estão inseridos em uma tupla.
-   Toda função (operação) executada em uma tupla, gera uma nova tupla
-   A linguagem cria automaticamente uma tupla, a partir do momento que é compactado em uma variável diversos elementos, mesmo que eles sejam do mesmo tipo.

```python
tupla1 = 1, 2, 3, 4, 5
print(tupla1)
print(type(tupla1))

# (1, 2, 3, 4, 5)
# <class 'tuple'>
```

-   Tentar criar uma tupla com apenas 1 elemento, não funciona

```python
tupla1 = (1)
print(tupla1)
print(type(tupla1))

# 1
# <class 'int'>
```

-   Para criar uma tupla com apenas 1 elemento, é necessário uma vírgula logo após o elemento:

```python
tupla1 = (1,)
print(tupla1)
print(type(tupla1))

# (1,)
# <class 'tuple'>
```

-   Também é possível criar uma tupla vazia:

```python
tupla1 = ()
print(tupla1)
print(type(tupla1))

# ()
# <class 'tuple'>
```

Tuplas são representadas por parênteses porém o que caracteriza que aquela variável, que possuí apenas 1 valor seja uma tupla é a vírgula.

```python
tupla1 = 1,
print(tupla1)
print(type(tupla1))

# (1,)
# <class 'tuple'>
```

---

## Desempacotamento de Tuplas

```python
tupla = ("Bruno", "Oliveira")
print(tupla)
print(type(tupla))

nome, sobrenome = tupla

print(nome)
print(sobrenome)

# ('Bruno', 'Oliveira')
# <class 'tuple'>

# Bruno
# Oliveira
```

---

Caso haja um número maior de itens do que a quantidade de variáveis disponíveis, isso pode ser contornado usando um asterisco antes do nome da variável em que você deseja que receba os valores excedentes:

```python
tupla = (1, 2, 3, 4, 5)
a, *b, c = tupla

print(a) # 1
print(b) # [2, 3, 4]
print(c) # 5
```

---

# Slicing

```python
tupla1 = (1, 2, 3, 4, 5, 6, 7, 8)
tupla2 = (9, 10, 11, 12, 13, 14, 15)

print(3 in tupla1)
```

## Iteração

```python
tupla1 = (1, 2, 3, 4, 5, 6, 7, 8)
tupla2 = (9, 10, 11, 12, 13, 14, 15)

for num in tupla1:
    print(num)

1
2
3
4
5
6
7
8
```

---

## Contando elementos:

```python
tupla1 = (1, 2, 3, 3, 3, 3, 7, 8)
tupla2 = (9, 10, 11, 12, 13, 14, 15)

print(tupla1.count(3)) # 4
```

---

Passando uma String para uma tupla:

```python
escola = tuple("Geek University")
print(escola)

# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

escola = tuple("Geek", "University")
print(escola)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 1, in <module>
    escola = tuple("Geek", "University")
TypeError: tuple expected at most 1 argument, got 2
'''

escola = tuple(1, 2)
print(escola)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 1, in <module>
    escola = tuple(1, 2)
TypeError: tuple expected at most 1 argument, got 2
'''

escola = tuple(["Geek", "University"])
print(escola)

# ('Geek', 'University')
```

A função `tuple` só funciona com 1 elemento, seja ele uma lista ou uma única string onde as palavras estão separadas por espaço.

---

## Contagem de Elementos:

```python
escola = tuple("Geek University")
print(escola)

# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

print(escola.count("e"))

# 3
```

---

# Acesso, iteração e outros com Tuplas

Encontrar um item a partir do índice:

```python
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", 
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print(meses[5]) # Junho

```

---

Também é possível encontrar o índice a partir do elemento:

```python
print(meses.index("Junho"))

# 5
```

OBS: Caso o elemento não exista será gerado um ERRO (ValueError)

---

É possível pesquisar o índice de algum elemento, a partir de uma posição definida:

```python
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", 
         "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

print(meses.index("Julho", 6)) # 6
```

---

## Iteração

```python
i = 0
while i < len(meses):
    print(meses[i])
    i = i +1

Janeiro
Fevereiro
Março
Abril
Maio
Junho
Julho
Agosto
Setembro
Outubro
Novembro
Dezembro
```

## Contando elementos:

```python
tupla1 = (1, 2, 3, 3, 3, 3, 7, 8)
tupla2 = (9, 10, 11, 12, 13, 14, 15)

print(tupla1.count(3)) # 4
```

---

Passando uma String para uma tupla:

```python
escola = tuple("Geek University")
print(escola)

# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

escola = tuple("Geek", "University")
print(escola)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 1, in <module>
    escola = tuple("Geek", "University")
TypeError: tuple expected at most 1 argument, got 2
'''

escola = tuple(1, 2)
print(escola)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 1, in <module>
    escola = tuple(1, 2)
TypeError: tuple expected at most 1 argument, got 2
'''

escola = tuple(["Geek", "University"])
print(escola)

# ('Geek', 'University')
```

A função `tuple` só funciona com 1 elemento, seja ele uma lista ou uma única string onde as palavras estão separadas por espaço.

---

Contagem de Elementos:

```python
escola = tuple("Geek University")
print(escola)

# ('G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y')

print(escola.count("e"))

# 3
```

---

# Concatenação das Tuplas

```python
tupla1 = (1, 2, 3, 4, 5, 6, 7, 8)
tupla2 = (9, 10, 11, 12, 13, 14, 15)

print(tupla1 + tupla2) # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

print(tupla1) # (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla2) # (9, 10, 11, 12, 13, 14, 15)
```

---

# Funções Aritméticas em Tuplas

Assim como em listas é possível fazer operações aritméticas desde que os itens dentro a tupla sejam número inteiros ou flutuantes:

```python
tupla = (1, 2, 3, 4, 5, 6, 7, 8)
print(tupla) # (1, 2, 3, 4, 5, 6, 7, 8)

print(sum(tupla)) # 36
print(max(tupla)) # 8
print(min(tupla)) # 1
print(len(tupla)) # 8
```

---

# Funções Inexistentes em Tuplas

Funções `insert, extend, pop, clear, reverse, sort` não funcionam em tuplas.

Em listas estas funções alteram naturalmente o dado, ou seja, qualquer uma das funções rodadas, automaticamente alteram a variável e isso se torna a nova ordem da lista, seja uma adição de elemento, a remoção, a ordenação etc.

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 2, in <module>
    tupla.pop()
AttributeError: 'tuple' object has no attribute 'Aqui o nome da função'
```

---

# Usabilidade das Tuplas

As tuplas são indicadas para uso quando não há necessidade de alterar os dados que estejam inseridos em uma coleção:

Exemplos:

```python
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")
print(meses)
```

Meses são imutáveis, ou seja, não há nenhum mês a mais para ser adicionado ou motivos para excluir um.

---

### Algumas Observações referente a usabilidade:

-   Tuplas são mais rápidas do que listas
-   Tuplas deixam o código mais seguro (imutabilidade)

#tuples #tuplas #tuplemethods #tuplasmetodos

---

# Named tuple
Esse tipo de tupla é muito parecido com dicionários, exceto que no caso dos dicionários seus elementos não são indexados.

Na `namedtuple` é como se fosse criado uma chave para cada valor e um nome para a tupla total.

Essas 'chaves' são chamadas de parâmetros (_field_names_).

Para criação da `namedtuple` é necessário que seja definido previamente o nome e os parâmetros

## Declarando uma `namedtuple`:

### Forma 1 - Declaração namedtuple

```python
>>> from collections import namedtuple

>>> cachorro = namedtuple('cachorro', 'idade raca nome')
```

O primeiro cachorro é o nome da variável, dentro dos parênteses estão definidos o nome e parâmetros, a palavra cachorro dentro dos parênteses é o nome, enquanto 'idade raca e nome' são os parâmetros.

### Forma 2 - Declaração namedtuple

Por parâmetros podem ou não ser separados por vírgula também, mas a linguagem aceita o espaçamento para separá-los.

```python
>>> from collections import namedtuple

>>> cachorro = namedtuple('cachorro', 'idade', 'raca', 'nome')
```

### Forma 3 - Declaração namedtuple

Também é aceito nos parâmetros (_field_name_) uma lista:

```python
>>> cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])
```

### Algumas regras para o _field_name:_

Os parâmetros (_field_names_) podem ser qualquer usados letras ou números o _underline_ porém não podem começar com números ou _underline_, bom como não podem ser palavras-chaves da linguagem. Também não é permitido repetição do _field_name_

Caso ocorra de ser usado uma palavra-chave ou seja repetido um _field_name_, esses serão substituídos automaticamente por **_i** onde i é o índice do elemento.

```python
>>> ['abc', 'def', 'def', 'abc']
>>> ['abc', '_1', 'ghi', '_3']
```

## Usabilidade:

```python
>>> cookie = cachorro(idade=3, raca='Golden Retriever', nome='Cookie')
>>> print(cookie)
>>> print(type(cookie))

cachorro(idade=3, raca='Golden Retriever', nome='Cookie')
<class '__main__.cachorro'>
```

Técnicamente é como se estivéssemos criando um TIPO de dado novo, assim como as strings, listas, dicionários, numbers, floats, e por ai vai, nesse caso nós criamos um tipo de dado chamado cachorro que recebe idade, raça e nome como valores.

As funções básicas da tupla normal podem ser utilizadas em namedtuples, como acesso a dados pelo indice, etc.

## NamedTuple methods
### .\_asdict()

Este método transforma o `namedtuple` e retorna como dicionário:

```python
>>> from collections import namedtuple

>>> cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

>>> cookie = cachorro(idade=3, raca='Golden Retriever', nome='Cookie')

>>> print(cookie)
>>> print(type(cookie))

cachorro(idade=3, raca='Golden Retriever', nome='Cookie')
<class '__main__.cachorro'>

>>> cookie_dic = cookie._asdict()
>>> print(cookie_dic)
>>> print(type(cookie_dic))

{'idade': 3, 'raca': 'Golden Retriever', 'nome': 'Cookie'}
<class 'dict'>
```

---

### .\_replace(_key=value_)

Ele retorna um novo valor ao parâmetro informado dentro dos parênteses, porém não susbistitui o valor da variável original, é necessário passar novamente:

```python
>>> cookie = cookie._replace(idade=4)
>>> print(cookie)

cachorro(idade=4, raca='Golden Retriever', nome='Cookie')
```

### .\_fields

Com ele é possível ver os _field_names_

```python
>>> print(cookie._fields)

('idade', 'raca', 'nome')
```

#namedtuplemethods,

