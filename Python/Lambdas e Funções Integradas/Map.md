# Introdução:

Quando se trabalha com python para ciência de dados, biotecnologia, inteligência artificial ou até desenvolvimento web. Em todas essas áreas trabalha-se muito com coleção de dados, através do `map`, podemos mapear dados nestas coleções para uma função.

Um exemplo é uma lista com diversos valores e precisa passar estes para uma função o map ajuda exatamente nesse trabalho.

<aside> ⚠️ Não podemos confundir `map` com Mapas (dicionários) `dict`

</aside>

No caso dos Mapas o que é executado é o mapeamento de chave/valor.

**No `map`, o mapeamento é entre valor/funçao**

# Sintaxe:

Map é uma função que recebe 2 valores, o primeiro a função, o segundo um iterável.

```python
>>> map(nome_funçao, nome_iterável)
```

## Demonstração:

Utilizando uma função para calcular a área de um círculo com raio 'r':

```python
>>> import math

>>> def area(r):
		    """Calcula a área de um círculo com raio 'r'."""
		    return math.pi * (r ** 2)

>>> print(area(2))
>>> print(area(5.3))

12.566370614359172
88.24733763933729
```

Imagine ter uma lista com diversos raios:

```python
>>> raios = [2, 5, 7.1, 0.3, 10, 44]
```

### Forma 1: Utilizando o loop for para iteração de cada elemento.

Poderíamos utilizar o loop para iteração destes valores, calcular a área e retornar todos os valores um uma nova lista:

```python
# Primeiro criamos uma lista vazia

>>> areas = [] # Primeiro criamos uma lista vazia
>>> for r in raios: # Aqui o laço for para fazermos a iteração dos elementos da lista raios, onde r será a varíavel criada para receber cada elemento da lista raios
		    areas.append((area(r))) # Com cada elemento da lista raios, o laço retornará o resultado da função area utilizando o valor da varíavel r, e adicionará na
																	# na lista vazia os resultados.

>>> print(areas) # Imprimir a lista vazia que agora recebeu os valores de area baseado na lista de raios.
```

**Resultado:**

```python
[12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
```

### Utilizando o Map:

```python
>>> areas = map(area, raios) # Cria-se uma variável que receberá o resultado da função map.
>>> print(list(areas)) # Imprime uma lista dos resultados que estão armazenados na variável areas.
```

**Resultado:**

```python
[12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
```

>[!warning] 
>O resultado direto da função map é um objeto próprio. Pedir a impressão sem o tratamento dos dados, resulta em algo como isso:

`<map object at 0x000001BF2B4925E0>`

**Exemplo:**

```python
>>> print(areas)

<map object at 0x000001BF2B4925E0>
```

Por isso a necessidade de se tratar o objeto, utilizando por exemplo a função `list`ou `tuple`, etc.

O tipo de dado armazenado na variável areas:

```python
>>> print(type(areas))

<class 'map'>
```

## Entendendo:

O que o map está executando realmente:

O map faz a iteração de cada dado do iterável, que no exemplo acima é uma lista e passa cada dado na função.

```python
>>> print(list(map(area, raios)))

"""
Imprimir o resultado de uma lista que receberá como elemento o resultado do mapeamento do iterável (raios) passsado na função area.
"""
```

<aside> ⚠️ Não é muito comum criar uma função para ser executada dentro de um map, o mais comum é utilizar um lambda no lugar do nome da função:

`>>> map(lambda, nome_iterável)`

</aside>

### Exemplo:

```python
>>> print(list(map(lambda r: math.pi * (r ** 2), raios)))

[12.566370614359172, 78.53981633974483, 158.36768566746147, 0.2827433388230814, 314.1592653589793, 6082.12337734984]
```

## Armazenamento dos dados na memória:

```python
Executando no terminal:

>>> import math
>>> def area(r):
...     return math.pi * (r ** 2)
...
>>> raios = [2, 4, 3.45]
>>> areas = map(area, raios)
>>> areas
<map object at 0x0335A208>
>>> list(areas)
[12.566370614359172, 50.26548245743669, 37.392806559352515]
>>>>>> list(areas)
[]
>>>
```

Podemos observar que a partir do momento que todos o map é executado, e caso o seu resultado não seja armazenado em uma variável, os valores são deletados a partir da primeira utilização.

---

## Recaptulando:

Em map temos:

-   Dados iteráveis: dados = a1, a2, ... an
-   Função: f(x):

Estruturando o map:

map(f, dados)

O map object executara: f(a1), f(a2) f(...), f(an)

Ou seja é necessário ter uma função, seja ela uma função nomeada ou um lambda, e dados iteráveis sejam eles strings, listas, tuplas, etc.

O map irá iterar os dados do iterável e para cada dado executará a função retornando um map object, esse map object poderá ser acessado criando-se uma nova lista, tupla, dicionário etc.

---

## Exemplos:

### Exemplo 1:

Lista com cidades e suas temperaturas em graus célsius ; cada elemento é uma tupla dentro de uma lista:

```python
>>> cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

>>> print(cidades)

[('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londres', 22)]
```

Porém foi solicitado que os dados fossem apresentado em fahrenheit:

<aside> 📌 Fórmula de conversão de célsius para fahrenheit:

f = 9/5 * c + 32

</aside>

Executando:

```python
>>> print(list(map(lambda dados: (dados[0], (9/5) * dados[1] + 32), cidades)))

[('Berlim', 84.2), ('Cairo', 96.8), ('Buenos Aires', 66.2), ('Los Angeles', 78.80000000000001), ('Tokio', 80.6), ('Nova York', 82.4), ('Londres', 71.6)]
```

---

# IMPORTANTE🛑

A função que será utilizada no map somente poderá ter 1 parâmetro.

#map #lambda