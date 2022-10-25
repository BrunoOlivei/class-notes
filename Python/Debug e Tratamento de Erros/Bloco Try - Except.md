# Try / Except

Bloco `try/except` é utilizado para tratar erros que podem ocorrer no código, Prevenindo que o programa pare de funcionar e o usuário receba mensagens de erro inesperados.

A forma geral mais simples é:

```python
try:
	//execução problemática
except:
	//o que deve ser feito em caso de problemas
```

## Exemplo 1:

Tentando executar uma função que não foi definida previamente:

```python
>>> bruno()

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1, in <module>
    bruno()
NameError: name 'bruno' is not defined
```

Utilizando o bloco Try / Except para tratar o erro:

```python
try:
    bruno()
except:
    print('Deu um problema aqui!')

Deu um problema aqui!
```

A forma acima é para tratamento de erro genérico, todos os erros básicos da linguagem serão tratados por este bloco.

O ideal na programação de python é tratar o erro de forma especifica:

## Exemplo 2:

```python
try:
    bruno()
except NameError:
    print('Deu um problema aqui!')
```

Nesse caso se o erro na tentativa de execução for diferente de NameError, ele não será tratado e o código pode parar.

## Exemplo 3:

Tratando um erro e aplicando os detalhes do erro na mensagem

```python
try:
    bruno()
except NameError as err:
    print(f'A aplicação gerou o erro: {err}!')

A aplicação gerou o erro: name 'bruno' is not defined!
```

## Exemplo 4:

```python
try:
    bruno()
except NameError as erra:
    print(f'A aplicação gerou um NameError: {erra}!')
except TypeError as errb:
    print(f'A aplicação gerou um TypeError: {errb}')
except:
    print('A Aplicação gerou um erro desconhecido')
```

## Exemplo 5:

Tratando erros dentro de uma função:

```python
def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None

dic = {'nome': 'Bruno'}

print(pega_valor(dic, 'nome'))
print(pega_valor(dic, 'game'))

Bruno
None
```

---

# Try, Except, Else e Finally
Saber quando e onde tratar o código:

Toda entrada de dados deve ser tratada.

## Utilizando o else:

```python
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
```

Resultado:

```python
Informe um número: 42
Você digitou 42

Informe um número: abc
Valor incorreto
```

O else serve para executar o código caso o erro não haja erro na entrada do dado. Dessa forma o programa entrega o resultado desejado e ao mesmo tempo trata o erro quando ocorrer.

## Finally

O bloco finally sempre é executado, independente se houve exceção ou não:

```python
try:
    num = int(input('Informe um número: '))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
finally:
    print('Executando o Finally')
```

Resultado:

```python
Informe um número: 42
Você digitou 42
Executando o Finally

Informe um número: abc
Valor incorreto
Executando o Finally
```

## Utilização:

O `finally` geralmente é utilizado para fechar ou desalocar um recurso, por exemplo um banco de dados, a partir do momento que não há mais a necessidade de acesso a determinado banco de dados, o `finnaly` entra em ação para encerrar o acesso.

## Exemplos:

### Exemplo 1:

Forma pythonica de tratar erros é dentro da função, sendo possível também já tratar o dado recebido:

```python
 def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Incorreto'
    except ZeroDivisionError:
        return 'Não é possível dividir um número por zero'

num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

print(dividir(num1, num2))
```

Resultado:

```python
Digite um número: 8
Digite um número: 0
Não é possível dividir um número por zero
```

### Exemplo 2:

Tratando os erros de forma semi-genérica:

```python
def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um erro: {err}'

num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

print(dividir(num1, num2))
```

Resultado:

```python
Digite um número: 4
Digite um número: 2
2.0

Digite um número: 4
Digite um número: b
Ocorreu um erro: invalid literal for int() with base 10: 'b'

Digite um número: 4
Digite um número: 0
Ocorreu um erro: division by zero
```

---

#try #else #finally #except #error