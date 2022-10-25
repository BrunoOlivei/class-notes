# Introdução a Estatística

# **Frequência**

Se dá pela contagem de ocorrências de um determinado dado em um conjunto de dados

{2, 2, 4, 6, 8, 10, 10, 10, 12, 12, 14, 16, 16, 16, 16, 18, 18, 20}

2 = 2 ⇒ 11%

4 = 1 ⇒ 6%

6 = 1 ⇒ 6%

8 = 1 ⇒ 6%

10 = 3 ⇒ 17%

12 = 2 ⇒ 11%

14 = 1 ⇒ 6%

16 = 4 ⇒ 22%

18 = 2 ⇒ 11%

20 = 1 ⇒ 6%

Total de 18 números

---

# **Média**

Soma dos dados divididos pela quantidade de dados

$$
\mu( \overline{x})  = \frac{\sum_{i=1}^N x_i}{n}
$$

A equação acima é o mesmo que: 

$$
\overline{x} = \frac{x_1 + x_2 + x_3+...+x_n}{n}
$$

---

# Média Aritmética Ponderada

# **Mediana**

São os dados encontrados no meio de uma lista ordenada de dados

{1, 3, 5, 7, **9,** 11, 13, 15, 17} ⇒ Mediana = 9

Ou quando temos uma quantidade de dados pares:

{1, 3, 5, **7, 9,** 11, 13, 15} ⇒ Mediana = (7 + 9) / 2 = 8

---

# **Moda**

Quando há um dado que possuí maior ocorrência

{1, 3, 3, 3, 5, 9, 11, 11, 13, 15, 17} ⇒ Moda = 3

Também pode ocorrer em um conjunto de dados onde dois valores de dados podem ter o mesmo número de ocorrências, assim a moda é os dois valores. 

---

# **Média Ponderada**

Quando um conjunto de dados possuí um *peso*

{10,0; peso 35%} ⇒ 10,0 x 35% ⇒ 10,0 x 0,35 = 3,50

{8,50; peso 25%} ⇒ 8,50 x 25% ⇒ 8,50 x 0,25 = 2,125

{6,25; peso 15%} ⇒ 6,25 x 15% ⇒ 6,25 x 0,15 = 0,9375

{2,00; peso 15%} ⇒ 2,00 x 15% ⇒ 2,00 x 0,15 = 0,3

{1,50; peso 10%} ⇒ 1,50 x 10% ⇒ 1,50 x 0,10 = 0,15

(3,50 + 2,125 + 0,9375 + 0,3 + 0,15) / (0,35 + 0,25 + 0,15 + 0,15 + 0,10) = **7,0125**

---

# **Amplitude**

Mede a distância entre da média e mediana para os pontos mais extremos dos dados (mínimo e máximo)

O cálculo se dá pela diferença entre o valor máximo e o valor mínimo.

---

# **Desvio Padrão**

((Dado1 - Média)² + (Dado2 - Média)² + ... + (DadoN - Média)²) / N-1⇒ Raiz Quadrada do Resultado = Desvio Padrão

Que percentagem de pontos de dados em um conjunto de dados deve estar dentro de 2 desvios-padrão da média? **O limite de 95% é definido pela regra empírica.**

---

# **Escore-z**

score-z = $\frac{x_{i} - \overline{x} }{S}$

Sendo: 

$**x_{i}**$ = ponto de dados = leia-se os dados que deseja-se calcular o score-z

$**\overline{x}**$ = média

$**s**$ = desvio-padrão

---

# **Percentis**

$$
⁍
$$

---

# Probabilidade

São as chances de um evento ocorrer.

## Espaço amostral

 

$$
\Omega = \{conjunto\ de\ todos\ resultados\ possíveis\}
$$

### Exemplo:

O lançamento de uma moeda, os possíveis resultados (n) são dois: cara (c) ou coroa (k). 

$$
\Omega=\{cara,coroa\}
$$

Se lançarmos a moeda duas vezes o possível resultado são:

$$
\Omega = \{cc,ck,kc,kk\}
$$

---

## Evento

É um subconjunto do espaço amostral $\Omega$ de um experimento aleatório. Pode ser considerado evento simples se consistir em um único resultado ou composto se houver mais de um resultado.

### Exemplo:

No lançamento do dado, um evento de interesse "*A*" pode ser "*obter a face par*". Então "*A*" será igual a:

$$
A = \{2,4,6\}\\ n = 3
$$

---

## Probabilidade de um evento

### Método Clássico

$$
P(A)=\frac{n(A)}{\Omega}
$$

💡 **Regras Básicas**

- A probabilidade deverá ser um valor que varie entre 0 e 1,

$$
0<P(A)<1
$$

- Um evento impossível é um conjunto vazio ($\varphi$) e atribui probabilidade 0, enquanto um evento certo tem probabilidade 1:
    
     
    
    $$
    P(\Omega)=1 \ \ \ \ P(\varphi)=0
    $$
    
- A soma das probabilidades para todos os resultados experimentais tem de ser igual a 1

---

# Teorema de Bayes

$$
P(A|B) = \frac{P(A|B)\times P(A)}{\sum_j P(B|A_j)\times P(A_j)}
$$

$P(A|B)$ = Probabilidade de A dado B

---

# Permutações

É o cálculo de quantas combinações de ordenação podem ser feitas para ***n*** objetos, sendo a fórmula para calcular o **fatorial**:

<aside>
💡 Número de formas que um conjunto de dados pode ser ordenado.

</aside>

$$
n!
$$

Quantas permutações podem ser feitas quando em uma lista de 8 corredores, somente os 3 primeiros colocados recebem a premiação:

$$
n!\div(n-x)!
$$

$n$ = Número total de objetos

$x$ = Número de objetos a serem selecionados

![25-permutação.jpg](25-permutao.jpg)

Os números idênticos entre a multiplicação de denominadores e a multiplicação de numeradores, podem ser cancelados, restando apenas os números não repetidos para se calcular.

$$
\frac{8\times7\times6\cancel\times\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1 }{\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1} 
$$

$$
8\times7\times6 = 336
$$

---

# Combinações

Às vezes a ordem dos objetos pesquisados são importantes, em outros momentos, não. 

Em uma classe com 10 alunos, e uma equipe de 4 estudantes seja escolhida aleatoriamente para representar a turma. 

Para descobrirmos a probabilidade de X e Y serem escolhidos para compor a equipe, precisamos saber quantas combinações de quatro alunos são possíveis. Porém, nesse cenário a ordem dos objetos não altera o grupo.

Fórmula

$$
n!\div[(n-x)!\times{x!}
$$

$n$ = número total de objetos

$x$ = número de objetos escolhidos ao mesmo tempo

$$
10!\div[(10-4)!\times{10!}
$$

$$
\frac{10!}{[(6)!\times{4!}]}
$$

$$
\frac{10\times9\times8\times7\times7\times6\times5\times4\times3\times2\times1}{(6\times5\times4\times3\times2\times1)\times(4\times3\times2\times1)}
$$

$$
\frac{10\times9\times8\times7\times7\times\cancel6\cancel\times\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1}{(\cancel6\cancel\times\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1)\times(4\times3\times2\times1)}
$$

$$
\frac{10\times9\times8\times7}{4\times3\times2\times1} = 210
$$

Há 210 equipes de 4 possíveis.

Se quisermos saber as possibilidades de Olivia e Leila ficarem na mesma equipe?

Sendo assim queremos saber quantas combinações com os 8 alunos restantes podem preencher os últimos 2 espaços no grupo com 4 alunos.

$$
n!\div[(n-x)!\times{x!}
$$

$$
8! \div [(8-2)!\times{2!}
$$

$$
8! \div [(6)!\times{2!]}
$$

$$
\frac{8\times7\times6\times5\times4\times3\times2\times1}{(6\times5\times4\times3\times2\times1)\times(2\times1)}
$$

$$
\frac{8\times7\times\cancel6\cancel\times\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1}{(\cancel6\cancel\times\cancel5\cancel\times\cancel4\cancel\times\cancel3\cancel\times\cancel2\cancel\times\cancel1)\times(2\times1)}
$$

$$
\frac{8\times7}{2\times1} = 28
$$

Isso significa que, das 210 combinações totais de 4 alunos na turma de 10, há 28 combinações de 4 alunos em que Leila e Olivia estão na equipe.

Dividimos os 28 resultados desejados por 210 resultados totais.

$$
28\div210 = 13,3%
$$

Assim há uma chance de 13,3% de Olivia e Leila estarem na mesma equipe que representa a turma. 

---

# Variável Aleatória

Em experimentos o valor do resultado é desconhecido/aleatório. Assim, o resultado do experimento é uma variável aleatória. 

**Variável Aleatória Discreta** são variáveis de números inteiros, como a probabilidade da soma do valor de dois dados lançados, ou a probabilidade da quantidade de bebida pedida pelo próximo cliente do Starbucks, como não há como pedir meia bebida, apenas números inteiros são considerados, portanto, discreta. 

**Variável Aleatória Contínua**, a quantidade total de chuva em um mês em Londres pode ser de 6,60mm, 34,29mm, 70,36mm, não há limites. Os valores na variável aleatória são infinitas.

---

# Média e desvio-padrão de distribuições de probabilidade discretas

[Média e desvio-padrão de distribuições de probabilidade discretas](https://docs.google.com/spreadsheets/d/19jRAvyGjHVSovtrBusd5lWD0sxVGkRoh77Q6Ea6q3tg/edit?usp=drivesdk)

---

# Valor monetário esperado

Podemos utilizar o cálculo de valor monetário esperado para projetar os custos de um projeto, as comissões para o próximo ano ou mês, ou qualquer valor em dinheiro a ser projetado. 

[Valor Monetário Esperado](https://docs.google.com/spreadsheets/d/1JNAWOCYOiM4TnjmjOgYaXht5R4SF18h8Y3as1E18lLE/edit?usp=drivesdk)

---

# Variável aleatória binomial

Um experimento que tem apenas dois resultados possíveis. 

Exemplo: 

- Lançamento de uma moeda, os resultados possíveis podem ser cara ou coroa.
- Eleitores podem votar ou não
- Um paciente pode receber um diagnóstico positivo ou negativo para uma doença

[Variável aleatória binomial](https://docs.google.com/spreadsheets/d/19N1Fl8ICMZZZS0AumM3QlflLaCHvPg4n1wuSKpdFz6E/edit?usp=drivesdk)

# Fundamentos Estatística II

## Teorema do Limite Central

Quanto mais amostras coletarmos, mais próximas às médias das amostras chegarão da média da população.

Exemplo:

Em um conjunto de dados onde temos:

10, 15, 20, 25, 5, 15, 20, 20, 5, 5, 15 e 20 a média é: 15

Se em três observações distintas, realizadas através de amostras levantadas em determinados momentos diferentes tivermos:

Amostra 1: 10, 15, 20, 25 — Média = 17,5

Amostra 2: 5, 15, 20, 20 — Média = 15

Amostra 3: 5, 5, 15, 20 — Média = 10

Agora se fizermos a média das médias chegaremos ao valor de 14,58 o que é bastante próximo da média de todos os valores.

<aside>
💡 Portanto, a premissa de que quanto mais amostras coletarmos, mais próximos às médias das amostras chegarão da média da população.

</aside>

Assim aumentando o tamanho da amostra a curva se torna cada vez mais normal, consequentemente o desvio padrão diminui. 

---

## Variabilidade das médias amostrais

Também conhecido como **Erro Padrão para médias**

$$
\sigma_{\overline{x}} = \frac{\sigma}{\sqrt{n}}
$$

<aside>
💡 Ao lidar com médias, o erro padrão é o mesmo que o desvio padrão das médias das amostras.

</aside>

---

## Variabilidade das proporções amostrais

Também conhecido como Erro Padrão para proporções, muito usado quando se trata de diversas amostras

$$
\sigma_{\widehat{p}}= \sqrt{\frac{p\times(1-p)}{n}}
$$

---

## Intervalos de Confiança

### Margem de Erro para Proporção Populacional

Usado quando se temos apenas 1 amostra e com base no nível de credibilidade desejado, queremos levantar os valores de uma variável. 

> Estamos 95% confiantes de que um adulto médio brasileiro beba de 2 a 3 litros de líquido por dia.
> 

Usado geralmente em pesquisas de opinião onde as possíveis respostas são apenas Sim/Não/Prefiro Não Opinar, assim a estatística utilizada para relatar os resultados é a proporção de pessoas da amostra que se encaixam em cada grupo, também conhecida como proporção amostral ou porcentagem amostral. 

A fórmula para o cálculo de margem de erro de uma proporção amostral é: 

$$
\widehat{p} \pm Z\times \sqrt{\frac{\widehat{p}\times (1-\widehat{p})}{n}}
$$

Onde:

- $\widehat{p}$ = proporção amostral - Dividindo o número de pessoas na amostra que possuem a característica a ser estudada pelo tamanho amostral (n).
- $n$ = tamanho da amostra
- $Z$= é o valor apropriado para o nível de credibilidade desejado, conforme tabela a baixo

| Intervalo de confiança | Valor de Z |
| --- | --- |
| 99% | 2.575 |
| 98% | 2.33 |
| 95% | 1.96 |
| 90% | 1.645 |

Passo a passo para o cálculo:

1. Encontre a proporção amostral, $\widehat{p}$, e o tamanho amostral, $n$ 
2. Multiplique $\widehat{p}\times(1-\widehat{p})$
3. Divida o resultado do passo anterior por $n$
4. Obtenha a raiz quadrada do valor calculado

Aqui obtemos o erro padrão

1. Multiplique o resultado pelo valor $Z$ apropriado ao nível de credibilidade desejado.  

#### Exemplo

Pesquisa sobre aprovação do presidente. Considerando o intervalo de confiança de 95% temos que $Z$ = 1,96. O número de entrevistados que disseram aprovar é 520, o que significa que a proporção amostral é, $\frac{520}{1000} = 0,52$, o tamanho da amostra $n$ é igual a 1000. 

$$
1,96\times \sqrt{\frac{0,52\times(1-0,52)}{1000}} = 0,0310 \\ \\ 3,10\%
$$

<aside>
💡 A proporção amostral é a versão decimal da porcentagem amostral

</aside>

---

### Erro de Amostragem (Margem de Erro Amostra)

Quando em uma pesquisa nos pedem um valor numérico (por exemplo, quantas pessoas moram em sua casa), a estatística utilizada para relatar os resultados é a média de todas as repostas dadas pelas pessoas da amostra, também conhecida como média amostral.

A fórmula geral para o cálculo da margem de erro para a sua média amostral é:

$$
\overline{x} \pm Z\times \frac{s}{\sqrt{n}}
$$

Onde:

- $s$ = é o desvio padrão amostral
- $n$ = é o tamanho da amostra
- $Z$ = é o valor Z apropriado para o nível de credibilidade
- $\overline{x}$ = média da amostra

---

### Intervalo de Confiança para diferença de duas médias populacionais

Usada, por exemplo, para comparar a diferença no salário médio de homens e mulheres, na idade de Democratas e Republicanos. 

$$
(\overline{x}-\overline{y}) \pm Z \times \sqrt{\frac{S_1^2}{n_1}+\frac{S_2^2}{n_2}}
$$

Onde:

- $\overline{x}$ = Média da primeira amostra
- $S_1$ = Desvio padrão da primeira amostra
- $n_1$ = tamanho amostral da primeira amostra
- $\overline{y}$ = Média da segunda amostra
- $S_2$ = Desvio padrão da segunda amostra
- $n_2$ = Tamanho amostral da segunda amostra
- $Z$ = Valor correspondente ao nível de confiança desejado, segundo a distribuição normal padrão (Score Z)

---

### Intervalo de Confiança para diferença de duas proporções populacionais

Quando a característica, como a opinião acerca de determinado assunto (apoia/não apoia), de dois grupos que estão sendo comparados por categoria, e suas diferenças proporcionais. Exemplo, a diferença entre a proporção de homens e mulheres que são a favor de uma semana com apenas quatro dias úteis. 

$$
(\widehat{p}_1-\widehat{p}_2)\pm Z\times \sqrt{\frac{\widehat{p}_1\times (1-\widehat{p}_1)}{n_1}+\frac{\widehat{p}_2\times (1-\widehat{p}_2)}{n_2}}
$$

Onde:

- $\widehat{p}_1$ = proporção amostral da primeira amostra
- $n_1$ = tamanho amostral da primeira amostra
- $\widehat{p}_2$ = proporção amostral da segunda amostra
- $n_2$ = tamanho amostral da segunda amostra
- $Z$ = valor correspondente ao nível de confiança desejado, segundo a distribuição normal padrão (Score Z)

---

## Teste de hipóteses

Um teste de hipótese é um procedimento estatístico desenvolvido para testar um argumento. Normalmente o argumento é feito sobre um parâmetro populacional (um número que caracteriza toda uma população). Por exemplo, o argumento de que 25% ou 0,25 de todas as mulheres têm varizes é um argumento sobre a proporção (parâmetro) de todas as mulheres (população) que têm varizes (a variável).

O argumento sobre as varizes é que o parâmetro, a proporção da população `p`, é igual a 0,25 (esse argumento é chamado **hipótese nula**). Se sairmos para testar esse argumento, estaremos questionando o argumento e conseguiremos nossa própria hipótese (chamada hipótese de pesquisa ou **hipótese alternativa**). Pode-se estabelecer uma hipótese, por exemplo, de que a real proporção de mulheres com varizes é menor que 0,25, segundo suas observações.

Podemos também estabelecer hipóteses de que, em virtude, da popularidade de sapatos de salto alto, a proporção pode ser ainda maior que 0,25. Ou se apenas estivermos questionando se a verdadeira proporção é 0,25, a hipótese alternativa será: "Não, não é 0,25".

Há também a possibilidade de testar hipóteses sobre **variáveis numéricas**, como tempo médio que as pessoas gastam para ir ao trabalho em São Paulo, ou a renda familiar média. Nesses casos, o parâmetro a ser estudado é a **média populacional.**

Hipóteses também podem ser testadas para mais de um único parâmetro. Por exemplo, comparar as rendas familiares médias ou o tempo que as pessoas gastam para ia ao trabalho em duas ou mais cidades. Também há possibilidade de avaliar a relação entre renda familiar e tempo gasto para chegar ao trabalho. 

### Configurando a hipótese

Todos os testes de hipótese contêm duas hipóteses. 

- Hipótese nula ($H_0$): sempre afirma que o parâmetro da população é igual ao valor do argumento.
- Hipótese alternativa ($H_a$):
    - O parâmetro da população NÃO é igual ao valor do argumento
        
        $H_a: parâmetro \neq argumento$
        
    - O parâmetro da população é MAIOR que o valor do argumento
        
        $H_a: parâmetro > argumento$
        
    - O parâmetro da população é MENOR que o valor do argumento
        
        $H_a: parâmetro < argumento$
        

<aside>
🧠 Os testes de hipótese funcionam como um tribunal, em que $H_0$ é semelhante ao veredicto de inocência e $H_a$ é o veredicto de culpabilidade. Em um tribunal, sempre se parte do princípio que o réu é inocente até se prove contrário.

</aside>

Em geral, quando a hipótese é testada, você estabelece $H_0$ e $H_a$ para que você acredite que $H_0$ é verdadeiro, a menos que suas evidências provem o contrário. 

Após o estabelecimento da hipótese alternativa, selecione uma amostra aleatória dos indivíduos da população e calcule a estatística amostral. Em seguida, transforme a estatística amostral em uma estatística de teste, convertendo-a em um escore padrão.

- Faça a diferença entre a estatística amostral e o número da hipótese nula. Essa será a distância entre a alegação e seus resultados.
- Divida essa distância pelo valor do erro padrão de sua estatística. Esse procedimento transforma a distância em unidades padrões.

Encontre o valor p para a estatística teste.

---

## Testes de Hipóteses mais Utilizados

### Teste Hipótese Média Populacional

Este teste é usado quando a variável estudada for numérica (por exemplo, idade, renda, tempo, etc) e somente uma população ou grupo está sendo estudado (por exemplo, todos os estudantes, todos os lares brasileiros, mães que trabalham fora, etc).

$$
\frac{\overline{x}-\mu_0}{\frac{s}{\sqrt{n}}}
$$

Onde:

$\mu_0$ = média populacional alegada ($H_0)$

$\overline{x}$ = média amostral (levantada através da pesquisa para o teste de hipótese)

$s$ = desvio padrão da amostra

$n$ = tamanho amostral

O resultado dessa equação nos mostra o **total de erros padrões acima ou abaixo da média populacional alegada**. Para decidirmos se a Hipótese Nula ($H_0$) é verdadeira, calculamos valor-$\rho$  encontrado na tabela de distribuição normal padrão.

- Se a Hipótese Alternativa ($H_a$) for de superioridade, subtraia 100% do percentil encontrado.
- Se a Hipótese Alternativa ($H_a$) for de inferioridade, encontre o percentil na tabela de distribuição normal padrão.
- Se e somente se a Hipótese Alternativa ($H_a$) for de NÃO igualdade, encontre o valor na tabela de distribuição normal e multiplique por dois.

### Teste de Hipótese Proporção Populacional

Este teste é utilizado quando a variável for categórica (por exemplo, sexo, partido político, situação/oposição, etc) e quando apenas uma única população ou grupo estiver sendo estudado (por exemplo, todos os brasileiros, ou todos os eleitores registrados, etc.)

$$
\frac{\hat{p}-p_0}{\sqrt{\frac{p_0\times(1-p)}{n}}}
$$

Onde:

$\hat{p}$ = Proporção amostral ($\frac{p}{n})$

$p_0$ = Valor alegado ($H_0$)

$n$ = Tamanho da amostra

O resultado desta equação é o erro padrão, com ele buscamos o percentil na tabela de distribuição normal padrão e dividimos por 100 para obter o valor-$\rho$.

### Comparando Duas Médias Populacionais Separadas

Este teste é usado quando a variável for numérica (por exemplo, renda, nível de colesterol, quilômetros rodados por litro) e quando duas populações ou grupos estiverem sendo comparados (por exemplo, homens vs. mulheres, atletas vs. não-atletas, carros de passeio vs. utilitários). É preciso que se coletem duas amostras aleatórias separadas, uma para cada população. A hipótese nula ($H_0$) é de que as duas médias populacionais são iguais, $H_0:\mu_x-\mu_y = 0$

$$
\frac{\overline{x}-\overline{y}}{\sqrt{\frac{s_x^2}{n_1}+\frac{s_y^2}{n_2}}}
$$

Onde:

$\overline{x}$ = Média amostral da primeira população

$\overline{y}$ = Média amostral da segunda população

$s_1$ = Desvio padrão da primeira amostra

$s_2$ = Desvio padrão da segunda amostra

$n_1$ = Tamanho da primeira amostra

$n_2$ = Tamanho da segunda amostra

Com o resultado, encontra-se o valor do percentil na tabela de distribuição normal padrão. Como a hipótese alternativa é de não igualdade, multiplica-se o valor encontrado na tabela por 2, em seguida transforme o resultado em uma probabilidade (dividindo por 100) e temos o valor-$\rho$.

---

Em uma cidade com uma população de 35.000 habitantes, 50% são homens e 50% são mulheres.

Uma vez por semana uma amostra de 50 pessoas é levantada para participação no juri. As mulheres estão reclamando que estão sendo mais convocadas que os homens. 

Os responsáveis por fazer a seleção alegam que o sorteio de convocação é totalmente aleatório.

Um comitê de investigação é chamado para apurar e utiliza uma amostra da convocação para juri. Essa amostra revela que 14 homens e 36 mulheres foram convocadas.

1. Etapa: formular as hipóteses
    
    $**H_0$ = Hipótese nula**
    
    Os números do júri aconteceram por acaso.
    
    Mostra chances de mulheres serem escolhidas como 50%
    
    $$
    H_0 \ é\ p\leq 0,50
    $$
    
    $H_a$ = Hipótese alternativa
    
    Números do juri não ocorreram por acaso
    
    Mostra chances de mulheres serem escolhidas acima de 50%
    
    $$
    H_a\ é\ p>0,50
    $$
    
2. Etapa: Estabelecer o nível de significância
    
    Definir um limiar para o teste. 
    
    Nível de significância = 5%. Se 36 ou mais mulheres que terminam no júri tiverem menos de 5% de chance de serem escolhidas aleatoriamente, rejeitaremos a hipótese nula.
    
3. Etapa: Identificar a estatística de teste
    
    Como podemos calcular se 36 mulheres e 14 homens, ou outro caso mais extremo, poderia acontecer aleatoriamente nessas circunstâncias. 
    
     Probabilidade Binomial
    
    $p$ = 0,50 é a probabilidade de uma mulher ser escolhida para o painel do juri, faremos 50 tentativas, já que esse é o número de cadeiras no painel. 
    
4. Etapa: Determinar o valor - p
    
    Procurar a probabilidade de o número de mulheres escolhidas para o júri ser de 36 ou mais.

---

# Pesquisas de Opinião

O processo de pesquisa pode ser dividido em dez passos:

1.  Estabelecimento do objetivo da pesquisa;
2.  Definição da população alvo;
3.  Escolha do tipo de pesquisa;
4.  Formulação das perguntas;
5.  Estabelecimento do momento certo para a pesquisa;
6.  Seleção da amostra;
7.  Coleta de dados;
8.  Insistência, insistência e mais insistência;
9.  Organização e análise dos dados;
10.  Formulação das conclusões.

## Estabelecendo o objetivo da pesquisa

Ao estabelecer o propósito da pesquisa, seja o mais específico possível, pense nos tipos de conclusões a que gostaria de chegar se tivesse que escrever um relatório e deixe que isso o ajude a determinar as metas de sua pesquisa. Quando mais específico mais fácil será a formulação das perguntas e mais prático será o relato dos resultados.

#pesquisaopinião #testehipótese #estatísticadescritiva #teoremalimitecentral #intervaloconfiança 