# All:

É uma função booleana que retorna True se TODOS os elementos do iterável são VERDADEIROS ou ainda se o iterável está VAZIO.

## Exemplo:

### Exemplo 1:

Observando o código abaixo este all retornará True?

```python
>>> print(all([0, 1, 2, 3, 4]))
```

**Não** pois 0 é False:

```python
False
```

Agora sem o 0:

```python
>>> print(all([1, 2, 3, 4]))
```

Resultado:

```python
True
```

Com um iterável vazio:

```python
>>> print(all([])) # Uma lista vazia
>>> print(all('')) # Uma string vazia
>>> print(all({})) # Um set vazio
>>> print(all(())) # Uma tupla vazia

True
True
True
True
```

---

### Outras usabilidades:

Verificando em uma lista se todos os nomes começam com a letra 'C':

```python
>>> nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina']

>>> print(all([nome[0] == 'C' for nome in nomes]))
```

A partir da lista nomes, verificar se o caractere na posição 0 de cada elemento começa com 'C'

Resultado:

```python
True
```

Se acrescentarmos um elemento que não comece com a letra 'C':

```python
>>> nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina', 'Bruno']

>>> print(all([nome[0] == 'C' for nome in nomes]))

False
```

>[!note]
>Ou seja todos os elementos de um iterável são verdadeiros com base em uma condição especificada.


>[!warning]
>IMPORTANTE: Ao utilizar o all deve se prestar muita atenção nas condições que estão sendo usadas, pois se o resultado da condição trouxer uma lista vazia por exemplo, o resultado do all será TRUE.

---

# Any:

Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio retorna False:

```python
>>> print(any([0, 1, 2, 3, 4]))
```

Resultado:

```python
True
```

Já que ele considera QUALQUER elemento, se pelo menos 1 for verdadeiro, o resultado será TRUE

```python
print(any([0, 0, 0, 0, 0]))
```

Resultado:

```python
False
```

Com apenas 1 elemento verdadeiro:

```python
print(any([0, 0, 0, 0, 'b']))
```

Resultado:

```python
True
```

Iteráveis vazios:

```python
>>> print(any([]))  # Uma lista vazia
>>> print(any(''))  # Uma string vazia
>>> print(any({}))  # Um set vazio
>>> print(any(()))  # Uma tupla  vazia
>>> print(any([0, False, {}, [], ()])) # 0 = Falso, False = Falso, Set Vazio = Falso, Lista Vazia = Falso, Tupla Vazia = Falso

False
False
False
False
False
```

#any #all #lambda 