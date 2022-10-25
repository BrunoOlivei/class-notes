# Introdução:

Generators são o que seriam chamados de Tuple Comprehensions.

## Relembrando os métodos Comprehensions:

```python
>>> def caixa_alta(nome):
		    nome = nome.replace(nome[0], nome[0].upper())
		    return nome

>>> amigos = ['maria', 'julia', 'pedro', 'guilherem', 'vanessa']

>>> print([caixa_alta(amigo) for amigo in amigos])

['Maria', 'Julia', 'Pedro', 'Guilherem', 'Vanessa']
```

```python
>>> resultado = [caixa_alta(amigo) for amigo in amigos]

>>> print(resultado)
['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']

>>> print(type(resultado))
<class 'list'>
```

---

# Utilizando o Generator:

Repare que a diferença do list comprehension por exemplo para o generator, e que trocamos os colchetes [ ] para parênteses ( ):

```python
>>> resultado = (caixa_alta(amigo) for amigo in amigos)
```

Agora imprimindo diretamente o resultado:

```python
>>> print(resultado)
<generator object <genexpr> at 0x000001D605D1C900>

>>> print(type(resultado))
<class 'generator'>
```

Foi criado um objeto na memória chamado `generator`, assim como em `map` e `filter` a partir do momento que este objeto for utilizado, ele é automaticamente deletado da memória:

```python
>>> print(list(resultado))

['Maria', 'Julia', 'Pedro', 'Guilherme', 'Vanessa']
```

Apesar de o objeto `generator` ainda ter um espaço reservado na memória, os elementos que nele continham não existem mais:

```python
>>> print(resultado)
<generator object <genexpr> at 0x000001EAE93AC900>

>>> print(tuple(resultado))
()
```

## Outra utilização:

Utilizando o exemplo do Any e All:

Uma lista com nomes queremos saber se algum elemento desta lista começa com a letra 'C'

```python
>>> nomes = ['Carlos', 'Camila', 'Carla', 'Cristiano', 'Cristina', 'Bruno']
```

Imprima se qualquer um dos elementos do iterável 'nomes' começa com 'C':

```python
>>> print(any((nome[0] == 'C' for nome in nomes)))

True
```

### Destrinchando:

Colocando o resultado da conferência se todos os elementos do iterável 'nomes' começam com 'C':

```python
>>> res = (nome[0] == 'C' for nome in nomes)
```

Imprimindo a variável:

```python
>>> print(res)

<generator object <genexpr> at 0x000001B8292FC900>

>>> print(type(res))

<class 'generator'>
```

Imprimindo em uma tupla a variável, como podemos ver o generator tem um comportamento muito parecido com o List Comprehension, Set Comprehension e os demais, porém na memória ele se comporta como o filter e o map.

Em quesito de performance o generator é melhor que qualquer comprehension.

```python
>>> print(tuple(res))

(True, True, True, True, True, False)
```

Se tentarmos acessar os dados novamente utilizando algum tipo de collection o retorno será vazio apesar de ainda ter um espaço reservado na memória para o objeto generator:

```python
>>> print(list(res))

[]
```

# Entendendo o uso de memória e a diferença entre Comprehension e Generator:

Utilizando o getsizeof, vamos visualizar o tamanho que ocupa de espaço em bytes na memória para cada:

```python
>>> from sys import getsizeof

# Gerando uma list comprehension:

>>> list_comp = getsizeof([x * 10 for x in range(1000)]) # Lista = List Comprehension

>>> set_comp = getsizeof({x * 10 for x in range(1000)}) # Set = Set Comprehension

>>> dic_comp= getsizeof({x: x * 10 for x in range(1000)}) # Dictionary = Dict Comprehension

>>> gen = getsizeof((x * 10 for x in range(1000))) # Generator Expression

Resultado:

>>> print('Para fazer a mesma tarefa, gastamos em memória:')
>>> print(f'List Comprehension: {list_comp} bytes')
>>> print(f'Set Comprehension: {set_comp} bytes')
>>> print(f'Dict Comprehension: {dic_comp} bytes')
>>> print(f'Generator Expression: {gen} bytes')

Para fazer a mesma tarefa, gastamos em memória:
List Comprehension: 9016 bytes
Set Comprehension: 32984 bytes
Dict Comprehension: 36960 bytes
Generator Expression: 112 bytes
```

---

# Iterando no Generator Expression:

```python
# Criamos um Generator Expression: onde criou um objeto com alguns elementos inseridos em memória,

>>> gen = (x * 10 for x in range(10))
>>> print(gen)
>>> print(type(gen))

<generator object <genexpr> at 0x0000025A56B3C900>
<class 'generator'>

# Expondo os elementos e iterando um a um:

>>> for num in gen:
		    print(num)

0
10
20
30
40
50
60
70
80
90
```

#generatorexpression 