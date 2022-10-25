# Introdução:

Retorna um iterador de tuplas, que agrega elementos de cada um dos iteráveis passados como argumento:

O resultado é um objeto do tipo zip, que ao ser iterado temos acesso aos seus dados, por exemplo utilizando uma lista, nesse caso teremos uma lista com tuplas como elementos. Cada tupla contém o primeiro elemento do primeiro iterável passado como argumento e o primeiro elemento do segundo iterável passado como argumento também, e assim por diante.

O iterador é parado quando a menor entrada iterável é esgotada.

## Sintaxe:

```python
zip(nome_iterável_1, nome_iterável_2, ..., nome_iterável_n) 
```

Exemplo:

```python
>>> lista1 = [1, 2, 3]
>>> lista2 = [4, 5, 6]

>>> zip1 = zip(lista1, lista2)
```

## Resultado (retorno):

O zip se comporta como o map, filter e generator o seu resultado é um objeto na memória:

```python
>>> print(zip1)
>>> print(type(zip1))

<zip object at 0x000002089360A5C0>
<class 'zip'>
```

É necessário transformar este objeto em um iterável para ter acesso aos dados nele armazenado:

```python
>>> print(list(zip1))

[(1, 4), (2, 5), (3, 6)]
```

A partir deste momento, não teremos mais acesso aos dados, apenas um iterável vazio:

```python
>>> print(list(zip1))

[]
```

## Exemplos

### Exemplo 1:

Utilizando mais de 2 iteráveis como argumento:

```python
>>> lista1 = [1, 2, 3]
>>> lista2 = [4, 5, 6]

>>> zip1 = zip(lista1, lista2, 'abc')

>>> print(list(zip1))

[(1, 4, 'a'), (2, 5, 'b'), (3, 6, 'c')]
```

### Exemplos 2:

Como dito anteriormente, o zip itera em tuplas os elementos de dois ou mais iteráveis até o momento em que o menor iterável passado como argumento é esgotado. Isso significa que caso passemos um iterável com 3 elementos e outro com 4 elementos o resultado excluirá o último elemento do 4 iterável:

```python
>>> lista1 = [1, 2, 3]
>>> lista2 = [4, 5, 6]
>>> lista3 = [7, 8, 9, 10, 11]

>>> zip1 = zip(lista1, lista2, lista3)

>>> print(list(zip1))

[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
```

>[!important]
>Observe que os elementos '10' e '11' da lista 3 (iterável) não foram considerados no resultado deste zip, não importa a posição em que os iteráveis sejam passados como argumento no zip. Sempre será encerrado no momento em que o menor for esgotado.

### Exemplo 3:

Podemos utilizar diferentes iteráveis entre si com o zip:

```python
>>> tupla = (1, 2, 3)
>>> lista = [4, 5, 6]
>>> conjunto = {7, 8, 9}
>>> dicionario = {'a': 10, 'b': 11, 'c': 12}
>>> texto = 'abc'

>>> zippando = zip(tupla, lista, conjunto, dicionario.values(), texto)

>>> print(list(zippando))

[(1, 4, 8, 10, 'a'), (2, 5, 9, 11, 'b'), (3, 6, 7, 12, 'c')]
```

>[!Note]
>Só lembrar que para dicionários é importante informar qual dado entre o par chave-valor deseja se iterar. Nesse caso pedimos os valores utilizando o `.value()`

# Desempacotando um zip:

Utilizando um * antes do iterável que contenha tuplas como elementos, podemos fazer a descompactação dos elementos e transformar em grupos de tuplas dentro de um iterável:

```python
>>> dados = [(1, 4), (2, 5), (3, 6)]

>>> print(list(zip(*dados)))

[(1, 2, 3), (4, 5, 6)]
```

Podemos ir além e separar cada tupla em uma iterável que será passado para duas variáveis diferentes:

Aqui descompactaremos os valores, criando 2 variáveis que receberam os elementos um uma lista cada:

```python
>>> dados = [(1, 4), (2, 5), (3, 6)]

>>> x, y = zip(*dados)

>>> print(list(x))
>>> print(list(y))

[1, 2, 3]
[4, 5, 6]
```

## Exemplos complexos:

### Exemplo 1:

A partir de 3 listas, 2 com notas de prova de alunos e uma com o nome de cada aluno, criaremos um dicionário que conterá como chave o nome do aluno e para o valor a maior nota entre as duas listas de notas, para isso usaremos o zip e o max:

```python
>>> prova1 = [80, 91, 78]
>>> prova2 = [98, 89, 53]
>>> alunos = ['maria', 'pedro', 'carla']
```

Qual é o caminho percorrido pelo código para chegar ao resultado esperado:

1.  Faremos o zip dos dados onde primeiro virá a lista de alunos em seguida as listas de notas, a partir das listas criadas;
2.  Em seguida usaremos um loop `for` para iterar cada elemento do zip, iterando cada elemento ou seja, cada tupla criada pelo zip;
3.  Pediremos para o dicionário criar como chave o dado de índice 0, conforme colocamos como sendo o primeiro elemento do zip;
4.  Como valor que será recebido para cada chave, faremos o max entre os dados no índice 1 e índice 2 que são as notas.

```python
>>> final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
```

#### Visualizando no terminal:

```python
>>> prova1 = [80, 91, 78]
>>> prova2 = [98, 89, 53]
>>> alunos = ['maria', 'pedro', 'carla']

>>> list(zip(alunos, prova1, prova2))

[('maria', 80, 98), ('pedro', 91, 89), ('carla', 78, 53)]

# Dessa forma visualizamos que a partir deste momento o loop for faz a iteração dos elementos e a partir do momento que indicamos quais dados estarão em quais locais,
# como chave e valor, criamos o dicionário.
```

#### Resultado:

```python
>>> print(final)

{'maria': 98, 'pedro': 91, 'carla': 78}
```

#### Podemos utilizar o map:

```python
>>> final2 = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

>>> print(dict(final2))

{'maria': 98, 'pedro': 91, 'carla': 78}
```

Aqui criamos o seguinte:

1.  Criamos um map onde receberá os valores zipados das listas de nota, e através de uma função lambda, irá retornar o valor máximo.
2.  A partir deste momento, criamos um novo zip que receberá alunos e o resultado deste map que gerou um iterável apenas com as notas máximas de cada aluno.
3.  O resultado deste último zip nós transformamos em um dicionário e imprimimos

#### Visualizando o passo a passo no terminal:

Criamos um zip com os valores de prova 1 e prova 2:

```python
>>> list(zip(prova1, prova2))

[(80, 98), (91, 89), (78, 53)]
```

A partir dele, utilizamos um map, para poder utilizar uma função integrada max para cada dado que será iterado por conta do map:

```python
>>> list(map(lambda nota: max(nota), zip(prova1, prova2)))

[98, 91, 78]
```

Agora utilizando o zip novamente iremos agrupar os valores da lista de nomes e os valores resultantes do map, esse é o resultado transformado em lista:

```python
>>> list(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))

[('maria', 98), ('pedro', 91), ('carla', 78)]
```

Como só temos tuplas com 2 valores, podemos facilmente transformar em um dicionário e tai nosso dicionário contendo os nomes dos alunos e suas notas mais altas:

```python
>>> dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))

{'maria': 98, 'pedro': 91, 'carla': 78}
```

#zip