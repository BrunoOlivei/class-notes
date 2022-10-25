# Kill, ps e grep

## `ps`

Dentro do termina, para entendermos quais os processos estão sendo executado, podemos executar o comando `ps`:

```bash
$ ps

PID TTY          TIME CMD
3796029 pts/0    00:00:00 bash
3796354 pts/0    00:00:00 ps
```

O comando ps apresenta somente os processos dentro do terminal que estão sendo executados.

Se quisermos saber todos os processos que estão sendo executados dentro de todo o Linux, podemos passar a flag `-e` para o comando `ps`:

```bash
$ ps -e

```

Podemos utilizar também `ps -ef`, que entrega várias outras informações relacionadas a cada processo listado:

```bash
$ ps -ef
```

O resultado do comando ps -e é bastante extenso, o que dificulta o usuário localizar determinado processo. 

## `grep`

Podemos encaminhar a lista que foi gerada pelo `ps`, utilizando a | e passando o nome do programa que fará a filtragem "grep" e o nome do processo/programa que desejamos filtrar, por exemplo: firefox.

```bash
$ ps -ef | grep firefox
```

O resultado são só as linhas que contém firefox. 

O grep pode ser útil também para identificar algum termo em determinado arquivo de texto, por exemplo:

```bash
$ cat google.txt | grep california
```

## `kill`

Utilizamos o comando `kill` para enviar um sinal para um processo. Os processos utilizam sinais para se comunicar entre si. Sinais também são utilizados pelo Linux para interferir no funcionamento dos processos.

Exemplos de sinais são o `STOP` e o `CONT`, que podem ser utilizados, respectivamente, para interromper a execução de 
um processo e retornar à execução do processo interrompido 
anteriormente.

Se por algum motivo desejamos encerrar algum processo que esteja sendo executado, podemos utilizar o comando `kill` passando como argumento o código do processo que podemos visualizar na primeira coluna, quando executamos o comando `ps -e`:

Quando não indicamos nenhum sinal para o comando `kill`, é o sinal TERM executado por padrão. O `kill -TERM` encerra o processo de forma que ele possa realizar tarefas antes de ser encerrado, como salvar uma cópia de recuperação.

```bash
$ kill 15524
```

Se um processo travou e não está conseguindo encerrar o seu processo com o comando `kill`, podemos passar a flag `-9` e o código do processo:

```bash
$ kill -9 15524
```

---

# `top`

O Linux possui um comando que fornece informações relacionadas aos processos em execução e valores, como, por exemplo, uso de memória, tempo, etc.

O `top` atualiza as informações de tempos em tempos.

No seu cabeçalho, o `top` mostra algumas informações sobre
 o sistema, como a quantidade de memória disponível e em uso, 
informações sobre o uso do processador, etc.

Na lista dos processos também temos informações sobre a utilização do processador e da memória. Os processos são ordenados, por padrão, pelo uso do processador.

```bash
top
```

![1-comando-top.png](1-comando-top.png)

Para mostrar apenas os processos de um determinado usuário, podemos utilizar a opção `u`:

```bash
$ top -u lucas
```

Para acompanhar as informações de um processo específico, podemos utilizar a opção `p` passando como argumento o `PID` do processo:

```bash
$ top -p 19509

```

Por padrão, o `top` atualiza a tela com novas informações sobre os processos a cada 3 segundos. Para alterar esse tempo basta pressionar `d` enquanto estiver rodando o `top`, inserir o valor desejado e pressionar a tecla `Enter.`

## `killall`

Utilizado para "matar" inúmeros processos que contenham o mesmo nome.

```bash
$ killall top
```

Assim como no kill podemos adicionar o flag -9 para matar os processos sem executar nenhum processo de recuperação.

---

## `pstree`

Quando executamos um programa através do termina, por exemplo, o firefox, o terminal fica travado enquanto o processo estiver em execução.

Se abrirmos uma nova aba e executarmos o comando `pstree`, temos como resultado uma série de processos que estão sendo executados e as relações entre eles, com esse comando iremos visualizar o firefox sendo executado pelo bash, ligado ao terminal.

>[!Note]
>🧠 Esse comando nos mostra um diagrama onde é possível identificar quem originou (processo pai) cada um dos processos (processo filho).

## `jobs`

Se executarmos `CTRL+Z` no terminal onde o firefox está em execução, o processo será interrompido temporariamente e o terminal ficará livre para uso.

Podemos visualizar os processos interrompidos através do comando jobs:

![2-comando-jobs.png](2-comando-jobs.png)

## `bg`

Se quisermos jogar o processo que está sendo executado pelo terminal para o "*background"*, utilizamos o comando `bg [número do processo parado]`

Quando enviamos um processo para ser executado no *background*, o nome do processo recebe um "&" após seu nome, esse caractere indica que o processo está sendo executado no *background*.

## `fg`

Se quisermos enviar novamente o processo para o "*forwardground"* basta utilizarmos o comando `fg [número do processo]`

## `&`

Se quisermos iniciar um processo através do terminal e já enviá-lo para o *background*, podemos utilizar o caractere `&` logo após o nome do processo:

```bash
$ firefox &
```