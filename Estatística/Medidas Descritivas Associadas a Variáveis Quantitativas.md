# Introdução

Podemos fazer a apresentação dos dados por meio de gráficos, tabelas, ou fazendo o uso de medidas que resumem as informações obtidas na coleta dos dados, chamadas **medidas descritivas**. Uma delas são as **medidas de posição ou tendência central,** que trás uma noção do que está ocorrendo com os dados, demonstrando a localização da maior concentração dos valores, se há uma distribuição por igual, etc.

As medidas de tendência central mais importantes são a **média aritmética, a mediana e a moda**. Há outras medidas de posição que são a **separatrizes**, que englobam: a própria mediana, os **quartis e os percentis.**

As **medidas de dispersão**, por sua vez, são utilizadas para avaliar o grau de variabilidade do conjunto de dados, mostrando se ele é homogêneo ou heterogêneo. As mais utilizadas são: **amplitude total, a variância, o desvio padrão e o coeficiente de variação**.

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

# Medidas de Posição

Para sumarizar as informações de um conjunto de observações utiliza-se medidas que resumem em um só número certas características. Temos as medidas de posição, de dispersão, de assimetria e de curtose. Se são calculadas a partir de uma amostra chama-se **estatística da amostra**, se são calculados a partir de uma população, chama-se **parâmetros da população**. 

As principais medidas de posição e as principais medidas separatrizes são:

### Mediadas de posição

- **Medidas de Tendência Central**
    - Média Aritmética
    - Mediana
    - Moda

- **Separatrizes**
    - Mediana
    - Quartis
    - Decis
    - Percentis

### Medidas de Dispersão

- Amplitude Total
- Variância

- Desvio Padrão
- Coeficiente de Variação

As medidas de posição servem para representar o ponto central de equilíbrio de um conjunto de observações ordenadas segundo suas grandezas. Destacam-se a **média, mediana e moda.**

## Média Aritmética

Esta fornece uma medida de posição central. É encontrada somando seus valores e dividindo pelo número de observações.

$$
\mu( \overline{x})  = \frac{\sum_{i=1}^N x_i}{n}
$$

<aside>
📌 Quando os dados são de uma amostra, a média é denotada por $\overline{x}$. Quando os dados são de uma população a média é denotada pela letra grega $\mu$.

</aside>

A equação acima é o mesmo que: 

$$
\overline{x} = \frac{x_1 + x_2 + x_3+...+x_n}{n}
$$

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

## Média Aritmética Ponderada

Existem situações em que não temos todos os dados disponíveis ou então temos "pesos" diferentes para os dados considerados, dessa forma utiliza-se a média aritmética ponderada para obtermos a média.

$$
\mu( \overline{x})  = \frac{\sum F_i.x_i}{n}
$$

Se a situação for de dados agrupados, a média é obtida a partir de uma ponderação em que os pesos são as frequências absolutas (Fi) de cada classe e xi é o ponto médio da classe i.

Para média de uma tabela com intervalo de classes, primeiro é necessário tirar o ponto médio de cada classe antes e a partir do resultado multiplicar pela frequência, somar cada um e por fim dividir pelo tamanho dos dados.

A tabela a seguir contém ambos exemplos de calculo de média.

[Média Aritmética Ponderada](https://docs.google.com/spreadsheets/d/1jCYv_YGPKtMiu_NBwa_KGfMiZXqcQEEd_pLnx9ACQeA/edit?usp=drivesdk)

Existem situações em que os dados possuem pesos diferentes para cada um deles. Um exemplo é a média da nota bimestral de um aluno, sendo composta de uma prova (com peso 8) e uma atividade (com peso 2):

Nota da prova = 7

Nota do trabalho  = 9

$$
\overline{x} = \frac{(8x7)+(2x9)}{8+2} = 7,4
$$

A média é a medida mais importante dentro de um conjunto de dados e possui algumas propriedades importantes:

1. A média é única em um conjunto de dados.
2. **A média é afetada por valores extremamente pequenos ou grandes.**
3. A média depende de todos os valores observados, qualquer modificação nos dados fará que a média fique alterada.
4. **A soma das diferenças dos valores observados em relação à média é zero.**

$$
\sum{(x_i-\overline{x}})=0
$$

A propriedade 2 é importante pois em um conjunto de dados muito heterogêneo, a média torna-se uma medida não apropriada para representar os dados.

A propriedade 4 é importante na definição de variância, uma medida de dispersão.

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

## Moda

Chamamos de **moda o valor que aparece com maior frequência** em um conjunto de dados. Quando um conjunto de dados possui apenas uma moda, é chamado unimodal, quando duas modas, e aqui é importante ressaltar que se dois elementos possui a mesma quantidade de frequência em um conjunto de dados, é considerado os dois valores e por isso chamado de bimodal. Em casos onde o conjunto de dados não possuí nenhum valor com maior frequência, é amodal ou antimodal. 

Quando os dados estão agrupados em classes, primeiramente é necessário identificar a classe modal que apresenta a maior frequência e calcular a moda.

Primeiramente determina-se a classe com maior frequência, em seguida aplica-se a fórmula abaixo com base na classe com a maior frequência.

$$
Mo = l_i + \frac{h\times(F_i-F_{i-1})}{(F_i-F_{i-1})+(F_i-F_{i+1})}
$$

$l_i$ = limite inferior da classe modal com maior frequência

$F_i$ = É a frequência absoluta da classe modal com maior frequência

$F_{i-1}$ = É a frequência absoluta da classe modal anterior a classe com maior frequência (ex: 7ª classe que é anterior a 8ª classe que possuí a maior frequência absoluta)

$F_{i+1}$ = É a frequência absoluta da classe modal posterior a classe com maior frequência (ex: 9ª classe que é posterior a 8ª classe que possuí a maior frequência absoluta)

$h$ = É a amplitude da classe com maior frequência, ou seja a diferença do limite superior e o limite inferior da classe em questão.

<aside>
📌 Se o conjunto de dados apresentar todos os elementos com a mesma frequência absoluta, não existirá moda. Se ocorrer várias frequências iguais, então teremos uma distribuição com mais de uma moda, portanto o calculo deve ser realizado para cada classe que apresente o maior número de frequência absoluta.

</aside>

[Moda](https://docs.google.com/spreadsheets/d/12jJwIGRDudHxKciaa9apQcNbYTD3UsQ4vK1ISdg1RfU/edit?usp=drivesdk)

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

## Mediana

Corresponde ao valor central ou à média aritmética dos dois valores centrais de um conjunto de observações organizadas em ordem crescente.

{1, 3, 5, 7, **9,** 11, 13, 15, 17} ⇒ Mediana = 9

Ou quando temos uma quantidade de dados pares:

{1, 3, 5, **7, 9,** 11, 13, 15} ⇒ Mediana = (7 + 9) / 2 = 8

### Dados Agrupados

Para dados agrupados em distribuição de frequência de classe, temos:

$$
Md = l_i+ \frac{h.(p-F_{ac-1})}{F_i}
$$

$Md$ = Mediana

$Li$ = Limite inferior da classe observada

$h$ = Amplitude da classe, ou seja, limite superior menos o limite inferior da classe observada.

$p$ = Posição da mediana, é calculado por $\frac{n}{2}$, com o resultado devemos observar a frequência acumulada na tabela de modo que encontremos a última classe que `p` ≤ frequência acumulada, essa será a classe observada.

$F_{ac-1}$ = A frequência acumulada da classe anterior a classe observada.

$F_i$ = Frequência Absoluta da classe observada.

[Mediana](https://docs.google.com/spreadsheets/d/1N7noxiDhE30i_ZVKQcguYCPZUKh7WXkVaHyyc8j258k/edit?usp=drivesdk)

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

# Medidas Separatrizes

As separatrizes são os valores que dividem as séries em partes iguais. As principais medidas separatrizes são: **mediana, quartis, decis e percentis.**

## Quartis

São os valores que dividem a distribuição em 4 partes iguais

- Primeiro Quartil: $Q_1 = 0,25 * (n + 1)$
- Segundo Quartil: $Q_2 = 0,50 * (n + 1)$
- Terceiro Quartil: $Q_3 = 0,75 * (n + 1)$

## Decis

São os valores que dividem a distribuição em 10 partes iguais

[Quatis-Decis](https://docs.google.com/spreadsheets/d/1y6ob2nO2WF_jyQm5D23ZwVavUi97xkC4iqgb2SAessg/edit?usp=drivesdk)

Quando o valor de `p` ou seja $p = s_z.(n+1)$ for um inteiro, a medida separatriz está na posição de número `p` ou seja, quando o tamanho do conjunto dos dados for par. Caso contrário o calculo das medidas separatrizes para os dados em rol é:

$$
S_k = X_i + (p - i).(X_{i+1}-X_i)
$$

$S_k$ = A medida separatriz a ser utilizada (quartis, decis, percentis)

$X_i$ = Posição dos dados no rol

$p$ = É a posição da medida separatriz adotada.

$i$ = é a parte inteira de `p`

[Quartil - Percentil - p decimal](https://docs.google.com/spreadsheets/d/1Pr0Rnot-C57GZDoPpc-MQI-86_hUU9HUxBYoos2gxbk/edit?usp=drivesdk)

### Dados Agrupados

$$
S_k = l_i + \frac{h.(p-F_{ac-1})}{F_i}
$$

$S_k$ = A medida separatriz a ser utilizada (quartis, decis, percentis)

$l_i$ = É o limite inferior da classe da separatriz

$h$ = É a amplitude da classe da separatriz

$p$ = é a posição da medida separatriz adotada

$$
p = \frac{n.k}{s}
$$

$s$ = é a separatriz adotada, 4 para quartis, 10 para decis e 100 para percentis.

$n$ = quantidade de elementos da amostra

$k$ = medida de separatriz desejada k = 1, 2, ou 3 para quartis, 1, 2, ..., 9 para decis e 1, 2, ..., 99 para percentis.

$F_{ac-1}$ = É a frequência acumulada da classe anterior observada.

$F_i$ = É a frequência absoluta da classe observada.

Ao determinar o valor de `p` busca-se na tabela de classes o a classe que tenha a Frequência Acumulada mais próxima de `p`  sem que ultrapasse o valor. Ou seja, p ≤ Fac.

[Separatriz em classes](https://docs.google.com/spreadsheets/d/1sw_edz53QvZ2Qy7QR7K6eq59vlpuyP-84t-eYzPeQAI/edit?usp=drivesdk)

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

# Medidas de Dispersão

As medidas de dispersão mostram a variabilidade de um conjunto de observações em relação à região central. Essas medidas indicam se um conjunto de dados é homogêneo ou heterogêneo, mostrando se a medida de tendência central escolhida representa bem o conjunto de dados que está sendo trabalhado pelo pesquisador. 

Por vezes podemos observar em conjunto de dados distintos o mesmo valor para a média aritmética, porém o detalhe que diferencia cada conjunto de dados é a variabilidade entre os elementos. 

Exemplo:

A = 15, 15, 15, 15, 15

B = 13, 14, 15, 16, 17

C = 5, 10, 15, 20, 25

Ambos possuem a mesma média aritmética (15) porém a dispersão entre os elementos de cada conjunto é diferente. 

## Amplitude Total

Amplitude total de um conjunto de dados é a diferença entre o maior e o menor valor. Vale destacar que esse cálculo é altamente influenciado pelos valores extremos.

$$
AT = x_{max} - x_{min}
$$

$x_{max}$ = É o maior valor no conjunto de dados.

$x_{min}$ = É o menor valor no conjunto de dados.

## Variância

A variância é uma medida de variabilidade que utiliza todos os dados. É calculada considerando o quadrado dos desvios em relação à média aritmética dos dados em estudo

**Variância de uma população**

$$
 \sigma^2= \frac{ \sum_{i=1}^N(x_i -  \mu)^2 }{N}
$$

**Variância de uma amostra**

$$
 s^2= \frac{ \sum_{i=1}^n(x_i -  \bar{x} )^2 }{n-1}
$$

Exemplo:

A variância das idades observadas em uma família:

Idades: 5, 10, 12, 35, 38

Média = $\bar{x}$

$$
\bar{x} = \frac{5+10+12+35+38}{5}
$$

Média = 20

$$
 s^2= \frac{ \sum_{i=1}^n(x_i -  \bar{x} )^2 }{n-1}
$$

$$
 s^2= \frac{ \sum_{i=1}^5(x_i -  20 )^2 }{5-1}
$$

$$
s^2 = \frac{(5-20)^2+(10-20)^2+(12-20)^2+(35-20)^2+(38-20)^2}{4}
$$

$$
s^2 = \frac{938}{4}
$$

$$
s^2 = 234,5
$$

### Dados Agrupados

Para dados agrupados em classes há uma diferença nas fórmulas de variância da população e da amostra:

$$
s^2 = \frac{{\sum^{n}_{i=1}}.(x_i-\bar{x})^2.F_i}{n-1}
$$

$$
\sigma^2 = \frac{{\sum^{N}_{i=1}}.(x_i-\mu)^2.F_i}{N}
$$

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

## Desvio Padrão

O desvio padrão dá a ideia de distribuição dos desvios ao redor do valor da média.

Para o cálculo basta extrair a raiz quadrada do resultado da variância, ou seja:

$$
s= \sqrt\frac{{ \sum(x- \overline{x} )^2}}{n-1} 
$$

$$
 \sigma = \sqrt\frac{{ \sum(x- \overline{x} )^2}}{n} 
$$

Um desvio padrão pequeno, basicamente, significa que os valores do conjunto de dado estão, na média, próximos do centro desse conjunto, enquanto um desvio padrão grande significa que os valores do conjunto de dados estão, na média, mais afastados do centro.

Que percentagem de pontos de dados em um conjunto de dados deve estar dentro de 2 desvios-padrão da média? **O limite de 95% é definido pela regra empírica.**

Para saber se o desvio padrão está alto ou baixo, vamos compará-lo com o valor da média. Quanto maior o valor do desvio padrão em relação à média, maior então será a variação dos dados e mais heterogêneo é o nosso conjunto de observações.

### Dados Agrupados

O procedimento é o mesmo, ou seja, a raiz quadrada da variância. 

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

## Coeficiente de Variação

É uma medida relativa e não absoluta, usada para verificar se o conjunto de dados é homogêneo e também conseguimos saber se a média é uma boa medida para representar o conjunto de dados. Outra utilização é comparar conjuntos com unidades de medidas distintas.

O coeficiente de variação (CV) tem o problema de deixar de ser explicativo da variação quando a média está perto de zero, pois esta situação pode deixá-lo alto demais, ao mesmo tempo, quanto mais baixo for o valor do CV, mais homogêneo é o conjunto e mais representativa será sua média.

$$
CV= \frac{ \sigma }{ \mu }.100 
$$

$$
CV = \frac{s}{\bar{x}}.100
$$

Quanto à representatividade em relação à média, podemos dizer que quando o coeficiente de variação (CV) é ou está:

- Menor que 10% significa que é um ótimo representante da média pois existe uma pequena dispersão (desvio padrão) dos dados em torno da média.
- Entre 10% e 20% é um bom representante da média
- Entre 20% e 35% é uma razoável representante da média
- Entre 35% e 50% representa fracamente a média por conta da grande dispersão dos dados em torno da média.
- Acima 50% não representa a média devido a grande dispersão dos dados em torno da média.

[Variância - DV - CV](https://docs.google.com/spreadsheets/d/1p0pnkOd0we9ePzTvXh91qFVzc5LXxId4AwIqNmI5w7o/edit?usp=drivesdk)

---

⬆️ [Índice](https://www.notion.so/Medidas-Descritivas-Associadas-a-Vari-veis-Quantitativas-b3527e58e46d4d5fb80b71621064ce6d)

# Exercícios

1. Das medidas de posição vistas na unidade, explique:
    1. Qual é a mais utilizada e por quê.
    2. Quais são os problemas que a média pode ter em sua utilização como medi-
    da representativa de um conjunto de dados.
2. Considere os seguintes diâmetros (mm) de eixos produzidos em certa fábrica de
autopeças:
    1. A média aritmética, a moda e a mediana.
    2. A variância, o desvio padrão.
    3. O coeficiente de variação (interprete).
    4. O 3o quartil e o 6o decil.
3. Considere a seguinte tabela de distribuição de frequências com os tempos (em
dias) que um corretor demora a concluir um negócio, observado em 40 operações:
    1. A média aritmética, a moda e a mediana.
    2. A variância, o desvio padrão.
    3. O coeficiente de variação (interprete).
    4. O 3° quartil e o 4° percentil.

[Exercícios Capítulo 3](https://docs.google.com/spreadsheets/d/1LRnimHJzMlAMMF9TDPPMaKDD2e6aS-Frbv5Bv3q6FVE/edit?usp=drivesdk)