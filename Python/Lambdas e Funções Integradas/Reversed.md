# Introdução

Não podemos confundir com a função reverse( ), esta função funciona somente para listas, e altera a ordem da lista original:

Podemos observar que a variável lista teve sua ordem alterada.

```python
>>> lista = [1, 2, 3, 4, 5]
>>> print(lista)

[1, 2, 3, 4, 5]

>>> lista.reverse()
>>> print(lista)

[5, 4, 3, 2, 1]
```

O reverse é um atributo do objeto list, portanto tentar utilizar em outro tipo de objeto causa AttributeError:

```python
>>> lista = (1, 2, 3, 4, 5)
>>> print(lista)

(1, 2, 3, 4, 5)

>>> lista.reverse()
>>> print(lista)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 3, in <module>
    lista.reverse()
AttributeError: 'tuple' object has no attribute 'reverse'
```

---

## `reversed()`

Ele funciona com qualquer iterável, com exceção do set. Sua função é inverter a ordem dos elementos de um iterável, ao contrário da argumento nomeado que pode ser passado em `sorted()` por exemplo, o `reversed()` não ordena os elementos de forma decrescente, ele apenas altera a ordem dos elementos conforme eles são apresentados:

Importante observar qual o tipo de objeto que o `reversed()` retorna como resultado.

```python
>>> lista = [1, 2, 3, 4, 5]

>>> resultado = reversed(lista)

>>> print(resultado)
>>> print(type(resultado))

<list_reverseiterator object at 0x00000210D0B5A160>
<class 'list_reverseiterator'>
```

A função `reversed()` retorna um objeto na memória assim como `filter()` e `map()`

No caso das listas o objeto que ela retorna é um `list_reverseiterator`

No caso de tuplas apenas um objeto chamado `reversed`:

```python
>>> lista = (1, 2, 3, 4, 5)
>>> resultado = reversed(lista)

>>> print(resultado)
>>> print(type(resultado))

<reversed object at 0x000001523AADA190>
<class 'reversed'>
```

No caso de string, também retorna um objeto `reversed`

```python
>>> lista = 'Bruno Oliveira'
>>> resultado = reversed(lista)

>>> print(resultado)
>>> print(type(resultado))

<reversed object at 0x000001EF36EA8640>
<class 'reversed'>
```

---

# Convertendo o objeto retornado em um iterável:

Podemos converter o objeto retornado em listas, tuplas ou conjuntos:

```python
>>> lista = [1, 2, 3, 4, 5]

>>> resultado_lista = reversed(lista)

>>> print(tuple(resultado_lista))

(5, 4, 3, 2, 1)
```

Obviamente que se tentar iterar novamente os elementos do objeto retornado no reversed, teremos como resultado um iterável vazio:

```python
>>> print(tuple(resultado_lista))

()
```

O mesmo acontece com o `reversed` de uma tupla, podemos converte-lo em uma lista, uma tupla ou um conjunto, porém ao ser iterado não podemos mais acessar seus dados, teremos um iterável vazio

```python
>>> tupla = (1, 2, 3, 4, 5)

>>> resultado_tupla = reversed(tupla)

>>> print(list(resultado_tupla))

[5, 4, 3, 2, 1]
```

Com strings:

```python
>>> iteravel_string = 'Bruno Oliveira'

>>> resultado_string = reversed(iteravel_string)

>>> print(set(resultado_string))

{'v', 'r', 'o', 'B', 'l', 'O', ' ', 'u', 'i', 'a', 'e', 'n'}
```

Em conjuntos a ordem dos elementos não são definidos e também não são aceitos elementos repetidos.

</aside>

---

# Iterando sobre o reversed:

Podemos iterar os elementos do resultado do reversed:

```python
>>> for letra in reversed('Bruno Oliveira'):
		    print(letra, end='')

arievilO onurB
```

Podemos executar de outras maneiras também, utilizando o join para iterar novamente sobre o resultado de reversed, transformando em uma única string. Lembrando sempre que o resultado de um reversed sempre será um objeto na memória por isso precisamos transforma-lo em um iterável, que neste exemplo utilizamos o list

```python
>>> print(''.join(list(reversed('Bruno Oliveira'))))

arievilO onurB
```

Outra forma:

```python
>>> print('Bruno Oliveira'[::-1])

arievilO onurB
```

---

# Contagem regressiva utilizando um loop for com range:

```python
>>> for n in reversed(range(0, 10)):
		    print(n)

9
8
7
6
5
4
3
2
1
0
```

#reversed
