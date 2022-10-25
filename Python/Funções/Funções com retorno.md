# Return

Algumas funções apensar de terem um resultado podem não retornar nada, existe uma diferença entre o retorno e o resultado.

O retorno é quando algum dado pode ser atribuído a uma nova variável e posteriormente usado em novas funções ou outras variáveis.

```python
>>> numeros = [1, 2, 3]

>>> ret_pop = numeros.pop()  # remove o último elemento da lista

>>> print(f'Retorno de pop: {ret_pop}')  # 3, pop é uma função que retorna

>>> ret_pr = print(numeros)  # print é uma função que não retorna nada, assim como clear, entre outras.

>>> print(numeros)

Retorno de pop: 3
[1, 2]
[1, 2]
49
Retorno de None
```

`print` é um exemplo de função que não retorna nada, ela somente exibe algum dado.

Quando uma função não retorna nenhum valor, o retorno é `none`

>[!warning] 
>Refatorar, é um verbo usado na programação para dizer reescrever um código

Exemplo:

```python
>>> def quadrado_de_sete():
	print(7 * 7)  # Imprime o resultado de 7 vezes 7

>>> ret = quadrado_de_sete() 

>>> print(f'Retorno de {ret}') # none
```

Refatorando:

```python
>>> def quadrado_de_sete():
	return 7 * 7

>>> ret = quadrado_de_sete()

>>> print(f'Retorno de {ret}')

Retorno de 49
```

>[!warning]
>Não precisamos necessariamente criar uma variável para receber o retorno de uma função, podemos passa a execução da função para outras funções, isso quer dizer que sabendo qual é o resultado que irá retornar de uma função ela pode ser usada em outras funções que utilizaram o valor retornado.

```python
def diz_oi():
    return 'Oi '

alguem = 'Bruno!'
print(diz_oi() + alguem)
```

No exemplo acima podemos observar a importância do `return`, se queremos utilizar o resultado de uma função o `return` é peça fundamental para que seja possível, observe a omissão do `return`:

```python
>>> def diz_oi():
	print('Oi ')

>>> alguem = 'Bruno!'
>>> print(diz_oi() + alguem)

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 26, in <module>
    print(diz_oi() + alguem)
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
```

Impossível realizar qualquer coisa com o retorno `none`

-   `return` finaliza a função ou seja ela sai da execução da função;

```python
>>> def diz_oi():
	print('Estou sendo executado antes do return')
	return 'Oi'
>>> print('Estou sendo executado depois do return')

>>> diz_oi()
```

Aqui um exemplo de como o `return` se comporta, o print 'Estou sendo executado antes do return' somente será exibido quando a função for chamada, enquanto o print 'Estou sendo executado depois do return' é executado independente da chamada da função ou não, já que ele está além do `return` o que o torna fora do escopo da função.

-   Podemos ter, em uma função diferentes returns;

```python
>>> def nova_funcao():
	variavel = True
	if variavel:
		return 4
	elif variavel is None:
		return 3.2
	return 'b'
```

Nesse exemplo enquanto o valor de 'variável' for True o código irá executar somente até a linha 4, e o retorno será o valor 4. Caso o valor da variável for None, o código ira executar a primeira parte do bloco, irá identificara que não é true e prosseguira chegando a linha 5, aqui está o None portanto o código irá retornar 3.2 e não executará mais nada.

Quando o valor da variável mudar para False, o código irá percorrer todo o bloco até o final e retornará o valor b.

-   Podemos, em uma função, retornar qualquer tipo de dado e até mesmo múltiplos valores;

```python
>>> def outra_funcao():
	return 2, 3, 4, 5

>>> print(outra_funcao())

(2, 3, 4, 5)
```

Aqui podemos observar que o código pode retornar múltiplos valores, eles também podem ser armazenados em diversas variáveis.

## Jogo Cara ou Coroa:

```python
# função para jogar uma moeda cara ou coroa

>>> from random import random

>>> def joga_moeda():
	if ramdom() > 0.5: # Gera um número pseudo randômico entre 0 e 1
		return 'Cara'
	return 'Coroa'

>>> print(joga_moeda())
```

É possível fazer o import de uma função no terminal:

```python
# Nesse exemplo ao invés de estarmos utilzando o SCRIPT estaremos utilizando o terminal direto:

from curso import joga_moeda
```

Onde 'curso' é o nome do arquivo python cujo a função 'joga_moeda' foi definida.

A partir disso é possível utilizar a função direto no terminal (interativo).

## Uso excessivo do else:

```python
>>> def eh_impar():
	numero = 5
	if numero % 2 != 0:
		return True
	else:
		return False

>>> print(eh_impar())
```

No exemplo acima o else não é necessário já que o retorno da função só pode ser ou um ou outro valor (True ou False), portanto o else é implícito e não necessita ser descrito.

O certo:

```python
>>> def eh_impar():
	numero = 5
	if numero % 2 != 0:
		return True
	return False

>>> print(eh_impar())
```

---
#return #returnfunction #funçõescomretorno 