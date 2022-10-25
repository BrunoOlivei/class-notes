# Introdução

A estatística apresenta muitas ferramentas para descrever e analisar dados de pesquisa. A escolha das ferramentas a serem utilizadas depende dos seus objetivos, bem como a categoria de variável com a qual se trabalha.

As variáveis podem ser qualitativas e quantitativas. As ferramentas utilizadas para uma categoria de variável nem sempre podem ser utilizadas para o outro tipo. Nas pesquisas, se utiliza um grupo de variáveis.

Em alguns casos, algumas variáveis podem estar relacionadas de alguma forma e a variação de uma vai depender da variação da outra. Decisões gerenciais, geralmente, são baseadas nas relações entre duas ou mais variáveis.

O fato de duas variáveis estarem ligadas permite tomar decisões se baseando em uma variável, porém esperando resposta em outra que seja de difícil mensuração ou só possa ser medida tardiamente. Existem algumas medidas estatísticas que permitem **medir o grau de associação entre duas variáveis.**

---

# Correção Linear

Em diversas situações, o objetivo é apenas estudar o comportamento conjunto de duas variáveis e verificar se elas estão relacionadas.

O termo correlação é usado para **indicar a força que mantém unidos dois conjuntos de valores.** O estudo da correlação visa estudar a existência ou não de uma relação; e seu grau de relação entre as variáveis.

Uma medida do grau da correlação e sua direção é dada pela covariância entre duas variáveis aleatórias, mas é mais conveniente medir o grau da correlação por meio do **Coeficiente de Correlação Linear de Pearson.**

## Coeficiente de Correlação Linear de Pearson

O coeficiente de correlação é uma medida que dimensiona a correlação. É representado pela letra "r" e dado pela seguinte fórmula:

$$
r= \frac{\sum {x\times y} - \frac{ (\sum x_i\times \sum y_i)}{n}}{ \sqrt{ \begin{bmatrix}\sum {x^2_i} - \frac{(\sum x_i)^2}{n} \end{bmatrix} \times \begin{bmatrix}\sum {y^2_i} - \frac{(\sum y_i)^2}{n} \end{bmatrix}}}
$$

<aside>
💡 O valor de r não depende de qual das duas variáveis em estudo é chamada "x" e de "y" e independe das unidades com as quais as variáveis são medidas.

</aside>

A intensidade do coeficiente de correlação (r) pode variar entre -1 e 1, sendo que quanto mais próximo de -1 ou de 1, mais forte será a associação entre as duas variáveis, quanto mais próximo de 0, mais fraca será a associação.

Quando $r$ = 1, todos os pares (x, y) estarão alinhados em linha reta com coeficiente angular positivo, quando $r$  = -1, todos os pares (x, y) estarão alinhados com o coeficiente angular negativo.  

Quanto ao direcionamento entre duas variáveis, o coeficiente de correlação pode ser positivo ou negativo. Se a correlação entre as duas variáveis for positiva, dizemos que as duas variáveis variam para o mesmo sentido. 

### Exemplo

1. Sabendo que a correlação entre renda familiar e gastos com alimentação é **positiva**, podemos dizer, que à medida que a renda familiar aumenta, também, aumentam os gastos com alimentação, bem como quando a renda diminui o gasto também diminui.
2. Se o conhecimento e tempo gasto para aprender a operar uma máquina têm uma correlação negativa, então podemos pensar que à medida que o conhecimento aumenta, o tempo gasto para aprender a operar uma máquina diminui ou vice-versa.
3. Se o coeficiente de correlação for igual a 0, dizemos que não existe associação linear entre as duas variáveis.

Uma forma de representar a correlação é através do diagrama de dispersão:

![53-diagrama-dispersao.png](53-diagrama-dispersao.png)

### Exemplo:

Verifique se existe correlação linear entre o número de nascidos vivos e a taxa de mortalidade infantil na região de Maringá-PR.

[Coeficiente de Correlação e de Determinação ](https://docs.google.com/spreadsheets/d/1qOjkRslIpIY3NZrCTgA8XmtwpAODU-sfUBoYtiaY2oQ/edit?usp=drivesdk)

O valor do coeficiente de correlação foi cerca de 0,84. Assim podemos concluir que existe uma forte correlação ou associação entre o número de nascidos vivos e a taxa de mortalidade antes de 1 ano de idade, uma vez que o valor 0,84 é próximo de 1. 

Além disso, podemos verificar que, como mostrado no diagrama de dispersão, o valor dessa correlação é positivo, então podemos pensar que, se aumenta o número de nascidos vivos, também há um aumento da taxa de mortalidade até 1 ano de idade. 

## Coeficiente de Determinação

O coeficiente de determinação é dado por $R^2$, ou seja, o símbolo do coeficiente de determinação é dado por "R" maiúsculo e é dado pelo valor encontrado para a correlação linear de Pearson "r" ao quadrado.

Ele expressa a porcentagem de variação dos valores de Y em função de X, ou seja, mostra até que ponto a variação conjunta dos dados é de fato linear. 

Os resultados variam de 0 a 1, quanto mais perto de 1, maior é a variação conjunta das duas variáveis somadas com a variável X que dará um resultado onde a variável X pode ser explicada pela variável Y.

Utilizando o r do exemplo anterior, onde temos 0,84, o coeficiente de determinação é dado por: 

$$
R^2 = 0,84^2 = 0,7056
$$

Isso mostra que a variação conjunta dos dados é boa, ou seja, a taxa de mortalidade pode ser explicada pela variação no número de nascidos vivos. 

---

# Regressão Linear

A análise de regressão é uma técnica estatística cujo objetivo é investigar e descrever a relação entre variáveis por meio de um modelo matemático. Esta relação é explorada de modo que se possa obter informações sobre uma variável, por meio dos valores conhecidos das outras. 

Primeiramente, é preciso estudar a dependência de uma variável em relação à outra e, assim, indicar a variável independente para o eixo "x" e a variável dependente para o eixo "y". A medida que a variável independente (ou explicativa) varia, provoca uma mudança na variável dependente (ou resposta).

Aplicações da regressão:

- Estimar valores de uma variável com base em valores conhecidos de outra variável.
- Situações em que as duas variáveis medem, aproximadamente, a mesma situação, mas uma delas é relativamente dispendiosa ou difícil de lidar enquanto a outra não.
- Explicar valores de uma variável em termos da outra, isto é, pode-se suspeitar de uma relação de causa e efeito.
- Predizer valores de uma variável para a análise de regressão: resta saber como é o tipo dessa relação.

## Regressão Linear Simples

Quando duas variáveis, X e Y (numéricas e contínuas) estão relacionadas linearmente. Isso quer dizer que à medida que X aumenta, Y também aumenta, ou à medida que X diminui, Y também diminui. 

A equação de regressão linear é dada por:

$$
\widehat{y} = a + b\times x
$$

- $\widehat{y}$ = valor predito da variável resposta
- $a$ = constante de regressão que representa o intercepto entre a linha de regressão e o eixo y
- $b$ = coeficiente linear de regressão da variável resposta y em função da variável explicativa x; inclinação da reta; taxa de mudança na variável y por unidade de mudança na variável x.
- $x$ = valor da variável explicativa

O coeficiente linear de regressão "b" fornece uma estimativa da variação esperada de y a partir de uma unidade x.

A partir dessa equação é possível encontrar os valores preditos para y e a reta de regressão.

![54-Reta de Regressão Linear](54-grafico-reta-regressao-linear.png)

54-Reta de Regressão Linear

O diagrama de dispersão mostra o tipo de relação que existe entre x e y e também verifica se o modelo proposto (y = a + bx) explica bem a variação dos dados. O modelo explicará melhor quanto mais perto dos dados ou dos pontos a reta estiver.

O método mais usado para ajustar uma linha reta a um conjunto de pontos é conhecido como método dos mínimos quadrados que nos fornece os seguintes resultados para estimarmos a e b:

$$
b= \frac{\sum {x\times y}  - \frac{ (\sum x_i\times \sum Y_i)}{n}}{ \sum {x^2_i} -  \frac{(\sum x_i)^2}{n} }
$$

$$
a = \overline{y} - b\times \overline{x} 
$$

$\overline{y}$ e $\overline{x}$ são as médias de y e x respectivamente.

Utilizando os mesmos dados do número de nascidos vivos e a taxa de mortalidade infantil na região de Maringá-PR, onde a variável x é o número de nascidos vivos enquanto a variável y é a taxa de mortalidade, visto que é evidente que a taxa de mortalidade depende do número de nascidos vivos.

A partir dessa definição, é necessária a estimação dos parâmetros da equação a e b.

[Regressão Linear Simples](https://docs.google.com/spreadsheets/d/1Unvd2tLR9sssgBgVT0A31yNORwgSRo9Zj72r-e_nAZY/edit?usp=drivesdk)

Conforme o valor de b, dizemos que a cada 1 nascido vivo esperamos um aumento (b positivo) de 0,015% na taxa de mortalidade de crianças de até 1 ano.

Assim, a equação da reta de regressão é dada por:

$$
\widehat{y} = -0,017 + 0,015\times x
$$

Com a equação estabelecida, basta substituir o valor de x pelo valor real da variável (Nascidos Vivos), conforme na tabela acima, assim para cada número de nascidos vivos, temos uma taxa de mortalidade prevista. 

A representação gráfica para esta situação pode ser observada no diagrama de dispersão a seguir:

![55-Diagrama de dispersão para a taxa de mortalidade prevista em função do número de nascidos vivos](55-diagrama-dispersao.png)

55-Diagrama de dispersão para a taxa de mortalidade prevista em função do número de nascidos vivos

Observe que, para cada número de nascidos vivos, foi construída uma equação e obtida uma taxa de mortalidade prevista.

Vimos que a correlação linear de Pearson mostrou um valor alto para a relação entre o número de nascidos vivos e a taxa de mortalidade (0,84)

Na análise de regressão, utilizamos, também, o coeficiente de determinação para verificar a precisão da reta de regressão e dizer se ela explica bem ou não a variação dos dados:

$$
R^2 = 0,7056
$$

A explicação para análise de regressão será:

70,56% da variação observada na taxa de mortalidade é explicada pela reta de regressão. Isto mostra que a reta se aproxima bem dos pontos observados. 

![Diagrama de dispersão para a taxa de mortalidade prevista e taxa de mortalidade observada em função do número de nascidos vivos](56-diagrama-dispressao.png)

Diagrama de dispersão para a taxa de mortalidade prevista e taxa de mortalidade observada em função do número de nascidos vivos

A partir da equação dada acima e também do diagrama de dispersão, podemos fazer predições para a variável dependente em função da variável independente, dentro do intervalo estudado, basta substituir o valor de x.

**Exemplo:**

Qual a taxa de mortalidade esperada para um número de 300 nascidos vivos:

$$
\widehat{y} = -0,17 + 0,015 \times 300 = 4,33\%
$$

No entanto, essas predições devem seguir alguns critérios:

- Só podemos fazer predições em casos de valores dentro do intervalo trabalhado para a variável independente.
- Só devemos fazer essas predições caso, de fato, a variável independente explique a variação da variável dependente.

---