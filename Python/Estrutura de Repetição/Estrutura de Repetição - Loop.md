# ITERAR:

Antes de tudo o que significa iterar.

De acordo com dicionário da lingua portuguesa, iterar significa:

>Repetir; tornar a fazer. "iterar", in Dicionário Priberam da Língua Portuguesa [em linha], 2008-2020, [](https://dicionario.priberam.org/iterar)[https://dicionario.priberam.org/iterar](https://dicionario.priberam.org/iterar) [consultado em 04-10-2020].

Alguns sinônimos de iterar são:

> Renovar, secundar, reiterar, repetir, refazer, ecoar, multiplicar, reproduzir, espelhar, reafirmar, rebater, reprisar.

Em programação podemos dizer que iterar seria reproduzir algo, por exemplo:

Uma string 'Keanu Reeves', ao ser iterada nós reproduzimos cada letra desta string.

Uma lista [1, 2, 3, 4, 5] ao ser iterada reproduzimos cada elemento da lista.

As ferramentas de controle de fluxo são perfeitas para este trabalho

## for

O comando for itera sobre uma sequencia, do começo ao fim e na ordem em que aparece

```python
>>> nome = 'Bruno'
>>> lista = [1, 3, 5, 7, 9]
>>> numeros = range(1, 10)

>>> for letra in nome:
		    print(letra)
B
r
u
n
o

>>> for numero in lista:
		    print(numero)
1
3
5
7
9

>>> for numero in range(1, 10):
		    print(numero)
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

Podemos observar que para cada objeto, string, lista, range etc. podemos facilmente reproduzir cada elemento destes objetos.

## Utilidades:

Podemos utilizar esta ferramenta de iteração para executar alguma operação ou condição e apresentar um resultado esperado:

### Exemplo 1

No exemplo abaixo estamos imprimindo o quadrado de cada número da lista:

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> for n in numeros:
		    print(n ** 2)

1
4
9
16
25

```

### Exemplo 2:

No exemplo abaixo estamos dando uma condição para que só retorne números onde o resultado de módulo 2 seja igual a 0, ou seja somente números pares.

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> for n in numeros:
		    if n % 2 == 0:
		        print(n)

2
4
```

### Exemplo 3:

Podemos também instruir uma operação e o resultado para cada elemento retorne em uma nova lista:

```python
>>> numeros = [1, 2, 3, 4, 5]

>>> soma = []
>>> for n in numeros:
		    n = n * 2
				soma.append(n)

>>> print(soma)

[2, 4, 6, 8, 10]
```

### Infinitas possibilidades:

Podemos realizar inúmeras coisas com o loop for, podemos iterar elementos para que sejam passados a uma determinada função, e retorne o resultado de cada elemento.

Podemos desmembrar uma string em uma lista com todas as letras.

#### Enumerate()

```python
for valor in enumerate(nome):
    print(valor)

(0, 'B')
(1, 'r')
(2, 'u')
(3, 'n')
(4, 'o')
(5, ' ')
(6, 'O')
(7, 'l')
(8, 'i')
(9, 'v')
(10, 'e')
(11, 'i')
(12, 'r')
(13, 'a')
(13, 'a')
```

#loop #estruturaderepetição

---

# Break
```python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop caiu sem encontrar um fator
        print(n, 'is a prime number')
```

```python
while True:
    comando = input("Digite 'sair para sair: ")
    if comando == "sair":
        break
```

