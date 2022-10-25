# raise

Com o raise eu posso forçar um erro:

```python
def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso na cor {cor}')
```

```python
>>> colore('Bruno', 'verde')

O texto Bruno será impresso na cor verde
```

```python
>>> colore('Bruno', 'preto')

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    colore('Bruno', 'preto')
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 8, in colore
    raise ValueError(f'A cor precisa ser uma entre {cores}')
ValueError: A cor precisa ser uma entre ('verde', 'amarelo', 'azul', 'branco')
```

```python
>>> colore(2, 'preto')

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    colore(2, 'preto')
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 4, in colore
    raise TypeError('Texto precisa ser uma string')
TypeError: Texto precisa ser uma string
```

```python
>>> colore('Bruno', 2)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    colore('Bruno', 2)
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 6, in colore
    raise TypeError('Cor precisa ser uma string')
TypeError: Cor precisa ser uma string
```