# Introdução:

Reduce( ) foi uma função integrada (built-in) porém a partir do python 3+ ela deixou de ser uma built-in e passou a integrar o módulo functools.

Portanto para utilização dela, é necessário fazer o import a partir da functools:

```python
>>> from functools import reduce
```

## Guido van Rossum (autor do python)

> Utilize a função reduce( ) se você realmente precise dela. Em todo caso 99% das vezes um loop for é mais legível.

## Entendendo a estrutura do reduce( ):

🛑 Ao contrário do `map` e do `filter` que recebem uma função que possui apenas um parâmetro, **o `reduce` recebe uma função que possui 2 parâmetros.**

Fora isso sua estrutura é muito parecida com `map` e `filter`, onde:

1.  Palavra reservada: `reduce`
2.  Parênteses: (
3.  Função que recebe 2 parâmetros
4.  Vírgula
5.  Dados Iteráveis
6.  Parênteses: )

```python
>>> reduce(nome_função_dois_parâmetros, dados_iteráveis)
```

## Entendendo o mecanismo do reduce( ):

Sabendo que o reduce recebe uma função com dois parâmetros e um dado iterável seu funcionamento é o seguinte:

Criando um dado iterável genérico e uma função genérica:

```python
>>> dados = ['a1', 'a2', 'a3', ..., 'an']

>>> def nome_função(x, y)
				return
```

### Passo a passo do funcionamento do reduce( ):

1.  Passo: resultado1 = nome_função('a1', 'a2') # Aplica a função nos dois primeiros elementos do iterável e armazena o resultado;
2.  Passo: resultado2 = nome_função(resultado1, a3) # Aplica a função utilizando como argumento o resultado1 e o terceiro elemento do iterável, armazena o resultado;
3.  Passo: resultado3 = nome_função(resultado2, a4) # Aplica a função utilizando como argumento o resultado 2 e o quarto elemento do iterável, armazena o resultado;
4.  .
5.  .
6.  .
7.  Passo: resultado_n = nome_função(resultado_m, an) # Aplica a função utilizando como argumento o resultado anterior e o elemento seguinte do iterável, armazena o resultado.

### Outra visão:

Podemos visualizar a função `reduce` da seguinte forma:

```python
>>> função(função(função(função(função(a1, a2), a3), a4), ...), an)

```

---

# Prática:

Aplicando a função `reduce` para multiplicar todos os números de uma lista:

```python
# Dados iteráveis

>>> dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Função com 2 parâmetros:

>>> multi = lambda x, y: x * y

# Reduce:

>>> resultado = reduce(multi, dados)

# Resultado:

>>> print(resultado)

25878772920
```

---

## Utilizando a mesma ideia com um loop:

```python
# Criando uma variável valendo 1 que irá receber o resultado final:

>>> resultado2 = 1

# para cada elemento na lista dados:
# resultado2 será o resultado * o elemento

>>> for num in dados:
		    resultado2 = resultado2 * num

>>> print(resultado2)

25878772920
```

#reduce #lambda 