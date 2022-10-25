# Comandos de arquivo

## `pwd`
Indica em qual diretório o terminal está rodando.

## `ls` 
Lista os diretórios inseridos no diretório mãe.

## `echo` 
Praticamente o que o comando `print` do python faz. O comando `echo` recebe um argumento e retorna esse mesmo argumento

Uma variação desse comando é, após o argumento, inserir o sinal de maior ">" e o nome de um arquivo formato texto, assim o terminal irá inserir o argumento dentro do arquivo, caso o arquivo não exista ele cria o arquivo com o argumento dentro.

Se executarmos o comando passando um novo argumento para um arquivo já pré-existente que contenha algum texto, esse será sobrescrito.

Para adicionar algum texto, concatenando, ou seja sem sobrescrever devemos utilizar **dois sinais de maior** `>>`

```bash
echo "Bem vindo" > bemvindo.txt
echo 
```

## `cat` 
Faz a leitura do conteúdo de um arquivo texto

Uma opção do comando `cat` é o `-n` que retorna além do conteúdo do arquivo, também indica a linha.

Suponhamos que tenhamos 5 arquivos **no mesmo diretório**, nomeados da seguinte forma:

- arquivo1.txt
- arquivo2.txt
- arquivo3.txt
- arquivo10.txt
- arquivo25.txt

Podemos realizar a leitura de todos esses arquivos de uma vez só, utilizando o comando `cat` como argumento passamos `arquivo?.txt` dessa forma ele irá ler todos os arquivos que possuem 1 caractere ao final do nome. Porém dessa forma não lê os arquivos 10 e 25. 

Para leitura desses arquivos também, utiliza-se um asterisco no final do nome, dessa forma ele entende que é todo e qualquer caractere `arquivo*.txt`

Podemos ainda utilizar o asterisco, seguido da extensão do arquivo para ler todos:

```bash
cat *.txt
```

## `clear` 
Limpa a tela do terminal - `Ctrl + L` também possui o mesmo efeito.

## `ls -l` 
Trás mais informações sobre os arquivos e diretórios de onde o terminal está localizado.

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/1-ls-l.jpg](1-ls-l.jpg)

Os itens com a letra "d" no primeiro conjunto de letras e hífens, localizados a esquerda, indicam que se tratam de diretórios, portanto todos que têm a letra "d" no começo são diretórios.

## `ls -la` 
Já essa variação do comando `ls` retornam todos os elementos ocultos, arquivos e diretórios ocultos no linux recebem um ponto no começo do nome.

## `ls..` 
Lista os arquivos e diretórios da pasta acima da hierarquia.

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/2-ls-la.jpg](2-ls-la.jpg)

Uma outra opção interessante do `ls` é passar um asterisco, dessa forma o terminal irá entender que o comando `ls` seja passado para cada elemento dentro do nosso diretório. Suponhamos que estejamos trabalhando dentro de um diretório chamado workspace, e dentro desse diretório temos 2 arquivos txt e 2 diretórios um contendo um arquvio txt, com o comando `ls` mais o asterisco iremos elemento a elemento passar o comando `ls` para visualizar o que tem contido:

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/3-ls_asterisco.jpg](3-ls_asterisco.jpg)

## `man` 
Esse comando vem da abreviação de manual, ou seja ele funciona como o help de algumas linguagens, depois do comando, pode ser inserido um outro comando como argumento para que seja retornado as informações e funcionalidades.

## `whoami` 
Retorna o nome do usuário que esta sendo usado.

## `cd` 
Com esse comando podemos acessar outros diretórios no qual estamos trabalhando, por exemplo área de trabalho. Para acessar diretórios com nome que possui várias palavras separadas por espaço, precisamos passar o argumento nome do diretório entre aspas simples.

Independente de qual diretório esteja trabalhando, se executarmos o comando `cd` apenas, sem nenhum argumento, somos diretamente levados para o diretório home do usuário que está logado.

`cd ..` retorna no diretório acima.

```bash
cd 'Área de Trabalho'
cd ..
cd 
```

## `mkdir` 
Cria um novo diretório onde estamos trabalhando.

## `rmdir` 
Deleta um diretório, porém só apaga diretórios que estão vazios.

## `rm` 
Deleta um arquivo

Uma opção para remover todos os arquivos de um diretório é utilizar o `-r` de recursivo, dessa forma deletamos todos os arquivos de um diretório, incluindo o próprio diretório

```bash
rm -r workspace/
```

## `cp` 
Copia um arquivo, basta passar como argumento o arquivo que deseja copiar e como segundo argumento o nome que o novo arquivo terá.

Para copiarmos um diretório com um novo nome, devemos passar como opção (flag) o `-r` (recursivo) assim como fazemos para deletar utilizando o `rm -r` assim passamos como argumento o nome do diretório que desejamos copiar e o segundo argumento o nome que a cópia irá receber.

## `mv` 
Move arquivos, mas também pode ser utilizado para renomear um arquivo, para isso basta passar como argumento o nome do arquivo que deseja ser renomeado e o novo nome.

Podemos também mover para um novo diretório, basta como primeiro argumento passar o nome do arquivo que deseja mover e o segundo argumento o diretório de destino. Caso além de mover para outra pasta deseje-se alterar o nome também, basta passar como terceiro argumento o novo nome do arquivo.

## `zip` 
Utilizado para compactar o conteúdo de um diretório em um novo arquivo *zipado* (compactado) para isso precisamos estar fora (um nível acima) do diretório que desejamos compactar e fazemos da seguinte forma:

```bash
zip -r work.zip workspace/
```

Temos **work.zip** como argumento do nome que o arquivo zipado recebera e **workspace/** como argumento do diretório que desejamos compactar e -r para que seja compactado de forma recursiva.

Assim como o `unzip` aceita a *flag* `-q` para que os arquivos sejam criado de forma silenciosa, o `zip` também aceita, mesmo já utilizando a *flag* `-r` podemos fazer da seguinte forma:

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/5-zip.jpg](5-zip.jpg)

Para **descompactar** podemos fazer da seguinte utilizando `unzip` 

```bash
unzip work.zip
```

Caso os diretórios e arquivos contidos dentro do arquivo compactado, já existam o terminal irá informar da tentativa e aguardar uma orientação do usuário para sobrescrever ou não e quais arquivos.

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/4-unzip.jpg](4-unzip.jpg)

Percebe-se que o comando `unzip` acaba **revelando** tudo que foi extraído e criado a partir do arquivo zipado, existe uma *flag* útil para realizar o processo de forma silenciosa sem revelar o que foi extraído e criado através do comando `unzip` a *flag* em questão é o `-q` 

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/5-unzip2.jpg](5-unzip2.jpg)

## `tar-gz` 
É um formato de arquivo compactado muito popular no mundo *linux*, através do terminal podemos facilmente criar um arquivo `.tar.gz` com o comando `tar`. Assim como o `zip` ele também recebe algumas *flags*

`-c` *Create* - para criar um arquivo *tar*

`-z` Zip - para compactar o arquito

Diferente do `zip` que como argumento recebe o nome do arquivo que será criado e depois o nome do diretório que desejamos compactar. O `tar` recebe primeiro o nome do diretório que deseja-se zipar, seguido de um sinal de maior (>) e por fim o nome do arquivo zipado com `.tar.gz` que é o formato padrão desse tipo de arquivo compactado.

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/6-tar.jpg](6-tar.jpg)

Para descompactar, utilizamos o mesmo comando `tar` porém agora com as *flags* `-x` de *extract* e `-z` de zipado, a diferença é que precisamos fazer um redirecionamento aqui, ou seja, precisamos direcionar que o desempacotamento do arquivo work.tar.gz deve ser feito dentro do diretório em que estamos trabalhando. Para isso utilizamos o sinal de menor (>), em seguida o nome do arquivo zipado

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/7-tar2.jpg](7-tar2.jpg)

O flag `-f`  indica que compactaremos para um arquivo, eliminando a necessidade de indicar o direcionamento com os sinais de maior ou menor.

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/8-tar-czf.jpg](8-tar-czf.jpg)

`-v` - Verbose: para que o comando verbalize o que foi feito

Podemos compactar utilizando o `bzip2` que é um formato mais eficiente em relação a compactação, criando arquivos menores, porém ele demanda mais tempo que o `gzip` para compactar. 

Para utilizar o formato `bzip2` utilizamos a flag `-j` ao invés do `-z`

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/9-tar-bz2.jpg](9-tar-bz2.jpg)

## `touch` 
Ele "encosta" no arquivo sem alterar nenhum conteúdo, nesse sentido a data de modificação dele é atualizada para o mesmo momento em que o comando `touch` é executado.

Repare o arquivo **bemvindo.txt**

![Linux%20I%20Conhecendo%20e%20utilizando%20o%20terminal%20f3d3da7742ca47579b4b21378f62cd77/10-touch.jpg](10-touch.jpg)

## `date` 
Verifica a data e hora atual do sistema

````perl
$ date "+%d/%m/%Y"
23/01/2016
````

## `head` `tail` `less`
Em arquivos com conteúdo muito extenso podemos utilizar os comandos `head` e `tail` que retorna as 10 primeiras linhas e as 10 últimas linhas respectivamente. 

Podemos passar como flag `-n` e informar o número de linhas que desejamos que retorne

```bash
$ head -n 2 arquivo.txt
$ tail -n 2 arquivo.txt
```

Também é possível ler o conteúdo do arquivo da mesma maneira que o comando `man` que apresenta os conteúdo da documentação com a possibilidade de percorrer com as setas as linhas do documento. 

Para sair basta apertar o botão `q`

`vi` com esse comando conseguimos acessar um editor de texto dentro do próprio termina, passando como argumento um arquivo txt.

`i` a tecla i minúsculo entra no modo edição, podemos escrever

`:w` salva o arquivo

`:q` sai do modo edição

# `chmod`

Comando para alterar permissões, sendo a 115 relacionadas a diretórios e arquivos, em seguida podemos informar qual diretório desejamos que as alterações sejam realizadas:

```bash
chmod 115 dados/
```

Para reverter a permissão basta executar novamente o comando `chmod` e como parâmetro o número 755 e o diretório em questão:

```bash
chmod 755 dados/
```

---
# Utilizando o editor VI
VI é um editor de texto nativo do linux, para acessá-lo basta digitar:

```bash
$ vi <nome_do_arquivo_texto>.txt
```

Com as setas do teclado podemos navegar entre as linhas. 

## `i` 
Esse comando instrui o VI para inserção, com o cursor posicionado onde desejamos podemos inserir textos.

## `ESC`
Esse comando sai do modo de edição por exemplo

## `:`
Os dois pontos abre um *executor* através deles podemos executar alguns comandos como por exemplo salvar `:w` e sair do editor `:q`.
- `:q`: sair do editor
- `:w`: salvar as alterações
- `:wq`: salvar e sair
- `:q!`: sair sem salvar

## `a`
Possibilita inserção no caracter seguinte

## `A`
Possibilita a inserção no final da linha

## `x`
Deleta o caractere atual, podemos informar a quantidade de caracteres que queremos deletar, para isso, devemos digitar a quantidade em números, por exemplo 11, em seguida o `x`

>[!Note]
>Existe a possibilidade de executar mais de um comando, a partir dos dois pontos (:) em sequência, por exemplo após a edição de um texto, podemos executar `:wq` para salvar e sair. 
>🎯 Lembrando que os comandos serão executados em sequência respeitando a ordem.

## `dd`
Remove uma linha inteira

## `G`
Leva o cursor para a última linha, também pode receber um numeral antes do da letra g maiúscula para que o cursor seja levado até a linha de número informado.

## `$`
Leva o cursor para o final da linha

## `0`
Leva o cursor para o início da linha

## `/`
Usado para localizar alguma palavra ou conjunto de caracteres dentro do texto, após inserir o que deseja podemos utilizar o `n` para que localize a próxima ocorrência, já o `N` localiza a ocorrência anterior.

## `yy`
Copia uma linha inteira do texto, para copiar mais de 1 linha basta digitar o número desejado em seguida do comando `yy`

## `p`
Cola a linha no local desejado, se o cursor estiver no inicio de uma linha ele colara logo no final da linha atual. Ele também aceita um numeral antes do comando para colar a quantidade de vezes desejada.













## ``



  



