# Introdução:

A função `seek()` é utilizada para movimentar o cursor pelo arquivo.

Conforme vimos na utilização da função read(), todo o conteúdo existente num arquivo é lido em toda a sua extensão, caso seja solicitado novamente por exemplo a impressão do conteúdo não terá resultado nenhum, uma vez que o cursor já percorreu todo o arquivo e se encontra no final dele.

```python
>>> print(arquivo.read())

A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
governos mais abertos, efetivos e responsáveis.
```

Tentando imprimir uma segunda vez:

```python
>>> print(arquivo.read())

```

Nenhum resultado é mostrado.

Na função read, também é possível atribuir uma posição limite, ou seja, ela deve ler o arquivo até a posição determinada e encerrar ali:

```python
>>> print(arquivo.read(44))

A expressão governo aberto (open government)
```

---

# Utilizando o seek

Se utilizarmos o seek para retornar até a posição inicial do arquivo texto, podemos imprimir novamente:

```python
>>> print(arquivo.read())

A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
governos mais abertos, efetivos e responsáveis.

>>> arquivo.seek(0)

>>> print(arquivo.read())

A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
governos mais abertos, efetivos e responsáveis.
```

O argumento passado entre parênteses na função seek, refere-se a posição desejada, podemos atribuir outros valores de acordo com a posição que desejamos que o cursor assuma, para isso devemos lembrar que o resultado do read é uma string única, onde cada caractere possui sua posição definica:

```python
>>> nome = "Hal Jordan"

>>> print(nome[0])

H
```

```python
>>> arquivo.seek(28)

>>> print(arquivo.read())

(open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
governos mais abertos, efetivos e responsáveis.
```

## readline()

Esta função retorna a leitura de cada linha do arquivo:

```python
>>> print(arquivo.readline())

A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
```

A cada execução o cursor inicia na nova linha e finaliza na próxima, ou seja, se a função for chamada mais uma vez o resultado que teremos será a próxima linha do texto:

```python
>>> print(arquivo.readline())

contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
```

Também é possível atribuir um valor como argumento para que a função leia até determinada posição, fazendo isso caso a função seja chamada novamente, ela assumira que a nova linha começa de onde parou baseado na limitação atribuída por argumento na função readline anterior:

```python
>>> print(arquivo.readline(11))

A expressão

>>> print(arquivo.readline())

governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
```

## readlines()

Cria uma lista com cada linha do texto sendo um elemento:

```python
>>> ret = arquivo.readlines()
>>> print(type(ret))

<class 'list'>
```

```python
>>> print(arquivo.readlines())

['A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta\\n', 'contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os\\n', 'governos mais abertos, efetivos e responsáveis.\\n']
```

## close()

A cada chamada da função open para algum arquivo, cria-se uma conexão entre o computador e o programa, essa conexão é chamada de streaming. Sempre que os trabalho com aquele programa ou arquivo for finalizado, é necessário que a conexão seja encerrada, para isso usa-se a função `close()`

Isso é necessário para evitar conflitos de versões do arquivo ou até mesmo de utilização, sendo que em alguns casos é bloqueado o acesso ao mesmo arquivo por outros meios ou pessoas.

O processo é muito simples:

```python
>>> arquivo.close()
```

## closed

Verifica se o arquivo em questão está fechado ou não retornando `True` se fechado e `False` se aberto.

```python
>>> print(arquivo.closed)

False
```

#seek #cursor #open #close