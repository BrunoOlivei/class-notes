# Max( )

Retorna o maior valor em um iterável ou o maior de dois ou mais elementos

```python
>>> lista = [1, 8, 4, 99, 34, 129]
>>> print(max(lista))

129

>>> tupla = (1, 8, 4, 99, 34, 129)
>>> print(max(tupla))

129

>>> conjunto = {1, 8, 4, 99, 34, 129}
>>> print(max(conjunto))

129

>>> dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
>>> print(max(dicionario))
>>> print(max(dicionario.values()))

f
129
```

<aside> ♻️ Relembrando como funciona o max em um iterável. Vale ressaltar também que o max utilizado em um dicionário trará a chave do maior valor, porém ao implementar `.values()` podemos acessar o maior valor.

</aside>

É possível passar elementos direto a função max( ):

```python
>>> val1 = int(input('Informe o primeiro valor: '))
>>> val2 = int(input('Informe o segundo valor: '))

32
12

print(max(val1, val2))

32
```

Podemos fazer também da seguinte forma:

Max( ) aceita quantos elementos necessários:

```python
>>> print(max(13, 67, 19, 54, 99, 102, 5, 68, 43, 86, 27, 1, 22))

102
```

Max( ) não serve somente para números inteiros:

Podemos utilizar com strings:

```python
>>> print(max('a', 'ab', 'abc'))
>>> print(max('a', 'b', 'c', 'v'))
>>> print(max('leão', 'zebra', 'macaco', 'bisao', 'girafa', 'elefante', 'hipopotamo'))
>>> print(max('Bruno Oliveira'))

abc
v
zebra
v
```

Podemos utilizar também para ponto flutuante:

```python
>>> print(max(3.145, 1.32, 6.43, 7.9875))

7.9875
```

---

# Min( )

Retorna o menor valor de um iterável ou o menor entre dois ou mais elementos:

Assim como o max porém resultado contrário:

```python
>>> lista = [1, 8, 4, 99, 34, 129]
>>> print(min(lista))

1

>>> tupla = (1, 8, 4, 99, 34, 129)
>>> print(min(tupla))

1

>>> conjunto = {1, 8, 4, 99, 34, 129}
>>> print(min(conjunto))

1

>>> dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
>>> print(min(dicionario))
>>> print(min(dicionario.values()))

a
1
```

Min( ) aceita quantos elementos necessários:

```python
>>> print(max(13, 67, 19, 54, 99, 102, 5, 68, 43, 86, 27, 1, 22))

1
```

É possível passar elementos direto a função min( ):

```python
>>> val1 = int(input('Informe o primeiro valor: '))
>>> val2 = int(input('Informe o segundo valor: '))

32
12

print(min(val1, val2))

12
```

Min( ) não serve somente para números inteiros:

Podemos utilizar com strings, no caso das strings o "Bruno Oliveira" o resultado será espaço, e não a letra 'a'

```python
>>> print(min('a', 'ab', 'abc'))
>>> print(min('a', 'b', 'c', 'v'))
>>> print(min('leão', 'zebra', 'macaco', 'bisao', 'girafa', 'elefante', 'hipopotamo'))
>>> print(min('Bruno Oliveira'))

a
a
bisao

```

Podemos utilizar também para ponto flutuante:

```python
>>> print(min(3.145, 1.32, 6.43, 7.9875))

1.32
```

---

# key=

O key do max e do min de acordo com a documentação do python, recebe uma função, sejá ela uma função definida ou um lambda

## Exemplos:

### Exemplo 1:

Como visto no exemplo de animais do continente africano, o max e o min trouxeram o menor elemento na ordem alfabética, ou seja o que começa com z ou mais próximo disso para o max e o que começa com a ou o mais próximo disso para o min:

Porém é possível buscar pelos elementos que possuem maior tamanho, por exemplo quantidade de letras:

```python
>>> animais = ['leão', 'zebra', 'macaco', 'bisao', 'girafa', 'elefante', 'hipopotamo']

>>> print(max(animais, key=lambda animal: len(animal)))

hipopotamo
```

Com o min( ):

```python
>>> print(min(animais, key=lambda animal: len(animal)))

leão
```

### Exemplo 2:

Utilizando o max e o min para encontrar em uma lista com dicionários onde têm o título da música e a quantidade de vezes que ela foi tocada:

```python
>>> musicas = [
		    {"titulo": "Thunderstruck", "tocou": 3},
		    {"titulo": "Dead Skin Mask", "tocou": 2},
		    {"titulo": "Back in Black", "tocou": 4},
		    {"titulo": "Too old to rock'in roll, to young to die", "tocou": 32}

>>> print(max(musicas, key=lambda musica: musica['tocou']))
>>> print(min(musicas, key=lambda musica: musica['tocou']))

{'titulo': "Too old to rock'in roll, to young to die", 'tocou': 32}
{'titulo': 'Dead Skin Mask', 'tocou': 2}
```

Relembrando que é possível trazer somente o valor de uma chave:

Basta acrecentar a chave que deseja imprimir do objeto após os parênteses fechados do max ou min:

```python
>>> print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
>>> print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])

Too old to rock'in roll, to young to die
Dead Skin Mask
```

# Uso de parâmetros default em Max e Min:

O parâmetro default especifica um objeto a ser devolvido se o iterável fornecido estiver vazio. Com o parâmetro nomeado default definido, sempre que houver um iterável vazio o retorno de max ou min será o parâmetro padrão.

```python
>>> lista = [1, 3, 5, 6, 7]
>>> teste = []

>>> print(max(teste, default='No Elements'))
>>> print(max(lista, default='No Elements'))

No Elements
7

>>> print(min(teste, default='No Elements'))
>>> print(min(lista, default='No Elements'))

No Elements
1
```

Também pode ser feito da seguinte forma:

Desde que o elemento que será retornado caso o iterável passado esteja vazio, seja único ou esteja em um iterável:

```python
>>> print(max(teste or ['No Elements']))
>>> print(max(lista or ['No Elements']))
```

#min #max
