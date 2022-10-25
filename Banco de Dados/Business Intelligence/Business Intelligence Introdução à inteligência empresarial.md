# Datawarehouse

Armazém de Dados, introduzido nos anos 90, os problemas de **unificação de conceitos**, diferentes **formas de agregaçã**o e de **fontes de dados** distintas de indicadores para tomada de decisão, faziam que um BI não fosse possível.

A solução foi a criação de uma estrutura apartada que pode ser aplicado conceitos únicos. 

- Integração de diversas fontes de dados, independente se as fontes são internas ou externas;
- Implementação das regras de negócio;
- Limpeza de dados;
- Análise ao longo de tempo.

<aside>
📌 O Datawarehouse tem como princípio básico possuir uma estrutura de dados separada das estruturas operacionais, para que os conceitos e regras de negócio sejam implementadas.

</aside>

## Entrevista

1. Entrevistar
    1. O que quero analisar?
    2. Como quero analisar?

O que eu quero analisar pode ser chamado também de i**ndicador, medida ou variável.**

Como quero analisar pode ser chamado como **dimensão.**

<aside>
📌 Estas são as perguntas chaves. O que quero analisar me determina os indicadores e como quero analisar me determina as dimensões.

</aside>

## Matriz Dimensão x Indicador

É um documento que vai registrar todas as informações levantadas durante a entrevista, realizada com as perguntas anteriormente realizadas.

Sua estrutura, é geralmente composta por uma matriz, onde as linhas são compostas pelos indicadores (qual informação quero ver, exemplo: vendas, custos, lucros, etc.). Já as colunas são representações das dimensões (como quero ver a informação, exemplo: cliente, empresa, tempo, etc.)

Após indicar quais serão os indicadores e dimensões, é necessário realizar o cruzamento das informações, ou seja, quais indicadores cruzaram com quais dimensões (linha x coluna) na tabela.

<aside>
📌 Como construir uma Matriz Dimensão Indicador?
Colocando nas linhas os indicadores, as colunas das dimensões e dentro da matriz marco os cruzamentos que fazem sentido entre indicadores e dimensões.

</aside>

# Tabela de Fato

O próximo passo é projetar as tabelas do Data warehouse, afinal trata-se de um banco de dados transacional que é composto de tabelas, campos, registros, índices, chaves primárias e estrangeiras. Quem irá dizer como o Data warehouse deve ser desenhado em termos de tabelas, campos e índices será a Matriz Dimensão X Indicador.

As tabelas do data warehouse se dividem em dois grandes grupos: as tabelas de **dimensão** e **tabelas de fato**. O que veremos nesta aula é como desenhar as tabelas baseadas na Matriz Dimensão X Indicador.

## Tabela de Fato

É definido quando há alguma ocorrência dentro de um determinado tempo, essa ação é registrada na tabela de ocorrências ou tabela de fato.

Quando temos um indicador (linha) totalmente relacionado com alguma dimensão (coluna), ou seja:

| Indicador | Dim1 | Dim2 | Dim3 | Dim4 |
| --- | --- | --- | --- | --- |
| Ind1 | X | X | X | X |
| Ind2 | X | X | X | X |

Os indicadores 1 e 2, como estão concomitantemente relacionados com todas as dimensões, serão parte de uma tabela de fato. 

| Indicador | Dim1 | Dim2 | Dim3 | Dim4 |
| --- | --- | --- | --- | --- |
| Ind1 | X | X | X | X |
| Ind2 | X | X | X | X |
| Ind3 |  | X | X | X |
| Ind4 |  | X | X | X |

Assim como os indicadores 3 e 4 que estão diretamente ligados as dimensões 2, 3 e 4 também farão parte de outra tabela de fato. 

Cada tabela de fato terá como campos representando cada uma das dimensões relacionadas na entrevista, e cada uma será uma chave primária. 

<aside>
📌 o cruzamento repetido dos conjuntos de indicadores e dimensões que determinam as tabelas de fato.

</aside>

## Detalhe de uma dimensão

![1divisoes+da+dimensao.png](1divisoesdadimensao.png)

Quando o usuário quer analisar as vendas por **cidade**, **estado**, **país** ou **produto**, não estamos falando exatamente de dimensões, mas sim, entidades. Quando estas entidades se relacionam entre si, constituem uma dimensão.

Dentro do ramo de relacionamento de entidades, há algumas que possuem uma sequência de relacionamentos única. Esse grupo de entidades dentro da dimensão, chamamos de **hierarquia**.

![2hierarquia.png](2hierarquia.png)

Na hierarquia temos uma entidade básica que chamamos nível, e a ele pode estar associados atributos.

![3nivel.png](3nivel.png)

<aside>
📌 Recapitulando: uma dimensão é composta de hierarquias, que no que lhe concerne são compostas por níveis que podem, ou não, possuir atributos.

</aside>

# OLAP (Online Analytical Processing)

É a capacidade para manipular e analisar um grande volume de dados sob múltiplas perspectivas.

Uma solução para o problema de desempenho nos Data warehouses. OLAPs são estruturas de bancos de dados, projetadas de uma maneira diferente dos bancos relacionais

Os OLAPs possuem uma estrutura diferente. Um OLAP não apresenta tabelas, campos ou registros e, sim, duas grandes estruturas.

A primeira delas é uma modelagem lógica das dimensões do data Warehouse.

Nós temos no nosso, Data Warehouse duas tabelas que estão em um banco de dados relacional que representam uma dimensão produto e cliente.

Em um OLAP, não possuímos a representação dos dados no formato de tabelas, mas como fórmulas matemáticas.

```
Suco = Suco de Laranja + Suco de Maça

Águas = Água com Gás + Agua sem Gás 

Todos os produtos = Sucos + Águas
```

```
Supermercados = Super Princesa + Super Gigante

Lanchonetes = Hamburguer de Ouro + Padaria da Maria

Todos os clientes = Supermercados + Lanchonete
```

Após a construção lógica construída, o OLAP cria uma estrutura matricial onde estarão localizadas todas as relações, em que as linhas conterão todos os membros de uma dimensão e nas colunas todos os membros da outra dimensão. 

<aside>
📌 O OLAP não tem campos, registros ou tabelas. Ele é uma estrutura lógica com fórmulas matemáticas baseadas nas dimensões e uma matriz onde todas as combinações possíveis e imagináveis são determinadas.

</aside>

Segundo passo é carregar o conteúdo da tabela de fato na tabela matricial 

| Produtos/Clientes | Super Princesa | Super Gigante | Hambúrguer de Ouro | Padaria da Maria | Supermercados | Lanchonetes | Todos os Clientes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Suco de Laranja | 100 | 250 | 0 | 50 | 350 | 50 | 400 |
| Suco de Maçã | 200 | 300 | 300 | 0 | 500 | 300 | 800 |
| Água com Gás | 150 | 250 | 70 | 70 | 400 | 140 | 540 |
| Água sem Gás | 300 | 100 | 120 | 120 | 450 | 240 | 690 |
| Sucos | 300 | 550 | 50 | 0 | 850 | 350 | 1200 |
| Águas | 450 | 350 | 190 | 190 | 800 | 380 | 1180 |
| Todos os Produtos | 750 | 900 | 490 | 240 | 1650 | 730 | 2380 |

O esforço operacional de buscar uma informação seja ela nível operacional quanto gerencial, é o mesmo.

Imaginando que tivéssemos uma terceira coluna na nossa tabela de fato, os estados. 

Nossa estrutura matricial agora teria 3 dimensões, sendo um cubo, onde a primeira fatia será as empresas do estado de SP, a segunda fatia do estado de RJ e a última fatia a soma das empresas de SP e RJ.

![6_1_42_terceira+dimensao.png](6_1_42_terceiradimensao.png)

Exatamente por isso representamos o banco de dados OLAP como um cubo. O termo "cubo" é muito utilizado no vocabulário de BI, como "temos de consolidar o cubo de vendas". Neste caso, sabemos que o banco de dados OLAP está em uso.

# Categorias de OLAPs

Os OLAPS são maiores que os Data Warehouses, o que antigamente era um problema considerável. Atualmente o espaço de disco é mais econômico do que há dez anos.

O crescimento do OLAP é exponencial conforme são adicionadas mais dimensões ao banco de dados. 

O número de cruzamentos de informações possíveis dentro de um OLAP é a multiplicação dos membros de cada dimensão, não apenas os mais baixos, mas todos presentes na hierarquia.

Por exemplo, se temos um modelo OLAP de:

- 10 empresas,
- 10.000 clientes,
- 300 produtos,
- 365 dias de análise,
- 5 formas de pagamento,
- 50 vendedores
- 2 tipos de entrega.

O tamanho desse OLAP será calculado pela multiplicação de cada uma dessas dimensões citadas, totalizando

$$
5.474.000.000.000
$$

Ou seja, 5 TRILHÕES

Felizmente, nem todas as empresas vendem para 10.000 clientes os 300 produtos, usando as formas de entrega e pagamento diariamente. Isto é, a combinação nunca é totalmente executada, além do que existem cruzamentos que não fazem sentido na lógica de negócio.

Tendo em vista esses fatores, é importante que saibamos a **densidade (esparsividade)** do OLAP a ser construído.

$$
Esparsividade = \frac{Número\ de\ Combinações\ Reais}{Número\ de\ Combinações\ Possíveis}
$$

Quanto mais próximo de 1 o resultado da esparsividade, mais denso será o cubo OLAP.

## OLAPs por Assunto

É interessante separar os OLAPs por assuntos, sendo inviável utilizar um único OLAP para modelar todo o Data Warehouse. Logo, teremos um OLAP para vendas, outro para a contabilidade e assim por diante.

## Categorias de OLAPs

- MOLAP: Multidimensional OLAP
- HOLAP: Hybrid OLAP
- ROLAP: Relational OLAP

### MOLAP

O MOLAP já registra no disco todos os cruzamentos possíveis em um OLAP e já disponibilizam para consulta. Possuem a melhor desempenho dentre os outros tipos existentes, porém construí-los demanda tempo.

Fazer os cálculos de todos os cruzamentos de uma base com o esparsividadade de 0,15 ou 0,20 podem demorar horas.

Essa categoria de OLAP já calcula os valores dos cruzamentos, por exemplo, vendas de sucos, águas, total de produtos, etc.

| Produtos/Clientes | Super Princesa | Super Gigante | Hambúrguer de Ouro | Padaria da Maria | Supermercados | Lanchonetes | Todos os Clientes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Suco de Laranja | 100 | 250 | 0 | 50 | 350 | 50 | 400 |
| Suco de Maçã | 200 | 300 | 300 | 0 | 500 | 300 | 800 |
| Água com Gás | 150 | 250 | 70 | 70 | 400 | 140 | 540 |
| Água sem Gás | 300 | 100 | 120 | 120 | 450 | 240 | 690 |
| Sucos | 300 | 550 | 50 | 0 | 850 | 350 | 1200 |
| Águas | 450 | 350 | 190 | 190 | 800 | 380 | 1180 |
| Todos os Produtos | 750 | 900 | 490 | 240 | 1650 | 730 | 2380 |

### HOLAP

Essa categoria de OLAP mantém algumas informações na tabela de fato e outras informações ele irá calcular e consolidar, 

Por exemplo, ele pode manter todos os dados desmembrados na tabela de fato e apenas calcular e consolidar os relacionamentos, por exemplo, total de vendas de sucos, águas e total de produtos. 

O tempo para criação do OLAP acaba sendo menor, porém, há uma queda de desempenho,  pois dependendo da informação algo deverá ser calculado e inserido na matriz. Alguns HOLAPs possuem o conceito de '*cache'* (memória transitória), ou seja, começamos a fazer a consulta no híbrido, se são consultas que não utilizam dados da matriz é executada uma busca no banco relacional. Essas informações são direcionadas à matriz em memória e caso essa consulta seja repetida ou muito parecida, é nesta matriz em memória que a informação é buscada.

### ROLAP

Os ROLAPs utilizam todas as informações do Data Warehouse no momento da consulta, e apenas armazena em sua estrutura os relacionamentos lógicos entre os membros da dimensão.

Eles também possuem a estrutura de '*cache*', se uma consulta consolidada é realizada, o ROLAP irá calcular apenas o que está sendo consultado e seja armazenado na memória transitória ('cache'), se for realizada a mesma consulta ou pelo menos parecida, o sistema buscará da memória e não da tabela de fato. 

O ROLAP aprende com o tempo, conforme as consultas são realizadas e assim ele só mantém em disco, aquelas que têm mais sentido e importância para o negócio.

---

# Relatórios Analíticos

É importante analisar qual é das pessoas que usam as ferramentas de BI. Podemos classificar os usuários em três núcleos:

- Análises Ad-Hoc;
- Análises Padronizadas;
- Análises Customizadas.

As Análises Ad-Hoc são completamente abertas, ou seja, você fornece o OLAP para o usuário de forma livre, e é ele quem criará o formato de saída dos relatórios e definirão os filtros ou indicadores.

As análises padronizadas são perfeitas para o usuário que não querem se perder com o OLAP, mas desejam possuir flexibilidade. Existem alguns exemplos clássicos de análises padrão, como ranking, ou seja, ordenar algo de acordo com um critério. Quem decide isso, será o usuário.

Outros exemplos são análise de Pareto, curva ABC e análise de exceções.

Análises customizadas são para o usuário que não está interessado em acessar o dado "cru", sem interpretações, e sim acessar a informação da forma mais inalterada possível, com relatórios bem elaborados que contenham gráficos em pizza ou em barra, além de outros elementos visuais.

---

# Resumindo

Primeira etapa temos que fazer a matriz dimensão/indicador, construída a partir das informações adquiridas através de entrevistas com os usuários, conhecendo o negócio que estamos modelando.  

Com a matriz definida, conseguimos construir o Data Warehouse, de onde sairão todas as tabelas de informações gerenciais. 

Em seguida, precisamos identificar as fontes de dados, como informações externas e internas da empresa e analisar quais transformações serão necessárias para unificar conceitos — ETL, das regras de negócio.

Eventualmente podemos precisar de um ODS — uma tabela temporária para carregar os dados de sistemas transacionais das fontes para o armazém de dados. 

Desde o Data Warehouse esteja populado com informações, definimos os OLAP's, que pode ser um para cada tema ou para cada relatório. 

E finalmente devemos identificar as melhores ferramentas de visualização e o que cada usuário está esperando do relatório.

---

# Matriz dimensão indicador

O que o cliente de Business Intelligence deseja ver, exemplo: faturamento, custo, impostos, custos fixos e variáveis, meta de faturamento, preço médio, etc.

Como o cliente de Business Intelligence deseja ver, exemplo: por dia, por setor, por cliente, por segmento, por marca, por vendedor, por equipe, etc.

---

# Variações do BI

São áreas dentro do Business Intelligence que tem ganhado espaço e especializações no mundo corporativo, são eles:

- Data Minnig
- Balance Scorecard
- Big Data

**Data Minnig**, do inglês Mineração de Dados, a partir de Data Warehouses massivos, as empresas têm buscado utilizar a estatística para análises preditivas, ou seja, através dos dados do passado, com modelos matemáticos avançados, tentar prever o futuro. 

Balance Scorecard, painel de dados, como um cockpit de um avião com painéis para indicadores específicos, no caso muito usado por KPI's (Key Performance Indicators, do inglês, indicadores-chave de performance), muito utilizados por empresas que possuem missão, visão e valores muito bem definidos, além de conhecerem bem suas forças, fraquezas e oportunidades, através da análise SWOT, e utilizam indicadores que fazem sentido para acompanhar o avanço em direção ao seu quadro de missão, visão e valores, como, por exemplo, ser empresa líder em automação residencial até 2040. 

Big Data é além dos dados internos da empresa, é usar dados que circulam na internet sobre a empresa que deseja usar, como as redes sociais, dados na nuvem, dados sobre o mercado, concorrência, etc. Tudo que seja relacionado a empresa e aos negócios e possível de ser captada através da internet é usado no Big Data. Hadoop é um software livre capaz de capturar essas informações pela internet para serem utilizadas pela empresa.