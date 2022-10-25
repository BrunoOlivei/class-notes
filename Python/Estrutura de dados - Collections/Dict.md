# Dict (Dicionário)

## Introdução

-   Em algumas linguagens de programação os dicionários são conhecidos como mapas
-   Dicionários são coleções do tipo chave/valor
-   Dicionários são representados por chaves {}

```python
print(type({}))

# <class 'dict'>
```

Os elementos no dicionários SEMPRE são seguidos pelos pares chave, dois pontos, valor. Cada elemento é separado por vírgula:

```python
pacientes = {'nome': 'Bruno', 'sobrenome': 'Oliveira', 'data nascimento': '03/10/1988'}

print(pacientes)
print(type(pacientes))

# {'nome': 'Bruno', 'sobrenome': 'Oliveira', 'data nascimento': '03/10/1988'}
# <class 'dict'>
```

Tanto chave e valor podem ser qualquer tipo de dado, podendo misturar os tipos:

---

Outra forma de de construir um dicionário (menos comum)

```python
paciente1 = dict(nome='Bruno', sobrenome='Oliveira', nascimento='03/10/1988')

print(paciente1)
print(type(paciente1))

# {'nome': 'Bruno', 'sobrenome': 'Oliveira', 'nascimento': '03/10/1988'}
# <class 'dict'>
```

---

Detalhes importantes sobre a dicionários:

-   Seus itens são facilmente mutáveis permitindo assim adicionar ou remover itens.
-   Ao contrario das listas e das tuplas, que podem ter seus itens acessados usando um índice, o conteúdo de um dicionário só pode ser acessado usando as chaves, portanto é importante conhecer as chaves que estão inseridas em cada dicionário.
-   As chaves só podem apontar para um único valor, ter 2 valores em uma chave causa erro.
-   Os nomes dados a cada chave devem ser único entre si, porém podem ser iguais se estiverem em dicionários diferentes.
-   Tuplas são interessantes de serem utilizadas como chave de dicionários, pois as mesmas são imutáveis.

```python
localidades = {
    (35.6895, 39.6917): 'Escritório em Tóquio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (47.7749, 122.4194): 'Escritório em São Paulo',
}
```

#dict #dicts

---

## Acessando Elementos do Dicionário

Ao contrario das listas e tuplas onde conseguíamos usar a indexação através dos colchetes [ ] para acessar elementos dos dois tipos de coleções, o dicionário não possuí índice para seus elementos.

No caso é usado a chave criada para cada elemento:

### Forma 1

Acessando via chave dentro de colchetes:

```python
paciente1 = dict(nome='Bruno', sobrenome='Oliveira', nascimento='03/10/1988')

print(paciente1["nome"]) # Bruno
print(paciente1["nascimento"]) # 03/10/1988

```

Tentar retornar um item que não possuí chave ou informar a chave incorretamente, causa erro no código:

```python
print(paciente1['nacimento'])

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 14, in <module>
    print(paciente1['nacimento'])
KeyError: 'nacimento'
'''
```

### Forma 2

Utilizando a palavra-chave `get`

```python
print(paciente1.get("nome")) # Bruno
print(paciente1.get("nascimento")) # 03/10/1988

print(paciente1.get('nacimento')) # None
```

Repare que utilizando o `get` ao chamar um item com uma chave incorreta ou inexistente o programa não acusa erro.

### None em ação

```python
paciente1 = dict(nome='Bruno', sobrenome='Oliveira', nascimento='03/10/1988')

paciente = paciente1.get(input('Digite a chave que deseja pesquisar: '))

>>> nome

if paciente:
    print(f"Encontrei o paciente {paciente}.")
else:
    print("Não encontrei nenhum dado do paciente 1.")

# Bruno

Se colocar endereço por exemplo o resultado será None portanto o que será imprimido 
na tela será "Não encontrei nenhum dado do paciente 1." já que None sempre será falso.
```

Outra forma de ser escrito o código acima:

```python
paciente = paciente1.get(input('Digite a chave que deseja pesquisar: '), "Não encontrado")
print(f'Encontrei o seguinte dado {paciente}.')

>>> nome
# Encontrei o seguinte dado Bruno.

>>> endereço
# Encontrei o seguinte dado Não encontrado.
```

Dessa forma é definido um valor padrão para os casos em que a chave informada não seja encontrada.

### Verificando se alguma chave está no dicionário:

```python
print('nome' in paciente1) # True
print('endereço' in paciente1) # False
print('Bruno' in paciente1) # False
```

Só é possível verificar as chaves. Os valores não são pesquisáveis.

#dict

---

## Métodos
```python
d = dict(a=1, b=2, c=3)
print(d)

# {'a': 1, 'b': 2, 'c': 3}
```

### .clear()

```python
d.clear()
print(d)

# {}
```

Limpa todos os elementos do dicionário deixando o vazio.

---

### .copy()

```python
novo = d.copy()
print(novo)

# {'a': 1, 'b': 2, 'c': 3}

novo['d'] = 4

print(d) # {'a': 1, 'b': 2, 'c': 3}
print(novo) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Cria uma _deep copy_, ou seja uma cópia totalmente independente e sem vinculo da original

---

### Shallow Copy:

```python
novo = d

novo['d'] = 4

print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(novo) # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
```

Cria uma cópia com vínculo, ou seja sempre que um elemento for criado ou excluído de uma a outra também sofrerá as alterações.

---

### .fromkeys(key, value)

```python
outro = {}.fromkeys('a', 'b')
print(outro) # {'a': 'b'}
print(type(outro)) # <class 'dict'>
```

Repare que o primeiro elemento se tornou uma chave e o segundo elemento se tornou o valor desta chave.

```python
usuario = {}.fromkeys(['nome', 'pontos', 'emails', 'profile'], 'desconhecido')

print(usuario)

# {'nome': 'desconhecido', 'pontos': 'desconhecido', 'emails': 'desconhecido', 'profile': 'desconhecido'}

print(type(usuario))

#<class 'dict'>
```

Agora repare que a lista criada para ser a chave foi iterada criando várias chaves e atribuindo o valor desconhecido para todos eles.

Qualquer tipo de iterável pode ser usado no campo key do `.fromkeys`

```python
veja = {}.fromkeys('teste', 'valor')
print(veja)

#{'t': 'valor', 'e': 'valor', 's': 'valor'}
```

A string por ser iterável se transforma nisso, ou seja todas as letras são separadas e atribuídos o valor informado, repare que o último 't' e 'e' não foi criado pois dicionários não respeitam chaves com nomes iguais.

```python
ultimo = {}.fromkeys(range(1, 11), 'novo')
print(ultimo)

# {1: 'novo', 2: 'novo', 3: 'novo', 4: 'novo', 5: 'novo', 6: 'novo', 7: 'novo', 8: 'novo', 9: 'novo', 10: 'novo'}
```

---

### Criando um dicionário utilizando fromKeys:

A ideia aqui é criar um dicionário onde as chaves receberá uma string que será padrão e um número de um range:

```python
dicionario = {'cliente1': 'desconhecido', 'cliente2': 'desconhecido', 'cliente3': 'desconhecido'}
```

Partindo do pressuposto que conhecemos a quantidade de clientes que teremos, vamos utilziar o range, para fazer os números:

```python
>>> dicionario = {}.fromkeys([f'cliente{n}' for n in range(1, 5)], 'desconhecido')

>>> dicionario
{'cliente1': 'desconhecido', 'cliente2': 'desconhecido', 'cliente3': 'desconhecido', 'cliente4': 'desconhecido'}
```

#dictmethods #dicionáriométodos

---

## Adicionar elementos:

```python
receita = {'jan': 100, 'fev': 120, 'mar': 300}
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300}
```

### Forma 1: (mais comum)

```python
receita['abr'] = 350
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350}
```

### Forma 2: (utilizando .update)

```python
novo_dado = {'mai': 500}
receita.update(novo_dado)
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500}
```

É igual a:

```python
receita.update({'jun': 350})
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 500, 'jun': 350}
```

## Atualizando dados no Dict:

### Forma 1:

```python
receita['mai'] = 550
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 550, 'jun': 350}
```

### Forma 2:

```python
receita.update({'mai': 600})
print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 350, 'mai': 600, 'jun': 350}
```

Se observarmos as formas que são possíveis de atualizar um dado de determinada chave, podemos concluir que chaves repetidas NÃO são possíveis.

## Remover itens em Dict:

### .pop(k, v)

k = chave, v = valor

>[!alert] 
>Importante salientar que os dicionários, por serem uma "lista" de itens sem ordem o método pop precisa ter inserido entre os parênteses a chave que se deseja remover.

```python
receita.pop('mar')
print(receita)

# {'jan': 100, 'fev': 120, 'abr': 350, 'mai': 600, 'jun': 350}
```

Ao remover um objeto utilizando o pop, ele sempre retorna o valor removido, ou seja é possível lançar ele em uma variável para ser utilizado depois.

Se a chave informada não existir um `KEYERROR` será retornado.

Apesar do erro ocasionado se a chave mencionada não existir, há uma maneira de evitar o erro criando um valor padrão:

```python
receita = {'jan': 100, 'fev': 120, 'mar': 300}

jan = receita.pop('jan')
print(jan) # 100

abr = receita.pop('abr', 0)
print(abr) # 0
```

Repare que mesmo que a chave `abr` não exista dentro do dicionário, ao chamar o pop e além da chave, um parâmetro como valor for passado após a vírgula, o sistema irá resultar no parâmetro e não em erro.

É possível utilizar o parâmetro somente como segurança, e se a chave existir dentro do dicionário em questão o parâmetro será ignorado e o valor da chave dentro do dicionário será retornado:

```python
fev = receita.pop('fev', 0)
print(fev)

# 120
```

### .del d[k]

d = dicionário

k = chave

```python
del receita['fev']
print(receita)

# {'jan': 100, 'abr': 350, 'mai': 600, 'jun': 350}
```

Se a chave informada não existir um `KEYERROR` será retornado.

Neste caso o valor removido não é retornado, é diretamente excluído.

### .popitem()

Remove o último de forma arbitrária o último item do dicionário e retorna uma tupla contendo a chave e o valor removido:

```python
receita = {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 200, 'mai': 400, 'jun': 350}

print(receita)

# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 200, 'mai': 400, 'jun': 350}

random = receita.popitem()
print(random)
print(receita)

# ('jun', 350)
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 200, 'mai': 400}

random = receita.popitem()
print(random)
print(receita)

# ('mai', 400)
# {'jan': 100, 'fev': 120, 'mar': 300, 'abr': 200}
```

>[!alert]
>.popitem em dicionário vazio causa `KeyError`

---

## Dictionary Comprehension

### Definição:

O príncipio do dictionary comprehension é o mesmo do list comprehension.

Para criarmos uma lista:

-   lista = [1, 2, 3, 4]

Para criarmos uma tupla:

-   tupla = (1, 2, 3, 4)

**Para criarmos um conjunto:**

-   conjunto {1, 2, 3, 4}

**Para criarmos um dicionário:**

-   dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

### Sintaxe:

{chave:valor for valor in iterável}

### Exemplos:

#### Exemplo 1:

Elevar os valores de um dicionário ao quadrado:

```python
>>> numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

>>> quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

>>> print(quadrado)

{'a': 1, 'b': 4, 'c': 9, 'd': 16, 'e': 25}
```

#### Exemplo 2:

A partir de uma LISTA, criaremos um dicionário com os valores da lista ao quadrado e utilizaremos como chaves deste resultado da potenciação os próprios números da lista:

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> quadrados = {valor: valor ** 2 for valor in numeros}

>>> print(quadrados)

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

#### Exemplo 3:

A partir de 2 iteráveis (uma string e uma lista) criaremos um dicionário utilizando cada caractere da string como chave e cada elemento da lista como valor:

```python
>>> chaves = 'abcde'
>>> valores = [1, 2, 3, 4, 5]

>>> mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

>>> print(mistura)

{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
```

#### Exemplo 4:

Criaremos um dicionário a partir de uma lista de números, o elemento desta lista será usado como chave, além disso faremos uma condicional para determinar os valores de cada chave, onde se o resultado do módulo do elemento da lista for igual a 0, então o valor desta chave será 'par', se não será 'ímpar':

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
>>> print(res)
```

#dictcomprehension

---

# Default Dict
No processo natural de utilização de um dicionário, buscar um valor de uma chave inexistente resulta em um `KeyError`.

Com o `defaultdict` é possível criar um dicionário utilizando um valor 'default' (padrão) que será utilizado sempre que não houver um valor definido a uma chave. Para isso utiliza-se um `lambda`

Uma outra diferença é que sempre que tentarmos acessar o valor de uma chave inexistente, o Default Dict criará automaticamente está chave e o valor default será atribuído.

Da mesma forma que o `Counter`, o `defaultdict` também precisa ser importado:

```python
>>> from collections import defaultdict
```

Aqui estamos criando um dicionário que recebera como valor padrão uma expressão lambda com valor 0, ou seja toda chave sem valor que for criada receberá como padrão o valor 0:

```python
>>> dicionario = defaultdict(lambda: 0)
```

Nesta etapa adicionamos a chave 'curso' recebendo como valor 'Programação em Python: Essencial' no dicionário e imprimimos o mesmo:

```python
>>> dicionario['curso'] = 'Programação em Python: Essencial'
>>> print(dicionario)

defaultdict(<function <lambda> at 0x00CECEC8>, {'curso': 'Programação em Python: Essencial'})

```

Repare que o primeiro elemento do dicionário é uma função, após ela, começa o dicionário em si com os pares chave valor conforme configurado no início.

Agora pedimos para imprimir o valor de uma chave que não existe em nosso dicionário:

```python
>>> print(dicionario['outro'])

0
```

O valor retorna 0 conforme configurado no início utilizando o `defaultdict` e uma função lambda

Aqui imprimimos novamente o dicionário:

```python
>>> print(dicionario)

defaultdict(<function <lambda> at 0x00CECEC8>, {'curso': 'Programação em Python: Essencial', 
'outro': 0})
```

Repare que agora além da função e do primeiro par de elemento, temos um segundo com chave 'outro' e valor 0.

#defaulddict

---

# Ordered Dict
Em um dicionário a ordem de inserção de dados não é garantida que será seguida quando o dicionário for chamado:

```python
>>> my_books = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> your_books = {'c': 3, 'd': 4, 'a': 1, 'e': 5, 'b': 2}
```

Entendendo a diferença de `OrderedDict` e `Dict`

Primeiro vamos comparar dois dicionários comuns com chaves e valores iguais, porém ordenados diferente:

```python
>>> print(my_books == your_books)

True
```

Repare que a comparação se os dois dicionários são iguais retorna verdadeiro, podemos concluir que não importa a ordem, chave e valores sendo iguais os dois dicionários então são iguais.

Agora comparando dois `OrderedDict` com mesmas chaves e valores porém com ordem diferente:

```python
>>> my_books = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
>>> your_books = OrderedDict({'c': 3, 'd': 4, 'a': 1, 'e': 5, 'b': 2})

print(my_books == your_books)

False
```

Aqui o resultado é falso, pois para o `OrderedDict` não só a chave e valores precisam ser iguais como a ordem em que se encontram também.

O OrderedDict é concebido por:

1.  Palavra reservada `OrderedDict`
2.  Parênteses
3.  Chaves
4.  Pares de chaves e valor separados por vírgula entre cada par e dois ponto entre a chave e o valor.

```python
>>> my_books = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
```

#ordereddict

## Médotos ordered dict
### .move_to_end(_key, last=True_)

Com essa função é possível mover o elemento que quiser para o final do dicionário, basta informar a chave. O atributo last pode ser omitido, se assim for subentende-se que é verdadeiro. Caso o atributo last receba False no lugar de True, a chave escolhida será movida para o começo:

```python
>>> from collections import OrderedDict

>>> my_books = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

>>> my_books.move_to_end('a', last=True)
>>> print(my_books)

OrderedDict([('b', 2), ('c', 3), ('d', 4), ('e', 5), ('a', 1)])

>>> my_books.move_to_end('e', last=False)
>>> print(my_books)

OrderedDict([('e', 5), ('b', 2), ('c', 3), ('d', 4), ('a', 1)])
```

### .popitem(_last=True_)

Essa função também presente no dicionário comum recebe uma nova atribuição no `OrderedDict`, com o atributo `last`, se `last` é igual a `True`, o pop remove e retorna o último par de elemento (chave e valor) seguindo a regra LIFO (last in first of - último que entra primeiro que sai), se `last` recebe o valor `False` o pop remove o primeiro par de elemento (chave e valor) do dicionário conforme o FIFO (first in first of - primeiro que entra primeiro que sai):

```python
>>> from collections import OrderedDict

>>> my_books = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

>>>lifo = my_books.popitem()
>>> print(lifo)
>>> print(my_books)

('e', 5)
OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
```

```python
>>> from collections import OrderedDict

>>> my_books = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

>>> lifo = my_books.popitem(last=False)
>>> print(lifo)
>>> print(my_books)

('a', 1)
OrderedDict([('b', 2), ('c', 3), ('d', 4), ('e', 5)])
```

