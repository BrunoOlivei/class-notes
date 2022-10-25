# Counter - High-performance Container Datatypes

## Introdução

High-performance Container Datatypes

Counter recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como valor e quantidade de ocorrências desse elemento:

Pode ser usado qualquer iterável

Primeiro é necessário fazer a importação desta funcionalidade, para isso:

```python
from collections import Counter
```

Veja um Counter em ação:

```python
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Aqui criamos uma lista com diversos elementos, inclusive repetindo.

res = Counter(lista)

# Aqui estamos criando uma váriavel que recebera o Counter da lista criada
# anteriormente.

>>> print(type(res))
<class 'collections.Counter'>

>>> print(res)
Counter({1: 5, 3: 5, 2: 4, 4: 3, 5: 3, 45: 2, 66: 2, 43: 1, 34: 1})

'''
Podemos observar que foi criado um dicionário utilizando cada elemento da
lista como chave, e como valor atribuido a cada chave a quantidade de vezes
em que o elemento foi repetido na lista, ou seja, o elemento 1 ocorreu 5
vezes na lista o elemento 3 também 5 vezes, o elemento 2, 4 vezes e assim
por diante.
'''
```

Outra utilização, lembrando que strings são dados iteráveis:

```python
>>> print(Counter('Bruno Goncalves Oliveira'))

Counter({'r': 2, 'n': 2, 'o': 2, ' ': 2, 'a': 2, 'l': 2, 'v': 2, 'e': 2, 
	'i': 2, 'B': 1, 'u': 1, 'G': 1, 'c': 1, 's': 1, 'O': 1})
```

Relembrando, o python é case sensitive ou seja ele diferencia caracteres em maiúsculo e minúsculo, sendo assim mesmo que a letra 'o' ocorra em minúsculo e maiúsculo a linguagem vai separá-los.

Aqui podemos observar que o Counter criou uma chave para cada letra da string, eliminando as repetições e como valor o número de ocorrências de cada caractere da string.

---

Utilizando um texto grande:

```python
>>>texto = """À medida que missões como os telescópios espaciais Hubble, TESS e Kepler, da Nasa, continuam 
a fornecer vislumbres sobre as propriedades dos exoplanetas (planetas ao redor de outras estrelas), 
os cientistas cada vez conseguem descobrir como esses planetas se parecem, do que são feitos e se poderiam 
ser habitáveis. 
Em um novo estudo, pesquisadores da Universidade Estadual do Arizona e da Universidade de Chicago (EUA) afirmam
que alguns exoplanetas ricos em carbono, nas circunstâncias certas, poderiam ser feitos de diamantes e sílica. 
"""

>>>palavras = texto.split()

>>>res = Counter(palavras)

>>>print(res)

Counter({'e': 4, 'que': 3, 'da': 3, 'de': 3, 'como': 2, 'os': 2, 'exoplanetas': 2, 'se': 2, 'do': 2, 'feitos': 2, 'poderiam': 2,
 'ser': 2, 'Universidade': 2, 'À': 1, 'medida': 1, 'missões': 1, 'telescópios': 1, 'espaciais': 1, 'Hubble,': 1, 'TESS': 1, 
'Kepler,': 1, 'Nasa,': 1, 'continuam': 1, 'a': 1, 'fornecer': 1, 'vislumbres': 1, 'sobre': 1, 'as': 1, 'propriedades': 1, 
'dos': 1, '(planetas': 1, 'ao': 1, 'redor': 1, 'outras': 1, 'estrelas),': 1, 'cientistas': 1, 'cada': 1, 'vez': 1, 
'conseguem': 1, 'descobrir': 1, 'esses': 1, 'planetas': 1, 'parecem,': 1, 'são': 1, 'habitáveis.': 1, 'Em': 1, 'um': 1, 
'novo': 1, 'estudo,': 1, 'pesquisadores': 1, 'Estadual': 1, 'Arizona': 1, 'Chicago': 1, '(EUA)': 1, 'afirmam': 1, 'alguns': 1, 
'ricos': 1, 'em': 1, 'carbono,': 1, 'nas': 1, 'circunstâncias': 1, 'certas,': 1, 'diamantes': 1, 'sílica.': 1})
```

Inicialmente cria-se uma lista com as palavras dentro da `string` texto utilizando a função `split`, a partir de uma variável para receber a lista com cada palavra do texto, o `Counter` cria um `dict` e utiliza cada palavra como chave (key) e a quantidade de ocorrências no texto como valor (value)

---

`Counter` também pode ser criado direto, exemplo:

```python
>>> c = Counter('gallahad')

>>> print(c)

Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
```

---

```python
>>> c = Counter({'red': 4, 'blue': 2})

>>> print(c)

Counter({'red': 4, 'blue': 2})
```

---

```python
>>> c = Counter(cats=4, dogs=8)

>>> print(c)

Counter({'dogs': 8, 'cats': 4})
```

Interessante reparar que a estrutura de um Counter é:

1.  Palavra-chave `Counter`
2.  Parênteses (
3.  Chaves (dicionário) {
4.  Chave
5.  Dois pontos
6.  Valor da chave
7.  Vírgula
8.  Fechamento das Chaves (dicionário) }
9.  Fechamento dos Parênteses )

Por se tratar de um tipo de dado sem índice ele utiliza dos artifícios do dicionário (chave: valor) para apresentar seus dados, que são chaves representando os elementos de uma dado prévio que seja iterável e como valor a quantidade de vezes que apareceu (ocorreu).

#counter

---

## Funções e métodos com Counter

### .elements()

`.elements` é uma função que sozinha retorna um objeto de cadeia para ferramentas iteráveis, é basicamente um container pseudo iterável cujo os elementos nele inseridos podem ser usados QUANDO, houver uma ferramenta iterável, exemplo de ferramenta é o `sorted`, `enumerate` ou estruturas `for in`:

Em si ela retorna uma lista com todos os elementos inclusive repetidos as quantidades de vezes conforme o Counter, baseados na ordem que foram encontrados na primeira vez.

```python
>>> from collections import Counter

>>> lista = ['a', 'a', 'c', 'd', 'd', 'e', 'f', 'f', 'g', 'h', 'h', 'h', 'a', 'b', 'c', 'c']

>>> res = Counter(lista)

>>> print(type(res))

<class 'collections.Counter'>
```

Utilizando o `sorted` para ordenar por ordem crescente todos os elementos:

```python
>>> print(sorted(res.elements()))

['a', 'a', 'a', 'b', 'c', 'c', 'c', 'd', 'd', 'e', 'f', 'f', 'g', 'h', 'h', 'h']
```

Utilizando o enumerate para numerar cada elemento 1 a 1:

```python
>>> nova = list(enumerate(res.elements()))
>>> print(nova)

[(0, 'a'), (1, 'a'), (2, 'a'), (3, 'c'), (4, 'c'), (5, 'c'), (6, 'd'), (7, 'd'), 
(8, 'e'), (9, 'f'), (10, 'f'), (11, 'g'), (12, 'h'), (13, 'h'), (14, 'h'), (15, 'b')]
```

Utilizando uma estrutura `for in`:

```python
>>> for i in res.elements():
>>>    print(i, end=" ")

a a a c c c d d e f f g h h h b
```

### .most_common(n)

Esta função retorna os elementos mais comuns, ou seja, que ocorrem mais baseados no `Counter`, o 'n' é a quantidade de elementos que você deseja receber como o mais comum.

Exemplo: os 3 mais comuns = `.most_common(3)`

```python
>>> print(res.most_common(2))

[('a', 3), ('c', 3)]
```

### .subtract(_iterable-or-mapping_)

Essa função subtrai os valores dos elementos de 2 Counters:

```python
>>> from collections import Counter

>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)

>>> c.subtract(d)
>>> print(c)

Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```

### .update(_iterable-or-mapping_)

Essa função soma os valores dos elementos de 2 Counters:

```python
>>> from collections import Counter

>>> c = Counter(a=4, b=2, c=0, d=-2)
>>> d = Counter(a=1, b=2, c=3, d=4)

>>> c.update(d)
>>> print(c)

Counter({'a': 5, 'b': 4, 'c': 3, 'd': 2})
```

### .values(_self_)

Esta função traz os valores do dicionário criado pelo `Counter`

```python
>>> print(d.values())

dict_values([1, 2, 3, 4])

```

Com ele também é possível usar o sum, min e mas para realizar operações ou encontrar os valores mínimos e máximos:

```python
>>> print(sum(d.values()))
>>> print(min(d.values()))
>>> print(max(d.values()))

10
1
4
```

### .clear(_self_)

Como já visto em outros tipos de dados, o `.clear` serve para limpar todos os dados (chave e valor) de um `Counter`

```python
>>> print(d)
>>> d.clear()
>>> print(d)

Counter({'d': 4, 'c': 3, 'b': 2, 'a': 1})
Counter()
```

### list(c)

Cria uma lista com as chaves do `Counter`:

```python
>>> print(list(c))

['a', 'b', 'c', 'd']

>>> who = list(c)
>>> print(who)
>>> print(c)

['a', 'b', 'c', 'd']
Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
```

### set(c)

Cria um conjunto com as chaves do `Counter`:

```python
>>> who = set(c)
>>> print(who)
>>> print(c)

{'b', 'c', 'd', 'a'}
Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
```

### dict(c)

Cria um dicionário comum para o `Counter`:

```python
>>> who = dict(c)
>>> print(who)
>>> print(c)

{'a': 4, 'b': 2, 'c': 0, 'd': -2}
Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
```

### .items(_self_)

Converte para uma lista com pares (elemento, contagem):

```python
>>> print(c.items())

dict_items([('a', 4), ('b', 2), ('c', 0), ('d', -2)])
```

### Counter(dict(_lista de pares_))

Cria um `Counter` baseado na lista de pares, é o inverso do `.items()`:

```python
>>> e = Counter(dict([('a', 4), ('b', 2), ('c', 0), ('d', -2)]))
>>> print(e)

Counter({'a': 4, 'b': 2, 'c': 0, 'd': -2})
```

### .most_common()[:-n-1:-1]

Com os parâmetros utilizados dentro dos colchetes é possível inverter a ordem do `.most_common()` e solicitar os dados menos comuns ou seja que ocorreram menos vezes:

Sendo 'n' o número de itens que você deseja recuperar.

```python
>>> print(c.most_common()[:-1-1:-1])

[('d', -2)]

>>> print(c.most_common()[:-2-1:-1])

[('d', -2), ('c', 0)]
```

### +Counter

Remove as chaves com valores negativos e zerados:

```python
>>> c = +c

Counter({'a': 4, 'b': 2})
```

#counter #countermethods #countermétodos

