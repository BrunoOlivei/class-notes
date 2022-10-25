# Introdução:

Estes módulos são bastante úteis para obter informações precisas sobre o ambiente de desenvolvimento, desde o sistema operacional na qual estamos trabalhando, a versão do python que está sendo utilizada até o diretório na qual o projeto está inserido.

---

# Módulo sys:

Para utilizar o módulo sys, primeiro é necessário importar da biblioteca padrão do python, basta utilizar os comandos `import sys.`

Este módulo possui algumas funções uteis, como por exemplo `.platform` que retorna o sistema operacional subjacente.

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/25_sys_platform.jpg](25_sys_platform.jpg)

No meu caso o sistema operacional subjacente é o win32

---

Nós também podemos consultar a versão do python que está sendo executada com o comando `sys.version`, assim como o comando `python --version` no prompt do windows:

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/26_sys_version.jpg](26_sys_version.jpg)

---

# Módulo os:

Os módulos os são bastante úteis também para basicamente trabalhar com diretórios, porém ele possui funcionalidades muito mais avançadas.

## .getcwd()

Utilizando a função `getcwd()` do módulo os nós recebemos como resultado o diretório onde está sendo executado o programa em questão.
Quando executamos este comando direto no console python o resultado será o caminho para a pasta onde a linguagem e o console estão instalados:

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/27_so.getcwd.jpg](27_so.getcwd.jpg)

---

## .chdir(*'endereço'*)

Esta função move nosso ambiente de trabalho para outro diretório, exige um argumento que é uma string e essa é o endereço no qual desejamos acessar:

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/28_os_chdir.jpg](28_os_chdir.jpg)

Se novamente executarmos a função `os.getcwd()` iremos receber agora como resultado o endereço que passamos na função `os.chdir()`

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/29_os_getcwd.jpg](29_os_getcwd.jpg)

---

## .listdir()

O `os.listdir()` retorna uma lista contendo os nomes dos arquivos na qual estamos inseridos.
Esta função pode receber também como argumento algum outro endereço na forma de uma string.

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/30_os_listdir.jpg](30_os_listdir.jpg)

---

## .mkdir('*nome*')

A função `os.mkdir()` é o mesmo que a que utilizamos nos terminais e consoles windows, mac os ou linux. Ela cria uma nova pasta com o nome que for usado dentro dos parenteses como argumento em formato de string, ou seja entre aspas simples ou duplas.

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/31_os_mkdir.jpg](31_os_mkdir.jpg)

Agora se utilizarmos novamente a função `os.listdir()` para listar as pastas e documentos dentro do nosso diretório poderemos ver que a pasta **teste** que criamos também está lá.

![Mo%CC%81dulo%20sys%20e%20os%208ac63800ad9543c39d80f0d68e058748/32_os_listdir.jpg](32_os_listdir.jpg)

---

# Extras

`getsizeof` (pega o tamanho de) é uma função da biblioteca sys que retorna a quantidade de bytes em memória do elemento passado como parâmetro:

```python
# Mostra quantos bytes o objeto está ocupando na memória:

>>> print(getsizeof('geek')) # 53

>>> print(getsizeof('University')) # 59

>>> print(getsizeof(9)) # 28

>>> print(getsizeof(3.15)) # 24

>>> print(getsizeof(983442009210)) # 32

>>> print(getsizeof(True)) # 28

>>> print(getsizeof([1, 2, 3, 4, 5])) # 96

>>> print(getsizeof([])) # 56

>>> print(getsizeof(lambda x: x + 1)) # 136

```