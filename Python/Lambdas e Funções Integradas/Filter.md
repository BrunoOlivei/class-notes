# Introdução

A função filter serve para filtrar dados de uma determinada coleção, exemplo fazer uma seleção das 10 músicas mais tocadas, as maiores vendas por cliente, os livros mais vendidos de ficção científica, linguagens de programação mais populares, aplicativos mais baixados, produtos que foram mais vendidos em determinado tempo, dia e horário de maior movimento na academia, termo mais pesquisado no google, etc.:

# Sintaxe:

A estrutuda do filter é basicamente igual a do map visto anteriormente:

filter(nome_função, nome_iterável)

```python
>>> filter(funcao, dados_iteráveis)
```

Assim como em map, também atribuimos a função filter a uma varíavel que criará um objeto da classe filter. Esse objeto fica arquivado na memória pronto para ser acessado, assim que o código acessa estes dados, seja através do tratamento utilizando as coleções como list, dict, set, tuple, etc, os dados são zerados.

Importante então guardar estes resultados em uma nova variável, caso seja o desejo usar estes dados futuramente.

```python
<filter object at 0x000001A5F01E54C0>
<class 'filter'>
```

## Exemplos:

### Exemplos 1:

Importar uma biblioteca com alguns módulos de estatistica:

```python
>>> import statistics
```

Um exemplo hipotéticos de uma coleção com dados extraidos de um sensor:

```python
>>> dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
```

Calculando a média dos dados, através de uma função importada na biblioteca `statistics`

```python
>>> media = statistics.mean(dados)

>>> print(media)

2.183333333333333
```

Filtrando apenas os valores acima da média:

```python
>>> resultado = filter(lambda x: x > media, dados)
```

A variável resultado recebe a função filter que, conforme sua sintaxe, começa com uma função, aqui utilizamos o lambda, que recebe apenas um parâmetro de entrada e retorna se o parâmetro for maior que o valor calculado anteriormente na média, o lambda irá utilizar os valores do iterável 'dados', após isso o filter irá colocar em um objéto da memória de classe filter.

```python
>>> print(list(resultado))

Resultado:
[2.7, 4.1, 4.3]
```

Utilizando o print para exibir os dados resultantes da função filter, porém antes o objeto é tratado utilizando o list.

### Exemplo 2

Um outro exemplo de utilização é a remoção de dados faltantes:

Usaremos uma lista de países onde alguns elementos estão vazios:

```python
>>> paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
```

Dados vazios podem distorcer as informações que desejamos visualizar, por exemplo uma pesquisa de intenção de votos feita por telefone, imagine ter um grupo de dados contendo todos os dados de pessoas que não atenderam, o resultado final pode ficar distorcido, ainda mais se a maior parte das pessoas contactadas não atenderam o telefone.

```python
>>> print(paises)

['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela']
```

Como podemos observar a lista mantém todos os valores vázios, inclusive em suas posições originais.

O que faremos é utilizar o filter para trazer apenas os nomes dos paises completos, é como filtar uma coluna no excel e selecionar apenas as células que estão preenchidas, deixando de visualizar as em branco:

```python
>>> resultado = filter(None, paises)

>>> print(list(resultado))

Resultado:
['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']
```

Aqui utilizamos no local de uma função o dado None, que é um tipo de dado que não possuí tipo, ou menos comum ser chamado de tipo vázio.

>[!note] 
>Para o filer uma string vazia tem valor nulo. Neste filter estamos dizendo: Elimine os valores nulos da lista 'paises'.

## Outras soluções para o mesmo problema:

Para cada elemento da lista paises, se o tamanho deste elemento for maior que 0, adicione o na filtro do resultado3.

```python
>>> resultado3 = filter(lambda pais: len(pais) > 0, paises)

>>> print(list(resultado3))

Resultado:

['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']
```

Utilizando um operador de comparação para identificar os elementos que são diferente de ' ':

```python
>>> resultado4 = filter(lambda pais: pais != '', paises)

>>> print(list(resultado4))

Resultado:

['Argentina', 'Brasil', 'Chile', 'Colombia', 'Equador', 'Venezuela']
```

<aside> 📌 No momento que for utilizar uma função lambda no filter usando um comparador que retorna um valor booleano (Verdadeiro / Falso) se comparar com o 0, dependendo do contexto o 0 sempre retorna falso.

</aside>

# Diferença entre Map e Filter:

A grande diferença entre os dois está no tipo de função que está sendo utilizada:

-   map( ): recebe como parâmetros uma função e um iterável, retornando um objeto mapeando a função para cada elemento do iterável. Ou seja o map executa uma função com cada dado do iterável e retorna o resultado de cada elemento.
-   filter( ): recebe como parâmetros uma função e um iterável, retornando um objeto filtrando apenas os elementos de acordo com as instruções da função que retorna sempre ou True ou False. Ou seja, cada elemento do iterável é passado pela função que geralmente possui uma operação de comparação para determinar quais elementos serão selecionado e quais ficaram de fora do objeto filter.

## Exemplo mais complexo:

### Exemplo 1:

Suponhamos que você venha a trabalhar com ciência de dados em uma grande empresa e receba alguns dados para trabalhar:

Estes dados estão como dicionários onde:

-   Chave: "Username" = Valor: String com o nome
-   Chave 2: "Tweets" = Valor: Lista de Tweets do usuário

```python
>>> usuarios = [
		    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
		    {"username": "carla", "tweets": ["Eu amo meu gato"]},
		    {"username": "jeff", "tweets": []},
		    {"username": "bob123", "tweets": []},
		    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
		    {"username": "gal", "tweets": []},
]
```

```python
>>> print(usuarios)

[{'username': 'samuel', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']}, {'username': 'carla', 'tweets': ['Eu amo meu gato']}, {'username': 'jeff', 'tweets': []}, 
{'username': 'bob123', 'tweets': []}, {'username': 'doggo', 'tweets': ['Eu gosto de cachorros', 'Vou sair hoje']}, {'username': 'gal', 'tweets': []}]
```

### Forma 1:

A tarefa é filtrar os usuários estão inativos no twitter:

```python
>>> inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
```

Crie uma lista filtrando:

Para cada usuário (u) filtre a partir do tamanho da lista 'tweets' os usuários que possuem 0 elementos na lista, ou seja 0 tweets publicados. tudo isso partindo da lista usuários.

```python
[{'username': 'jeff', 'tweets': []}, {'username': 'bob123', 'tweets': []}, {'username': 'gal', 'tweets': []}]
```

### Forma 2:

Realizando a mesma tarefa de uma forma diferente:

```python
>>> inativos2 = list(filter(lambda u: not u['tweets'], usuarios))
```

Crie uma lista filtrando:

Para cada usuário (u) da lista usuários, filtre o usuário onde a lista 'tweets' seja falsa:

```python
# Usando o terminal para visualização:

>>> usuario = {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]}

>>> usuario['tweets']
['Eu gosto de cachorros', 'Vou sair hoje']

>>> not usuario['tweets']
False

>>> usuario2 = {"username": "gal", "tweets": []}

>>> usuario2['tweets']
[]

>>> not usuario2['tweets']
True

>>> bool([])
False

>>> bool(['a'])
True
```

Podemos observar que uma lista vazia é False, portanto no código utilizado para filtrar os elementos vazios estamos negando os valores de 'tweets' que sejam True, para assim entregar somente os valores False que são as listas de 'tweets' vazias.

# Como combinar filter com map:

Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que cada nome tenha menos de 5 caracteres:

```python
>>> nomes = ['Vanessa', 'Ana', 'Maria']
```

Crie uma lista com com a string:

'Sua instrutora é {nome},

A partir dos dados filtrados onde cada nome da lista nomes será comparado se possui mais de 5 caracteres, caso seja menor que 5 caracteres adicione a lista que será utilizada no map para criar a string 'Sua instrutora é {nome}.

```python
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
```

Resultado:

```python
>>> print(lista)

['Sua instrutora é Ana']
```

Adicionando mais nomes com menos de 5 caracteres:

```python
>>> nomes = ['Vanessa', 'Ana', 'Maria', 'Bia']
```

Utilizando a mesma combinação de map e filter:

```python
lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
```

Resultado:

```python
>>> print(lista)

['Sua instrutora é Ana', 'Sua instrutora é Bia']
```

#filter #lambda 