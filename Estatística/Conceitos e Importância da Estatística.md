# Introdução

A análise estatística tem como objetivo a resolução de problemas, bem como a produção de conhecimentos que geram novos problemas, é uma ciência multidisciplinar, que se preocupa com a demonstração dos dados de uma pesquisa. Seu principal objetivo é auxiliar na tomada de decisões em todas as áreas ou avaliar uma determinada situação.

> Uma ciência que estuda e pesquisa tanto o levantamento de dados quanto o processamento desses para a quantificação da incerteza existente na resposta para um determinado problema e a tomada de decisão sob condições de incerteza, sob o menor risco possível.
> 

## Exemplos de aplicação

- Analisar as probabilidades de ocorrerem erros
- Verificar resultados e compará-los
- Testar diversos produtos e processos
- Controle de qualidade
- Observar a evolução dos dados
- Verificar a aceitação de certos produtos em alguma região
- Estimativas de crescimento
- Índices
- Avaliar os indicadores de qualidade e produtividade.

# Conceitos básicos

A estatística tem por objetivo fornecer métodos e técnicas para que se possa lidar com situações de incerteza, e pode ser subdividida em 3 áreas:

- Descritiva
- Inferencial
- Probabilística

## Estatística Descritiva

Também chamada de dedutiva, tem como **objetivo organizar, resumir e simplificar as informações**, a fim de torná-las mais fáceis de serem entendidas, transmitidas e discutidas. Ela descreve os fenômenos de forma prática e acessível, por meio de tabelas, gráficos e medidas resumo.

**Exemplos:**

- Taxa de desemprego
- Consumo médio de combustível por quilômetro
- Nota média de estudantes

## Estatística Inferencial

Objetiva "inferir" conclusões sobre a população, interpretando os dados coletados de uma amostra e projetando esses resultados para toda a população de dados. Exemplo: pesquisa de intenção de votos em eleições. Para isso utiliza a **Teoria das Probabilidades**, que é fundamental para avaliar situações envolvendo o acaso. A aplicação do método probabilístico nos permite "quantificar" a importância do acaso. 

Assim os resultados obtidos por amostragem são "testados", utilizando-se conhecimentos probabilísticos, a fim de **determinar até que ponto eles são significativos, isto é, não são obra do acaso.**

**Dados estatísticos** podem ser obtidos por dois processos:

- **Censo:** processo que consiste no exame de todos os elementos da população. Exemplo: censo demográfico, censo industrial, etc.
- **Estatísticas:** utilizadas para avaliar os elementos de uma amostra.

A partir do **censo**, são encontrados medidas que descrevem toda a sua população, chamados **parâmetros**. Ao se trabalhar com amostras são obtidos estimações e a partir delas os **Estimadores**

- **Parâmetros:** medidas descritivas de uma população. Exemplos: a contagem do número total de habitantes de uma região.
- **Estimadores:** medidas descritivas de uma amostra, que indiretamente estimam um parâmetro pelo calculo probabilístico. Exemplo: proporção de votantes em um determinado candidato obtido por amostra.

# População e Amostra

**População** pode ser definida como sendo uma coleção de elementos que possuem alguma característica em comum, podendo ser animados ou inanimados.

Quando se consegue todas as informações desejadas de uma população, temos o censo, porém existem inúmeras restrições que uma pesquisa enfrenta para entrevistar todos os dados desejados de uma população inteira, como por exemplo:

- Restrição de tempo e recurso;
- População "infinita, entre outros.

Assim é comum coletar um subconjunto das população, as chamadas **amostras**.

**Amostra** pode ser definido como parte da população. Uma amostra deve ser representativa da população, contendo todas as características da população de onde foi extraída

A partir do estudo do conjunto de dados obtidos da amostra, faz-se uma extrapolação dos seus resultados para a população toda. Essa extrapolação é chamada de **Inferência**.

**Exemplo:** pesquisa de opinião pública, pesquisa de intenção de votos, resistência de materiais, durabilidade de aparelhos, etc.

A escolha das unidades que comporão a amostra é feita por processo chamado **Amostragem**

# Amostragem

Uma analogia básica que ilustra vem a amostragem, é imaginar uma grande panela de sopa (população), você pega um pouco dessa sopa com a colher (amostra) para poder experimentar se o tempero está bom (inferência). 

Em pesquisas científicas, na qual desejamos, muitas vezes conhecer algumas características (parâmetros) de uma população, podemos utilizar técnicas de amostragem, afim de obtermos valores aproximados (estimativas) para os parâmetros que estamos interessados.

Esse tipo de pesquisa é chamado de **levantamento por amostragem**.

A seleção de elementos de uma população (amostragem) deve ser feito sob uma metodologia adequada.

Amostragem é interessante quando:

- **Economia**
- **Tempo**
- **Confiabilidade e operacionalidade:** quando pesquisamos em um número reduzido de elementos, podemos dar mais atenção aos casos individuais.

Quando a amostragem não é interessante:

- **População pequena**
- **Características de fácil mensuração**
- **Necessidade de alta precisão**

Existem dois grandes grupos de técnicas de amostragem:

- **Probabilística:** quando todos os elementos da população têm probabilidade conhecida e diferente de zero de pertencer a amostra.
- **Não probabilística:** quando nem todos os elementos de uma população têm probabilidade conhecida de pertencer a uma amostra.

Sendo a **amostragem probabilística** a mais indicada para garantir a representatividade da amostra, pois implica em um sorteio dos elementos com regras bem determinadas, sendo possível apenas quando a população é finita.

## Amostragem casual simples

Para se ter uma amostra casual simples, precisa-se ter uma listagem de todos os elementos da população a ser estudada. A amostra conterá elementos obtidos de forma totalmente aleatória, por sorteio e sem restrição. Assim todos os elementos da população têm a mesma probabilidade de pertencer a amostra. $\big(\frac{n}{N}\big)$ 

## Amostragem sistemática

A amostragem sistemática é utilizada quando os elementos de uma população se apresentam de forma ordenada. Sendo a retirada dos elementos feito de forma periódica.

Com a posse de todos os elementos ordenados de uma população, estabelece-se o intervalor de seleção $i = \frac{N}{n}$

Em seguida sorteia-se um número dentre o intervalo. Esse número de ordem do primeiro sorteado da lista, os demais elementos da amostra, serão selecionados utilizando o intervalo I a partir do primeiro número sorteado. 

**Exemplo:** 

Se desejamos obter uma amostra de 5 alunos dentre uma turma de 32, utilizando a fórmula temos que N = 32, n = 5 e o intervalo de seleção é $i = \frac{32}{5}$ = 6,4. Para o valor do intervalo deve ser considerado apenas o valor inteiro, logo $i = 6$

O primeiro elemento da amostra, deve ser retirado entre os 6 primeiros da lista, para obter os demais elementos da amostra, somamos  intervalo I ao elemento anterior. Supondo que o primeiro sorteado entre os 6 foi o elemento 4, temos **4, 10, 16, 22 e 28.**

## Amostragem estratificada

Neste tipo de amostragem, a população deve ser subdividida em subgrupos (estratos). Cada subgrupo, os indivíduos (elementos) devem ser semelhantes entre si. Assim pode-se obter uma amostra aleatória de elementos em cada grupo. Esse procedimento pode gerar amostras bastante precisas. 

Quando os estratos possuem o mesmo tamanho entre si, sorteia-se um número igual de elementos em cada subgrupo. Caso contrário o sorteio é proporcional ao número de elementos de cada estrato. 

## Amostragem por conglomerado

Amostragem por conglomerado a população é dividida em diferentes grupos e extrai-se uma amostra apenas dos conglomerados selecionados. O ideal é que cada grupo representasse tanto quanto possível a população. 

**Exemplo:** estudar a população de uma cidade realizando uma pesquisa apenas em um bairro. 

**Importante atentar-se que as amostras não podem conter vícios e devem ser utilizados técnicas de amostragem adequadas com o tamanho amostral (n)**

## Amostragem não aleatória

Procuram gerar amostras que, de alguma forma, representem razoavelmente bem a população de onde foram extraídas.

### Amostragem por cotas

Semelhante a amostragem estratificada, a amostragem por cota também subdivide a população em diversos subgrupos. Assim seleciona-se uma cota de cada subgrupo proporcional ao seu tamanho. Costuma-se dividir a população em uma grande números de subgrupo. 

**Exemplo:** Pesquisas socioeconômicas subdividas por localidade, nível de instrução, faixa de renda, etc.

### Amostragem por julgamento

Os elementos escolhidos são aqueles julgados como típicos da população que deseja-se estudar. Exemplo: um estudo sobre a produção científica de um departamento de uma universidade, dessa forma escolhe-se os departamentos que julga-se correspondente a característica que deseja ser estudada.

# Dimensionamento da amostra

O tamanho da amostra irá depender do nível de confiança estabelecido para pesquisa em função direta do **erro amostral**, previamente fixado pelo pesquisador. Mais utilizado é 5%, o máximo é 10%.

Quanto menor o **erro amostral**, maior o tamanho da amostra e consequentemente maior a precisão das estimativas populacionais e maior o custo para a pesquisa.

Ou seja, para determinar o tamanho da amostra o pesquisador precisa especificar o erro amostral tolerável, o que significa o quanto se admite errar na avaliação dos parâmetros de interesse.

É a famosa margem de pontos percentuais para mais ou para menos.

Para dimensionamento da amostra podemos utilizar a seguinte equação:

$$
\frac{ Z^{2} \times  p^{ \wedge} \times  q^{ \wedge}\times N}{d^{2}\times (N-1) + Z^{2}\times p^{ \wedge}\times q^{ \wedge}}
$$

- $N$ = Tamanho da população
- $p^{\wedge}$ = Estimativa da verdadeira proporção de um dos níveis da variável escolhida
- $q^{\wedge}$ = 1 - p
- $Z^{2}$ = Abcissa da curva norma padrão, fixado em um nível de confiança
- $d$ = Erro amostral

Quando não sabemos o valor de $p^{\wedge}$ e $q^{\wedge}$ podemos adotar 0,5 para cada o valor de Z pode ser observado no quadro:

[Intervalo de confiança e valores Z](https://www.notion.so/6c376d590a34455ba925c8b7625b762a)

## Exemplo

![Conceitos%20e%20Importa%CC%82ncia%20da%20Estati%CC%81stica%209fd0282ab33f4f6cbbe8130b277766ef/1-tamanho-amostral.jpg](1-tamanho-amostral.jpg)

---

# Tipos de variáveis

**Variável** é uma característica que possa ser avaliada (ou medida) em cada elemento da população, sob as mesmas condições. Uma variável observada (ou medida) **deve gerar apenas um resultado**.

**Exemplo:**

Podemos considerar variáveis de uma população de funcionários de uma determinada empresa:

- Tempo de serviço
- Salário
- Estado civil
- Idade
- Sexo

A medição dessas características pode ser realizada através de uma unidade de medida (km, cm, anos, meses, moedas, quilo, etc) ou definindo atributos (casado, solteiro, homem, mulher, forte, fraco, etc).

Para melhor descrever o grupo ou amostra, é necessário identificar o **tipo dessa variável** que podem ser: **Quantitativas** ou **Qualitativas**.

## Variáveis Qualitativas ou Categóricas

São variáveis que assumem como possíveis valores **atributos ou qualidades**. Se assumem uma ordenação natural (grau de escolaridade, classe social, etc) recebem o nome de **qualitativas ordinais.** Caso contrário são chamadas **qualitativas nominais** (cor dos olhos, campo de estudo, etc.).

## Variáveis Quantitativas

São as variáveis que assumem como possíveis valores os **números**. Quando os números são resultantes de contagens são chamadas de quantitativas discretas (quantidade de irmãos, de defeitos em uma peça, etc.), caso assumam valores de medição  são chamadas de quantitativas contínuas (altura, peso, velocidade).

---

# Fases do método estatístico

Após a definição do problema a ser estudado, os passos seguintes são:

- Planejamento
- Coleta de dados
- Crítica, organização e sumarização dos dados
- Apresentação dos dados
- Análise e interpretação

## Planejamento

Nesta fase, deve se estabelecer com clareza os objetivos e os procedimentos, que serão adotados, como a maneira de coleta dos dados, o tamanho necessário para a amostra e a maneira mais indicada de selecioná-la.

## Coleta de dados

Baseado na finalidade da pesquisa, a coleta pode ser:

- **Contínua:** obtendo-se registros de fenômenos de interesse do pesquisador.
- **Periódica:** quando necessita de avaliações sistemáticas. Ex: Censo realizado por governos.
- **Ocasional:** quando existe um interesse momentâneo em determinado fenômeno. Ex: número de infectados de determinada doença.

O conjunto de dados coletados dá origem às **Séries Estatísticas,** que podemos categoriza-las:

- **Históricas ou Cronológicas (Temporal)**: quando o fenômeno é estudado ao longo de um tempo, em determinado momento e local.
- **Geográficas ou Territoriais:** quando se observa valores da variável segundo sua localização.
- **Específica ou Categórica:** quando a variável é observada em determinado momento e local, discriminada por especificações categóricas.

## Crítica, organização e sumarização

Têm a finalidade de eliminar erros, através de uma revisão crítica dos dados, retirando os valores que estranhos que podem ocorrer por quem coletou ou quem foi abordado na pesquisa.

## Apresentação dos dados

Feita através de **tabelas e gráficos**, onde a primeira é mais rica em precisão, enquanto a segunda proporciona maior rapidez na interpretação.

## Análise e interpretação

Com o objetivo de determinar as medidas estatísticas, a finalidade de descrever de forma prática e objetiva as características gerais de uma população.

### Tabelas e gráficos

O objetivo é transformar os dados em informações que permitam a fácil visualização e interpretação da pesquisa, além de verificar a existência de algum padrão, comparar esse padrão com os resultados ou julgar sua adequação a alguma teoria.

As **tabelas** são quadros em que serão dispostas as informações por alguma categoria pelo cálculo de alguma frequência.

Um **gráfico** é uma figura utilizada na estatística para representar um fenômeno, ele deve refletir padrões gerais e específicos do conjunto de dados. Um gráfico dispõe tendências, os valores mínimos e máximos, as variações dos dados e as ordens de grandeza dos fenômenos que estão sendo observados.

---