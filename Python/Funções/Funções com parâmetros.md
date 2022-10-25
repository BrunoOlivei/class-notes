# Funções com parâmetros
## Parâmetro de Entrada

Funções que recebem dados para serem processados.

Um programa geralmente consiste em:

entrada → processamento → saída

Funções podem:

-   Não possuir entrada;
-   Não possuir saída;
-   Possuir entrada mas não possuir saída;
-   Não possuir entrada mas possuir saída;
-   Possuir entrada e saída.

### Refatorando uma função 01:

Função original:

```python
>>> def quadrado_de_sete():
			return 7 * 7
```

Função refatorada:

```python
>>> def quadrado(numero):
	    return numero * numero

>>> print(quadrado(7)) # 49
>>> print(quadrado(2)) # 4
>>> print(quadrado(5)) # 25
```

No exemplo acima a função recebe um parâmetro, esse parâmetro será o DADO DE ENTRADA. Portanto quando for chamada a função, é necessário que se passe um valor de entrada (dentro dos parênteses) caso contrário gerará um erro do tipo `TypeError`:

```python
>>> def quadrado(numero):
	    return numero * numero

>>> print(quadrado())

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 5, in <module>
    print(quadrado())
TypeError: quadrado() missing 1 required positional argument: 'numero'
```

Alguns tipos de dados também podem incorrer em caso de erro, por exemplo na função acima:

```python
>>> def quadrado(numero):
	    return numero * numero

>>> print(quadrado('b'))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 5, in <module>
    print(quadrado('b'))
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 2, in quadrado
    return numero * numero
TypeError: can't multiply sequence by non-int of type 'str'
```

### Refatorando uma função 02:

Função Original:

```python
>>> def cantar_parabens():
	print('Parabéns para você')
	print('Nessa data querida')
	print('Muitas felicidades')
	print('Muitos anos de vida')
	print('Viva o aniversariante!')
```

Refatorando e criando um parâmetro de entrada:

```python
>>> def cantar_parabens(aniversariante):
				print('Parabéns para você')
		    print('Nessa data querida')
		    print('Muitas felicidades')
		    print('Muitos anos de vida')
		    print(f'Viva o/a {aniversariante}!')

>>> cantar_parabens('Marcos')
>>> cantar_parabens('Patrícia')
>>> cantar_parabens('Cookie')
```

Assim como na função anterior, omitir o dado de entrada causará um `TypeError`:

```python
>>> cantar_parabens()

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 9, in <module>
    cantar_parabens()
TypeError: cantar_parabens() missing 1 required positional argument: 'aniversariante'
```

Nesse caso passar um int como valor de entrada, não causou erro, porém o resultado foi inesperado:

```python
>>> cantar_parabens(40)

Parabéns para você
Nessa data querida
Muitas felicidades
Muitos anos de vida
Viva o/a 40!
```

### Múltiplos parâmetros

Funções podem ter n parâmetros de entrada, ou seja podemos receber como entrada em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

#### Exemplo 1

No exemplo abaixo criamos 2 parâmetros:

```python
>>> def soma(a, b):
	    return a + b
```

Chamada da função:

Os valores de entrada devem ser separados por vírgula

```python
>>> print(soma(2, 3))

5
```

O que acontece se omitirmos um dos parâmetros:

O resultado é um `TypeError`, indicando que falta 1 argumento e qual o argumento que falta:

```python
>>> print(soma(2))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 13, in <module>
    print(soma(2))
TypeError: soma() missing 1 required positional argument: 'b'
```

#### Exemplo 2

Passando dois parâmetros para uma função que irá retornar a multiplicação destes dois parâmetros:

```python
>>> def multiplica(num1, num2):
	    return num1 * num2
```

Chamada da função:

```python
>>> print(multiplica(3, 5))

15
```

```python
>>> print(multiplica('Bruno ', 5))

Bruno Bruno Bruno Bruno Bruno
```

Omitir um dos valores causa um TypeError:

```python
>>> print(multiplica('Bruno '))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 13, in <module>
    print(multiplica('Bruno '))
TypeError: multiplica() missing 1 required positional argument: 'num2'
```

#### Exemplo 3

Passando 3 parâmetros para uma função:

```python
>>> def outra(num1, b, msg):
	    return (num1 + b) * msg
```

Chamada da função:

```python
>>> print(outra(3, 2, 'Bruno '))

Bruno Bruno Bruno Bruno Bruno
```

Omitir um dos valores causa um TypeError:

```python
>>> print(outra(3, 2))

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 13, in <module>
    print(outra(3, 2))
TypeError: outra() missing 1 required positional argument: 'msg'
```

---

### TypeError: missing _ required positional argument:

Passando argumentos a mais do que foi parametrizado:

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 13, in <module>
    print(soma(3, 2, 5))
TypeError: soma() takes 2 positional arguments but 3 were given
```

---

## Nomeando Funções e Parâmetros:

### Exemplo:

```python
>>> def nome_completo(string1, string2):
	    return f'Seu nome completo é {string1} {string2}.'
```

Repare que os parâmetros desta função foram nomeados como 'string1' e 'string2', algo bem genérico que alguém que não esteja envolvido no projeto vai olhar e não irá saber distinguir qual a diferença entre um e outro além de deduzir que qualquer tipo de dado do tipo string possa ser introduzido.

### Refatorando:

```python
>>> def nome_completo(nome, sobrenome):
	    return f'Seu nome completo é {nome} {sobrenome}.'
```

Aqui já podemos distinguir melhor a diferença de cada parâmetro facilitando o entendimento do código.

---

## Diferença entre Parâmetros e Argumentos:

Na definição da função os valores/variáveis informados dentro dos parênteses são chamados de **parâmetros** já no momento da chamada de função, os valores passados dentro dos parênteses são chamados de **argumentos**.

```python
#Definição de função = Criando uma função

>>> def nome_da_funcao(parâmetros):
			return retorna + alguma + coisa

# Chamada da função = Executando uma função

>>> nome_da_funcao(argumentos)
```

### A ordem dos parâmetros importam:

Em alguns casos dependendo do que a função executa em seu bloco de código, a ordem dos ARGUMENTOS não faz diferença, mas é importante ter em mente sempre que sim a ordem faz toda diferença:

```python
>>> def nome_completo(nome, sobrenome):
	    return f'Seu nome completo é {nome} {sobrenome}.'
```

Chamada da Função:

```python
>>> nome = 'Bruno'
>>> sobrenome = 'Oliveira'

>>> print(nome_completo(sobrenome, nome))

Seu nome completo é Oliveira Bruno.
```

### Argumentos Nomeados (Keyword Arguments)

Caso seja utilizado o nome dos parâmetros nos argumentos para informa-los, podemos utilizar qualquer ordem:

```python
>>> print(nome_completo(nome='Bruno', sobrenome='Oliveira'))
>>> print(nome_completo(nome=nome, sobrenome=sobrenome))
>>> print(nome_completo(sobrenome='Parker', nome='Peter'))

Seu nome completo é Bruno Oliveira.
Seu nome completo é Giovana de Moraes.
Seu nome completo é Peter Parker.
```

Ou seja podemos de forma literal passar os valores para cada parâmetro chamando os seus keywords no momento da chamada de função, dessa forma independente da ordem que for escrito a função será executada corretamente.

---

## Erro comum na utilização do Return:

Repare no código abaixo:

Essa função irá iterar uma lista de números e cada numero será executado a sua divisão por 2, se o resto desta divisão for diferente de 0 ele ira ser armazenado no total e para cada número em que o resto for diferente de 0 será somado, ao final ira retornar a soma de todos estes números em que a divisão por 2 o resto foi diferente de 0 ou seja a soma dos números impares:

```python
>>> def soma_impares(numeros):
	    total = 0
	    for num in numeros:
        if num % 2 != 0:
            total = total + num
            return total
```

Chamando a função:

```python
>>> lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(soma_impares(lista1))

Resultado:

1
```

O resultado não retornou o que era esperado.

O motivo é por que o return está identado na posição errada, ele irá finalizar apenas o if nesse caso, o certo é identar ele dentro do escopo do for, para que a função seja finalizada no for e retorne o resultado desejado:

```python
>>> def soma_impares(numeros):
	    total = 0
	    for num in numeros:
        if num % 2 != 0:
            total = total + num
      return total
```

Chamando a função:

```python
>>> lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> print(soma_impares(lista1))

Resultado:

25
```

---

## Usando outra função como parâmetro padrão:

Abaixo criaremos 2 funções, a primeira normal com parâmetros definidos e sem nenhum default, no segundo criaremos uma nova função que recebera um parâmetro padrão com a primeira função, e em seguida uma terceira função que poderá ser utilizada como argumento na segunda função, substituindo assim o parâmetro padrão:

```python
# Definindo a primeira função que terá como parâmetro 2 variáveis e retornará a soma destas 2
# variáveis.

>>> def soma(num1, num2):
		    return num1 + num2

# Definindo a segunda função que terá como parâmetro as mesmas 2 variáveis da primeira e uma
# terceira variável que receberá um argumento padrão que é a função som e retornaro resultado da
# função que for passada como argumento, se não for passado nenhuma então ela automáticamente
# assumira como padrão a função soma: 

>>> def mat(num1, num2, fun=soma):
		    return fun(num1, num2)

# Definindo uma terceira função que recebera como parâmetro 2 variáveis e retornará a 
# subtração dos valores das duas variáveis:

>>> def subtracao(num1, num2):
		    return num1 - num2
```

Com as funções definidas, agora chamaremos a função mat:

```python
>>> print(mat(2, 3))

5
```

Podemos observar que o a função mat automaticamente realizou a soma dos dois argumentos passados:

Como parametrizamos um função, podemos argumentar no momento da chamada, qualquer outra função que já tenha sido definida anteriormente e assim obter o resultado esperado:

```python
>>> print(mat(2, 2, subtracao))

0
```

Aqui passamos como argumento no parâmetro fun, a função já definida subtração, o resultado foi a subtração dos argumentos num1 e num2 conforme esperado.

---

## Escopo

### Variáveis globais:

Variáveis globais são variáveis criadas em no contexto global, ou seja, não está inserida em nenhum bloco de código:

```python
>>> exemplo = "Odin o Gato"

>>> def diz_miau():
			  return f'{exemplo} disse miau!'

>>> print(diz_miau())

Odin o Gato disse miau!
```

Aqui podemos observar que a variável definida de forma global, é completamente acessível em blocos de códigos.

Agora observe a seguir:

### Variáveis Locais

Variáveis locais são variáveis criadas dentro de um bloco de código especifico, geralmente podemos observar como característica a identação:

Usando o mesmo código temos:

```python
>>> exemplo = "Odin o Gato"

>>> def diz_miau():
		    exemplo = 'Pandora a Gata'
		    return f'{exemplo} disse miau!'

>>> print(diz_miau())

Pandora a Gata disse miau!
```

Ao ser criada uma variável com mesmo nome dentro do contexto da função, ou seja, no bloco da função, quando chamamos a função, ela automáticamente verifica primeiro dentro do escopo em que a função está inserida se a variável foi definida ali, se sim ela retorna o valor conforme o bloco de código da função pede, caso e linguagem não encontre nenhuma variável com o nome solicitado no bloco de código, dentro do escopo da função, então ela irá procurar um nível acima, que no caso do código acima é no contexto global.

Importante salientar que se a função acima estivesse inserida dentro de outra função o código iria procurar a variável primeiro na função mais interna, se não encontrasse, subiria um nível, procurando na função mais externa e caso não encontrasse ai sim iria procurar no contexto global.

---

### Acessando uma variável local:

Tentar acessar uma variável local, ou seja que está inserida em um contexto de um bloco de código, caracterizada por identação, causa um NameError:

```python
>>> def diz_miau():
		    exemplo = 'Pandora a Gata'
		    return f'{exemplo} disse miau!'

>>> print(diz_miau())
>>> print(exemplo)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 9, in <module>
    print(exemplo)
NameError: name 'exemplo' is not defined
```

Isso porque a variável só pode ser acessada dentro do contexto em que ela está inserida, nesse caso somente conseguimos acessar se primeiro invocarmos a função.

Observe o caso a seguir:

```python
>>> exemplo = "Odin o Gato"

>>> def diz_miau():
			  return f'{exemplo} disse miau!'

>>> print(diz_miau())
>>> print(exemplo)

Odin o Gato disse miau!
Odin o Gato
```

Isso porque a variável está em um contexto global, nesse contexto ela fica mais acessível.

---

### ATENÇÃO com Variáveis Globais:

>[!alert] 
>Evite criar variáveis no contexto global.

Uma demonstração do que pode acontecer se criarmos variáveis no contexto global e tentarmos inicializa-lá num contexto local:

```python
>>> total = 0

>>> def incrementa():
		    total = total + 1
		    return total

>>> print(incrementa())

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 9, in <module>
    print(incrementa())
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 5, in incrementa
    total = total + 1
UnboundLocalError: local variable 'total' referenced before assignment
```

### UnboundLocalError: local variable 'total' referenced before assignment

**Variável local 'total' referenciada antes da atribuição**

Isso quer dizer que estamos fazendo referencia a variável 'total' antes mesmo de realizarmos uma atribuição, na verdade o erro está aqui:

```python
total = total + 1
```

Estamos nos referindo a total antes mesmo dele receber uma atribuição, o certo seria se:

```python
total = 0
total = total + 1
```

Aqui conseguiríamos executar o código. Porém você deve estar se perguntando, mas a variável foi atribuída no inicio do código em contexto global.

Uma forma de contornar esta situação é com a palavra-chave `global`

```python
>>> total = 0

>>> def incrementa():
		    global total

		    total = total + 1
		    return total

>>> print(incremento())

1

>>> print(incremento())

2
```

Com a palavra-chave `global`, estamos dizendo a linguagem que queremos utilizar a variável no contexto global.

---

### Utilizando Variáveis um escopo acima:

Não é muito comum porém pode ser que você encontre algum código onde tenha função dentro de função:

```python
>>> def fora():
		    contador = 0
    
		    def dentro():
		        contador = contador + 1
			       return contador
		    return dentro()
```

No caso acima podemos identificar que a variável contador foi definida em um escopo superior ao local onde estamos fazendo referência a ela (contador = contador + 1).

Aqui teremos o mesmo erro `UnboundLocalError`

Porém ao mesmo tempo a variável não está no contexto global, ou seja, não podemos utilizar a palavra-chave `global` para fazer referência a ela.

A solução é utilizar a palavra-chave `nonlocal` o código ficará assim:

```python
>>> def fora():
		    contador = 0
    
		    def dentro():
						nonlocal contador
		        contador = contador + 1
			       return contador
		    return dentro()

>>> print(fora())

1
```

---

>[!alert] 
>Importante ressaltar que a função dentro não é reconhecida fora do escopo da função fora, portanto é impossível invocar a função separadamente - `NameError`

#function #função #funções #funçãocomparametro

---

# Funções com Parâmetro Padrão
Default Parameters:

São funções onde a passagem de parâmetro seja opcional:

Exemplo de função onde a passagem de parâmetro é opcional:

```python
>>> print('Bruno Oliveira')

>>> print()

Resultado:

Bruno Oliveira

```

Exemplo de função onde a passagem de parâmetro é obrigatória:

```python
>>> def quadrado(numero):
				return numero ** 2

>>> print(quadrado(3))
>>> print(quadrado())

Aqui o segundo print retornará um TypeError

```

## Criando uma função com Parâmetro Padrão:

No exemplo a seguir iremos criar uma função que executará uma potenciação de dois valores que serão passados como argumento, caso não seja passado nenhum argumento para o parâmetro do expoente, a função automaticamente irá atribuir como argumento o 2 para o expoente:

Exemplo função sem parâmetro padrão

```python
>>> def exponencial(numero, potencia):
				return numero ** potencia

>>> print(exponencial(2, 3))
>>> print(exponencial(3, 2))

8
9
```

Refatorando a função:

```python
>>> def exponencial(numero, potencia=2):
				return numero ** potencia

>>> print(exponencial(3))
>>> print(exponencial(3, 5))

9
243
```

Se o usuário passar somente um parâmetro este será atribuído ao parâmetro número e automaticamente será usado o valor padrão (2) na operação, caso o usuário passar 2 valores como argumento a operação será realizada elevando a variável número pelo argumento passado para potência.

É possível atribuir valores padrões para qualquer um dos parâmetros:

```python
>>> def exponencial(numero=2, potencia=2):
				return numero ** potencia

>>> print(exponencial(3))
>>> print(exponencial(3, 5))

```

Porém isso não é possível:

```python
>>> print(exponencial( , 3))

File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 5
    print(exponencial(,3))
                      ^
SyntaxError: invalid syntax
```

Em função python os parâmetros com valores padrão DEVEM sempre estar ao final da declaração:

```python
>>> def exponencial(numero=2, potencia):
				return numero ** potencia

>>> print(expoente(6))

File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1
    def exponencial(numero=2, potencia):
                    ^
SyntaxError: non-default argument follows default argument
```

Ou seja para parametrizar valores nos parâmetros SEMPRE começar atribuindo valores do último para o primeiro

---

## Por que utilizar parâmetros com valor default?

1.  Nos permite ser mais flexíveis nas funções;
2.  Evita erros com parâmetros incorretos
3.  Nos permite trabalhar com exemplos mais legíveis de código.

---

## Outros exemplos:
### Exemplo 1:

```python
>>> def soma(num1, num2):
				return num1 + num2

>>> print(soma(4,3)) # 7
>>> print(soma(4)) # TypeError
>>> print(soma()) # TypeError

```

### Exemplo 2:

```python
>>> def mostra_informacao(nome='Geek', instrutor=False)
				if nome == 'Geek' and instrutor:
						return 'Bem vindo instrutor Geek!'
				elif nome == 'Geek':
						return 'Eu pensei que você era o instrutor'
				return f'Olá {nome}'

>>> print(mostra_informacao())
>>> print(mostra_informacao('Geek'))
>>> print(mostra_informacao(True))
>>> print(mostra_informacao(instrutor=True))
>>> print(mostra_informacao('Bruno'))
>>> print(mostra_informacao('Bruno', instrutor=True))
>>> print(mostra_informacao('Geek', instrutor='Bruno'))

Eu pensei que você era o instrutor
Eu pensei que você era o instrutor
Olá True
Bem vindo instrutor Geek!
Olá Bruno
Olá Bruno
Bem vindo instrutor Geek!
```

Traduzindo a função: Se o argumento passado for 'Geek' e Instrutor for True, então retorna 'Bem vindo instrutor Geek!', se o argumento passar como argumento somente 'Geek' e qualquer outro argumento para instrutor ou até mesmo sua omissão, retornar 'Eu pensei que você era o instrutor.' e por fim se qualquer valor for passado como argumento para nome e instrutor (com exceção a 'Geek' e True) retorna 'Olá e o nome que foi passado'

Observe que no caso do instrutor foi necessário passar como parâmetro literalmente 'instrutor=True'

---

## Quais os tipos de dados permitidos como parâmetro default?

1.  Números
2.  Strings
3.  Floats
4.  Booleanos
5.  Listas
6.  Tuplas
7.  Dicionários
8.  Funções
9.  Etc.

#defaultparameter #parametropadrão #funções #funçãocomparametro 

