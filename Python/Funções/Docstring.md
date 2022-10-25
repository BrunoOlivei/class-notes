# O que é uma DocString:

DocString são comentários feitos no código, geralmente utilizando 3 aspas no começo do comentário e 3 aspas no final, para delimitar e indicar o que é comentário no código e o que não é.

O DocString é literalmente documentar, criar um manual, informar, partes importantes do código. Um exemplo de DocString (documentação) nós podemos ver utilizando o help para acessar algumas informações acerca de uma funcionalidade da linguagem:

```python
>>> help(print)

print(...)
    print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)

    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

## Exemplo 1:

A documentação pode ser usafa para descrever o que uma função faz:

```python
>>> def diz_oi():
		    """Uma função simples que retorna a string 'Oi!"""
		    return 'Oi!'

print(diz_oi())
```

Se importarmos no terminal a função diz_oi e executarmos o help dela:

```python
>>> help(diz_oi)
Help on function diz_oi in module curso:

diz_oi()
    Uma funþÒo simples que retorna a string 'Oi!
```

O resultado é exatamente o que foi escrito utilizando dentro das tres aspas. Dessa forma podemos com rápidez encontrar a documentação de determinada parte de um código sem a necessidade de percorrermos todas as linhas até encontrar.

Também é possível acessar a documentação utilizando a _propriedade_ `.__doc__`no terminal:

```python
>>> print(diz_oi.__doc__)
Uma função simples que retorna a string 'Oi!
```

## Exemplo 2

>[!Note] 
>📌 O Pycharm possui uma funcionálidade que auxilia muito a documentação no código. A partir do momento que você insere as três aspas duplas e pressiona o `enter,` o pycharm já automaticamente coloca algumas informações básicas sobre a função na qual o docstring está inserido:


```python
>>> def exponencial(numero, potencia=2):
		    """

		    :param numero:
		    :param potencia:
		    :return: 
		    """
```

Aqui podemos documentar o que a função faz, o que significa cada parâmetro e qual o retorno da função:

```python
>>> def exponencial(numero, potencia=2):
		    """
		    Funcao que retorna por padrão o quadrado de 'numero' ou 'numero a 'potencia' informada.
		    :param numero: Numero que desejamos gerar a potencia (base)
		    :param potencia: Valor que queremos que seja o exponencial ou seja potencializar o 'numero'
		    :return: retorna o exponencial de 'numero' por 'potencia' caso nao seja atribuido nenhum valor potencia = 2
		    """
		    return numero ** potencia
```

Ao chamar no terminal o help da função exponencial:

```python
>>> help(exponencial)
Help on function exponencial in module curso:

exponencial(numero, potencia=2)
    Funcao que retorna por padrÒo o quadrado de 'numero' ou 'numero a 'potencia' informada.
    :param numero: Numero que desejamos gerar a potencia (base)
    :param potencia: Valor que queremos que seja o exponencial ou seja potencializar o 'numero'
    :return: retorna o exponencial de 'numero' por 'potencia' caso nao seja atribuido nenhum valor potencia = 2
```

#function #funções #docstring #documentation 