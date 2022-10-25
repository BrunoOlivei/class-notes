# Modos de Abertura de Arquivos

| Caractere | Siginificado |
| --- | --- |
| 'r' | Abre para leitura (padrão) |
| 'w' | Abre para escrita, truncando o arquivo primeiro (removendo tudo o que estiver contido no mesmo) ou seja deleta tudo e escreve em cima |
| 'x' | Abre para criação exclusiva, falhando caso o arquivo já exista |
| 'a' | Abre para escrita, anexando ao final do arquivo caso o mesmo exista, adiciona texto em um arquivo que já possua algo inserido. |
| 'b' | Abre o conteúdo do arquivo em binário, ideal para arquivos que não possuam texto. |
| 't' | Modo texto (padrão) |
| '+' | Abre para atualização (leitura e escrita) |

# Modo 'x'

Abrindo um arquivo com o modo 'x', ele irá criar automaticamente um novo arquivo caso ele já exista retorna erro `FileExistsError`

```python
>>> with open('pedido.txt', 'x', encoding='UTF-8') as pedido:
		    pedido.write('Pedido nº 001/2020\n')

# Arquivo pedido.txt criado com o texto 'Pedido nº 001/2020
# Se tentarmos executar o mesmo código com o arquivo criado novamente:

with open('pedido.txt', 'x', encoding='UTF-8') as pedido:
    pedido.write('Pedido nº 001/2020\n')

Traceback (most recent call last):
  File "C:/Users/bruol/PycharmProjects/guppe/curso.py", line 1, in <module>
    with open('pedido.txt', 'x', encoding='UTF-8') as pedido:
FileExistsError: [Errno 17] File exists: 'pedido.txt'
```

---

# Modo 'a'

Abre para escrita, adicionando o conteúdo ao final do arquivo. Se o arquivo não existir, será criado:

```python
with open('lista_de_pacientes.txt', 'a', encoding='UTF-8') as lista:
    while True:
        paciente = input("Informe o nome completo do paciente ou digite sair: ")
        if paciente != 'sair':
            lista.write(paciente + '\n')
        else:
            break
```

<aside>
⚠️ Abrindo o arquivo no modo a, não conseguiremos utilizar o comando seek para controlar o cursor

</aside>

---

# Modo 'r+'

O sinal de '+' é sempre utilizado com alguma outra letra que corresponde a algum modo para abertura de arquivo, no caso do r ele combina a abertura para leitura e escrita

Utilizando o r, o comando write substituirá o que já estiver escrito no documento. 

```python
with open('lista_de_pacientes.txt', 'r+', encoding='UTF-8') as lista:
    while True:
        paciente = input("Informe o nome completo do paciente ou digite sair: ")
        if paciente != 'sair':
            lista.write(paciente + '\n')
        else:
            break
```

Ao rodar esse comando os nomes informados foram escritos no documento apagando os 3 primeiros. 

---

# Modo 'a+'

Utilizando o modo a+ para abertura de arquivo, podemos acessar o documento e adicionar conteúdo sem apagar o que já estava escrito.

```python
with open('lista_de_pacientes.txt', 'a+', encoding='UTF-8') as lista:
    while True:
        paciente = input("Informe o nome completo do paciente ou digite sair: ")
        if paciente != 'sair':
            lista.write(paciente + '\n')
        else:
            break
```

---