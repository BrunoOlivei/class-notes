# Introdução Lambda

## Definição:

Conhecidas por Expressões Lambdas ou somente Lambdas

Lambdas são funções sem nome (anônimas), que podem ou não receber parâmetros de entrada e retornar valores.

```python
# RELEMBRANDO COMO SÃO FUNÇÕES:

>>> def funcao(x):
				return 3 * x + 1

>>> print(funcao(5))

16

```

Observamos aqui que 'funcao' é o nome desta função.

## Sintaxe:

As expressões lambda possuem uma sintaxe simples:

1.  Palavra reservada `lambda`
2.  Parâmetro
3.  Dois pontos ( : )
4.  Bloco de código de Retorno

Exemplo utilizando a mesma ideia da função anterior:

```python
>>> lambda x: 3 * x + 1

```

A expressão lambda declarada em si não possuí nenhum efeito já que ela não possuí nenhum nome para ser chamada como as funções definidas com def, que para rodarem seu bloco de código precisam ser 'chamadas'.

Tentar executar uma expressão lambda desta forma não tem nenhum resultado.

## Como utilizar uma expressão lambda?

Uma das formas é passar a expressão lambda para uma variável:

```python
>>> teste = lambda x: 3 * x + 5

PEP 8: E731 do not assign a lambda expression, use a def
```

Repare que o PEP 8 indica que nãos e designa um nome a uma expressão lambda, que para isso o certo é utilizar o def.

Porém desta forma conseguimos executar a expressão:

```python
>>> print(teste(5))

16
```

>[!warning]
>Esta forma de declarar uma função lambda não é a ideal muito menos a mais utilizada.

## Caracteristicas:

1.  Podemos ter expressões lambda com múltiplas entradas (parâmetros):

```python
>>> nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
```

Aqui temos 2 parâmetros 'nome' e 'sobrenome' antes dos dois pontos ( : ), em seguida temos o bloco de código que será executado quando os argumentos forem passados, a função irá transformar o dado 'nome' somente a primeira letra capitalizada e excluir qualquer espaço que tenha sido adicionado acidentalmente, irá concatenar com um espaço e com o sobrenome que será transformado também em uma string com a primeira letra capitalizada e qualquer espaço acidental removido.

```python
>>> print(nome_completo('PETER ', '  PARKER  '))

Peter Parke
```

2.  Podemos ter, em expressões lambda, nenhuma parâmetro:

```python
>>> amar = lambda: 'Como não amar Python?'

>>> print(amar())

Como não amar Python?
```

Se não foi definido nenhum parâmetro, nenhum argumento é obrigatório.

Quando um parâmetro é definido, a expressão lambda exige um argumento, assim como as funções, a omissão do argumento causa um TypeError.

```python
>>> amar = lambda x: 'Como não amar Python?'

>>> print(amar())

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    print(amar())
TypeError: <lambda>() missing 1 required positional argument: 'x'
```

Para uma expressão lambda definida com apenas um parâmetro, também resultará em erro caso a expressão for chamada passando mais de 1 argumento:

```python
>>> amar = lambda x: 'Como não amar Python?'

>>> print(amar(1, 2))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 12, in <module>
    print(amar(1, 2))
TypeError: <lambda>() takes 1 positional argument but 2 were given
```

Podemos ter quantos parâmetros quisermos:

n = lambda x1, x2, ... xn: <expressão>

```python
>>> dois_parametros = lambda x, y: (x + y) ** 2
>>> tres_parametros = lambda x, y, z: (x + y + z) ** 3

>>> print(dois_parametros(2, 3))
>>> print(tres_parametros(4, 6, 8))

25
5832

```

---

## Exemplos:

### Exemplos 1: Método mais utilizado.

A partir de uma lista de autores, com nome e sobrenome, criaremos uma expressão lambda que irá ler apenas o sobrenome e reordenará a lista por ordem alfabética a partir do sobrenome:

```python
>>> autores = ['Philip K. Dick', 'H. G. Wells', 'Julio Verne', 'Isaac Asimov', 'Wiliam Gibson', 'Arthur C. Clarke',
           'Aldous Huxley', 'Margaret Atwood', 'Ray Bradbury']
>>> print(autores)

['Philip K. Dick', 'H. G. Wells', 'Julio Verne', 'Isaac Asimov', 'Wiliam Gibson', 'Arthur C. Clarke', 'Aldous Huxley', 'Margaret Atwood', 'Ray Bradbury']
```

#### Criando a expressão lambda:

```python
>>> autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
```

-   As expressões `autores.sort` irá fazer a ordenação dos elementos
-   `key` especifica a função de argumento usado para extrair a chave de comparação de cada elemento iterável, dentro dela é que ficara o lambda com todas as instruções necessárias para alterar o que for necessário e entregar os elementos da forma correta para que o sort leia e faça a ordenação correta.
-   Expressão `lambda`
-   `sobrenome.split(' ')`, irá separar os elementos da lista pelo espaço que há entre eles,
-   `[-1]` irá selecionar o último elemento da relação dos sobrenomes que foram extraídos pelo `sobrenome.split`
-   `.lower()` irá transformar tudo em minúsculo, pela linguagem ser case sensitive, através da padronização de todas as letras minúsculas, a ordenação fica mais ascertiva.

Essa linha de código em momento algum altera os elementos que estão inseridos na lista, o resultado é somente a ordenação, não existe nenhuma perda de dado, ou alteração de letra maiúscula para minúscula, justamente por conta do parâmetro key= que faz o papel de passar os argumentos que devem ser considerados para fazer a ordenação sem a necessidade de alteração dos dados listados.

#### Resultado:

```python
>>> print(autores)

['Isaac Asimov', 'Margaret Atwood', 'Ray Bradbury', 'Arthur C. Clarke', 'Philip K. Dick', 'Wiliam Gibson', 'Ursula K. Le Guin', 'Aldous Huxley', 'Julio Verne', 'H. G. Wells']
```

Como podemos observar não foi necessário nem jogar o resultado para uma nova variável, o .sort() já é um módulo que altera a própria variável em que ele for descrito.

---

### Exemplo 2:

Criando uma expressão quadrática, muito utilizada para projetar trajetória de projéteis (foguetes, mísseis, munição, etc.)

<aside> 📌 Fórmula da função quadrática: f( x ) = a * x ** 2 + b * x + c

</aside>

#### Definindo a função:

```python
>>> def geradora_funcao_quadratica(a, b, c):
		    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
		    return lambda x: a * x ** 2 + b * x + c
```

#### Executando:

```python
# Aqui estamos executando a função geradora_funcao_quadratica com os três parâmetros obrigatórios (a, b, c).
>>> teste = geradora_funcao_quadratica(2, 3, -5)

# com os valores padronizados na função geradora_funcao_quadratica, aqui estamos passando o argumento para a lambda:
>>> print(teste(0))
>>> print(teste(1))
>>> print(teste(2))

Resultado:

-5
0
9
```

#### Executando direto:

```python
# Também é possível executar tudo em uma única linha de código, basta acessar a função, definir no primeiro parênteses os argumentos obrigatórios (a, b, c) e abrir
# um segundo parênteses para definir o argumento da lambda (x).

>>> print(geradora_funcao_quadratica(2, 3, -5)(2))

Resultado:

9
```

---

## Aplicabilidade:

Geralmente expressões lambda são utilizadas para ordenagem e filtragem de dados. Porém elas não se limitam a isso.

#lambda
