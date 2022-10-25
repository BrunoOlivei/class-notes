# Introdução:

Em qualquer sistema operacional para que o programa (código) que estivermos escrevendo, tenha acesso a documentos dentro do diretório, é preciso uma permissão, tanto para leitura quanto para edição.

# StringIO

Utilizado para ler e criar arquivos em memória, não irá gravar no disco, ficará somente na memória do disco. StringIO não faz parte das funções integradas, para isso precisamos importar do módulo io.

```python
from io import StringIO
```

# Criando um arquivo na memória:

```python
# Primeiro realizamos o import
from io import StringIO

# Aqui criamos uma mensagem e atribuimos a uma variável
mensagem = 'Esta é apenas uma string normal'

# Criamos uma variável que receberá a função StringIO para criar um arquivo com a mensagem
arquivo = StringIO(mensagem)

# Agora podemos fazer acesso ao arquivo:
print(arquivo.read())
```

Se observarmos o tipo de objeto que o 'arquivo' é:

```python
>>> print(arquivo)

<_io.StringIO object at 0x000002E1225864C0>

>>> print(type(arquivo))

<class '_io.StringIO'>
```

<aside> ⚠️ Se repararmos não foi criado nenhum arquivo no nosso diretório do projeto, está tudo em memória.

</aside>

Também é possível escrever diretamente qualquer string, sem a necessidade de atribuí-la a uma variável, utilizando a função `.write()`

```python
# Escrevendo outros textos diretamente no arquivo:
arquivo.write('\\nOutro Texto')
```

Se pedirmos para ler novamente o arquivo não obteremos resultado, já que o cursor se encontra no final do arquivo.

```python
# Pedindo para ler novamente
print(arquivo.read())
```

Para ler novamente precisamos utilizar a função `.seek()` para mover o cursor até o início do arquivo:

```python
# Movendo o cursor para o inicio do arquivo:
arquivo.seek(0)

# Pedindo para ler novamente
print(arquivo.read())

Esta é apenas uma string normal
Outro Texto
```

#stringio
