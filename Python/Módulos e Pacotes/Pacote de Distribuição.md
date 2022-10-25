# Introdução
A biblioteca padrão do python, traz diversos módulos com funcionalidades úteis para o dia a dia, como por exemplo o módulo `random`. Podemos baixar módulos extras publicados na biblioteca online do python.

Tudo isso é muito útil e pode ser utilizado em qualquer projeto, porém e se quiséssemos utilizar um módulo, criado por nós, sempre que necessário?

# Nossos Módulos

Ao importar um módulo em um arquivo python, a linguagem realiza primeiro a pesquisa dentro do diretório onde se encontra o arquivo que estamos trabalhando, caso não encontre ele parte para pesquisa na biblioteca padrão da linguagem, que já vem pré-carregada ao instalar a linguagem na máquina, não obtendo resultado na pesquisa, o a linguagem busca nos pacotes do site, se não encontrar a linguagem retorna erro.

Portanto, caso o NOSSO módulo não estiver no mesmo diretório em que estamos trabalhando não conseguiremos importa-lo para nosso arquivo atual.

# Pacote de Distribuição

A solução poderia ser copiar, sempre que necessário, o módulo para os diretórios que estamos trabalhando, porém caso fosse necessário alguma atualização no código desse módulo em questão, teríamos que alterar um a um, cópia por cópia, o que fica inviável.

A solução é criar um pacote de distribuição e publica-lo no site de pacotes python, e sempre que necessário realizar alguma alteração, os outros arquivos que importam funcionalidades do módulo são também atualizados.

Para criar e publicar esses pacotes de distribuição precisamos seguir alguns pontos importantes:

1.  Criar uma descrição da distribuição
2.  Gerar um arquivo de distribuição
3.  Instale o arquivo de distribuição

## Setuptools

Dentro do diretório onde se encontra o módulo que se deseja publicar, crie um arquivo `[setup.py](<http://setup.py>)` e digite as seguintes linhas:

```python
from setuptools import setup

setup(
"""Função setup com diversos argumentos opcionais"""
	name="nomemodulo", # Aqui é a identificação, por convenção é comum nomear a distribuição segundo o nome
	version="1.0",
	description="Uma breve descrição da funcionalidade",
	author="Seu Nome",
	author_mail="nome@mail.com",
	url="Uma url do seu projeto caso haja",
	py_modules=["nomemodulo"] # Aqui é uma lista dos arquivos que se deseja incluir no pacote, caso haja mais de um arquivo, eles são separados por vírgula, assim como lista.
)
```

## README

Além do arquivo do módulo que deseja publicar e o arquivo [setup.py](http://setup.py), o pacote de distribuição requer um arquivo README em txt.

# Criando o arquivo de distribuição

Pelo windows, abra o prompt a partir da pasta onde se encontra o módulo que deseja ser distribuído.

```powershell
C:\\Users\\bruol\\OneDrive\\workspace\\formacao-python\\meus_modulos_python> py -3 setup.py sdist
```

O executar a linha de comando acima, diversas mensagens serão apresentadas, porém uma em especial diz que obtivemos exito:

```powershell
removing 'nomemodulo - versão' (and everything under it)
```

Dentro da pasta onde se encontra o módulo, foi criada uma nova pasta chamada **dist** nessa pasta contém um arquivo .ZIP.

# Instalando o arquivo de distribuição

Dentro da pasta **dist**, clique com o botão direito para abrir o menu suspenso contextual e selecione a opção _abrir janela de comando aqui_

No prompt de comando digite o seguinte comando:

```powershell
C:\\Users\\...\\meus_modulos_python\\dist> py -3 -m pip install nomemodulo-versao.tar.gz
```

Ao final se nenhuma mensagem de erro for apresentada, teremos a seguinte mensagem:

```powershell
Successfully installed nomearquivo
```

# Conclusão

Agora podemos utilizar nosso módulo em qualquer arquivo python, basta realizar a importação. Se atualizarmos os códigos do módulo, devemos seguir todos os três passos, atribuindo a uma nova numeração para a versão do módulo.