# Estrutura de uma sinalização de erro (PyCharm)

É claro que cada IDE possui seu mecanismo para ajudar o programador a encontrar erros, no caso do PyCharm, o alerta de erro exibido é igual ao de baixo. Basicamente em todas as IDEs possíveis de se trabalhar com python o alerta de erro será muito parecido.

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1, in <module>
    printf("Bruno Oliveira")
NameError: name 'printf' is not defined
```

## Traceback:

Saída de erros

## File:

Indica em qual arquivo está o comando com erro, imaginando que estejamos trabalhando em um projeto com inúmeros arquivos que se comunicam um com o outro, o file ajuda a localizar exatamente onde está o erro, além de informar qual o arquivo, também indica em qual linha de código está o erro (line).

## Comando:

Em seguida ele imprime no console o comando escrito que está o erro, no exemplo acima é: `printf('Bruno Oliveira')`

## Erro:

Aqui ele indica que tipo de erro é, alguns exemplos:

-   TypeError
-   NameError
-   SyntaxError
-   ZeroDivisionError
-   RuntimeError
-   OSError

No nosso exemplos ele indica que `printf` não está definida, ou seja ele não reconhece essa palavra nem qualquer função que ela poderia exercer.

---

# Funcionalidades do PyCharm para Erros:

No Pycharm, quando um erro é alertado, na linha onde ele indica o arquivo (file) é possível através do link que a IDE criou, ao clicar você é levado até o arquivo e a linha onde se encontra o código com erro.

Na linha de código errada, aparece uma lâmpada que ao clicar surge uma janela com algumas sugestões do pychar para o que pode ser feito para corrigir, alguns exemplos:

-   Creat function: sugere criar a função para o nome que não foi definido.
-   Rename Reference: renomear a referência buscando alguma variável que já tenha sido definida
-   Ignorar
-   Mark unresolved

---

>[!warning]
>É de suma importância prestar atenção e aprender a ler as saídas de erros geradas pela execução.

# Erros mais comuns:

## SyntaxError:

Ocorre quando o Python encontra um erro de syntaxe, significa que algo foi escrito que o Python não reconhece como parte da linguagem, da estrutura esperada dentro daquela linha ou bloco de código.

### Exemplo 1:

Vamos definir uma função:

```python
>>> def funcao:
		    print('Bruno Oliveira')
```

Ao executar o código recebemos o seguinte erro:

```python
File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1
    def funcao:
              ^
SyntaxError: invalid syntax
```

O erro acima é um pouco diferente do que vimos anteriormente, porém apresenta as mesmas informações necessárias para o tratamento:

-   File: sinaliza qual o arquivo e a linha de código onde encontra-se o erro:
-   Comando: mostra qual comando foi escrito que está errado
-   Sinalização ^: demonstra exatamente onde se encontra o erro, no caso acima indica que está nos dois pontos ( : )
-   Nome do Erro: sinaliza o tipo de erro que foi gerado, no caso SyntaxError.

---

Podemos observar no exemplo acima que a SyntaxError ocorreu por que o código escrito está faltando elementos que compõem a definição de uma função, no caso desse exemplo, o que faltou foram os parênteses entre o `nome_da_função` e os dois pontos ( : )

```python
>>> def funcao():
		    print('Bruno Oliveira')
```

Agora sim nenhum erro é gerado.

### Exemplo 2:

Definindo uma variável utilizando uma palavra reservada da linguagem Python:

```python
>>> None = 1
```

Utilizando uma palavra reservada como o None para atribuir um valor como se fosse uma variável, temos o seguinte erro:

```python
File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1
    None = 1
    ^
SyntaxError: cannot assign to None
```

Como podemos observar também se trata de um erro de sintaxe (SyntaxeError) pois não podemos atribuir valor como se fosse uma variável a um elemento cujo o nome é uma palavra reservada da linguagem Python.

-   O alerta de erro traz o File indicando qual arquivo e dentro dele qual linha de código está localizado o erro.
-   O comando que está errado.
-   O sinal ^ indicando onde está o erro no comando
-   O nome do erro e o motivo.

### Exemplo 3:

Colocando a palavra return fora de uma função:

```python
>>> return
```

A palavra reservada return fora do escopo de uma função gera um erro de sintaxe (SyntaxeError):

```python
File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1
    return
    ^
SyntaxError: 'return' outside function
```

Como podemos observar a palavra reservada return é esperada dentro do escopo de uma função, utilizá-la fora disso retorna o SyntaxeErro

-   Alerta de erro com File indicando qual o arquivo e a linha de código está localizado o erro
-   Comando que está errado
-   O sinal ^ indicando onde no comando está o erro
-   O nome do erro e o motivo.

---

## NameError:

NameError é acusado pela linguagem quando uma variável ou função não foi definida anteriormente:

### Exemplo 1:

Solicitando a impressão de uma suposta variável:

```python
>>> print(geek)
```

O nome geek não foi definido em momento algum, pedir para executá-lo em uma função como o print por exemplo causa o NameError:

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1, in <module>
    print(geek)
NameError: name 'geek' is not defined
```

Como podemos observar o nome geek não está definido:

-   Alerta de erro mais recente;
-   File indicando o arquivo e a linha de código onde se encontra o erro;
-   O comando que está errado
-   O tipo de erro, no caso NameError, explicando o motivo.

### Exemplo 2:

Chamando uma função que não foi definida préviamente

```python
>>> geek()
```

Como sabemos, a syntaxe para a chamada de uma função é nome_da_função( ), no caso acima não haviamos definido anteriormente a função, por isso é indicado um NameError

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1, in <module>
    geek()
NameError: name 'geek' is not defined
```

Como podemos objservar o NameError aqui é muito parecido com o anterior pois não houve a definição do 'geek':

-   Alerta de erro mais recente;
-   File indicando o arquivo e a linha de código onde se encontra o erro;
-   O comando que está errado
-   O tipo de erro, no caso NameError, explicando o motivo.

### Exmplo 3:

Utilizando um bloco if definindo uma variável local e tentando acessá-la globalmente:

No exemplo abaixo estamos definindo uma variável chamada 'a' que recebe o valor de 8.

Abrimos um bloco de código if onde se 'a' é menor que 10, a variável 'msg' recebe a string "É menor que 10"

Fora do bloco, ou seja, no escopo global, tentamos imprimir a variável 'msg'

```python
>>> a = 8

>>> if a < 10:
		    msg = "É menor que 10"

>>> print(msg)
```

Resultado:

```python
É menor que 10
```

Ocorreu tudo normal, agora se alterarmos o valor da variável 'a' para 18 e tentarmos executar o mesmo código:

```python
>>> a = 18

>>> if a < 10:
		    msg = "É menor que 10"

>>> print(msg)
```

Como o valor da variável 'a' é maior que 10, a condição if não irá executar o código já que 'a' não se encaixa no se 'a' for menor que 10.

Sendo assim ele não dará continuidade ao codigo a seguir dentro do escopo do bloco If e não atribuirá a string "É menor que 10" a variável 'msg'

Quando tentarmos imprimir a variável 'msg' que não foi atribuida, teremos um NameError

```python
Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 6, in <module>
    print(msg)
NameError: name 'msg' is not defined
```

Resumindo, blocos de código com condições que não são executados graças a essas condições, pode gerar um erro caso seja solicitado a chamada de uma variável ou função, no escopo global, que esteja dentro do bloco de código que não foi executado graças a condição estabelecida

-   Alerta de erro mais recente;
-   File indicando o arquivo e a linha de código onde se encontra o erro;
-   O comando que está errado
-   O tipo de erro, no caso NameError, explicando o motivo, que no caso indica que 'msg' não foi definido.

---

>[!warning]
>A única maneira de fugir do NameError é declarando anteriormente a variável ou a função.

#error #erro
