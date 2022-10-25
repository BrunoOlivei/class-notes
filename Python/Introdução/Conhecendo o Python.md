# Conhecendo o Python

## Instalação:

Primeira etapa é a instalação do python no computador, para isso é necessário acessar o site: [www.python.org](http://www.python.org). Esse é o site oficial da linguagem python mantido pelo criador e a comunidade que constantemente alimenta e aprimora a linguagem.

![Site python.org](2_site_python.jpeg)

Site python.org

Após realizar o download da linguagem na máquina e executar o arquivo baixado, podemos verificar se realmente está instalada:

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/3_instalando_python.jpg](3_instalando_python.jpg)

Na janela para instalação do Python, vamos deixar selecionado a caixa **Add Python 3.9 to PATH** e clicar em *Install Now*:

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/4_instalando_python.jpg](4_instalando_python.jpg)

Se caso surgir uma nova janela pedindo permissão para a instalação, basta selecionar sim para prosseguir.

Através do terminal windows, escreva o comando `python --version`, se o terminal não reconheceu o comando executado o python não foi instalado, caso o terminal tenha retornado algo como `python 3.8.3` isso siginifica que já está instalado e a numeração apresentada corresponde a versão na qual você está trabalhando. Para checar se a versão instalada é a mais atual, verifique no site [python.org](www.python.org) qual a versão mais atual:

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/1_terminal_versao_python.jpg](1_terminal_versao_python.jpg)

---

## Primeiro Contato:

Utilizando o prompt do windows, digite *python* e aperte enter. Você provavelmente terá algo parecido com isso:

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/5_primeiro_contato.jpg](5_primeiro_contato.jpg)

Se tudo deu certo o cursor agora está posicionado logo após a `>>>` isso signicifica que agora você deve escrever códigos python.

O prompt também trouxe algumas informações interessantes na linha onde:

```
Type "help", "copyright", "credits" or "license" for more information 
```

Vamos experimentar o “help” digite `help` no prompt e aperte `enter` 

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/6_funcao_help.jpg](6_funcao_help.jpg)

Recebemos uma mensagem como retorno:

```
Type help() for interactive help, or help(object) for help about object.
```

Help em python é uma função, todas as funções em python recebem `()` após a palavra-reservada, que nesse caso é *help*.

Já `help(object)` pode ser utilizado quando queremos receber ajuda de um determinado objeto da linguagem python como por exemplo o `print` que também é uma função dentro da linguagem.

Primeiro vamos olhar com mais calma somente o `help()`, digite no console e aperte enter: 

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/7_funcao_help.jpg](7_funcao_help.jpg)

Recebemos como resultado muitas informações interessantes que podem nos ajudar nos estudos, como por exemplo um link para um tutorial da linguagem no site oficial.

Esse texto também explica que podemos escrever o nome de qualquer módulo (module), palavra-chave (keyword) ou tópico para recebermos ajuda de como escrever programas python e usar os módulos.

Basta digitar uma das palavras: *modules*, *keywords*, *symbols*, ou *topics* para receber uma lista do que está disponível dentro da linguagem.

Agora observe que o cursor está logo após `help>` isso siginifica que estamos dentro do ambiente de ajuda da linguagem, aqui não conseguiremos escrever códigos python, apenas receber ajuda sobre a linguagem.

Para testarmos vamos pedir ajuda para a função `print()` conforme disse anteriormente digite `print` e aperte enter:

![1%20Conhecendo%20o%20Python%200e7be9c52db34b2480ad54f55ea97ee0/8_help_print.jpg](8_help_print.jpg)

---

#primeirospassos #python #iniciante #instalação #python3

---

# Iniciando um projeto
```bash
# Criando o diretório que conterá os arquivos do projeto
mkdir <nome_diretorio_projeto>
cd <nome_diretorio_projeto>
```

```bash
# Instalando o virtualenv
virtualenv -p python<versão> <nome_ambiente_virtual>
```

```bash
# Ativando o ambiente virtual
source env/bin/activate
```

```bash
# Instalando os pacotes desejados
pip install <nome_pacote>==<versão>
```

---

