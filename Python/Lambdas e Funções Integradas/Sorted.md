# Sorted

Não podemos confundir o `sorted( )` com a função `sort( )` que foi estudado em listas. O `sort( )` só funciona com listas enquanto o `sorted( )` pode ser utilizado com qualquer iterável.

O sorted( ) serve para ordenar os elementos.

Relembrando o sort( ):

```python
>>> lista = [4, 7, 3, 9, 8, 1, 2]

>>> lista.sort()
>>> print(lista)

[1, 2, 3, 4, 7, 8, 9]
```

Como podemos observar o sort( ) altera a própria lista em no qual a função foi chamada.

O sort( ) SOMENTE funciona para listas, tentar utiliza-lo com outros tipos de iteráveis causa um AttributeError, como o exemplo abaixo o objeto tuple não possuí o atributo sort

```python
>>> tupla = (4, 7, 3, 9, 8, 1, 2)

>>> tupla.sort()

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 8, in <module>
    tupla.sort()
AttributeError: 'tuple' object has no attribute 'sort'
```

Enquanto o sorted( ) pode ser utilizado com qualquer iterável INCLUSIVE as listas.

---

# Exemplos:

## Exemplo 1:

Observe o exemplo abaixo, utilizando a função sorted( ) e passando como argumento o iterável números, que é uma lista obtivemos a lista com seus elementos ordenados de forma crescente. Porém ao imprimimos a lista novamente, recebemos como resultado a lista na sua ordem original.

Isso se dá pois a função sorted( ) cria uma nova lista.

```python
>>> numeros = [6, 1, 8, 2]

>>> print(numeros)

[6, 1, 8, 2]

>>> print(sorted(numeros))

[1, 2, 6, 8]

>>> print(numeros)

[6, 1, 8, 2]
```

---

## Exemplo 2:

Podemos utilizar o sorted( ) em qualquer tipo de iterável:

```python
>>> numeros_tupla = (6, 1, 8, 2)
>>> numeros_set = {6, 1, 8, 2}
>>> iteravel_string = 'bruno'

>>> print(sorted(numeros_tupla))

[1, 2, 6, 8]

>>> print(sorted(numeros_set))

[1, 2, 6, 8]

>>> print(sorted(iteravel_string))

['b', 'n', 'o', 'r', 'u']
```

>[!warning] 
>Repare que o resultado, independente do tipo de iterável, todos foram uma nova LISTA com os elementos ordenados por ordem crescente.

Lembrando que o sorted( ) não altera o elemento principal:

```python
>>> print(numeros_tupla)

(6, 1, 8, 2)

>>> print(numeros_set)

{8, 1, 2, 6}

>>> print(iteravel_string)

bruno
```

---

# Conversão do resultado list do sorted( ) para outro tipo de iterável:

Podemos utilizar as funções para transformar algum dado em listas, set, tuplas:

```python
>>> numeros = [6, 1, 8, 2]

>>> print(tuple(sorted(numeros)))

(1, 2, 6, 8)

>>> print(set(sorted(numeros)))

{8, 1, 2, 6}
```

>[!warning]
>Lembrando que o set não possui ordenação.

---

# Parâmetros key em sorted( ):

É possível passar funções como parâmetro key para que no momento da ordenação cada elemento passe por essa função e retorne o resultado desejado:

## Reverse=False

Sua sintaxe é: `sorted(nome_do_iterável, parâmetro_key)`

O Reverse é implícito na função `sorted`, a sua omissão deduz que reverse = False. Porém podemos colocar como valor o booleano `True` para que a ordenação seja feita de forma decrescente:

```python
>>> numeros = [6, 1, 8, 2]

>>> print(sorted(numeros, reverse=True))

[8, 6, 2, 1]
```

## Utilizando o key

```python
>>> usuarios = [
		    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
		    {"username": "carla", "tweets": ["Eu amo meu gato"]},
		    {"username": "jeff", "tweets": []},
		    {"username": "bob123", "tweets": []},
		    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
		    {"username": "gal", "tweets": []},
]
```

```python
>>> print(usuarios)

[{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}, {'username': 'carla', 'tweets': ['Eu amo meu gato']}, {'username': 'jeff', 'tweets': []}, 
{'username': 'bob123', 'tweets': []}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'gal', 'tweets': []}]

>>> print(sorted(usuarios))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    print(sorted(usuarios))
TypeError: '<' not supported between instances of 'dict' and 'dict'
```

>[!error]
>Repare que o sorted( ) não consegue executar sobre esta lista pois não consegue iterar em no dicionário.
>
>`TypeError: '<' not supported between instances of 'dict' and 'dict'`

Para conseguirmos trabalhar com os dicionários precisamos utilizar o parâmetro key do sorted:

```python
>>> print(sorted(usuarios, key=lambda usuario: usuario['username']))

[{'username': 'bob123', 'tweets': []}, {'username': 'carla', 'tweets': ['Eu amo meu gato']}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']},
 {'username': 'gal', 'tweets': []}, {'username': 'jeff', 'tweets': []}, {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}]
```

Ordenando pelo número de tweets de cada usuário:

```python
>>> print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

[{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}, {'username': 'carla', 'tweets': ['Eu amo meu gato']},
 {'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}]
```

---

# Exemplos utilizando o key:

## Exemplo 1:

Uma lista com título da música e a quantidade de vezes em que ela foi tocada:

```python
>>> musicas = [
		    {"titulo": "Thunderstruck", "tocou": 3},
		    {"titulo": "Dead Skin Mask", "tocou": 2},
		    {"titulo": "Back in Black", "tocou": 4},
		    {"titulo": "Too old to rock'in roll, to young to die", "tocou": 32}
]

# Ordena da que menos tocou para a que mais tocou

>>> print(sorted(musicas, key=lambda musica: musica['tocou']))

[{'titulo': 'Dead Skin Mask', 'tocou': 2}, {'titulo': 'Thunderstruck', 'tocou': 3}, {'titulo': 'Back in Black', 'tocou': 4},
 {'titulo': "Too old to rock'in roll, to young to die", 'tocou': 32}]

# Ordena do que mais tocou a que menos tocou:

>>> print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

[{'titulo': "Too old to rock'in roll, to young to die", 'tocou': 32}, {'titulo': 'Back in Black', 'tocou': 4}, {'titulo': 'Thunderstruck', 'tocou': 3},
 {'titulo': 'Dead Skin Mask', 'tocou': 2}]
```

## Exemplo 2:

Ordenando os pacientes por idade:

```python
>>> pacientes = [
			  {'nome': 'Priscila Faria Teixeira Pimenta', 'convenio': 'Sao Lucas Saude', 'idade': 33},
		    {'nome': 'Joseilton Lima Santos', 'convenio': 'Sao Lucas Saude', 'idade': 32},
		    {'nome': 'Raphaela Júlia da Silva', 'convenio': 'Sao Lucas Saude', 'idade': 20},
		    {'nome': 'Agnaldo José Diniz', 'convenio': 'Sao Lucas Saude', 'idade': 57}
]

>>> print(sorted(pacientes, key=lambda paciente: paciente['idade']))

[{'nome': 'Raphaela Júlia da Silva', 'convenio': 'Sao Lucas Saude', 'idade': 20}, {'nome': 'Joseilton Lima Santos', 'convenio': 'Sao Lucas Saude', 'idade': 32},
 {'nome': 'Priscila Faria Teixeira Pimenta', 'convenio': 'Sao Lucas Saude', 'idade': 33}, {'nome': 'Agnaldo José Diniz', 'convenio': 'Sao Lucas Saude', 'idade': 57}]
```

## Exemplo 3:

Utilizando tuplas dentro de listas e ordenando:

No caso de tuplas utilizamos o índice do elemento que desejamos usar para a ordenação.

```python
>>> pacientes = [
		    ('Priscila Faria Teixeira Pimenta', 'Sao Lucas Saude', 33),
		    ('Joseilton Lima Santos', 'Sao Lucas Saude', 32),
		    ('Raphaela Júlia da Silva', 'Sao Lucas Saude', 20),
		    ('Agnaldo José Diniz', 'Sao Lucas Saude', 57)
]

>>> print(sorted(pacientes, key=lambda idade: idade[2]))
```

# Reverse

O argumento opcional reverse se omitido será igual a False ou seja a ordenação seguirá o padrão de ordem crescente, enquanto se o argumento for True a ordenação seguira a ordem decrescente.

#sorted

