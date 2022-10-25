# Introdução

A linguagem python permite realizar a leitura (acesso) a arquivos e ler o conteúdo deste arquivo, poderia ser um arquivo contendo uma obra literária, um artigo científico, notícias, ou uma simples frase.

Para leitura de um conteúdo de um arquivo em Python utiliza-se a função integrada `open()`.

# Sintaxe:

open(*file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None*)

1. *file*: é um objeto caminho, ele fornece o caminho para no diretório para acesso ao arquivo, é descrito em forma de string ou seja entre aspas simples ou duplas
2. *mode*: é uma string opcional que especifica o modo como o arquivo será aberto, no caso de sua omissão o valor padrão é 'r'
| Caractere | Siginificado |
| --- | --- |
| 'r' | Abre para leitura (padrão) |
| 'w' | Abre para escrita, truncando o arquivo primeiro (removendo tudo o que estiver contido no mesmo) ou seja deleta tudo e escreve em cima |
| 'x' | Abre para criação exclusiva, falhando caso o arquivo exista |
| 'a' | Abre para escrita, anexando ao final do arquivo caso o mesmo exista, adiciona texto em um arquivo que já possua algo inserido. |
| 'b' | Abre o conteúdo do arquivo em binário, ideal para arquivos que não possuam texto. |
| 't' | Modo texto (padrão) |
| '+' | Abre para atualização (leitura e escrita) |
3. *buffering* é um inteiro opcional usado para definir a política de buffering. Passe o valor 0 para desativar o buffering (permitido somente em modo binário), passe 1 para selecionar buffering de linha (permitido somente em modo texto), e um inteiro > 1 para indicar o tamanho em bytes de um buffer com tamanho fixo. Quando nenhum valor é fornecido no argumento *buffering*, a política de buffering padrão funciona conforme as seguintes regras:
    - Arquivos binários são armazenados em pedaços de tamanho fixo; o tamanho do buffer é escolhido usando uma heurística que tenta determinar o “tamanho de bloco” subjacente do dispositivo, e usa `[io.DEFAULT_BUFFER_SIZE](https://docs.python.org/pt-br/3/library/io.html#io.DEFAULT_BUFFER_SIZE)` caso não consiga. Em muitos sistemas, o buffer possuirá tipicamente 4096 ou 8192 bytes de comprimento.
    - Arquivos de texto “interativos” (arquivos para os quais `[isatty()](https://docs.python.org/pt-br/3/library/io.html#io.IOBase.isatty)` retornam `True`) usam buffering de linha. Outros arquivos de texto usam a política descrita acima para arquivos binários.
4. *enconding* é o nome da codificação usada para codificar ou decodificar o arquivo, exemplo: UTF-8
5. *errors* é uma string opcional que especifica como erros de codificação e de decodificação devem ser tratados — isso não pode ser utilizado no modo binário. Uma variedade de tratadores de erro padrão estão disponíveis (listados em [Error Handlers](https://docs.python.org/pt-br/3/library/codecs.html#error-handlers)), apesar que qualquer nome para tratamento de erro registrado com `[codecs.register_error()](https://docs.python.org/pt-br/3/library/codecs.html#codecs.register_error)` também é válido. Os nomes padrões incluem:
    - `'strict'` para levantar uma exceção `[ValueError](https://docs.python.org/pt-br/3/library/exceptions.html#ValueError)` se existir um erro de codificação. O valor padrão `None` tem o mesmo efeito.
    - `'ignore'` ignora erros. Note que ignorar erros de código pode levar à perda de dados.
    - `'replace'` faz um marcador de substituição (tal como `'?'`) ser inserido onde existem dados malformados.
    - `'surrogateescape'` representará quaisquer bytes incorretos, conforme códigos apontados na área privada de uso da tabela Unicode, indo desde U+DC80 até U+DCFF. Esses códigos privados serão então convertidos de volta para os mesmos bytes quando o tratamento de erro para `surrogateescape` é usado ao escrever dados. Isto é útil para processar arquivos com uma codificação desconhecida.
    - `'xmlcharrefreplace'` é suportado apenas ao gravar em um arquivo. Os caracteres não suportados pela codificação são substituídos pela referência de caracteres XML apropriada `&#nnn;`.
    - `'backslashreplace'` substitui dados malformados pela sequência de escape utilizando contrabarra do Python.
    - `'namereplace'` (também é suportado somente quando estiver escrevendo) substitui caractere não suportados com sequências de escape `\N{...}`.
6. *newline* controla como o modo de [novas linhas universais](https://docs.python.org/pt-br/3/glossary.html#term-universal-newlines) funciona (se aplica apenas ao modo texto). Ele pode ser `None`, `''`, `'\n'`, `'\r'` e `'\r\n'`. Ele funciona da seguinte forma:
    - Ao ler a entrada do fluxo, se *newline* for `None`, o modo universal de novas linhas será ativado. As linhas na entrada podem terminar em `'\n'`, `'\r'` ou `'\r\n'`, e são traduzidas para `'\n'` antes de retornar ao chamador. Se for `''`, o modo de novas linhas universais será ativado, mas as terminações de linha serão retornadas ao chamador sem tradução. Se houver algum dos outros valores legais, as linhas de entrada são finalizadas apenas pela string especificada e a finalização da linha é retornada ao chamador sem tradução.
    - Ao gravar a saída no fluxo, se *newline* for `None`, quaisquer caracteres `'\n'` gravados serão traduzidos para o separador de linhas padrão do sistema, `[os.linesep](https://docs.python.org/pt-br/3/library/os.html#os.linesep)`. Se *newline* for `''` ou `'\n'`, nenhuma tradução ocorrerá. Se *newline* for um dos outros valores legais, qualquer caractere `'\n'` escrito será traduzido para a string especificada.

[[Modos de Abertura de Arquivos]]

## Tipo de objeto:

Com o arquivo criado e utilizando a função open para atribuir o objeto a uma variável, solicitamos a impressão direta desta variável e o tipo dela:

```python
>>> arquivo = open('texto.txt')

>>> print(arquivo)

<_io.TextIOWrapper name='texto.txt' mode='r' encoding='cp1252'>

>>> print(type(arquivo))

<class '_io.TextIOWrapper'>
```

Observamos que se trata de um objeto com uma classe específica. A impressão do objeto diretamente não trás como resultado o texto contido no arquivo.

## Imprimindo o texto

Para impressão do texto no console é necessário utilizar a função `.read()` 

```python
>>> print(arquivo.read())

A expressão governo aberto (open government) refere-se a projetos e ações que visam à promoção da transparência, à luta
contra a corrupção, ao incremento da participação social e ao desenvolvimento de novas tecnologias, de modo a tornar os
governos mais abertos, efetivos e responsáveis.
```

<aside>
⚠️ A função `.read()` transcorre e lê todo o conteúdo do arquivo e retorna uma string.

</aside>

```python
>>> ret = arquivo.read()

>>> print(type(ret))

<class 'str'>
```

## Comando `with`

O comando `with` cria um bloco de código que gera um contexto, através dele é possível operacionalizar algumas funções e ao final de seu bloco tudo que foi feito é automaticamente encerrado, com isso podemos utiliza-lo para abrir documentos, trabalhar com eles e encerrar a conexão automaticamente. 

Considerado o bloco de contexto, muito utilizado para manipulação de arquivos de leitura e escrita como o CSV. 

```bash
with open("dados/contatos.csv", encoding='latin-1') as arquivo:
```

Além de arquivos, podemos utilizar o `with` para gerenciar processos que precisam de uma pré e pós condição de execução; por exemplo: abrir e fechar o arquivo, realizar conexão com o banco de dados, sockets, entre outros.

```python
>>> with open('texto.txt') as arquivo:
		    print(arquivo.readlines())

['A expressÃ£o governo aberto (open government) refere-se a projetos e aÃ§Ãµes que visam Ã\xa0 promoÃ§Ã£o da transparÃªncia, Ã\xa0 luta\n', 'contra a corrupÃ§Ã£o, ao incremento da participaÃ§Ã£o social e ao desenvolvimento de novas tecnologias, de modo a tornar os\n', 'governos mais abertos, efetivos e responsÃ¡veis.\n']
```

Utilizando a função `closed` podemos checar se o arquivo está fechado:

```python
>>> print(arquivo.closed)

True

```


>[!tip]
>Esta é a forma recomendada (Pythonica) de se trabalhar com arquivos

## Escrevendo em arquivos

Conforme vimos anteriormente, a função open possui alguns argumentos que podem ser informados para o modo como o arquivo será aberto, dentre eles está o modo padrão que abre o arquivo somente para a leitura, e alguns modos que permitem a escrita no arquivo. 

---

## Utilizando o 'w':

Passando como argumento para o mode o 'w' no momento de abrir um arquivo. Quando o 'w' é informado na abertura de um arquivo, se este arquivo não existe ele automaticamente o cria escrevendo o que se deseja nele:

```python
>>> with open('novo.txt', 'w') as arquivo:
		    arquivo.write('Este é um exemplo de um arquivo criado dentro de um programa python\n')
		    arquivo.write('Para isso utilizamos a função open() com o arqumento "w" para o mode\n')
		    arquivo.write('Com isso a linguagem criou automaticamente o arquivo e inseriu este texto nele\n')
```

O resultado no console não retorna nada. Podemos observar o resultado abrindo o documento:

```python
>>> with open('novo.txt') as resultado:
		    print(resultado.read())

Este é um exemplo de um arquivo criado dentro de um programa python
Para isso utilizamos a função open() com o arqumento "w" para o mode
Com isso a linguagem criou automaticamente o arquivo e inseriu este texto nele
```

---

## Escrevendo com .write()

Para inserir algum texto em um arquivo, utilizamos o `.write()`, está função retorna automaticamente o número de caracteres escritos no arquivo. 

Um detalhe importante está no tipo de objeto permitido para escrita, o write só permite strings ou bytes, portanto todos os outros objetos devem ser convertidos para string antes de utilizarmos o write:

```python
>>> value = ('the answer', 42)
>>> s = str(value)  # convert the tuple to string
>>> f.write(s)
```

Se tentarmos passar algum outro objeto que não seja uma string no write teremos um `TypeError`

---

>[!Info]
>Importante ressaltar que ao abrir um arquivo no modo 'w', nós podemos escrever nele e caso o arquivo não exista ele será automaticamente criado. Caso o arquivo já exista e escrevermos algo novo, todo conteúdo anterior será perdido.


# Módulo CSV

O módulo CSV traz muitas facilidades para leitura e escrita de arquivos csv. No quesito leitura através do método `csv.reader()`, podemos passar um arquivo CSV e o resultado desse método será um objeto `<class '_csv.reader'>`

```python
import csv

caminho = "dados/contatos.csv"
encoding = "latin-1"

with open(caminho, encoding=encoding) as arquivo:
    leitor = csv.reader(arquivo)

    print(type(leitor))
```

```python
<class '_csv.reader'>
```

O objeto `csv.reader` é um iterável, ou seja, podemos utilizar um laço for para fazer a leitura do seu conteúdo e temos como resultado:

```python
for linha in leitor:
        print(linha)
```

```python
['1', 'Guilherme', 'guilherme@guilherme.com.br']
['2', 'Elias', 'elias@elias.com.br']
['3', 'Gabriel', 'gabriel@gabriel.com.br']
['4', 'Anderson', 'anderson@anderson.com.br']
['5', 'Alex', 'alex@alex.com.br']
['6', 'Vini', 'vini@vini.com.br']
['7', 'Letícia', 'leticia@leticia.com.br']
['8', 'Giulia', 'giulia@giulia.com.br']
['9', 'Felipe', 'felipe@felipe.com.br']
['10', 'Luísa', 'luisa@luisa']
```

Listas com os elementos em cada coluna do arquivo CSV separados, sendo assim, sabendo quais são as colunas e qual a posição delas dentro da lista, podemos facilmente atribuir valores a variáveis que poderão ser utilizadas para operações diversas.

```python
for linha in leitor:
	  id, nome, email = linha
	  contato = Contato(id, nome, email)
	  contatos.append(contato)
```

# 🥒 Pickle

Pickle em Python é usado principalmente para serializar e desserializar uma estrutura de objeto Python. Em outras palavras, é o processo de conversão de um objeto Python em um fluxo de bytes para armazená-lo em um arquivo / banco de dados, manter o estado do programa nas sessões ou transportar dados pela rede. O fluxo de bytes em conserva pode ser usado para recriar a hierarquia do objeto original removendo o fluxo. Todo esse processo é semelhante à serialização de objetos em Java ou .Net.

O primeiro passo é importar a biblioteca `pickle`

```python
import pickle
```

Em seguida criamos uma função que irá serializar os dados do arquivo CSV, utilizando o método `dump` do pickle.

```python
def contato_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as arquivo:
        pickle.dump(contatos, arquivo)
```

Dessa forma, podemos invocar a função passando como argumento um objeto python no nosso caso vamos passar os contatos e criar um arquivo de extenção `.pickle` padrão para esse método. 

```python
contatos_uteis.contato_para_pickle(contatos, 'dados/contato.pickle')
```

O conteúdo do arquivo é binário e humanamente impossível de ler:

```python
��.      ]�(�contato��Contato���)��}�(�id��1��nome��	Guilherme��email��guilherme@guilherme.com.br�ubh)��}�(h�2�h�Elias�h
�elias@elias.com.br�ubh)��}�(h�3�h�Gabriel�h
�gabriel@gabriel.com.br�ubh)��}�(h�4�h�Anderson�h
�anderson@anderson.com.br�ubh)��}�(h�5�h�Alex�h
�alex@alex.com.br�ubh)��}�(h�6�h�Vini�h
�vini@vini.com.br�ubh)��}�(h�7�h�Letícia�h
�leticia@leticia.com.br�ubh)��}�(h�8�h�Giulia�h
�giulia@giulia.com.br�ubh)��}�(h�9�h�Felipe�h
�felipe@felipe.com.br�ubh)��}�(h�10�h�Luísa�h
�luisa@luisa�ube.
```

Podemos utilizar esse arquivo para retornar os nossos dados, ou seja, podemos receber um arquivo `pickle` e retornar os dados dele. 

>[!danger]
>Importante ressaltar que arquivos pickle podem conter códigos maliciosos, que ao serem desserializados podem rodar esses códigos e corromper a máquina, portanto é importante ter ciência da origem do arquivo pickle.

Agora vamos criar a função que recebe como parâmetro o endereço de onde se encontra o arquivo pickle e utilizando o método `load` retornar os dados:

```python
def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos
```

Em seguida fazemos a chamada da função: 

```python
contatos = contatos_uteis.pickle_para_contatos('dados/contato.pickle')
```

Como a função retorna os contatos, temos como resultado no terminal:

```python
1 - Guilherme - guilherme@guilherme.com.br
2 - Elias - elias@elias.com.br
3 - Gabriel - gabriel@gabriel.com.br
4 - Anderson - anderson@anderson.com.br
5 - Alex - alex@alex.com.br
6 - Vini - vini@vini.com.br
7 - Letícia - leticia@leticia.com.br
8 - Giulia - giulia@giulia.com.br
9 - Felipe - felipe@felipe.com.br
10 - Luísa - luisa@luisa
```

Seguindo os mesmos padrões que foram serializados. 

**Para saber mais sobre:**

[Python pickling: What it is and how to use it securely | Synopsys](https://www.synopsys.com/blogs/software-security/python-pickling/)

---