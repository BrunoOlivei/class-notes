# Generators

*Generators* são i*terators*, porém o contrário não é verdadeiro pois nem todo *iterator* é um *generator*.

- *Generators* podem ser criados com funções geradoras
- Funções geradoras utilizam a palavra reservada `yield`
- *Generators* podem ser criados com Expressões Geradoras

## Diferenças entre funções e *Generator Functions*

| Funções | Generator Functions |
| --- | --- |
| Utilizam return | Utilizam yield |
| Retorna 1 vez | Pode utilizar yield múltiplas vezes |
| Quando executada pode (ou não) retornar um valor | Quando executada retorna um Generator |

## Exemplo de *Generator Function*
#generatorfunction

Uma *generator function* **não é um *Generator***. Ela gera um *Generator*

```python
def conta_ate(valor_maximo: int):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

gen = conta_ate(5)
```

```python
>>> print(type(gen))
<class 'generator'>
```

```python
>>> print(next(gen))
1
>>> print(next(gen))
2
>>> print(next(gen))
3
>>> print(next(gen))
4
>>> print(next(gen))
5
```

```python
>>> print(next(gen))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

<aside>
🔑 O segredo está na palavra reservada `yield`, ao contrário da palavra `return` que retorna o resultado de uma função e sai da mesma, a palavra `yield` retorna um valor porém NÃO sai da função, aguardando uma função `next()` ser chamada novamente.

</aside>

Podemos usar estruturas de repetição no Generator

```python
>>> gen = conta_ate(5)
>>> for num in gen:
...     print(num)
...
1
2
3
4
5
```

Também podemos gerar todos os resultados de uma vez só, passando a chamada da função geradora dentro de uma lista:

```python
>>> list(conta_ate(5))
[1, 2, 3, 4, 5]
>>> tuple(conta_ate(5))
(1, 2, 3, 4, 5)
>>> set(conta_ate(5))
{1, 2, 3, 4, 5}
```

---

# Generator expression
#generatorexpression

```python
>>> ge2 = (num for num in range(1, 10)) # Generation Expression
>>> print(type(ge2))
<class 'generator'>

>>> print(ge2)
<generator object <genexpr> at 0x000001FFA8230510>
```

É possível realizar operações matemáticas nas expressões geradoras

```python
>>> print(sum(num for num in range(1, 10)))
45
```

---

# Teste de uso de memória com Generators

```python
def fib_lista(max):
    nums = []
    a, b = 0, 1
    while len(nums) < max:
        nums.append(b)
        a, b = b, a + b
    return nums

def fib_gen(max):
    a, b, contador = 0, 1, 0
    while contador < max:
        a, b = b, a + b
        yield a
        contador += 1

for n in fib_gen(10000):
    print(n, end=", ")

# Utiliza menos memória mas não quer dizer que é mais rápido
```

# Teste de velocidade utilizando Generators

```python
# Teste de velocidade
import time

# Generator Expression
gen_inicio = time.time()

print(sum(num for num in range(100000000)))

gen_tempo = time.time() - gen_inicio

# List Comprehension

list_inicio = time.time()

print(sum([num for num in range(100000000)]))

list_tempo = time.time() - list_inicio

print(f"Tempo de execução do Generator Expression: {gen_tempo}")
print(f"Tempo de execução do List Comprehension: {list_tempo}")
```

```python
4999999950000000
4999999950000000
Tempo de execução do Generator Expression: 5.424114465713501
Tempo de execução do List Comprehension: 9.480979442596436
```