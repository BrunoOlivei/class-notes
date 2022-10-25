# Args

## Definição:

O \*args é um parâmetro de entrada de uma função como outra qualquer. Teoricamente por ser um parâmetro como outro qualquer, ele poderia ser chamado de qualquer coisa, desde que tivesse o * antes da palavra, mas por convenção da comunidade ficou definido \*args:

## O que é:

Então \*args é um parâmetro utilizado em uma função onde todos os valores extras informados como entrada (argumento) são inseridos em uma tupla. Lembrando que tuplas são imutáveis:

>[!note]
>Importante lembrar da aula de Parâmetros e Parâmetros Padrão, onde vimos que quando uma função possui 2 parâmetros, se passarmos como argumento na chamada da função 3 números o código gerará um erro `TypeError`.

Vejamos:

```python
>>> def soma_todos_numeros(num1, num2, num3):
		    return num1 + num2 + num3

>>> print(soma_todos_numeros(1, 2, 3, 4))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 5, in <module>
    print(soma_todos_numeros(1, 2, 3, 4))
TypeError: soma_todos_numeros() takes 3 positional arguments but 4 were given
```

Utilizando o \*args:

```python
>>> def soma_todos_numeros(*args):
		    return args

>>> print(soma_todos_numeros(1, 2, 3, 4))

(1, 2, 3, 4)
```

Retorno foi uma tupla

Podemos usar um loop para iterar os valores desta tupla e soma-los conforme a função anterior:

```python
>>> def soma_todos_numeros(*args):
		    total = 0
		    for numero in args:
		        total = total + numero
		    return total

>>> print(soma_todos_numeros(1, 2, 3, 4))

10
```

Ou podemos refatorar o código e escrever da seguinte forma:

```python
>>> def soma_todos_numeros(*args):
		    return sum(args)

>>> print(soma_todos_numeros(1, 2, 3, 4))

10
```

>[!check] 
>Uma função utilizando o *args podemos passar a quantidade de argumentos na chamada da função que quisermos que irá corresponder.

Uma função pode possuir parâmetros obrigatórios e o \*args ao mesmo tempo:

```python
>>> def contato(nome, email, *args):
		    return
```

Nesse caso sempre que a função for chamada é necessário passar pelo menos 2 argumentos, que correspondem a 'nome' e 'email', para que a função seja executada corretamente, o \*args aceita nada ou qualquer quantidade de dados:

```python
>>> def soma_todos_numeros(*args):
		    return sum(args)

>>> print(soma_todos_numeros())
>>> print(soma_todos_numeros(1))
>>> print(soma_todos_numeros(1, 2))
>>> print(soma_todos_numeros(1, 2, 3))
>>> print(soma_todos_numeros(1, 2, 3, 4))

0
1
3
6
10
```

---

## Exemplos de utilização \*args:

### Exemplo 1:

```python
>>> def verifica_info (*args):
		    if 'Geek' in args and 'University' in args:
		        return 'Bem-vindo Geek!'
		    return 'Eu não tenho certeza quem você é...'

>>> print(verifica_info())
>>> print(verifica_info(1, True, 'University', 'Geek'))
>>> print(verifica_info(1, 'University', 3.145))
```

A função acima irá retornar 'Bem-vindo Geek!' se `args` tiver 'Geek' e 'University' inseridos, caso não encontre os 2 valores retorna 'Eu não tenho certeza quem você é...'

```python
Eu não tenho certeza quem você é...
Bem-vindo Geek!
Eu não tenho certeza quem você é...
```

Podemos questionar por quê o terceiro print retornou 'Bem-vindo Geek!'

Isso se dá pois a função foi escrita para encontrar 'Geek' e 'University' dentro de args, como sabemos que o \*args acrescenta todos os argumentos passados em uma tupla, ao fazer o laço for ele encontra os dois valores, não importa em qual ordem e retorna verdadeiro para esse bloco.

### Exemplo 2:

Na função abaixo vamos criar uma função que irá somar todos os argumentos passados para o parâmetro args:

Sabendo que o args acrescenta todos os argumentos passados em uma tupla, o que aconteceria se passarmos uma lista?

```python
>>> def soma_todos_valores(*args):
		    return sum(args)

>>> print(soma_todos_numeros())
>>> print(soma_todos_numeros(3, 4, 5, 6))

0
18

numeros = [1, 2, 3, 4, 5, 6, 7]
print(soma_todos_numeros(numeros))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 38, in <module>
    print(soma_todos_numeros(numeros))
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 9, in soma_todos_numeros
    return sum(args)
TypeError: unsupported operand type(s) for +: 'int' and 'list'
```

O código não conseguiria fazer a soma dos valores da lista pois a tupla entende a lista como um único valor.

É assim que ficaria:

```python
print(soma_todos_valores(numeros, 3, 4, 5, 6))

([1, 2, 3, 4, 5, 6, 7], 3, 4, 5, 6)
```

A Tupla seria isso, um grupo de dados com uma lista junto com outros números.

### Utilizando * no argumento:

É possível utilizarmos o * antes do argumento para indicar que o que está sendo passado como argumento na chamada da função é uma coleção de dados e que será necessário fazer o desempacotamento dos dados para conseguir realizar o bloco de código da função:

```python
>>> def soma_todos_valores(*args):
		    return sum(args)

>>> numeros = [1, 2, 3, 4, 5, 6, 7]
>>> print(soma_todos_valores(*numeros))
>>> print(soma_todos_valores(*numeros, 3, 4, 5, 6))

28
46
```

>[!error]
> Isso funciona para listas e tuplas por exemplo, porém para dicionários não, já que cada dado dentro deles é um par de chave e valor.

#args

---

# Kwargs

## Definição

O \*\*kwargs por definição da comunidade de programadores python, definiu que para ao se utilizar esse tipo de parâmetro, que ele fosse nomeado desta forma, o nome poderia ser qualquer um por exemplo \*\*xis, porém por convenção sempre que for utilizar os 2 asteriscos que seja utilizado o nome kwargs.

Assim como o \*args, o \*\*kwargs é como um parâmetro qualquer que armazena valores extras que são passados como argumento em uma função, porém o \*\*kwargs exige que esses valores ao serem armazenados possuam o nome, ou seja assim como os dicionários que exigem uma par chave e valor, o \*\*kwargs também exige o par chave e valor. Esses dados são armazenados consequentemente em um dicionário.

### Exemplo:

```python
>>> def cores_favoritas(**kwargs):
		    print(kwargs)

>>> cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

{'marcos': 'verde', 'julia': 'amarelo', 'fernanda': 'azul', 'vanessa': 'branco'}
```

### O que podemos fazer:

Iteração dos elementos do dicionário (resultado da função com \*\*kwargs):

```python
>>> def cores_favoritas(**kwargs):
				for pessoa, cor in kwargs.items():
				    print(f'A cor favorita de {pessoa.title()} é {cor}.')

>>> cores_favoritas(marcos='verde', julia='amarelo', fernanda='azul', vanessa='branco')

A cor favorita de Marcos é verde.
A cor favorita de Julia é amarelo.
A cor favorita de Fernanda é azul.
A cor favorita de Vanessa é branco.
```

>[!note] 
>Lembrando que tanto para *args quanto para **kwargs os argumentos não são obrigatórios:

```python
>>> cores_favoritas()
>>> cores_favoritas(bruno='vermelho')

A cor favorita de Bruno é vermelho.
```

O código não apresenta erro como em parâmetros normais.

---

## Exemplo mais complexo:

Criando uma função que irá ler o conteúdo do dicionário criado pelo \*\*kwargs e caso este dicionário possua 'Geek' e essa palavra for a chave do valor 'Python', o retorno será 'Você recebeu um cumprimento Pythonico Geek!'.

Caso a palavra 'Geek' esteja inserida no dicionário seja como chave ou como valor mas tenha qualquer outra coisa como valor ou até mesmo como chave, o retorno será o valor que está vinculado a palavra chave 'Geek' junto com uma string 'Geek!'.

E por fim caso não tenhamos nenhuma string 'geek' sendo usada como valor no \*\*kwargs, o retorno será 'Não tenho certeza quem você é...":

```python
>>> def cumprimento_especial(**kwargs):
		    if 'geek' in kwargs and kwargs['geek'] == 'Python':
		        return 'Você recebeu um cumprimento Pythonico Geek!'
		    elif 'geek' in kwargs:
		        return f"{kwargs['geek']} Geek"
		    return 'Não tenho certeza quem você é...'

print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

Não tenho certeza quem você é...
Você recebeu um cumprimento Pythonico Geek!
Oi Geek
especial Geek
```

---

## Ordem dos diversos tipos de parâmetros:

1.  Parâmetros obrigatórios;
2.  \*args;
3.  Parâmetros default (não obrigatórios);
4.  \*\*kwargs.

### Exemplo:

```python
>>> def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
		    print(f'{nome} tem {idade} anos')
		    print(args)
		    if solteiro:
				    print('Solteiro')
		    else:
		        print('Casado')
		    print(kwargs)
```

1.  Parâmetros Obrigatórios: idade e nome
2.  \*args: qualquer valor
3.  Parâmetros Default: Solteiro = True or False
4.  \*\*kwargs

**Essa função retornará:** 
- 'Nome em idade anos' 
- Argumentos em lista se forem passado (\*args) 
- Se solteiro for True, então irá imprimir 'Solteiro', se não 'Casado' 
- Argumentos passados com o par chave e valor serão adicionados no \*\*kwargs 
- Tudo isso será imprimido

#### Resultado 1

```python
minha_funcao(8, 'Julia')

# aqui só foi passado como argumento os dois parâmetros obrigatórios, nenhum *args e como o parâmetro default automáticamente associa um valor padrão como argumento,
# o resultado será Casado já que a linguagem entende que a omissão do valor False, siginifica que é True, e para argumentos chave e valor, não foi passado nenhum.
# O resultado:

Julia tem 8 anos
()
Casado
{}
```

#### Resultado 2:

```python
>>> minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)

# Aqui foram passados além dos argumentos para os parâmetros obrigatórios (idade e nome) também foi passado 3 números para *args, que resultam numa lista com esses 3 valores,
# e para o parâmetro default, foi passado o valor True, para **kwargs que são argumentos em par de chaves e valor, não foi passado nada
# Resultado:

Felicity tem 18 anos
(4, 5, 3)
Solteiro
{}
```

#### Resultado 3:

```python
>>> minha_funcao(34, 'Felipe', eu='Não', voce='Vai')

# Neste caso forma passados como argumentos os parâmetros obrigatórios, nenhum argumento para o parâmetro *args, e a omissão do parâmetro default resulta em solteiro = False
# com pares de chave e valor foram passados os argumentos para **kwargs
# Resultado:

Felipe tem 34 anos
()
Casado
{'eu': 'Não', 'voce': 'Vai'}
```

#### Resultado 4:

```python
>>> minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Aqui temos os argumentos para os parâmetros obrigatórios, 3 valores que foram adicionados como argumento para o *args, a omissão do parâmetro default o resultado é
# casado, e como argumentos para o **kwargs pares de chave e valor.
# Resultado:

Carla tem 19 anos
(9, 4, 3)
Casado
{'java': False, 'python': True}
```

---

## Entendendo a importância da ordem dos parâmetros:

Forma correta:

```python
>>> def mostra_info(a, b, *args, intrutor='Geek', **kwargs):
		    return [a, b, args, intrutor, kwargs]

>>> print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

[1, 2, (3,), 'Geek', {'sobrenome': 'University', 'cargo': 'Instrutor'}]
```

Forma incorreta, muito comum programadores executarem dessa maneira errada:

Alterando a ordem somente colocando, parâmetros obrigatórios, parâmetros default, \*args e \*\*kwargs:

```python
>>> def mostra_info(a, b, intrutor='Geek', *args, **kwargs):
		    return [a, b, args, intrutor, kwargs]

>>> print(mostra_info(1, 2, 3, sobrenome='University', cargo='Instrutor'))

[1, 2, (), 3, {'sobrenome': 'University', 'cargo': 'Instrutor'}]

```

Aqui podemos verificar que os valor para a e b estão corretos, o \*args ficou vazio podemos ver que o resultado de parênteses vazio, o 3 se tornou o argumento para o parâmetro default, ou seja instrutor se tornou 3 e o \*\*kwargs está correto.

---

## Desempacotamento dos argumentos \*\*kwargs:

Será criada uma função que receberá como argumentos um \*\*kwargs, o retorno será imprimir uma string com o nome e o sobrenome:

Como argumento será passado uma variável que recebe como valor um dicionário contendo pares de chave e valor:

chave: 'nome' - valor: uma string com o nome,

chave: 'sobrenome' - valor uma string com o sobrenome.

Na execução da função, será passado a variável:

```python
>>> def mostrar_nomes(**kwargs):
		    return f"{kwargs['nome']} {kwargs['sobrenome']}"

>>> nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

>>> print(mostrar_nomes(nomes))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 7, in <module>
    print(mostrar_nomes(nomes))
TypeError: mostrar_nomes() takes 0 positional arguments but 1 was given
```

Para conseguirmos executar essa função será necessário realizar o desempacotamento, para isso basta colocar 2 asteriscos antes do nome da variável:

```python
>>> print(mostrar_nomes(**nomes))

Felicity Jones
```

## A funcionalidade do asterisco:

Relembrando o uso do asterisco antes do nome de uma variável como desempacotador nas funções:

```python
>>> def soma_multiplos_numeros(a, b, c):
		    print(a + b + c)
```

Passando uma variável com uma lista, outra com uma tupla e uma terceira com um conjunto, como argumentos para a função:

```python
>>> lista = [1, 2, 3]
>>> tupla = (1, 2, 3)
>>> conjunto = {1, 2, 3}

>>> soma_multiplos_numeros(*lista)
>>> soma_multiplos_numeros(*tupla)
>>> soma_multiplos_numeros(*conjunto)

6
6
6
```

O asterisco antes do nome da variável que recebe como valor uma lista, ou tupla ou conjunto, faz o desempacotamento dos valores, assim sendo possível executar o bloco de código da função.

Com dicionários não é muito diferente, é só acrescentar 2 asteriscos antes do nome da variável que recebeu como valor um dict:

```python
>>> dicionario = dict(a=1, b=2, c=3)

>>> soma_multiplos_numeros(**dicionario)

6
```

>[!warning]
>OBSERVAÇÃO: Os nomes das chaves do dicionário devem ser os mesmos dos parâmetros da função.

```python
>>> dicionario = dict(d=1, e=2, f=3)

>>> soma_multiplos_numeros(**dicionario)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 15, in <module>
    soma_multiplos_numeros(**dicionario)
TypeError: soma_multiplos_numeros() got an unexpected keyword argument 'd'
```

#kwargs

---
