# sqrt( )

A função integrada `sqrt()` realiza a operação de raiz quadrada do elemento que é passado a ela.

Só aceita um argumento por vez:

```python
>>> from math import sqrt

>>> num = 25
>>> print(sqrt(num))

5.0
```

---

# hypot( )

A função integrada ao módulo math, hypot() calcula a hipotenusa de um triângulo retângulo utilizando o teorema de Pitágoras:

A fórmula matemática para o calculo é:

$$ h = \sqrt{a² + b²} $$

Sintaxe: `hypot(a, b)`

```python
from math import hypot

>>> lado1 = 4
>>> lado2 = 3

>>> print(hypot(lado1, lado2))

5.0
```

A função hypot() aceita 1 argumento ou até mais que dois, não necessariamente ela exclusiva para a fórmula da hipotenusa, podendo calcular a a raiz quadrada da soma de mais de 2 elementos elevados ao quadrado cada:

```python
>>> **from math import hypot

>>> lado1 = 4
>>> lado2 = 3
>>> lado3 = 2

>>> print(hypot(lado1, lado2, lado3))**
```

---