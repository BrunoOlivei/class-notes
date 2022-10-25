# Set (Conjunto)

## Introdução

-   Set (conjunto) é um tipo de dado não ordenado.
-   Representado por chaves {} com seus elementos separados por vírgula
-   `set( )` pode ser usado para criação de um conjunto
-   Cada item é único o que quer dizer que não aceita itens duplicados.
-   Cada item é imutável, não pode ser alterado, por conta disso, as funções, `insert, extend, reverse, append, sort` não podem ser executadas.
-   Por ser uma coleção de itens não ordenada, seus elementos não possuem índice.
-   Podem armazenar itens de diferentes tipos ao mesmo tempo

```python
my_set = {1, "Hello", (1, 2, 3), 31.8}
```

É possível passar um conjunto que tenha elementos repetidos, porém o resultado será um conjunto com um item de cada elemento passado:

```python
my_cities = {"Londres", "Nova York", "São Paulo", "Berlim", "Berlim", "Shangai",
             "Tokyo", "Shangai"}
print(my_cities)

# {'Shangai', 'Berlim', 'Tokyo', 'São Paulo', 'Londres', 'Nova York'}
```

Um set não consegue armazenar uma lista:

```python
my_cities = ["Londres", "Nova York", "São Paulo", "Berlim", "Berlim", "Shangai",
             "Tokyo", "Shangai"]

print(my_cities)

# ['Londres', 'Nova York', 'São Paulo', 'Berlim', 'Berlim', 'Shangai', 'Tokyo', 'Shangai']

print(type(my_cities))

# <class 'list'>

my_set = {31, "Bruno", "Oliveira", ["São Paulo", "Belo Horizonte", "Americana"]}
print(my_set)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 6, in <module>
    my_set = {31, "Bruno", "Oliveira", ["São Paulo", "Belo Horizonte", "Americana"]}
TypeError: unhashable type: 'list'
'''

my_cities = {["Londres", "Nova York", "São Paulo", "Berlim", "Berlim", "Shangai",
             "Tokyo", "Shangai"]}
print(my_cities)
print(type(my_cities))
```

Tuplas podem ser passadas para formar um set:

```python
my_tecnologies = {("Java", "Peral", "Ruby")}
print(my_tecnologies)
print(type(my_tecnologies))

# {('Java', 'Peral', 'Ruby')}
# <class 'set'>
```

Os itens do conjunto não podem ser mutáveis, porém o conjunto pode, assim é possível adicionar e remover itens.

```python
my_tecnologies = {"Java", "Peral", "Ruby"}
print(my_tecnologies) # {'Peral', 'Java', 'Ruby'}
print(type(my_tecnologies)) # <class 'set'>

my_tecnologies.add("Python")
print(my_tecnologies) # {'Python', 'Peral', 'Java', 'Ruby'}

```

É possível a iteração dos valores de um conjunto utilizando por exemplo o for:

```python
my_set = {1, "Hello", (1, 2, 3), 31.8}

print(my_set)
print(type(my_set))

# {1, 'Hello', 31.8, (1, 2, 3)}
# <class 'set'>

for valor in my_set:
    print(valor)
# 1
# Hello
# 31.8
# (1, 2, 3)
```


#set #conjuntos 

---

## Métodos

### .add(elemento)

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'São Paulo', 'Belo Horizonte', 'Americana'}

my_cities.add("Rio de Janeiro")
print(my_cities)

# {'Rio de Janeiro', 'São Paulo', 'Belo Horizonte', 'Americana'}
```

OBS:

-   O set não permite que seja adicionado uma lista ao seu conjunto, isso resultará em erro.
-   Adicionar um elemento que já exista no conjunto não resultará em nada
-   O `add` não permite adicionar mais de 1 elemento

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'Americana', 'São Paulo', 'Belo Horizonte'}

my_cities.add("Americana")
print(my_cities)

#{'Americana', 'São Paulo', 'Belo Horizonte'}
```

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'Americana', 'São Paulo', 'Belo Horizonte'}

my_cities.add(["Rio de Janeiro", "Vitória"])
print(my_cities)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 5, in <module>
    my_cities.add(["Rio de Janeiro", "Vitória"])
TypeError: unhashable type: 'list'
'''
```

### .clear( )

A função `clear` elimina todos os elementos de um conjunto, resultando em um conjunto vazio.

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'Belo Horizonte', 'Americana', 'São Paulo'}

my_cities.clear()
print(my_cities) # set()
print(type(my_cities)) # <class 'set'>
```

### .copy( )

Cria uma _shallow copy_ que não altera o conjunto que foi copiado:

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'Americana', 'São Paulo', 'Belo Horizonte'}

cities_backup = my_cities.copy()
my_cities.clear()

print(my_cities) # set()
print(cities_backup) # {'Americana', 'São Paulo', 'Belo Horizonte'}
```

### Deep Copy:

Cria uma cópia vinculada ao conjunto original, toda alteração (seja adição ou remoção de elemento) em um conjunto vai ter o mesmo efeito no outro automaticamente:

```python
my_cities = {'São Paulo', 'Belo Horizonte', 'Rio de Janeiro'}
print(my_cities)

# {'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}

your_cities = my_cities

print(your_cities)

# {'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}

print(type(your_cities))

# <class 'set'>

your_cities.add('Recife')

print(your_cities)

# {'Recife', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}

print(my_cities)

# {'Recife', 'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}
```

### .update(elementos)

Update pode ser utilizado para passar vários elementos que sejam iteráveis:

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'São Paulo', 'Belo Horizonte', 'Americana'}

my_cities.update(["Rio de Janeiro", "Vitória"])
print(my_cities)

# {'Vitória', 'Americana', 'Belo Horizonte', 'São Paulo', 'Rio de Janeiro'}
```

OBS:

-   Para que uma string não seja iterada ao ser passada para o conjunto, usar a sinalização de listas, que são os colchetes [ ] .
-   Caso passe uma string sem os colchetes representando que aqueles elementos são uma lista, o resultado será desastroso:

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'São Paulo', 'Belo Horizonte', 'Americana'}

my_cities.update("Rio de Janeiro", "Vitória")
print(my_cities)

# {'V', 'd', 'o', 't', 'r', 'R', 'ó', 'Belo Horizonte', 'São Paulo', 'J', 'e', 'a', 'Americana', 'i', 'n', ' '}

```

OBS: números inteiros, números flutuantes não são iteráveis, portanto devem ser passados dentro de uma lista.

Listas são iteráveis:

```python
meus_num = {31, 35, 40, 45, 50}
meus_num.update(55, 60, 65)
print(meus_num)

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 8, in <module>
    meus_num.update(55, 60, 65)
TypeError: 'int' object is not iterable
'''
```

### .discard(elemento)

A função discard elimina um determinado elemento da lista, se esse elemento existir, caso não exista nada é resultado.

Nenhum valor é retornado.

Só aceita um elemento por vez.

```python
**my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

my_cities.update(["Rio de Janeiro", "Vitória"])
print(my_cities)

# {'Rio de Janeiro', 'Belo Horizonte', 'São Paulo', 'Americana', 'Vitória'}

my_cities.discard("Rio de Janeiro")
print(my_cities)

# {'Belo Horizonte', 'São Paulo', 'Americana', 'Vitória'}**
```

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'Americana', 'São Paulo', 'Belo Horizonte'}

my_cities.discard("Rio de Janeiro")
print(my_cities)

# {'Americana', 'São Paulo', 'Belo Horizonte'}
```

### .remove(elemento)

É necessário informar o valor na função remove já que o conjunto não possui indice ou chave.

Nenhum valor é retornado.

Mesma função do discard, porém se o elemento que deseja-se ser removido não existe no conjunto, o resultado é um erro:

Só aceita um valor por vez.

```python
my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
print(my_cities)

# {'São Paulo', 'Belo Horizonte', 'Americana'}

my_cities.remove("Americana")
print(my_cities)

# {'São Paulo', 'Belo Horizonte'}

my_cities.remove("Rio de Janeiro")

'''
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/teste.py", line 7, in <module>
    my_cities.remove("Rio de Janeiro")
KeyError: 'Rio de Janeiro'
'''
```

### .pop( )

Essa função remove e retorna um elemento aleatório do conjunto:

```python
>>> my_cities = {"São Paulo", "Belo Horizonte", "Americana"}
>>> my_cities
{'Americana', 'Belo Horizonte', 'São Paulo'}
>>> my_cities.pop()
'Americana'
>>> my_cities
{'Belo Horizonte', 'São Paulo'}
>>>
```

Se o conjunto estiver vazio o resultado será um erro:

```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'pop from an empty set'
```

### .difference( )

Retorna a diferença, ou seja os elementos que não se repetem entre 2 ou mais conjuntos, em um novo conjunto:

```python
x = {"a", "b", "c", "d", "e"}
y = {"b", "c"}
z = {"c", "d"}
print(x.difference(y))

# {'d', 'a', 'e'}
```

É possível realizar a comparação com mais de 2 conjuntos:

```python
print(x.difference(y).difference(z))

# {'e', 'a'}
```

O sinal de menos (subtração) também pode ser usado para ambos os casos:

```python
print(x - y) # {'e', 'a', 'd'}
print(x - y - z) # {'e', 'a'}
```

### .difference_update(variável)

Não retorna nada, apenas atualiza o conjunto inicial eliminando os elementos que se repetem no conjunto que está sendo comparado:

```python
x = {"a", "b", "c", "d", "e"}
y = {"b", "c"}

print(x) # {'d', 'c', 'b', 'a', 'e'}

x.difference_update(y)
print(x) # {'d', 'a', 'e'}
```

Essa função é exatamente igual a seguinte linha de código:

```python
x = x - y
print(x)

# {'d', 'a', 'e'}
```

Onde x recebera a diferença entre os valores do conjunto x e o conjunto y, que resulta na eliminação dos elementos que se repetem.

X então passa a ser um conjunto com os itens que não existem dentro do conjunto y.

### .union(set)

Une os elementos de dois conjuntos distintos:

```python
my_cities = {'São Paulo', 'Belo Horizonte', 'Rio de Janeiro'}
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}

our_cities = my_cities.union(your_cities)

print(my_cities) # {'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'}
print(your_cities) # {'Belo Horizonte', 'Varginha', 'Americana'}

print(our_cities)

# {'Belo Horizonte', 'Rio de Janeiro', 'Americana', 'Varginha', 'São Paulo'}
```

A repetição de elemento é ignorada.

É necessário criar uma nova variável que irá receber a união dos dois conjuntos.

Existe outra forma, que pode ser feita utilizando o caractere pipe |

```python
our_cities = my_cities | your_cities

print(my_cities) # {'Belo Horizonte', 'Rio de Janeiro', 'São Paulo'}
print(your_cities) # {'Belo Horizonte', 'Varginha', 'Americana'}

print(our_cities) 

# {'Belo Horizonte', 'Rio de Janeiro', 'Americana', 'Varginha', 'São Paulo'}
```

### .intersection(set)

Traz como resultado o elemento que se repete em dois conjuntos distintos:

```python
my_cities = {'São Paulo', 'Belo Horizonte', 'Rio de Janeiro'}
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}

same_cities = my_cities.intersection(your_cities)

print(my_cities) # {'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}
print(your_cities) # {'Varginha', 'Americana', 'Belo Horizonte'}

print(same_cities) # {'Belo Horizonte'}
```

Existe outra forma de obter este resultado, utilizando o caractere &:

```python
my_cities = {'São Paulo', 'Belo Horizonte', 'Rio de Janeiro'}
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}

same_cities = my_cities & your_cities

print(my_cities) # {'Rio de Janeiro', 'Belo Horizonte', 'São Paulo'}
print(your_cities) # {'Varginha', 'Americana', 'Belo Horizonte'}

print(same_cities) # {'Belo Horizonte'}
```

### Soma, Valor Máximo, Valor Mínimo e Tamanho

É possível realizar estas operações, desde que os elementos do conjunto sejam números inteiros ou flutuantes, com exceção do tamanho usando a função `len` que serve para qualquer conjunto com qualquer tipo de dado inserido:

```python
s = {1, 2, 3, 4, 5}

print(sum(s)) # 15
print(max(s)) # 5
print(min(s)) # 1
print(len(s)) # 5
```

### .isdisjoint(set)

Método que retorna um `boolean` como resultado, ele compara dois conjuntos distintos verificando se possuem ou não alguma intersecção, se sim retorna `false`, se não retorna `true`

```python
my_cities = {'São Paulo', 'Belo Horizonte', 'Rio de Janeiro'}
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}
other_cities = {'Curitiba', 'Recife', 'Salvador'}

print(my_cities.isdisjoint(your_cities)) # False
print(my_cities.isdisjoint(other_cities)) # True
```

### .issubset(set)

Verifica se um conjunto é um subconjunto de outro, exemplo:

Conjunto 1 {1, 2, 3, 4, 5}

Conjunto 2 {2, 3}

Conjunto 1 é um subconjunto de 2? = Não (false)

Conjunto 2 é um subconjunto de 1? = Sim (true)

O conjunto 2 é um subconjunto de 1 pois seus 2 únicos elementos são encontrados no conjunto 1

```python
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}
other_cities = {'Americana', 'Belo Horizonte'}

print(your_cities.issubset(other_cities)) # False
print(other_cities.issubset(your_cities)) # True
```

Os sinais de maior e menor, também podem ser usados para este fim:

```python
your_cities = {'Americana', 'Varginha', 'Belo Horizonte'}
other_cities = {'Americana', 'Belo Horizonte'}

print(your_cities < other_cities) # False
print(your_cities > other_cities) # True
print(your_cities >= other_cities) # True
```

### .issuperset(set)

Verifica se um conjunto é um conjunto universo de outro, ou seja engloba os elementos que outro conjunto menor também possui exemplo:

Conjunto 1 {1, 2, 3, 4, 5}

Conjunto 2 {2, 3}

Conjunto 1 é um conjunto universo de 2? = Sim (true)

Conjunto 2 é um conjunto universo de 1? = Não (false)

O conjunto 1 é um conjunto universo de 2 o segundo conjunto possui apenas 2 elementos que também estão inseridos no conjunto 1.

```python
my_set = {1, 2, 3, 4, 5}
your_set = {2, 3}

print(my_set.issuperset(your_set)) # True
print(your_set.issuperset(my_set)) # False
```

Também é possível utilizar os sinais de maior e menor para obter este resultado:

```python
print(my_set > your_set) # True
print(my_set < your_set) # False
```

#setmethods #conjuntosmétodos

---

## Set Comprehension

### Definição:

O princípio do set comprehensions é o mesmo da lista, unica diferença é que as regras para set não mudam:

### Exemplo 1:

```python
>>> numeros = {num for num in range(1, 7)}
>>> print(numeros)

{1, 2, 3, 4, 5, 6}
```

### Exemplo 2:

```python
>>> quadrado = {x ** 2 for x in range(10)}
>>> print(quadrado)

{0, 1, 64, 4, 36, 9, 16, 49, 81, 25}
```

### Desafio:

Transformar a estrutura acima para que o resultado seja um dicionário:

```python
>>> quadrado = {x: x ** 2 for x in range(10)}
>>> print(quadrado)

{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
```

### Exemplo 3:

Criando um conjunto a partir de uma string que possui caracteres repetidos:

```python
>>> letras = {letra for letra in 'Geek University'}
>>> print(letras)

{'s', 'e', 'G', 'i', ' ', 'v', 'n', 't', 'y', 'k', 'r', 'U'}
```

Sabemos que conjunto é um tipo de dado NÃO ORDENADO e que não aceira elementos repetidos, por isso o resultado do código acima está fora de ordem e também eliminou os elementos que se repetiam.

#setcomprehension
