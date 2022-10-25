# List (Listas)
Existem diversos métodos e funções que podemos utilizar em listas, para acrescentar ou remover elementos, reordenar, substituir, etc:

```python
>>> lista1 = ['Bruno', 'Laura', 'Giovana', 'Felipe']
>>> lista2 = list('Bruno Oliveira')
>>> lista3 = [1, 45, 54, 23, 32, 15, 89, 65]
>>> lista4 = list(range(1, 11))

>>> print(lista1)
>>> print(lista2)
>>> print(lista3)
>>> print(lista4)

['Bruno', 'Laura', 'Giovana', 'Felipe']
['B', 'r', 'u', 'n', 'o', ' ', 'O', 'l', 'i', 'v', 'e', 'i', 'r', 'a']
[1, 45, 54, 23, 32, 15, 89, 65]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

---

## Operações aritméticas:

Utilizando as funções `sum`, `max`, `min` é possível retornar a soma dos elementos, o elemento com valor máximo, e o elemento com valor mínimo. Enquanto o `len` retorna o tamanho da lista, que nada mais é do que a quantidade de elementos que ela possui.

```python
>>> print(sum(lista4))
>>> print(max(lista4))
>>> print(min(lista4))
>>> print(len(lista4))

55
10
1
10
```

---

## Sinal de Multiplicação '*'

O sinal de multiplicação seguido de um n, retorna uma lista com seus itens repetidos n vezes:

```python
>>> print(lista1 * 2)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Bruno', 'Laura', 'Giovana', 'Felipe']
```

---

# Métodos de Objetos:

Métodos são atributos de instâncias, ou seja, é uma função que pertence a um objeto instância, objetos como listas, possuem seus métodos que podem ou não alterar seu estado, aqui veremos alguns métodos que podem ser utilizado com listas:

Geralmente sua estrutura é o nome da lista seguido por um ponto final e o nome do método com parênteses que podem ou não conter outros parâmetros e valores.

---

## .index(_elemento_)

Este método traz o índice do elemento desejado:

```python
>>> print(lista1.index('Laura'))
>>> print(lista2.index('l'))
>>> print(lista3.index(15))
>>> print(lista4.index(7))

1
7
5
6
```

---

## .append(_elemento_)

Adiciona um e APENAS UM elemento ao final da lista,

```python
>>> lista1.append('Cookie')
>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Cookie']
```

---

## .extend(_iterável_)

Com este método é possível acrescentar mais de 1 elemento a uma lista, desde que o objeto a ser adicionado seja um iterável (ex: strings, lista com números, etc):

```python
>>> lista3.extend([77, 8, 13])
>>> print(lista3)

[1, 45, 54, 23, 32, 15, 89, 65, 77, 8, 13]
```

---

## .insert(_índice, elemento_):

Insere um elemento em uma posição determinada, sua estrutura é índice onde deseja acrescentar o elemento vírgula e um elemento, também só é possível adicionar 1 elemento por vez. Também é possível passar como parâmetro um índice negativo, assim o elemento será adicionado contando de trás para frente:

```python
>>> lista1.insert(1, 'Odin')
>>> print(lista1)

['Bruno', 'Odin', 'Laura', 'Giovana', 'Felipe', 'Cookie']
```

```python
>>> lista1.insert(-1, 'Odin')
>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Odin', 'Cookie']
```

---

## Sinal de Soma:

Com o sinal de soma é possível realizar a concatenação de duas listas:

```python
>>> lista5 = ['Odin', 'Lucifer', 'Lilith', 'Gin']
>>> lista1 = lista1 + lista5
>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Cookie', 'Odin', 'Lucifer', 'Lilith', 'Gin']
```

---

## .remove(_elemento_)

Remove o elemento desejado:

```python
>>> lista3.remove(89)
>>> print(lista3)

[1, 45, 54, 23, 32, 15, 65, 77, 8, 13]
```

---

## .pop(_índice_):

Remove o item do índice informado e o retorna, podendo assim esse elemento ser adicionado em uma nova variável. Caso o índice não seja informado, o pop automaticamente removerá o último elemento da lista:

```python
>>> num = lista3.pop()
>>> print(num)
>>> print(lista3)

13
[1, 45, 54, 23, 32, 15, 65, 77, 8]

```

```python
>>> num = lista3.pop(3)
>>> print(num)
>>> print(lista3)

23
[1, 45, 54, 32, 15, 65, 77, 8, 13]
```

Informar um índice inexistente no método pop causa erro:

```python
>>> num = lista3.pop(11)
>>> print(num)
>>> print(lista3)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 17, in <module>
    num = lista3.pop(11)
IndexError: pop index out of range
```

---

## .clear()

Remove todos os itens de uma lista e a retorna vazia:

```python
>>> lista3.clear()
>>> print(lista3)
>>> print(type(lista3))

[]
<class 'list'>
```

---

## del\[_índice_inicio_:_índice_fim_]

Com essa função embutida é possível limpar toda ou apenas uma parte de uma lista, o índice_inicio e índice_fim indicam a parte que o del irá deletar, começando de um índice e indo até outro, também é possível utilizar índices negativos:

```python
>>> del lista3[:]
>>> print(lista3)

[]
```

```python
>>> del lista3[5:7]
>>> print(lista3)

[1, 45, 54, 23, 32, 77, 8, 13]
```

```python
>>> del lista3[5:]
>>> print(lista3)

[1, 45, 54, 23, 32]
```

---

## .count(elemento)

Esse método conta quantas ocorrências de determinado elemento:

```python
>>> print(lista2.count('i'))

2
```

---

## .sort(_reverse=False_)

Reorganiza a ordem dos elementos de forma crescente, quando o parâmetro reverse é igual a True, a ordem é decrescente. O parâmetro reverse quando não explicitado remete a true, ou seja, ordem crescente:

```python
>>> lista3.sort()
>>> print(lista3)

[1, 8, 13, 15, 23, 32, 45, 54, 65, 77]

>>> lista3.sort(reverse=True)
>>> print(lista3)

[77, 65, 54, 45, 32, 23, 15, 13, 8, 1]
```

---

## .reverse()

Inverte a ordem dos elementos, ele não ordena de forma decrescente, apenas inverte a ordem conforme apresentado.

```python
>>> lista1.reverse()
>>> print(lista1)

['Felipe', 'Giovana', 'Laura', 'Bruno']
```

---

## .copy()

Cria uma cópia superficial da lista:

```python
>>> lista5 = lista1.copy()
>>> print(lista5)

['Bruno', 'Laura', 'Giovana', 'Felipe']

>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe']

>>> lista1.append('Cookie')
>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Cookie']

>>> print(lista5)

['Bruno', 'Laura', 'Giovana', 'Felipe']
```

---

## len(_lista_)

O método len tem diversas utilidades, desde apenas retornar o tamanho da lista até adicionar novos elementos:

Aqui podemos fazer a inserção de um novo elemento ao final da lista.

```python
>>> lista1[len(lista1):] = ['Bacon']
>>> print(lista1)

['Bruno', 'Laura', 'Giovana', 'Felipe', 'Bacon']
```

#python #list #listas #listmethods #listamétodos

---

# Nested List (Listas Aninhadas)

## Introdução:

Em algumas linguagens de programação como C e Java, elas possuem uma estrutura de dados chamadas de arrays.

Essas arrays podem ser dividas em:

-   Unidimensionais (Arrays/Vetores)
-   Multidimensionais (Matrizes)

Porém nestas linguagens sabemos que existem limitações quanto a quantidade de elementos e o tipo de dado que uma array pode receber.

Em Python temos as listas, que são basicamente iguais as Arrays/Vetores que temos em outras linguagens, com a vantagem que elas podem receber uma quantidade extensa de elementos e também qualquer tipo de dado, inclusive numa mesma lista possuir elementos de tipos de dados diferentes.

## Exemplo:

```python
>>> listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3
```

No exemplo acima temos uma lista aninhada, ou seja, uma lista contendo outras 3 listas como elementos. Em algumas linguagens de programação isso é reconhecido como Matriz 3 x 3, dentro de uma array possuem 3 conjuntos que são os elementos da lista global com 3 elementos cada.

Além de ser conhecido por Matriz, é também popularmente categorizado como multidimensional, enquanto em python é chamado de Lista Aninhada - Nested List.

É muito comum em diversas áreas da técnologia.

---

## Como acessar os dados individualmente?

Devemos enxergar as listas aninhadas como um conjunto de dados inseridos em uma tabela contendo colunas e linhas:

Sendo assim fica fácil visualizar o seguinte:

```python
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

Portanto para acessar um valor específico que está em uma lista aninhada, usamos a seguinte sintaxe:

```python
>>> print(listas[0][2])

3
```

O primeiro colchete refere-se a linha enquanto o segundo refere-se a coluna. Dessa forma damos o endereço (linha/coluna) para linguagem de onde se encontra o elemento que queremos:

```python
>>> **print(listas[1][2])

6**
```

Também é possível acessar de tras pra frente usando indices negativos:

```python
>>> print(listas[1][-2])

5
```

---

## Iterando com loops em listas aninhadas:

```python
>>> for lista in listas:
		    for num in lista:
		        print(num)

1
2
3
4
5
6
7
8
9
```

O primeiro for faz a iteração das listas aninhadas e o segundo for faz a iteração de cada elemento das listas aninhadas.

---

## Utilizando List Comprehension em listas aninhadas:

```python
>>> [[print(num) for num in lista] for lista in listas]

1
2
3
4
5
6
7
8
9
```

Repare que o List Comprehension é como utilizar a estrutura de Loop de trás pra frente.

---

## Exemplos:

Utilizando o List Comprehension:

### Exemplo 1:

Criando um tabuleiro/matriz 3 x 3:

```python
>>> tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
>>> print(tabuleiro)

[[1, 2, 3], [1, 2, 3], [1, 2, 3]]
```

### Exemplo 2:

Criando um jogo da velha:

```python
>>> velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
>>> print(velha)

[['O', 'X', 'O'], ['O', 'X', 'O'], ['O', 'X', 'O']]
```

### Exemplo 3:

```python
>>> print([['*' for i in range(1, 4)]for j in range(1, 4)])

[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
```

---

# List Comprehension
## Definição:

Utilizando a list comprehension podemos gerar novas listas com dados processados a partir de outro iterável:

---

## Sintaxe:

[dado for dado in iterável]

### Exemplo 1:

Para cada valor dentro da lista 'numeros', multiplique este valor por 10 e traga todos os resultados em uma nova lista chamada res

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> res = [numero * 10 for numero in numeros]

>>> print(res)

[10, 20, 30, 40, 50]
```

### Exemplo 2:

Para cada elemento da lista numeros, divida cada por 2 e retorne numa nova lista chamada res:

```python
>>> res = [numero / 2 for numero in numeros]
>>> print(res)

[0.5, 1.0, 1.5, 2.0, 2.5]
```

### Exemplo 3:

Função que recebera um valor como argumento e retornará a multiplicação dele com ele mesmo.

Para cada elemento da lista 'numeros', execute a função em cada um e retorne o resultado numa nova lista chamada res:

```python
>>> def funcao(valor):
		    return valor * valor

>>> res = [funcao(numero) for numero in numeros]
>>> print(res)

[1, 4, 9, 16, 25]
```

---

## List Comprehension vs. Loop:

Entendendo o potencial do List Comprehension comparado com o loop:

### Utilizando Loop:

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> numeros_dobrados = []
>>> for numero in numeros:
		    numeros_dobrados.append(numero * 2)

>>> print(numeros_dobrados)

[2, 4, 6, 8, 10]
```

---

### Utilizando List Comprehension:

```python
>>> print([numero * 2 for numero in [1, 2, 3, 4, 5]])

[2, 4, 6, 8, 10]
```

Mesmo resultado para quantidade de códigos diferentes.

#### Exemplo 1:

```python
>>> nome = 'Geek University'

>>> print([letra.upper() for letra in nome])

['G', 'E', 'E', 'K', ' ', 'U', 'N', 'I', 'V', 'E', 'R', 'S', 'I', 'T', 'Y']
```

#### Exemplo 2:

Função caixa_alta: nome recebe a substituição da primeira letra por ela mesma só que maiúscula e retorna o nome.

Para cada elemento na lista 'amigos' execute a função caixa_alta e retorne o resultado em uma nova lista imprimindo-a.

```python
>>> def caixa_alta(nome):
		    nome = nome.replace(nome[0], nome[0].upper())
		    return nome

>>> amigos = ['maria', 'julia', 'pedro', 'guilherem', 'vanessa']

>>> print([caixa_alta(amigo) for amigo in amigos])

['Maria', 'Julia', 'Pedro', 'Guilherem', 'Vanessa']
```

#### Exemplo 3:

```python
>>> print([numero * 3 for numero in range(1, 10)])

[3, 6, 9, 12, 15, 18, 21, 24, 27]
```

#### Exemplo 4:

```python
>>> print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

[False, False, False, True, True, True]
```

#### Exemplo 5:

```python
>>> print([str(numero) for numero in [1, 2, 3, 4, 5]])

['1', '2', '3', '4', '5']
```

Podemos adicionar estruturas condicionais lógicas as nossas List Comprehensions:

## Condicionais lógicas If:

### Exemplo 1:

A partir da lista 'numeros', crie uma lista chamada pares para cada elemento da lista 'numeros' se o módulo de 2 para esse elemento for igual a 0:

```python
>>> numeros = [1, 2, 3, 4, 5, 6]

>>> pares = [numero for numero in numeros if numero % 2 == 0]

>>> print(pares)

[2, 4, 6]
```

### Exemplo 2:

A partir da lista 'numeros', crie uma lista chamada impares para cada elemento da lista 'numeros' se o módulo de 2 para esse elemento for diferente de 0:

```python
>>> impares = [numero for numero in numeros if numero % 2 != 0]

>>> print(impares)

[1, 3, 5]
```

---

## Refatorando os exemplos acima:

-   Qualquer módulo de 2 em número PAR o resultado é 0.
-   0 em Pythons é False.
-   If numero % 2 = como o resultado de módulo % 2 para números pares é igual a 0, então o resultado de If será False.
-   If not quer dizer se não for Verdadeiro, ou seja se retornar 0.

```python
>>> pares = [numero for numero in numeros if not numero % 2]

[2, 4, 6]

```

-   Qualquer módulo de 2 em número PAR o resultado é 0.
-   0 em Pythons é False.
-   If numero % 2 = como o resultado de módulo % 2 para números impares o resultado é 1, então o resultado de If será True
-   Utilizando apenas o if para o módulo de número por 2, quer dizer que para os resultados 1 (True).

```python
>>> impares = [numero for numero in numeros if numero % 2]

[1, 3, 5]
```

### Exemplo 2:

Para cada elemento da lista 'numeros' multiplique por dois o elemento que o resultdo do módulo de 2 for igual a 0, para os elementos diferente disso, dividá cada um por dois:

```python
>>> res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

>>> print(res)

[0.5, 4, 1.5, 8, 2.5, 12]
```

#listcomprehension 

---

## Ordenando lista de dicionários pelo valor

```python
sorted(dataset, key=lambda i: i[<nome_chave>])
```

