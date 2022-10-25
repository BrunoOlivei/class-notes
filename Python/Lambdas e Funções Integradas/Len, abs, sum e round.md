# len( ):

Retorna o tamanho, ou seja o número de elementos de um iterável:

```python
>>> print(len('Bruno Oliveira'))
14

>>> lista = [1, 2, 3, 4, 5]
>>> print(len(lista))
5

>>> tupla = (1, 2, 3, 4, 5)
>>> print(len(tupla))
5

>>> conjunto = {1, 2, 3, 4, 5}
>>> print(len(conjunto))
5

>>> dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
>>> print(len(dicionario))
5

```

Por tras dos panos que a função len( ) executa, está uma função que é chamado no python de dunder: **len**( )

```python
>>> print('Bruno Oliveira'.__len__())
14
```

---

# abs( )

Retorna o valor absoluto de um número inteiro ou real:

Ele elimina o sinal negativo do número, só pode ser usado para números inteiros ou floats

```python
>>> print(abs(-5))
>>> print(abs(5))
>>> print(abs(3.14))
>>> print(abs(-3.14))

5
5
3.14
3.14
```

---

# sum( )

Recebe como parâmetro um iterável e retorna a soma total dos elementos, pode receber um valor inicial (start = ) na operação total além da soma dos iteráveis o valor inicial também será executado na soma.

Podemos passar a lista, conjunto, dicionário e tupla direto na função sum:

```python
>>> print(sum([1, 2, 3, 4, 5]))
>>> print(sum((1, 2, 3, 4, 5)))
>>> print(sum({1, 2, 3, 4, 5}))
>>> print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))

15
15
15
15
```

>[!warning]
>Observar que no momento de utilziar a função sum em um dicionário é preciso se atentar ao que deseja-se somar, se serão as chaves ou os valores, pois o sum não faz esta distinção e tenta somar todos os elementos (chaves e valores):

```python
>>> print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 9, in <module>
    print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Podemos também criar as listas, tuplas, conjuntos e dicionários em uma variável e passar a variável como argumento na função sum:

```python
>>> lista = [1, 2, 3, 4, 5]
>>> tupla = (1, 2, 3, 4, 5)
>>> conjunto = {1, 2, 3, 4, 5}
>>> dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

>>> print(sum(lista))
>>> print(sum(tupla))
>>> print(sum(conjunto))
>>> print(sum(dicionario.values()))

15
15
15
15
```

---

## Parâmetro Default ou Start=

Dentro da função sum também é possível informar um valor que será usado na hora de somar. É como se a soma partisse de um número já pré definido, nós podemos nomear utilizando a palavra start seguida de sinal de igual e o número que desejamos.

```python
>>> print(sum([1, 2, 3, 4, 5], 5))
>>> print(sum((1, 2, 3, 4, 5), start=5))
>>> print(sum({1, 2, 3, 4, 5}, start=5))
>>> print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values(), 5))

20
20
20
20
```

```python
>>> print(sum(lista, 5))
>>> print(sum(tupla, 5))
>>> print(sum(conjunto, start=5))
>>> print(sum(dicionario.values(), start=5))

20
20
20
20
```

Esse parâmetro padrão é muito interessante quando se deseja somar um valor padrão de frete por exemplo a uma lista de produtos.

---

# round( )

round retorna um número arredondado para n digito de precisão após a casa decimal. Se a precisão não for informada o round retorna um valor inteiro mais próximo da entrada:

Os valores são arredondados para o múltiplo mais próximo de 10 para a potência de menos _ndigit. S_e dois múltiplos são igualmente próximos, o arredondamento é feito para a opção par (por exemplo, `round(0.5)` e `round(-0.5)` são `0` e `round(1.5)` é `2`)

Sintaxe:

```python
>>> round(valor_de_entrada, quantidade_digitos)
```

Se a quantidade de dígitos não for informada, o round retorna um inteiro:

```python
>>> print(round(10.2))
>>> print(round(10.5))
>>> print(round(10.6))
>>> print(round(1.2121212121, 2))
>>> print(round(1.2199999, 2))

10
10
11
1.21
1.22
```

>[!important]
>Importante reparar que ele segue uma lógica de arredondamento que dependendo do caso de uso, pode atrapalhar os resultados. É preciso ter cautela.

#len #abs #sum #round