# Deque
Deque são listas de alta performance ou seja elas se comportam exatamente como uma lista, inclusive os variados métodos utilizados nas listas padrões podem ser utilizados no deque incluindo outros métodos exclusivos:

```python
>>> from collections import deque

>>> d = deque('ghi')
>>> print(d)
>>> print(type(d))

deque(['g', 'h', 'i'])
<class 'collections.deque'>
```

---

## Deque Methods

### Código Fonte:

```python
>>> from collections import deque

>>> d = deque('ghi')
>>> print(d)
>>> print(type(d))

deque(['g', 'h', 'i'])
<class 'collections.deque'>
```

### .append(_element_)

Adiciona um novo elemento após todos os elementos ao lado direito.

```python
>>> d.append('j')
>>> print(d)

deque(['g', 'h', 'i', 'j'])
```

### .appendleft(_element_)

Adiciona um elemento no início do deque, ou seja no lado extremo esquerdo:

```python
>>> d.appendleft('f')
>>> print(d)

deque(['f', 'g', 'h', 'i', 'j'])
```

### .clear()

Remove todos os elementos do deque mantendo um deque vazio:

```python
>>> d.clear()
>>> print(d)

deque([])
```

### .copy()

Cria uma shallow copy do deque:

```python
>>> e = d.copy()
>>> print(e)
>>> print(d)

deque(['f', 'g', 'h', 'i', 'j'])
deque(['f', 'g', 'h', 'i', 'j'])
```

### .count(_element_)

Conta quantas ocorrências há do elemento informado:

```python
>>> print(e.count('f'))

1
```

### .extend(_iterável_)

Acrescenta após o último elemento do lado direito do deque novos elementos a partir de um iterável:

```python
>>> e.extend('klm')
>>> print(e)

deque(['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
```

### .extendleft(_iterável_)

Acrescenta antes do primeiro elemento no lado esquerdo do deque novos elementos a partir de um iterável:

>[!alert]
>Repare que o .extendleft espelha o iterável ao inseri-lo ao deque:


```python
>>> e.extendleft('cde')
>>> print(e)

deque(['e', 'd', 'c', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
```

Para seguir uma ordem é necessário que no momento de informar os elementos a serem inseridos dentro dos parênteses do .extendleft, eles estejam invertidos em sua ordem para que ao serem inseridos essa ordem seja espelhada e entrem na ordem correta:

```python
>>> e.extendleft('edc')
>>> print(e)

deque(['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
```

### .index(_elemento, start, stop_)

É possível procurar o índice de um elemento utilizando o `.index()` informando o elemento desejado dentro dos parênteses, também é possível otimizar a busca parametrizando onde a busca começa e termina, para isso é só inserir uma vírgula após o elemento, informar o índice de começo, uma vírgula e o índice final:

```python
>>> print(e.index('f', 2, 5))

3
```

### .remove(_elemento_)

Remove a primeira ocorrência do elemento informado dentro dos parênteses, se não encontrado retorna ValueError

```python
>>> e.remove('k')
>>> print(e)

deque(['e', 'd', 'c', 'f', 'g', 'h', 'i', 'j', 'l', 'm'])
```

### .insert(_índice, elemento_)

Insere um elemento novo a partir do índice informado dentro dos parênteses, a regra é informar o índice primeiro, seguido por vírgula e o elemento a ser inserido:

```python
>>> e.insert(8, 'k')
>>> print(e)

deque(['e', 'd', 'c', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
```

### .pop()

Esse método remove o último elemento, ou seja o primeiro da direita para esquerda, e o retorna, podendo assim ser inserido em uma nova variável:

```python
>>> c = e.pop()
>>> print(c)
>>> print(e)

m
deque(['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
```

### .popleft()

Já este remove o primeiro elemento do deque, ou seja o último elemento da direita para esquerda, e o retorna podendo também ser inserido em uma nova variável:

```python
>>> b = e.popleft()
>>> print(b)
>>> print(e)

c
deque(['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
```

### .reverse()

Esse método inverte a ordem dos elementos do deque, seu retorno é none o que quer dizer que ele altera a ordem do deque permanentemente, a variável agora terá sua ordem invertida:

```python
>>> e.reverse()
>>> print(e)

deque(['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd'])
```

### .rotate(_n_)

Conforme vimos em listas, que são nada menos que um círculo de itens, onde conseguimos fazer a rotação dos elementos e assim alterar sua ordem, dessa forma o rotate opera, ele gira a ordem dos elementos, onde n informado dentro dos parênteses representam o número de rotações.

```python
>>> e.rotate(1)
>>> print(e)

deque(['d', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e'])
```

É possível também rotacionar no sentido oposto, para isso basta informar valor de n negativo:

```python
>>> e.rotate(-1)
>>> print(e)

deque(['l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd'])
```

#dequemethods

---
