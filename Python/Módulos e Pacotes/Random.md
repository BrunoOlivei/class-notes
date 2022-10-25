# Conceito:

São outros arquivos python, por exemplo os arquivos que criamos em um projeto são módulos.

# Utilidade:

São úteis para que possamos deixar nosso programa mais simples e também reutilizar códigos em outros projetos.

Podem ser escritos por nós e também podem ser escritos pela comunidade e disponibilizados para utilização.

# Acesso:

Existem 2 métodos para se acessar e utilizar as suas funcionalidades:

## Forma 1:

Importando todo o módulo, todas as funções, atributos, classes e propriedades que estiverem dentro do módulo, estarão disponíveis e em memória pronto para utilização.

Esse método não é recomendado por conta do uso da memória

```python
import random
```

## Forma 2:

Importando uma função especifica do módulo:

Forma recomendada:

```python
from random import random
```

---

# Random

Este módulo implementa geradores de números pseudoaleatórios para várias distribuições.

## Sintaxe:

As funções do pacote (módulo) random, são todas acessadas utilizando a palavra reservada do pacote, seguido de ponto e o nome da função, isso quando o import foi feito do pacote todo.

```python
random.random()
```

Quando fazemos o import apenas de uma função especifica não a sintaxe muda:

```python
random()
```

## Funções:

### random()

Retorna o próximo número de ponto flutuante aleatório no intervalo [0.0, 1.0].

```python
# Usando o import de todo módulo random:
>>> print(random.random())

0.26430231574073926

# Usando o import apenas da função especifica random do módulo random:
>>> print(random())

0.29550376541403256
```

### uniform(_a, b_)

Retorna um valor aleatório ponto flutuante entre a e b passado como argumento:

```python
>>> print(uniform(1, 10))

3.8885832610770623
```

### randint(_a, b_)

Retorna um inteiro aleatório N de forma que a <= N <= b.

```python
>>> print(randint(1, 10))

3
```

### choice(_iter_)

Retorna um elemento aleatório da sequência não vazia seq (iterável). Se seq estiver vazio, levanta IndexError.

```python
>>> jogadas = ('pedra', 'papel', 'tesoura')

>>> print(choice(jogadas))

pedra
```

### shuffle(_x, [random]_)

Embaralha a sequencia x:

```python
>>> from random import shuffle

>>> cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

>>> print(cartas)

['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10']

shuffle(cartas)
print(cartas)

['6', '3', '10', '5', '9', 'K', 'Q', '2', 'J', '7', '4', '8', 'A']
```