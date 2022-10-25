# Iterator

-   Um objeto que pode ser iterável
-   Um objeto que retorna um dado, sendo um elemento por vez quando uma função `next()` é chamada

# Iterable

-   Um objeto que irá retornar um _iterator_ quando uma função iter() for chamada
    
-   Exemplos de _iterables_ que não são iteráveis
    
    -   Strings
    
    ```python
    >>> nome = "Bruno"
    >>> print(next(nome))
    
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'str' object is not an iterator
    ```
    
    -   Listas
    
    ```python
    >>> numeros = [1, 2, 3, 4, 5]
    >>> print(next(numeros))
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'list' object is not an iterator
    ```
    

## Transformando iterables em iterator

```python
>>> it1 = iter(nome)
>>> print(next(it1))
B
>>> print(next(it1))
r
>>> print(next(it1))
u
```

```python
>>> it2 = iter(numeros)
>>> print(next(it2))
1
>>> print(next(it2))
2
>>> print(next(it2))
3
```

O _python_ levanta uma exceção (erro) quando a função `next` é chamada mesmo depois do _iterator_ ter chegado ao fim.

```python
>>> print(next(it2))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Estruturas de repetição como o for fazem uso das funções `iter()` e `next()`:

```python
>>> for i in numeros:
				print(i)
1
2
3
4
5
```

## Criando função loop de um iterável (`for`)

```python
def meu_iteravel(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break
```

## Criando o `range` do zero

```python
class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor += 1
            return numero
        else:
            raise StopIteration

contador = Contador(1, 10)
for numero in contador:
    print(numero)
```