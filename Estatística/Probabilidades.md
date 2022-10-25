# Probabilidades

Created: August 26, 2021 10:13 AM

# Introdução

Identificar a chance de ocorrência de um determinado resultado de interesse em situações nas quais não é possível calcular com exatidão o valor real do evento. Então, desta forma, trabalhamos com chances ou com probabilidades.

As decisões nos negócios são frequentemente baseadas na análise de incertezas, tais como: chances de investimento ser lucrativo, chances das vendas descerem se o preço for aumentado, probabilidade de projetos terminarem no prazo, etc.

---

# Probabilidade

<aside>
💡 **Experimento determinístico** são experimentos que, realizados nas mesmas condições, conduzem a resultados praticamente iguais, exemplo: misturar água e óleo de cozinha e observar o resultado obtido após algum tempo, o resultado sempre será o mesmo, o óleo sempre ficará acima da água.

</aside>

As probabilidades são utilizadas para delinear a hipótese de ocorrência de determinado evento. Seus valores são sempre atribuídos numa escala de 0 a 1. A probabilidade próxima de 1 indica um evento quase certo, enquanto a probabilidade próxima de zero indica um evento improvável de acontecer.

Probabilidade define experimentos como ações ou processos que geram resultados bem definidos. 

<aside>
💡 Os **experimentos aleatórios** são aqueles que, repetidos várias vezes, apresentam resultados imprevisíveis, devendo sempre especificar o que deverá ser observado.

</aside>

A análise qualitativa de risco é definida como o processo de avaliação do impacto e probabilidade de riscos identificados. Este processo prioriza riscos conforme os seus efeitos potenciais nos objetivos do projeto. Análise qualitativa de risco é um modo de determinar a importância de se endereçar riscos específicos e guiar respostas de risco. 

A questão crítica do tempo e as ações relacionadas ao risco podem ampliar a importância de um risco.  

Essa análise qualitativa de risco requer que a probabilidade e as consequências dos riscos sejam avaliadas, usando métodos e ferramentas de análise qualitativa estabelecida. Tendências nos resultados, quando a análise qualitativa é repetida, pode indicar a necessidade de mais ou menos ação da gerência de risco. 

Uso dessas ferramentas ajuda a corrigir influências que estão frequentemente presentes em um plano de projeto. 

---

## Exemplos Práticos de Probabilidades

O estudo da ocorrência das faces de um dado, será o experimento aleatório. Sabe-se que um dado tem 6 faces, podemos construir o modelo probabilistico da seguinte maneira:

![26-modelo-probabilistico.jpg](26-modelo-probabilistico.jpg)

Se o experimento for o lançamento de uma moeda, sabendo-se que só podem ocorrer duas situações: cara ou coroa, o modelo probabilístico para esta situação seria:

![27-modelo-probabilistico.jpg](27-modelo-probabilistico.jpg)

Em um grupo de 50 pessoas, onde 20 são homens e 30 são mulheres, se um deles for sorteado ao acaso, o modelo probabilístico será:

![28-modelo-probabilistico.jpg](28-modelo-probabilistico.jpg)

<aside>
📌 Um modelo probabilístico envolve os conceitos de espaço amostral e eventos.

</aside>

---

## Espaço amostral

São os conjuntos de todos os resultados possíveis de um experimento, representado por $\Omega$. Os elementos do **espaço amostral** são chamados **pontos amostrais**.

**Exemplo:**

O lançamento de uma moeda, os possíveis resultados (n) são dois: cara (c) ou coroa (k). 

O espaço amostral é dado por:

$$
⁍
$$

Se lançarmos a moeda duas vezes o possível resultado são:

$$
\Omega = \{cc,ck,kc,kk\}
$$

---

## Evento

É um subconjunto do espaço amostral $\Omega$ de um experimento aleatório. Pode ser considerado evento simples se consistir em um único resultado ou composto se houver mais de um resultado.

### **Exemplo:**

O lançamento de uma moeda $\Omega = \{cara, coroa\}$. Um evento de interesse "*A*" pode ser "*obter cara no lançamento de uma moeda*", então $A=\{cara\}$ e o $n$ para este evento será 1. Sendo $n$ o número de resultados para o evento.

No lançamento do dado, um evento de interesse "*A*" pode ser "*obter a face par*". Então "*A*" será igual a:

$$
A=\{2,4,6\}
$$

Então:

$$
n=3
$$

---

## Probabilidade de um evento

Existem três formas distintas:

- **Método clássico:** quando o espaço amostral tem resultados [equiprováveis](https://www.dicio.com.br/equiprovavel/).
- **Método empírico:** baseado na frequência relativa de um grande número de experimentos repetidos.
- **Método subjetivo:** baseia-se em estimativas pessoais de probabilidade com certo grau de crença.

### Método Clássico

Considerando um experimento aleatório em que se queira determinar um evento (A). A probabilidade deste evento ocorrer é denotada por $P(A)$, sendo dada pela razão do número de resultados do evento (A), $n(A)$, pelo número total de resultados no espaço amostral $\Omega$:

$$
P(A)=\frac{n(A)}{\Omega}
$$

### **Exemplo:**

Considere o lançamento de um dado, calcule a probabilidade de obetermos uma face ímpar (evento A) e a probabilidade de sair as faces 2 e 5 (evento B)

O espaço amostral é composto por todos os resultados possíveis:

$$
\Omega=\{1,2,3,4,5,6\}, n=6
$$

Os resultados possíveis para o evento A e B:

$$
A = \{1,3,5\}, n=3
$$

$$
B=\{2,5\}, n=2
$$

Assim:

$$
P(A)=\frac{n(A)}{\Omega}
$$

$$
P(A)=\frac{3}{6}
$$

$$
P(A)=0,5 = 50\%
$$

$$
P(B)=\frac{n(B)}{\Omega}
$$

$$
P(B)=\frac{2}{6}
$$

$$
P(B)=0,33 = 33\%
$$

## Regras Básicas

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

## Operações com Eventos

Nos cálculos de probabilidades, algumas vezes, o interesse do pesquisador está na determinação da probabilidade de combinação dos eventos relacionados ao experimento aleatório, sendo:

- Evento **intersecção** de A e B, denotado por $A\cap{B}$, é o evento em que A e B ocorrem simultaneamente.
    
    ![37-interseccao.png](37-interseccao.png)
    
- O evento reunião de A e B, denotado por $A\cup{B}$, é o evento em que A ocorre ou B (ou ambos) sendo a soma da probabilidade de A e B, podendo haver intersecção ou não nos dois conjuntos probabilísticos
    
    ![38-uniao.png](38-uniao.png)
    
- Evento complementar de A, denotado $A^c$ é o evento em que não ocorre, na imagem abaixo a área azul é o evento complementar de A:
    
    ![39-complemento.png](39-complemento.png)
    

### Exemplo

Um baralho com 53 cartas, desejamos saber qual a probabilidade de sair um rei de copas. Para este evento o calculo das probabilidades é uma intersecção, já que determina que seja um rei de copas, são duas variáveis ao mesmo tempo.

$$
P(A\cap{B})
$$

$A$ = É a probabilidade da carta ser um rei

$B$ = É a probabilidade da carta ser de copas

Agora a probabilidade de sair uma carta de valor dois ou uma carta de valor 5:

$$
P(C\cup{D})
$$

$C$ = A probabilidade de sair uma carta de valor 2

$D$ = A probabilidade de sair uma carta de valor 5

### Regra Adição

Essa regra considera a ocorrência do evento A ou a ocorrência do evento B, ou ainda de ambos os eventos. Denotada por $P(A\cup{B})$ e dizemos união de A ou B.

No cálculo dessa probabilidade, surgem duas situações:

A primeira quando os eventos A e B são mutuamente excludentes (não têm elementos em comum):

![40-uniao-excludente.png](40-uniao-excludente.png)

$$
P(A\cup{B}) = P(A)+P(B)
$$

### **Exemplo:**

Em um lançamento de par de dados, a vitória é se a soma dos resultados for 7 ou 11. Dos 36 cenários possíveis há 6 onde se a soma dos resultados são 7 e outras 2 possibilidades de obter soma 11, nesse cenário não há sobreposição:

$$
\frac{6}{36}+\frac{2}{36}=\frac{8}{36} = 22,2\%
$$

A segunda, quando os eventos A e B não são mutualmente excludentes (têm elementos em comum):

![39-uniao-nao-excludente.png](39-uniao-nao-excludente.png)

$$
P(A\cup{B}) = P(A) + P(B) - P(A\cap{B})
$$

Supondo 

$P(A\cap{B})$ = Probabilidade de A e B ocorrerem simultaneamente; intersecção entre eventos A e B.

![37-interseccao.png](37-interseccao%201.png)

Em um jogo de moedas, jogamos duas vezes, ganha se sair cara uma vez ou em ambas às vezes, quais são as chances de ganhar? Primeiro vamos ver quais são os possíveis resultados, sendo Ca para Cara e Co para Coroa:

- CaCo
- CoCo

- CoCa
- CaCa

Nos 4 cenários existem 3 possibilidades de vitória, porém há uma sobreposição no evento 3

Evento 1 = CaCo

Evento 2 = CaCo

Evento 3 = CaCa

$$
\frac{Evento1}{50\%} + \frac{Evento2}{50\%} -\frac{sobreposição}{25\%} = 75\%
$$

Em um lançamento de par de dados,  a vitória é se sair um seis em um dado ou nos dois. Dos 36 cenários possíveis há 6 onde se obtém o número 6 no primeiro dado e outras 6 possibilidades de obter o número 6 no segundo dado, porém há uma sobreposição, assim para calcular a probabilidade total tem:

$$
\frac{6}{36}+\frac{6}{36}-\frac{1}{36} = \frac{11}{36} = 30,56\%
$$

---

## Complemento de um Evento

Dado um evento A, o complemento de $A(A^c)$ é um evento que consiste de todos os pontos amostrais que não estão em A.

$$
P(A^c)=1-P(A)
$$

![39-complemento.png](39-complemento%201.png)

### Exemplos:

Considere o lançamento de um dado e os seguintes eventos: sair faces pares (A), sair faces ímpares (B), sair faces cujo valor é maior do que 3 (C). Ou seja:

Ω = {1, 2, 3, 4, 5, 6} 

A = {2, 4, 6} 

B = {1, 3, 5}

C = {4, 5, 6} 

n(Ω) = 6

n(A) = 3

n(B) = 3

n(C) = 3

Vamos calcular as seguintes probabilidades: P(A ∩ B), ou seja, a probabilidade do evento A e B ocorrerem simultaneamente, P(A ∩ C), ou seja, a probabilidade do evento A e C ocorrerem simultaneamente, P(A ∪ B) é a probabilidade do evento A ou B  ou ambos ocorrerem e P(Ac) são os eventos complementares. Temos que:

A ∩ B = {}

A ∩ C = {4, 6}

A ∪ B = {1, 2, 3, 4, 5, 6} = Ω

Ac = {1, 3, 5}

n(A ∩ B) = 0

n(A ∩ C) = 2

n(A ∪ B) = 6

n(Ac) = 3

$$
P(A\cap{B})=\frac{0}{6}=0
$$

$$
P(A\cap{C})=\frac{2}{6}=0,33
$$

$$
P(A\cup{B})=\frac{6}{6}=1
$$

$$
P(A^{c})=\frac{3}{6}=0,5
$$

---

# Exercício 1

Um digitador comete erros em 30% das páginas digitadas. Em um concurso ele é aprovado se digita uma folha inteira sem cometer erros, permitido apenas 3 tentativas. Sendo "X" número de tentativas feita pelo candidato, determine a probabilidade de X ser igual a 3, ou seja, o candidato fazer 3 tentativas. 

$$
\frac{erro}{0,3}\times\frac{erro}{0,3}\times\frac{erro}{0,3}+\frac{erro}{0,3}\times\frac{erro}{0,3}\times\frac{acerto}{0,7}\\ 0,027+0,063\\0,09\\9\%
$$

---

# Exercício 2

Dos 50 alunos de uma sala, **10 foram reprovados em física,** **12 em matemática e 6 reprovaram em física e matemática**. Se um aluno é escolhido ao acaso, sabendo que ele foi reprovado em física, qual a probabilidade de ele ter sido reprovado em matemática?

![47-exercicio-ao-vivo.jpg](47-exercicio-ao-vivo.jpg)

$$
\frac{6}{10}=0,6\\6\%
$$

---

## Probabilidade Condicional

Frequentemente, a probabilidade de um evento é influenciada pela ocorrência de um evento paralelo. Seja A um evento com probabilidade P(A). Se obtivermos a informação extra que o evento B ocorreu paralelamente, iremos tirar vantagem dela no cálculo de uma nova probabilidade para o evento A. Esta será escrita como P(A | B) e lida como “**probabilidade de A dado B**”.

Se soubermos que o imóvel é um apartamento, qual é a hipótese de ser da região norte? Reformulando a pergunta, poderíamos ter o interesse de saber: dado que o imóvel é um apartamento, qual a probabilidade de pertencer à região norte? Observe que estamos impondo uma condição ao evento. Sabemos que o imóvel é um apartamento, essa é a condição imposta. Quando impomos alguma condição em probabilidade, dizemos então que a probabilidade é condicional e, assim, reduzimos então o espaço amostra à condição imposta.

$P(B|A)$ lê se a probabilidade de B dado A, sendo a condição A.

$$
P(A|B)=\frac{P(A\cap{B})}{P(B)}
$$

---

## Eventos Independentes

Dois eventos A e B são independentes se P(A | B) = P(A) ou P(A | B) = P(B). Caso contrário, os eventos são dependentes.

$$
P(A|B)=\frac{P(A\cap{B})}{P(B)}
$$

Desta relação, obtemos a regra do produto das probabilidades, em que:

Neste cenário a probabilidade de A está condicionada por B, mostrando haver uma dependência. Portanto a probabilidade de A e B ocorrerem conjuntamente está sob a condição anterior $P(A|B)$.

$$
P(A\cap{B})={P(B)}\times{P(A|B)}
$$

Em caso de A e B serem eventos independentes, ou seja, a probabilidade de um evento não depender da ocorrência do outro evento, nesta condição A probabilidade de A e B ocorrer é dada pela probabilidade de A vezes a probabilidade de B.

$$
P(A\cap{B})=P(A)\times{P(B)}
$$

### **Exemplo:**

Uma urna contém duas bolas brancas e três bolas pretas. Sorteamos duas
bolas ao acaso sem reposição. Isto quer dizer que sorteamos a primeira bola, verificamos sua cor e não a devolvemos à urna. As bolas são novamente misturadas e sorteamos então a segunda bola. Para resolver as probabilidades nesta situação, ilustraremos a situação por um diagrama de árvore em que em cada “galho da árvore” estão indicadas as probabilidades.

![31-arvore-probabilidades.png](31-arvore-probabilidades.png)

O cálculo das probabilidades, na segunda retirada, fica condicionado aos resultados da primeira retirada:

![32-probabilidades-arvore.png](32-probabilidades-arvore.png)

Considere agora que vamos fazer o mesmo sorteio, mas repondo a primeira bola sorteada novamente na urna. Assim, as probabilidades são:

![33-arvore.png](33-arvore.png)

![34-probabilidades-arvore.png](34-probabilidades-arvore.png)

---

## Regras Básicas da Probabilidade

- P(A ou B), para eventos não mutuamente excludentes:
    
    $$
    P(A\ ou\ B\ ou\ ambos) = P(A)+P(B)-P(A\ e\ B)
    $$
    
- Para eventos mutuamente excludentes:
    
    $$
    P(A\ ou\ B)=P(A)+P(B)
    $$
    
- Para eventos independentes:
    
    $$
    P(A\ e\ B)=P(A)\times{P(B)}
    $$
    
- Para eventos dependentes:
    
    $$
    P(A\ e\ B)=P(B)\times{P(A|B)}\ ou\ P(A)\times{P(B|A)}
    $$
    

---

## Distribuições de Probabilidade

Os métodos de análise estatística requerem sempre que sejam enfocados certos aspectos numéricos dos dados (média, desvio padrão, etc.), independentemente de o experimento originar resultados qualitativos ou quantitativos.

O meio de descrever, por valores numéricos, os resultados experimentais é o conceito de **Variável Aleatória.**

Uma variável aleatória permite passar cada um dos resultados do experimento para uma função numérica dos resultados. Em geral, cada resultado é associado por um número, especificando-se uma regra de associação.

Observe o exemplo do lançamento de uma moeda duas vezes. A variável aleatória é o “número de caras” em duas jogadas. Considerando C como sair cara e K como sair coroa, os possíveis resultados são:

![35-distribuicao-probabilidades.png](35-distribuicao-probabilidades.png)

A distribuição de probabilidades ficará:

![36-distribuicao-probabilidade.png](36-distribuicao-probabilidade.png)

---

# Distribuição de Probabilidades Discretas

Existem experimentos cujos resultados, refletidos em uma variável aleatória, seguem um comportamento previsível em relação às suas probabilidades de ocorrência e, podem ser modelados por uma equação específica.

Dentre as principais distribuições discretas, destaca-se a Distribuição de Bernoulli, Distribuição Binomial e Distribuição de Poisson.

## Distribuição de Bernoulli

A distribuição de Bernoulli consiste em uma distribuição em que a variável aleatória assume apenas dois possíveis resultados: sucesso (o evento se realiza) ou fracasso (o evento não se realiza).

Exemplo:

- Uma peça é escolhida ao acaso: o resultado é defeituosa ou não.

Em todos os casos definimos uma variável aleatória X que só assuma dois valores possíveis:

$$
X=\begin{cases}0&\rightarrow fracasso\\1&\rightarrow sucesso\end{cases}
$$

$$
P(X=0)=q\ 
$$

$$
P(X=1)=p
$$

A função probabilidade de Bernoulli é dada:

$$
P(X=k)=p^k\times{q^{1-k}}
$$

O cálculo dos diversos aspectos numéricos dos dados são dados pelas funções a seguir:

- Média (chamada de Esperança):
    
    $$
    E(X)=p
    $$
    
- Variância:
    
    $$
    Var(X)=pq
    $$
    
- Desvio Padrão:
    
    $$
    \sigma(X)=\sqrt{pq}
    $$
    

### **Exemplo:**

Supondo que a probabilidade de venda amanhã seja de 0,8.

Seja a **variável aleatória "vender"**, temos:

- A probabilidade de não vender este produto é:
    
    $P(X=0)=q$
    
    $P(X=0)=1-p$
    
    $P(X=0)=1-0,8=0,2$
    
    Ou seja, 20% de chances de não vender.
    
- A probabilidade de vender este produto é:
    
    $P(X=1)=p$
    
    $P(X=1)=0,8$
    
    Ou seja, 80% de chances de vender.
    
- A média, a variância e o desvio padrão da venda são:
    
    $E(X)=p=0,08$
    
    $Var(X)=pq=0,8\times{0,2}=0,16$
    
    $\sigma(X)=\sqrt{pq}=\sqrt{0,16}=0,4$
    

---

[⬆️Índice](https://www.notion.so/Probabilidades-35785fcffca647aeb80c1abd3ab46d27)

## Distribuição Binomial

Um experimento binomial é aquele que consiste em uma sequência de N ensaios idênticos e independentes. Cada tentativa pode resultar em apenas dois resultados possíveis: sucesso e fracasso.

<aside>
💡 Quando a ordem dos eventos não influenciar, utiliza-se a Binominal.

</aside>

**Exemplos:**

- Lançar uma moeda 5 vezes e observar o número de caras.
- 10 peças são escolhidas ao acaso e observamos as falhas.
- 5 cidades são observadas quanto ao acesso à rede de internet.

$$
P(X=k)=\begin{pmatrix}n\\k\end{pmatrix}=\frac{n!}{k!(n-k)!}\times{p^k}\times{q^{n-k}}
$$

$k$ = número de sucessos;

$n$ = número de elementos da amostra

$p$ = probabilidade de sucesso

$q$ = probabilidade de fracasso → $q = 1 - p$

A média, a variância e o desvio padrão de uma distribuição binomial são
dadas por:

- Média (chamada Esperança)
    
    $$
    E(x)=n\times{p}
    $$
    
- Variância
    
    $$
    Var(x)=n\times{p}\times{q}
    $$
    
- Desvio Padrão
    
    $$
    \sigma(X)=\sqrt{n\times{p}\times{q}}
    $$
    

### Exemplo:

Um processo industrial na fabricação de monitores opera com média de 5% de defeituosos. Baseado em amostras de 10 unidades, calcule as probabilidades de uma amostra apresentar:

1. Nenhum monitor com defeito:
    
    $n = 10$
    
    $k=0$
    
    $p=5\% \ \ ou \ \ 0,05$
    
    $q=1-0,05=0,95$
    
    $$
    P(x=0)=\frac{10!}{0!\times{(10-0)!}}\times{0,05^0}\times{0,95^{10}}=0,598
    $$
    
2. Três monitores com defeito:
    
    $n = 10$
    
    $k=3$
    
    $p=5\% \ \ ou \ \ 0,05$
    
    $q=1-0,05=0,95$
    
    $$
    P(x=3)=\frac{10!}{3!\times{(10-3)!}}\times{0,05³}\times{0,97⁷}=0,010
    $$
    
3. Pelo menos 9 monitores com defeito:
    
    $$
    P(x ≥ 9) = P(x = 9) + P(x =10)
    $$
    
4. No máximo 2 monitores com defeito:
    
    $$
    P(x ≤ 2) = P(x = 0) + P(x = 1) + P(x = 2)
    $$
    

A média, variância e desvio padrão:

$$
E(X) = 10\times{0,05}=0,5
$$

$$
Var(X)=10\times{0,05}\times{0,95}=0,475
$$

$$
\sigma(X)=\sqrt{10\times{0,05}\times{0,95}}=0,689
$$

---

## Distribuição de Poisson

A distribuição de Poisson é frequentemente útil para estimar o número de ocorrências sobre um intervalo de tempo ou de espaços específicos. 

<aside>
💡 Utilizado ao ter certeza que em determinado intervalo (tempo, por exemplo) há ocorrência do evento que se deseja estudar.

</aside>

Exemplos:

- Número de chamadas telefônicas durante dez minutos.
- Número de falhas de uma máquina durante um dia de operação.
- Número de acidentes ocorridos numa semana.
- Número de mensagens que chegam a um servidor por segundo.
- Defeitos por m², etc.

$$
P(x=k) =  \frac{e^{-\lambda}\times{\lambda ^k}}{k!}
$$

$\lambda$ = É a taxa de ocorrência do evento em um intervalo.

$k$ = É o número de ocorrências do evento.

$e$ = É uma constante matemática $\simeq{2,71828}$

A média, variância e desvio padrão da distribuição de Poisson são dadas por:

- Média (chamada Esperança):
    
    $$
    E(X)=\lambda
    $$
    
- Variância:
    
    $$
    Var(X)=\lambda
    $$
    
- Desvio Padrão:
    
    $$
    \sigma(X)=\sqrt{\lambda}
    $$
    

### Exemplo:

Um departamento de polícia recebe 5 solicitações por hora em média, relacionadas a crimes cometidos. Qual a probabilidade de receber:

1. Duas solicitações numa hora selecionada aleatoriamente?
    
    $$
    P(X=2)=\frac{2,71828^5\times{5^2}}{2!} = 0,0842\ \ ou \ \ 8,42\%
    $$
    
2. No máximo duas solicitações numa hora selecionada aleatoriamente?
    
    $$
    P (X ≤ 2) =P(x = 0)+ P(x = 1) + P(x = 2)
    $$
    
    $$
    P(x=0)=\frac{2,71828^5\times{5^0}}{0!} = 0,0067\ \text{ou 0,67\%}
    $$
    
    $$
    P(x=1)=\frac{2,71828^5\times{5^1}}{1!} = 0,0337\ \text{ou 3,37\%}
    $$
    
    $$
    P(x=2)=\frac{2,71828^5\times{5^2}}{2!} = 0,0842\ \text{ou 8,42\%}
    $$
    
    $$
    P(X\leq2)=0,0067+0,0337+0,0842 = 0,1246\ \text{ou 12,46\%}
    $$
    

Em um posto de gasolina, sabe-se que, em média, 10 clientes por hora
param para colocar gasolina numa bomba. Pergunta-se:

1. Qual é a probabilidade de 3 clientes pararem qualquer hora para
abastecer?
    
    $$
    P(X)=\frac{2,71828^{10}\times{10^3}}{3!}=0,0076\ \text{ou 0,76\%}
    $$
    
2. Qual é a média, a variância e o desvio padrão para essa distribuição?
    - Valor Médio: $E(X)=10$
    - Variância: $Var(X)=10$
    - Desvio Padrão: $\sigma(X)=\sqrt{10}=3,16$

### Exercícios ao Vivo

[Exercício aula ao Vivo 6](https://www.notion.so/Exerc-cio-aula-ao-Vivo-6-10159d32703e4514a8f9d31497b3d698)

---

# Distribuição e Probabilidades Contínua

As variáveis aleatórias contínuas são aquelas que assumem qualquer valor numérico em um intervalo de números reais. Exemplo: podemos calcular a probabilidade de um indivíduo medir entre 160 cm e 180 cm. 

Para o cálculo da área, usamos o artifício matemático chamado de integral. Assim, definimos dois pontos [a, b], a probabilidade da variável estar entre a e b é dado por:

$$
P(a \leq X\times{b})= \int_a^b f(x)\times{d}\times{x}
$$

A função $f(x)$ é chamada de densidade de probabilidade (f.d.p.) da variável aleatória X. Assim, podemos construir modelos teóricos para variáveis aleatórias contínuas, escolhendo adequadamente as funções densidade de probabilidade. 

## Distribuição Uniforme

Sendo a mais simples de se conceituar, é usada em situações em que a função densidade de probabilidade é constante dentro de um intervalo de valores da variável aleatória X.

![41-distribuicao-uniforme](41-distribuicao-uniforme.png)

41-distribuicao-uniforme

$$
f(x)=\frac{1}{b-a}\\
 se: \ a\leq x\leq b
$$

As fórmulas para valor médio (valor esperado) e para variância são:

$$
E(x)=\frac{a+b}{2}
$$

$$
Var(x)=\frac{(a-b)^2}{12}
$$

---

## Distribuição Normal de Probabilidade

A forma desta distribuição é ilustrada por uma curva em forma de sino. Seu formato é simétrico em relação à média e seus extremos se estendem ao infinito em ambas as direções. 

![42-curva-sino](42-curva-sino.png)

42-curva-sino

O desvio-padrão determina a curva. Curvas mais largas e planas resultam de valores maiores de desvio-padrão, mostrando maior variabilidade dos dados. A área total sob a curva à esquerda e à direita é equivalente a 0,5 de cada lado. 

### Distribuição Normal Padrão

Quando uma variável aleatória tem uma distribuição normal com média zero e desvio padrão 1, tem uma distribuição normal padrão de probabilidade. 

Nenhuma das técnicas de integração padrão pode ser usada para calcular a integral (fórmula usada para calcular a distribuição normal). Assim, quando $\mu = 0$ e $\sigma=1$, essa expressão foi calculada e tabulada para valores determinados de a e b. 

![43-distribuicao-normal-padrao](43-distribuicao-normal-padrao.png)

43-distribuicao-normal-padrao

A partir dessas integrais obtidas numericamente e utilizando a curva normal padronizada, podemos obter as probabilidades por meio de tabelas prontas que mostram a área sob a curva normal correspondente

[Tabela de Distribuição Normal Reduzida](https://docs.google.com/spreadsheets/d/1OUlXX4gdPC6HSuXiyW5ABMLhEEHgW1j4OU0XjnPn770/edit?usp=drivesdk)

Para utilizar a tabela, as variáveis aleatórias x precisam se padronizadas. A fórmula usada para esta conversão é:

$$
z=\frac{x_i-\mu}{\sigma}
$$

Em que:

- $x_i$ = ponto que se deseja converter em z.
- $\mu$ = média da normal original.
- $\sigma$ = desvio padrão da normal original.

<aside>
🚨 1. Quase todos os escores padrão, (99,7% deles), se encontram entre os valores de -3 e +3, graças a regra empírica.
2. Um escore padrão negativo indica que o escore original estava abaixo da média.
3. Um escore padrão positivo indica que o escore original estava acima da média.
4. Um score padrão igual a 0 indica que o escore original era a própria média.
5. Escores que vêm de uma distribuição normal, quando padronizados, têm uma distribuição normal especial com média 0 e desvio padrão 1. Essa distribuição é chamada d*istribuição normal padrão.*

</aside>

### Utilizando os percentis com escore padrão:

- Suponha-se que um estudante tenha feito uma prova de vestibular e obteve pontuação igual a 235.
- Sabendo que as pontuações da prova apresenta uma distribuição normal com média igual a 250 e desvio padrão igual a 15 e que o corte para aprovação são os 60% dos estudantes que conseguiram melhores notas e consequentemente, os 40% que obtiveram as piores notas são reprovados.
- A nota do estudante ficou abaixo da média, mas ainda é o suficiente para que passe no vestibular?

Considerando que 60% dos estudantes que obtiveram as melhores notas passam no vestibular e os 40% restantes não, a nota de corte para passar/reprovar está no 40º Percentil. 

A nota que o estudante em questão tirou está a 1 desvio padrão da média, pois a diferença da pontuação do estudante, menos a média é igual a -15, -15 dividido pelo desvio padrão, sendo 15, é igual a -1.

Seguindo a regra empírica, onde 68% dos valores em uma distribuição normal, se encontram entre 1 desvio padrão da média, sabemos que o resto é (100% - 68% = 32%), ou seja, 32% se encontram fora dessa variação.

Metade do que se encontra fora da variação de mais ou menos 2 desvios padrões é 16%, que é o caso do estudante, assim sendo, ele se encontra no 16º percentil, portanto reprovado