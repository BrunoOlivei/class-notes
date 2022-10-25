# Sistemas de controle de versões

Os principais pontos em que um sistema de controle de versões podem nos ajudar no nosso fluxo de trabalho:

- Nos ajudam a manter um histórico de alterações;
- Nos ajudam a ter controle sobre cada alteração no código;
- Nos ajudam para que uma alteração de determinada pessoa não influencie na alteração realizada por outra;
- Etc

---

# Instalando no Ubuntu

Geralmente as distribuições Linux já vem com o GIT instalado, se não for o caso o comando utilizado é:

```bash
apt-get install git
```

Antes de iniciarmos o versionamento, precisamos informar quem somos para o git:

```bash
git config --global user.email "EMAIL"

git config --global user.name "NOME"
```

---

# Primeiros Passos

Para iniciarmos o controle de versionamento, precisamos primeiramente acessar o diretório onde se encontra nossos arquivos que desejamos controlar as versões com o git.

Através do comando `cd` vamos acessar o diretório desejado:

```bash
$ cd Workspace/web-scrapping
```

Agora que estamos dentro do diretório, podemos inicializar o git, através do comando `git init`.

```bash
$ git init

Repositório vazio Git inicializado em  
/home/bruno/Workspace/web-scrapping/.git/
```

Um comando que podemos utilizar para verificar o status do nosso repositório, quais arquivos foram alterados, quais arquivos foram adicionados e quais não foram, etc. é o `git status`:

```bash
$ git status

No ramo master

No commits yet

Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	.ipynb_checkpoints/
	estatistica-nba.ipynb

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
```

Podemos observar algumas informações como: `No commits yet` que significa que não houve nenhum commit realizado até o momento, além disso, temos informação dos `arquivos não monitorados` e uma lista de alguns arquivos, além de uma sugestão de comando para adicionarmo-los.  

De qualquer forma, ao utilizarmos o git init no diretório, nós informamos ao git que ele deve monitorar os arquivos inseridos. 

---

# Adicionando os primeiros arquivos

Através do comando `git add` passando como argumento o nome do arquivo. Se tivéssemos mais de um arquivo e quisermos adicionar todos os arquivos, usamos o ponto (.) como argumento do `git add`. 

```bash
$ git add estatistica-nba.ipynb
```

Se o terminal não acusar nenhuma informação, quer dizer que o comando foi executado com sucesso. 

Se utilizarmos novamente o comando `git status` percebemos que houve algumas mudanças:

```bash
$ git status

No ramo master

No commits yet

Mudanças a serem submetidas:
  (utilize "git rm --cached <arquivo>..." para não apresentar)
	new file:   estatistica-nba.ipynb

Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	.ipynb_checkpoints/
```

Uma informação que nos chama atenção é `Mudanças a serem submetidas:` aqui temos as alterações que precisam do comando `commit`. O commit irá criar um *checkpoint* das alterações realizadas no diretório e consequentemente nos arquivos.

A partir disso podemos utilizar o comando `commit`

```bash
$ git commit -m "" 
```

<aside>
💡 O comando commit recebe um parâmetro, nesse caso o `-m` que pede uma mensagem. A mensagem é passada entre aspas duplas ("") e como boa prática é importante passar uma mensagem descritiva a cerca das alterações realizadas nos arquivos que estão sendo "*commitados*"

</aside>

```bash
$ git commit -m "Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA"

[master (root-commit) 6ff13d7] Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA
 1 file changed, 470 insertions(+)
 create mode 100644 estatistica-nba.ipynb
```

Se utilizarmos novamente o comando `git status` vamos observar a seguinte mensagem:

```bash

$ git status

No ramo master
Arquivos não monitorados:
  (utilize "git add <arquivo>..." para incluir o que será submetido)
	.ipynb_checkpoints/

nada adicionado ao envio mas arquivos não registrados estão presentes (use "git add" to registrar)
```

Ainda temos arquivos que não foram adicionados. 

---

# Vendo o histórico

Através do comando `git log` recebemos diversas informações uteis sobre os commits realizados entre outras:

```bash
$ git log

commit 6ff13d7eb514f142e28400051913e0ed7501fbe5 (HEAD -> master)
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Mon Sep 20 16:22:41 2021 -0300

    Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA
```

A primeira informação é uma série alfanumérica que consiste na criptografia do commit, não existem 2 ou mais commits com a mesma chave criptográfica (hash). 

A segunda informação é o branch (ramo) onde o commit se encontra. 

A terceira informação é o autor do commit, a data realizado e a mensagem. 

Existem alguns comandos que configuram as mensagens do log, uma delas é o `git log --oneline` que traz as informações em uma única linha de forma resumida. 

```bash
$ git log --oneline

6ff13d7 (HEAD -> master) Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA
```

Podemos também solicitar informações relacionadas a alterações realizadas nos arquivos, através do comando `git log -p` 

```bash
$ git log -p
```

Alguns comandos que podem ser executados com o git log:

[git log cheatsheet](http://devhints.io/git-log)

---

# Configurações

Através do comando `git config` podemos passar como parâmetro o `--local` que será relacionado apenas ao diretório que se encontra o git, ou o `--globa` para uma configuração generalizada que será atribuída a qualquer operação realizada com o git. 

Algumas configurações que podem ser realizadas são o nome e-mail do autor, para isso passamos o comando `user.name` para nome e `user.email` para o endereço de e-mail, entre aspas duplas passamos o valor desejado. 

```bash
$ git config --local user.name "Bruno Oliveira"
```

Podemos visualizar quais valores estão configurados para determinados parâmetros:

```bash
$ git config user.name
Bruno Oliveira

$ git congig user.email
bruoli3@gmail.com
```

Algumas outras opções que o `git config` nos proporciona:

[Git - Git Configuration](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration)

---

# Ignorando arquivos

Uma forma de ignorar arquivos através do `.gitignore` é através da IDE, criamos um arquivo com o nome .gitignore, nele adicionamos o nome dos arquivos ou diretórios que desejamos ignorar, no caso desejamos ignorar o diretório `.ipynb_checkpoints` basta adicionarmos o nome do diretório seguido de uma barra (/).

Desta forma o git irá entender que aquele diretório e tudo que contém dentro dele deve ser ignorado. 

Após, precisamo adicionar o arquivo `gitignore` e submeter (commit). 

---

# Repositório Remoto

O primeiro passo para criarmos um repositório remoto é criar um diretório que conterá somente o controle das versões dos nossos arquivos. Para isso precisamos primeiramente criar esse novo diretório. 

Então um nível acima do diretório que estamos trabalhando, vamos criar uma nova pasta chamada "servidor":

```bash
$ cd ..
$ mkdir servidor
```

Feito isso vamos acessar nossa pasta servidor e iniciar o git passando um novo argumento `--bare` ele dirá que esse repositório é puro, não haverá alterações nele a não ser o controle dos commits realizados. 

```bash
$ cd servidor/
$ git init --bare
Repositório vazio Git inicializado em  /home/bruno/Workspace/servidor/
```

Agora precisamos voltar para o diretório onde se encontram os arquivos versionados:

```bash
$ cd ../web-scrapping/
```

Agora precisamos fazer com que o repositório que estamos trabalhando reconheça o servidor, para que futuramente ele possa enviar as informações. 

```bash
$ git remote add local /home/bruno/Workspace/servidor/
```

Através do comando `git remote add` estamos adicionando um servidor remoto, logo após o comando colocamos o nome, que no nosso caso será "local", em seguida adicionamos a informação do endereço que se encontra nosso servidor, no nosso caso "/home/bruno/Workspace/servidor/". 

>[!Note]
>Importante ressaltar que o endereço pode ser um local físico dentro da nossa máquina, o nosso caso, pode também ser um endereço da nossa rede local, pode ser um URL em um servidor na nuvem, entre outras opções.

Após executar o comando acima, podemos verificar se o local está correto, através do comando `git remote -v`: 

```bash
$ git remote -v
local	/home/bruno/Workspace/servidor/ (fetch)
local	/home/bruno/Workspace/servidor/ (push)
```

Fetch informa o local onde o git irá buscar informações e push para onde ele irá enviar. Existem casos que os endereços, para busca e envio de informações podem ser diferentes.

---

# Sincronizando os dados

Agora precisamos enviar os dados do repositório para o servidor local:

```bash
$ git push local master
```

Para enviar as informações, utilizamos o comando `git push` que recebe como parâmetros o nome do servidor, que no nosso caso é "local" e quais são as informações que desejamos que sejam enviadas, como queremos que tudo vá para o servidor, informamos "master". 

```bash
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (6/6), 16.74 KiB | 8.37 MiB/s, done.
Total 6 (delta 0), reused 0 (delta 0)
To /home/bruno/Workspace/servidor/
 * [new branch]      master -> master
```

## Compartilhando

Imaginemos que uma pessoa que esteja trabalhando conosco, deseja baixar os arquivos e dados que estão no nosso repositório. 

Para isso a segunda pessoa precisará clonar, através do endereço do nosso servidor. 

Na pasta que se deseja baixar todos os dados do repositório, utilizamos o comando `git pull` por padrão o git clone irá renomear o repositório para "origin", caso desejemos renomear, basta executarmos o comando `git remote rename origin local` assim renomeamos de origin para local. 

Agora voltando para o comando `git pull` podemos passar o nome "local".

---

# GitHub

Enviando um repositório do git para o GitHub.

Primeiro acesso o github e crie o repositório, na página quick setup que o GitHub disponibiliza, copie o link referente ao repositório. 

Agora no terminal execute o comando:

```bash
git remote add origin [link do github]
```

Em seguida precisamos enviar os dados, assim como fizemos no servidor criado localmente:

```bash
git push -u origin master
```

O `-u` indica que a partir deste comando de git push, todas às vezes que forem executados serão automaticamente enviados o origin para master, sendo assim não haverá necessidade de informar novamente, basta executar o comando `git push`.

 Após esse comando, o git irá pedir o usuário e o login. 

>[!Info] 
>Caso a sua conta do github utiliza autenticação em dois fatores, é necessário emitir um token de acesso. O token criado será usado no lugar do login. 
Para saber mais: [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

---

# Branchs

Branchs são utilizados para definir partes de um determinado projeto para diferentes pessoas que integrem uma equipe, por exemplo, um arquivo HTML, onde uma pessoa ficará responsável pelo cabeçalho e outra com um formulário, dentro de uma mesma estrutura/arquivo HTML.

O comando `git branch` quando executado, mostra qual parte do projeto, no nosso caso é a master.

Para criar um branch novo, basta executarmos o seguinte comando:

```python
$ git branch sports 
```

Se executarmos novamente o comando `git branch`:

```python
$ git branch
* master
  sports
```

O asterisco (\*) antes da palavra master, mostra onde estamos trabalhando.

Para deletar uma branch `git branch -d [nome da branch]`, mas importante salientar que para isso é necessário estar fora da branch.

Em alguns casos, o Git pode se recusar a deletar seu branch local: quando ele contém commits que não foram mesclados em nenhum outro branch local ou enviado para um repositório remoto. 
Esta é uma regra muito sensata que protege você contra a perda inadvertida de dados de commit.

Para deletar tal branch utilize a flag `-D`

Para alterar para a nova branch, utilizamos o comando `git checkout` e o nome da nova branch:

```python
$ git checkout sports
Switched to branch 'sports'
```

Existe uma forma mais simples para criar um novo branch e realizar o checkout para ele ao mesmo tempo, basta executarmos o seguinte comando:

```python
git checkout -b economia
```

Assim, além de criarmos o novo branch já realizamos o checkout automaticamente para ele.

A ferramenta a seguir nos permite visualizar o comportamento do git.

[Visualizing Git](https://git-school.github.io/visualizing-git/)

![1.visualizando-branch.png](1.visualizando-branch.png)

Agora criaremos o branch título e em seguida faremos o checkout do master para o título:

![2.visualizando-branch.png](2.visualizando-branch.png)

Repare que já houve mudança, o título passou a ser o segundo item: vamos realizar fazer alguns commits a partir do título e em seguida voltar para a master e realizar mais um commit para verificar o comportamento:

![3.visualizando-branch.png](3.visualizando-branch.png)

Podemos observar que foi criado um novo "galho" para o nosso projeto. Dentro de uma equipe, um time que esteja trabalhando dentro do branch título e outro na master, podem atuar de forma que as alterações realizadas no título que não interfiram no trabalho do master, assim uma equipe não precisaria ficar atualizando e trazendo para o seu próprio repositório, todas as alterações que não sejam relevantes no momento. 

## Executando alterações na branch criada.

Vamos alterar nosso arquivo de trabalho `estatísticas-nba.ipynb` dentro do branch título, vamos adicionar nosso arquivo para *commitar*. 

Após alterações realizadas e o arquivo salvo, no terminal execute os comandos:

```python
$ git branch sports
$ git add estatísticas-nba.ipynb
$ git commit -m "Alterando o arquivo para teste"
```

Em seguida checamos, com o comando `git log` as alterações realizadas até aqui:

```python
$ git log

commit e68ae2d6773b760c3028909454e1c5e7eb7ccb05 (HEAD -> sports)
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Sun Sep 26 11:38:28 2021 -0300

    checando caracteristicas das colunas

commit a5104d96041db2ebbee3c3607f0a1d54f6eca9e5 (origin/master, master)
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Wed Sep 22 21:05:40 2021 -0300

    Analise dos preços de combustíveis levantados pelo Gov. Federal, em Julho 2021

commit 9096151f929e2f65954b5426269f76adb31c284a (local/master)
Author: Bruno Oliveira <bruoli3@gmail.com>
Date:   Mon Sep 20 17:29:28 2021 -0300

    Criando arquivo gitignore

commit 6ff13d7eb514f142e28400051913e0ed7501fbe5
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Mon Sep 20 16:22:41 2021 -0300

    Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA
```

Já na primeira linha podemos verificar, após a chave criptográfica do commit, o branch

Assim, essa última alteração realizada foi feita apenas nessa branch, para quem for trabalhar a partir da branch master, não verá a alteração que realizamos, a não ser que essa pessoa faça um pull das alterações. 

Isso facilita também o controle de versões, se precisarmos alterar ou restaurar o trabalho antes das alterações realizadas no branch sports, facilmente conseguiríamos localizar.

Agora vamos voltar para branch master e executar o log:

```python
$ git checkout master
$ git log

commit a5104d96041db2ebbee3c3607f0a1d54f6eca9e5 (HEAD -> master, origin/master)
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Wed Sep 22 21:05:40 2021 -0300

    Analise dos preços de combustíveis levantados pelo Gov. Federal, em Julho 2021

commit 9096151f929e2f65954b5426269f76adb31c284a (local/master)
Author: Bruno Oliveira <bruoli3@gmail.com>
Date:   Mon Sep 20 17:29:28 2021 -0300

    Criando arquivo gitignore

commit 6ff13d7eb514f142e28400051913e0ed7501fbe5
Author: BrunoOlivei <bruoli3@gmail.com>
Date:   Mon Sep 20 16:22:41 2021 -0300

    Criando arquivo jupyter notebook com estatísticas relacionadas as temporadas de 2015 a 2020 da NBA
```

Aqui vemos que o commit realizado na branch sports, não aparece. 

---

# Levando o trabalho de uma branch para outra

Levando em considerações as alterações realizadas até aqui no branch sports, queremos juntar as alterações realizadas no branch sports com o branch master, partindo do pressuposto que a nossa branch master é onde se concentrará o projeto finalizado.

Para isso, utilizamos o comando `git merge` a partir da branch que desejamos TRAZER os trabalhos de outra branch:

```python
$ git checkout master
$ git merge sports
```

O comportamento será:

![4.git-merge.png](4.git-merge.png)

O git automaticamente cria um commit contendo todo o conteúdo da branch sports.

No terminal ao executarmos o comando `git merge sports` o editor VIM será aberto, para salvarmos o merge, o comando é dois pontos (:) e x. 

---

# Como mover os commits de uma branch para a master sem criar um commit de merge.

Para termos os commits realizados em uma branch, sem ser criado um commit de merge, ou seja, enviando todos os commits da branch sports para a branch master, basta realizarmos o comando `git rebase [nome da branch]` dentro da branch master.

![5.git-rebase.png](5.git-rebase.png)

Dessa forma a branch master passa a ter todos os commits que haviam somente na branch título. 

No terminal temos uma forma de visualização aproximada do Visualization Git, através do comando `git log --graph` com ele pode visualizar as linhas de trabalho.

---

# Resolvendo conflitos

Suponhamos que duas pessoas alteraram uma mesma linha de um arquivo, agora as duas versões precisam ir para a branch master, como resolvemos esse conflito?

Se uma segunda pessoa tenta realizar um `merge` ou `rebase` o terminal irá acusar um conflito, IDE's como o Visual Studio Code auxiliam também mostrando onde está o conflito de forma visual. 

Através da IDE, podemos deletar a modificação que menos faz sentido. 

A partir disso, ao executarmos o `git status` receberemos uma mensagem que indica que houve 2 modificações, a atual já commitada e a que estamos tentando unir. 

Com as correções feitas na IDE podemos adicionar o arquivo, através do `git add` em seguida realizar o `git commit`.

## Git Push de dois branches

Se uma pessoa que esteja trabalhando em uma branch do projeto realiza o merge ou rebase no master e envia para o servidor através do push outra pessoa que também esteja trabalhando em outra branch ao precisar fazer o push das alterações no master receberá uma mensagem de falha. 

Isso se dá, pois, o git informa que o ramo do trabalho em que a pessoa está não é a versão mais atualizada do projeto, para resolvermos isso, essa pessoa precisará atualizar seu projeto, através do comando `git pull` do que está no servidor com a sua versão da master. 

Após a atualização a pessoa desenvolvedora desse ramo do projeto poderá enviar para o servidor através do `git push`

---

# Ctrl + Z no Git

O `git restore` consegue restaurar as versões  de arquivos.

```python
No ramo master
Seu ramo está à frente de 'origin/master' por 2 submissões.
  (use "git push" to publish your local commits)

Changes not staged for commit:
  (utilize "git add <arquivo>..." para atualizar o que será submetido)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   preco_combustiveis.ipynb

nenhuma modificação adicionada à submissão (utilize "git add" e/ou "git commit -a")
```

```python
git restore preco_combustiveis.ipyn
```

Se executarmos o `git status` temos como resultado que não há nenhuma alteração a ser adicionada e commitada. 

```python
$ git status
No ramo master
Seu ramo está à frente de 'origin/master' por 2 submissões.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

E no arquivo a alteração foi desfeita.

**Agora como podemos desfazer uma alteração que já foi enviada para o stage, ou seja, já está pronta para ser commitada?**

```python
git restore --staged preco_combustiveis.ipynb
```

Dessa forma o arquivo voltara para status *unstaged*. 

**Como desfazer um commit?**

Agora o pior dos casos, onde foi feita a alteração e commitado o código:

Depois do arquivo commitado, vamos executar o comando git log, ele trará as informações de cada commit realizado, com essa informação, copiamos o código hash do commit que desejamos desfazer e através do comando `git revert [código do commit]`

O resultado é um ambiente de edição de texto do terminal, com as informações necessárias para salvar e até copiar os dados do commit no final da tela.

> Com o `git checkout` nós desfazemos uma alteração que ainda não foi adicionada ao index ou stage, ou seja, antes do git add. Depois de adicionar com `git add,` para desfazer uma alteração, precisamos tirá-la deste estado, com `git reset`. Agora, se já realizamos o commit, o comando `git revert` pode nos salvar.

---

# Guardando para depois

Suponhamos que você esteja trabalhando em algo do código e em determinado momento chegou uma nova tarefa para ser executada, mas ainda precisamos checar se aquele trabalho que estávamos executando está correto, antes de commitar.

Precisamos guardar essas alterações para outro momento, principalmente se a nova tarefa exige que precisemos realizar as alterações e sejam commitadas com urgência. 

Para isso utilizamos o `git stash`, onde podemos salvar todas as alterações para um local temporário que possa ser recuperado posteriormente. 

```python
$ git stash
Saved working directory and index state WIP on master: aa05d6a Revert "Alterando o tipo de dado da coluna data de coleta para formato date"
```

Se executarmos o `git stash list` recebemos uma lista com todas as alterações salvas temporariamente. 

Se executarmos um `git status` veremos que as alterações feitas não estão mais sendo indicadas.

Agora vamos alterar outra linha do nosso código e salvar o arquivo e executar novamente o `git status`.

Podemos commitar as nossas novas alterações.

O trabalho salvo temporariamente continua no seu estado atual, se executarmos novamente o `git stash list` podemos visualizá-lo. 

Podemos utilizar o comando `git stash pop`, que além de trazer as modificações salvas temporariamente, também remove da lista do stash. Porém, esse método traz todas as alterações listadas no stash, se quisermos trazer uma específica, podemos utilizar o `git stash apply [numero da stash]` em seguida utilizar o `git stash drop`. 

```python
$ git stash pop
Mesclagem automática de preco_combustiveis.ipynb
No ramo master
Seu ramo está à frente de 'origin/master' por 5 submissões.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
Dropped refs/stash@{0} (95b4cd5e9da746d194a697d53f0d757c05d882df)
```

---

# Viajando o tempo

Se quisermos voltar nosso código para um estágio do desenvolvimento conforme nossos commits, podemos realizar através do `git checkout [código com 7 primeiros dígitos do commit]`, com isso podemos ver como o código estava antes das alterações realizadas.

Porém, um detalhe muito importante é que qualquer alteração realizada nesse código antigo não será anexada a branch de trabalho, portanto não ficará salvo no nosso controle de versionamento. 

Para conseguirmos colocar as alterações dentro do nosso controle, precisamos criar uma branch a partir do commit que voltamos, para isso utilizamos o comando `git checkout -b [nome da nova branch]`. Dessa forma conseguimos anexar as nossas alterações ao controle de versionamento, de forma que possamos acessá-la futuramente. 

Em seguida podemos também realizar o merge, para agrupar todas as branchs, caso seja necessário. 

>[!note]
>🧠 A descrição do comando `git checkout --help`, em uma tradução livre é: "Atualizar os arquivos na working tree para ficarem na versão especificada. [...]". Basicamente, podemos deixar o nosso código no estado do último commit de uma branch, de um commit específico, ou mesmo tags (que veremos adiante).

---

# Vendo alterações

O comando `git diff`, mostra a diferença do código entre cada commit. 

Para utilizarmos o comando precisamos informar pelo menos os 7 primeiros caracteres do commit, se quisermos avaliar as diferenças de mais de dois commits podemos utilizar dois pontos (..) entre os caracteres dos commits.

```python
$ git diff db40fe3..aa05d6a
```

As linhas em vermelho são as versões alteradas enquanto as verdes são as alterações. As brancas são linhas que não sofreram alteração.

>[!note]
>🧠 O sinal de subtração (-) antes da linha indica que ela não está mais presente no arquivo. Já o sinal de adição (+) mostra que é uma linha nova. Alterações são representadas por uma remoção e uma adição de linha.

Além disso, o comando `git diff` mostra tudo que foi alterado, entre os arquivos, que ainda não foram adicionados para commit, ou seja, a partir que o arquivo for adicionado para commit ele não aparece mais no comando `git diff`.

---

# Tags e Releases

Com um projeto finalizado, pronto para ser lançado/publicado, por exemplo, podemos sinalizar através do git que a partir de determinado commit tempos um código pronto para release, servindo também para definir um marco em certo ponto do projeto, para controle interno da equipe.

Dessa forma o sistema fica estático, ou seja, qualquer alteração feita no código surtirá efeito após outra release, não interferindo no marco anterior.

Para definição de marcos dentro do projeto o git trabalha com tags. Para criarmos uma tag utilizamos o comando `git tag -a` passando um nome como valor, no caso utilizaremos v0.1.

```python
$ git add -a v0.1
```

Podemos passar também a flag -m e uma mensagem entre aspas.

```python
$ git add -a v0.1 -m "lançando a primeira versão (BETA) da aplicação"
```

Se executarmos somente o comando git tag recebemos como resultado a lista das tags criadas, no nosso caso "v0.1".

Através do git push, podemos enviar para o servidor (local ou em nuvem, até mesmo um serviço como o github) o nome da tag.

```python
$ git push origin v0.1
```

No github podemos visualizar na aba releases a versão que enviamos utilizando a tag "v0.1", assim outros usuários do site podem ter acesso a essa versão, baixando um arquivo compactado do código e executando em seu computador, por exemplo.

---
