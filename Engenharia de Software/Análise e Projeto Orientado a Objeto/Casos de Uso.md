# Introdução

As etapas de análise são as mais críticas e difíceis na produção de um software, é o momento em que ocorrem as tentativas de delimitar o domínio do problema e entendê-lo; crítica porque uma análise malfeita comprometerá todas as outras fases do software.

Existem diversos modelos de processo de software que se baseiam no modelo em cascata e o evolucionário.

Os requisitos de software são objetivos ou restrições estabelecidos por clientes e usuários do sistema, que definem as diversas propriedades dele. Requisitos funcionais que definem as funções do sistema e os requisitos não funcionais que definem outras categorias de características, os quais o sistema deverá possuir. 

O levantamento desses requisitos é de suma importância e podem utilizar uma narrativa ou representações gráficas como o diagrama de caso de uso, utilizado para representar, de forma panorâmica os requisitos funcionais de um sistema do ponto de vista do usuário. 

---

# Fases da Análise e do Projeto

<aside>
📌 A etapa de análise é considerada a fase mais difícil e crítica da produção de um software.

</aside>

A análise de sistemas é a atividade inicial do processo de desenvolvimento de software, em que se determina e específica o que um sistema deve fazer, assim como as circunstâncias sob as quais ele deve operar, envolvendo, geralmente, esforço colaborativo entre analistas de sistemas e usuários. A análise é realizada com os seguintes objetivos em mente:

- Identificar a necessidade do usuário.
- Executar análise econômica (custos) e técnica (existe tecnologia, treinamento dos usuários, etc).
- Atribuir funções a hardware, software, pessoas, banco de dados e demais elementos do sistema.
- Estabelecer as restrições de prazo e de custo.
- Criar uma definição de sistema que constitua a base para todo o trabalho.

![20 - Ciclo produção software](20-ciclo-producao-software.png)

20 - Ciclo produção software

Independente do método ou processo utilizado para a análise, projeto e implementação, algumas etapas são comuns:

- Identificação da necessidade.
- Estudo de viabilidade.
- Análise.
- Projeto (ferramentas).
- Implementação (codificação)
- Implantação
- Manutenção (adaptativa, corretiva ou evolutiva)

## Identificação da necessidade

Nesta etapa, são definidas as metas globais do sistema, representa algo que o usuário/cliente "precisa" para resolver um problema, suas descrições possuem forte significado para o stakeholder. O foco da identificação da necessidade é o que o sistema irá RESOLVER e não COMO irá fazer. 

- Por que estamos fazendo este trabalho?
- Onde e como o resultado do trabalho será utilizado?
- Quais são os objetivos do negócio?
- O que o cliente deseja realmente resolver?
- O que o cliente realmente precisa?
- O que incomoda o cliente?

## Estudo de viabilidade

Visa determinar se o problema pode ser resolvido considerando cinco aspectos: técnico, legal, operacional, temporal e econômico.

A viabilidade técnica analisa se o projeto pode ser desenvolvido e implementando usando os recursos existentes, se existe recurso humano a disposição. A viabilidade legal analisa se não existem conflitos entre o sistema e os compromissos legais que a empresa tem. Operacional verifica se o sistema conseguirá executar as funções projetadas no ambiente organizacional existente com o pessoal atual, se há necessidade ou não de treinamento para os usuários. O aspecto tempo é o cronograma de desenvolvimento e também o tempo necessário para o retorno do investimento, a viabilidade econômica analisa o custo benefício. 

- Quais informações serão produzidas?
- Quais informações devem ser fornecidas?
- Quais funções e desempenho são exigidos?
- Existe tecnologia para construir o sistema?
- Qual o custo de produção e o tempo necessário para conclusão?
- Qual é o mercado em potencial para o produto?
- Como este produto se compara com os produtos dos concorrentes?

O estudo de viabilidade é um reconhecimento de toda a área da proposta do projeto. Deve apresentar um quadro equilibrado que incorpore todos os aspectos possíveis, isto é:

1. Dados existentes;
2. Escopo, objetivos e premissas;
3. Esboço de estratégia;
4. Análise financeira (fatores externos, quando relevante);
5. Análise financeira (base do projeto);
6. Avaliação do retorno sobre o investimento e o esforço;
7. Avaliação de riscos;
8. Fontes de apoio do projeto;
9. Avaliação tecnológica;
10. Análise política (quando cabível);
11. Avaliação de impacto ambiental (AIA, EIA)
12. Avaliação do impacto sociológico (quando apropriada) e identificação de interassados (stakeholders);
13. Estrutura geral e administração do projeto;
14. Recursos do projeto.

## Ciclo de vida do software

1. Análise
2. Projeto
3. Implementação (produção)
4. Implantação (software finalizado e posto em operação)
5. Manutenção

![21 — Ciclo de produção software](21-ciclo-producao-software.png)

21 — Ciclo de produção software

## Análise

Para uma análise completa de um sistema, o analista deve considerar:

- Entender os objetivos do sistema.
- Entender as exigências do sistema.
- Entender que os objetivos e as exigências são satisfeitos através de cuidadosa análise.
- Entender as áreas-problema do sistema.

As técnicas para o levantamento dessas informações são:

- Estudo dos manuais de procedimentos.
- Análise de formulários.
- Entrevistas.
- Questionários.
- Observação.

## Projeto

É a solução informática dada ao problema. Descreve a estrutura do software que será implementado, contendo os dados e a interface entre os componentes do sistema. O projeto de software é importante para formalizar as regras de negócio do sistema, melhorando a comunicação entre o cliente e o programador.

## Implementação

Estágio em que se cria uma versão executável, utilizando ferramentas de desenvolvimento definidas no projeto. 

## Implantação

Corresponde a fase em que o software é entregue ao cliente.

O projeto é construído com base no estudo de viabilidade técnica, utilizando ferramentas suportadas pelo hardware e entendidas pelo usuário, portanto os riscos da implantação não funcionar são minimizados no projeto. O fator mais preocupante é a adaptação do usuário.

## Manutenção

Processo de modificar o sistema desenvolvido depois que ele é colocado em operação, fase do ciclo de vida do software com maior duração.

Softwares são constantemente modificados, seja em resposta a requisitos novos pedidos pelo cliente, correções de erros ou adaptação para novos ambientes de implantação e mudanças na legislação e regras de negócios. 

---

# Modelos de Processo

A análise e o projeto de sistemas de software devem fornecer para a equipe envolvida uma única compreensão do projeto. A UML é uma linguagem. Um **método** é composto por processos e um modelo de linguagem. Os **processos** são os passos que devem ser seguidos para construir o projeto. O **modelo de linguagem** é a notação que o método usa para descrever o projeto, enquanto um **modelo de processo de software** define a sequência de atividades do processo serão realizadas.

## Modelo em cascata

Considera as atividades de especificação, desenvolvimento, validação e evolução como fases separadas do processo.

A primeira fase, análise e definição de requisitos, visa estabelecer, por meio da consulta aos usuários, as funções, restrições e os objetivos do sistema.

A segunda fase é o projeto, em que os requisitos em sistemas de hardware ou de software são agrupados, estabelecendo uma arquitetura do sistema geral.

A terceira fase é a implementação e o teste de unidade, o projeto de software é compreendido como um conjunto de programas, o teste verifica se cada conjunto atende à sua especificação.

A quarta fase é a integração e o teste de sistema, as unidades de programa são integrados e testados como um sistema completo, visando garantir que os requisitos foram atendidos.

A quinta fase é a operação e manutenção é onde o sistema é instalado e colocado em operação. A manutenção envolve corrigir erros que não foram descobertos nos estágios anteriores ou aumentar as funções desse sistema a medida que novos requisitos são descobertos.

Alguns pontos negativos no modelo em cascata:

- Demora na entrega do produto;
- Acúmulo de riscos;
- Inflexível a, mudanças nos requisitos;

Neste modelo de processo pressupões-se que o domínio do problema foi inteiramente compreendido, indicado quando conhecemos por inteiro a regra de negócio do software e os requisitos são estáveis. A metodologia é extremamente amparada em documentação, respeitando cada etapa dos processos, só inciando a próxima depois que totalmente finalizada a etapa anterior.

![22 — Modelo Cascata](22-modelo-cascata.png)

22 — Modelo Cascata

## Modelo evolucionário

Tem como base a ideia de desenvolver uma implementação inicial, expor o resultado ao comentário do usuário e fazer seu aprimoramento através de muitas versões, até que um sistema adequado seja desenvolvido. 

Em vez de ter as atividades de especificação, desenvolvimento, e validação em separado, todo esse trabalho é realizado concorrentemente, com rápido feedback por meio dessas atividades. Além disso, os modelos evolucionários tendem a diminuir a quantidade de artefatos de documentação relacionados ao projeto, devido ao dinamismo com que os requisitos podem mudar, conforme são postos a prova ou as regras de negócio mudam. Portanto, é imprescindível que os stakeholders do projeto sejam muito bem gerenciados e acompanhem de perto a produção do software. 

Produzir sistemas que atendam às necessidades imediatas do usuário, muitas vezes, pode ser mais eficaz que o modelo em cascata. Porém, podem ocasionar problemas como:

- Inviabilidade de produzir documentos que reflitam cada versão do sistema.
- Os sistemas, frequentemente, são mal estruturados. A mudança constante tende a corromper a estrutura do software, incorporar modificações torna-se cada vez mais difícil e oneroso.

![23 — Modelo Evolucionário](23-modelo-evolucionario.jpg)

23 — Modelo Evolucionário

## Linguagem de modelagem — UML

Corresponde ao ponto principal da comunicação. É por meio da linguagem de modelagem que, as partes envolvidas no projeto, se entendem.

A UML define uma notação e um meta-modelo. Todos os elementos de representação gráfica são notação.

![24 — UML](24-uml.png)

24 — UML

O modelo **RUP** (*Rational Unified Process*), desenvolvido pela IBM com base na UML, demonstra a interação entre as etapas do ciclo de vida de um software e qual a concentração das atividades em cada fase.

![25 — RUP (Rational Unified Process) by IBM](25-rup.png)

25 — RUP (Rational Unified Process) by IBM

---

# Requisitos de Software

Também chamada Engenharia de Requisitos, visa compreender o sistema, ou seja, preocupa-se com "O que fazer" e não o "Como fazer". As principais atividades da engenharia de requisitos são:

- Especificar o problema (elicitar).
- Compreender o problema (analisar).
- Definir uma proposta (modelo válido).
- Atualizar requisitos (gerenciar).

![26 — Requisitos de Software](26-requisitos-software.png)

26 — Requisitos de Software

Na primeira atividades, devemos obter o máximo de informações para o conhecimento do objetivo em questão no domínio do problema.

## Domínio

São os limites do software, podem ser determinados por meio do estabelecimento dos objetivos pretendidos. Centra-se na finalidade e limita o problema. 

![27 — Domínio](27-dominio.png)

27 — Domínio

## Requisitos

São os objetivos e as restrições estabelecidas pelo usuário do sistema. Em um primeiro momento, é interessante definir os requisitos sem se preocupar em detalhá-los, isto permite ter uma visão global do domínio de maneira mais rápida.

<aside>
🗣 Característica, atributo, habilidade ou qualidade que um sistema deve prover para ser útil a seus usuários.

</aside>

Para a definição de requisitos, produzimos um documento contendo declarações dos requisitos e restrições do sistema. Especificação, produzimos um documento estruturado contendo requisitos e restrições descritos detalhadamente.

Os requisitos precisam atender alguns critérios que caracterizam um bom documento de requisitos são eles:

- **Completude:** o requisito está escrito no formato estabelecido, se representa uma necessidade, se está escrito na voz ativa e no afirmativo, as palavras-chave estão associadas ao seu respectivo significado no glossário, não existem outros requisitos que descrevem a mesma coisa ou contradiz outro.
- **Ambiguidade:** avaliar se o requisito possuí uma e somente uma interpretação. Algumas palavras suspeitas que podem trazer ambiguidade para o requisito como, alcançável, adequado, aproximadamente, completo, eficiente, minimizar, maximizar, flexível, modular, nominal, normalmente, etc, otimizado, tipicamente, usualmente, geralmente, frequentemente, fácil, simples, muitos, vários, alguns, poucos, tanto quanto possível, pequeno, grande, baixo, alto, versátil, amigável, escalável, e/ou.
- **Testabilidade:** verifique se o requisito está escrito de modo que seja possível determinar se a funcionalidade estará ou não presente no sistema e se existem cenários ou exemplos que podem ser anexados ao texto do requisito.

Os requisitos podem ser divididos em:

- Requisitos funcionais (RF).
- Requisitos não funcionais (RNF).

Os **requisitos funcionais** definem as funções do sistema, o que espera que o sistema faça e é intimamente ligado a continuidade do negócio, a fluidez. 

- Monitorar sensores de temperatura.
- Cancelar o débito na conta-corrente caso a operação não seja completada.
- Avisar quando o estoque chegar ao limite mínimo.

Os **requisitos não funcionais** estão relacionados às tecnologias utilizadas, **à usabilidade, ao desempenho, à segurança, confiabilidade, manutenibilidade e disponibilidade** que o sistema deverá possuir:

- O sistema deverá apresentar interface gráfica (padrão Windows).
- Facilidade de uso.
- Possibilidade de ajuda no contexto.

O **documento preliminar de requisitos** deve conter algumas características de qualidade:

1. **Precisam ser corretas:** cada declaração de requisito deve expressar, exatamente, a funcionalidade almejada, apenas o usuário pode determinar se a declaração está correta através de inspeções.
2. **Precisam ser possíveis:** o analista deve ser hábil em implementar cada requisito declarado, observando os recursos e as limitações do sistema e ambiente, os técnicos podem auxiliar determinar as possibilidades dentro do que há disponível de tecnologia.
3. **Precisam ser necessários para o projeto:** cada declaração de requisito deve documentar apenas as necessidades do cliente ou qualquer outra necessidade que exija atender a um requisito externo, ou a uma interface externa ou, ainda, um padrão.
4. **É necessário definir prioridades:** clientes devem ter sua parte de responsabilidade do estabelecimento de prioridades.
5. **Não podem ser ambíguas:** cada declaração deve ser explicitada de maneira que permita somente uma interpretação, cada requisito deve ser escrito na linguagem do cliente de forma sucinta, simples, direta, sem utilizar jargões técnicos.
6. **Precisam ser verificáveis:** através de testes ou outras abordagens de verificação, como inspeções ou demonstrações, de modo a certificar-se que cada requisito será implementado apropriadamente. 

Este documento deverá sofrer um processo de análise, que envolve uma série de atividades como: validação e verificação, análise de viabilidade, resolução de conflitos e definição de prioridade.

Os casos de uso permitem criar um cenário do domínio, representam funcionalidades completas para o usuário. O diagrama de casos de uso é um artefato de comunicação entre cliente, usuários e desenvolvedores, também serve como um contrato entre a equipe desenvolvedora e o cliente.

O diagrama de casos de uso é apenas um panorama visual das funcionalidades do sistema, é necessária uma descrição textual para detalhar os casos. A fase de análise de requisitos é composta por:

- Lista de requisitos funcionais e não funcionais.
- Diagrama de casos de uso e definições textuais dos casos.

---

# Diagrama de Casos de Uso

<aside>
📌 O modelo de casos de uso representa, de forma panorâmica, os requisitos funcionais de um sistema do ponto de vista do usuário.

</aside>

O modelo de casos de uso é o principal resultado da fase de análise de requisitos, são utilizados para representar de forma panorâmica, os requisitos funcionais de um sistema do ponto de vista do usuário. 

O modelo de caso de uso é um diagrama utilizado na análise de requisitos com objetivos claros:

- Compreender o problema (elicitar).
- Delimitar o sistema (domínio).
- Definir as funcionalidades oferecidas ao usuário (sem se preocupar com a implementação, ou seja, como será feito apenas o que DEVE ser feito).

Os elementos básicos deste diagrama são:

- Atores.
- Casos de uso.
- Relações entre atores e casos de uso.

## Atores

Através do homem palito, representam um ator no sistema que pode ser uma pessoa, outro sistema ou uma entidade externa ao sistema, um dispositivo, por exemplo (sensor, câmera, placa, banco de dados). 

Para identificar os atores de um sistema:

- Examine o problema procurando por pessoas ou sistemas do entorno.
- Faça as seguintes perguntas:
    - Quais são as pessoas ou departamentos interessados em determinado requisito funcional?
    - Quem suprirá o sistema com informações e quem receberá informações dele?
    - Quais os recursos externos utilizados pelo sistema?
    - Uma pessoa desempenha diferentes papéis?
    - O sistema interage com outros sistemas existentes?

![13 — Ator](13-ator.png)

13 — Ator

<aside>
🧠 O conjunto de casos de uso representa todas as possíveis interações que serão descritas nos requisitos de sistema.

</aside>

## Casos de uso

A coleção de casos de uso representa, do ponto de vista do usuário, todos os modos de execução do sistema. Todos os casos de uso são acionados por um ator. Um caso de uso é uma sequência de ações que produz um resultado significativo para um ator, e, assim, são necessárias as seguintes definições:

- Tarefas de cada ator,
- Quais informações o ator obtém do sistema.
- Quem fornece as informações.
- Quem captura as informações.
- Se algum ator precisa ser informado sobre eventos produzidos pelo sistema.
- Se existem eventos externos que devem ser notificados ao sistema.

A elipse é a notação para os casos de uso. Um caso de uso representa uma atividade que o ator realiza. 

![14 — Use Case](14-use-case.png)

14 — Use Case

O diagrama, por si só, não é suficiente. Os casos de uso devem vir acompanhados de uma descrição em que, normalmente, relacionamos os seguintes itens:

- Nome
- Descrição
- Requisitos funcionais providos pelo caso de uso
- Restrições, tais como pré e pós-condições.
- Pré-condições: defino o que deve ser verdadeiro para que o caso de uso seja iniciado.
- Pós-condições: o que se torna verdadeiro pela execução do caso de uso.
- Variantes: condições que são verdadeiras durante a execução do caso de uso.
- Fluxos de eventos: descrição de interações entre atores e sistema que ocorrem durante a execução do caso de uso.
- Outras informações: data, autor, etc.

![29 — Descrição Caso de Uso](28-descricao-caso-uso.png)

29 — Descrição Caso de Uso

## Relações de dependência

A linha sólida representa uma associação entre o ator e o caso de uso. 

Representadas por uma seta tracejada, parte do caso de uso que depende de outro em algum momento. 

![15 — Dependência](15-dependencia.png)

15 — Dependência

Se um caso de uso inclui o comportamento de outro, então dizemos que um usa o outro. A linha tracejada com uma seta também pode representar uma inclusão de outro caso de uso. Nesse caso o include força a execução de determinado caso de uso, ou seja, é necessário que para que um caso de uso seja executado, NECESSARIAMENTE outro caso de uso, onde a seta aponta, deve ser executado. 

![16 — Inclusão](16-inclusao.png)

16 — Inclusão

As extensões adicionam um comportamento a um caso de uso que descreve uma variação do comportamento normal. Nesta situação, o caso de uso base pode ser executado mesmo sem a extensão.

![17 — Extensão](17-extensao.png)

17 — Extensão

O diagrama de casos de uso é apenas um panorama visual das funcionalidades do sistema; é necessária uma descrição textual para detalhar os casos de uso.

![29 — Generalização](29-relacao-especialidade.png)

29 — Generalização

O exemplo acima demonstra uma generalização/especialização, o que define um caso de uso global e um caso de uso especialista, que herda características do caso de uso pai, porém possui características próprias. A representação é feita por uma seta vazada.   

A descrição textual para o caso de uso Resolver Expressões Aritméticas:

![18 — Descrição Textual para caso de uso](18-descricao-textual.png)

18 — Descrição Textual para caso de uso

![19 — Descrição Textual para caso de uso (contin.)](19-descricao-textual.png)

19 — Descrição Textual para caso de uso (contin.)

Essa descrição textual detalha o caso de uso, mostrando prés e pós-condições para execução, bem como o fluxo básico de execução.

Um fluxo descreve como o sistema e os atores colaboram para produzir algo de valor aos atores e o que pode impedir a sua obtenção, descreve um caminho entre muitos possíveis, visto que um caso de uso pode ser executado de vários modos. Existem os fluxos básicos, que demonstram o fluxo normal de eventos, e os alternativos, que dizem o que fazer, caso não seja possível seguir o fluxo básico.

Um fluxo alternativo apresenta um comportamento opcional de um caso de uso. São utilizados para representar tratamento de exceções ou comportamento alternativo complexo que tornaria o fluxo básico muito longo e de difícil compreensão.

---

# Conclusão

O papel da análise é obter, a partir dos usuários, em um processo gradual e cumulativo, o maior conhecimento possível acerca do domínio do problema e do respectivo ambiente, a identificação da necessidade, o estudo de viabilidade, a análise, o projeto, a implementação, a implantação e a manutenção.

Um método precisa de um modelo de linguagem que é a notação que o método usa para descrever o projeto, e um processo, que descreve os passos que devem ser seguidos para construí-lo.

Engenharia de requisitos específica o problema, bem como, compreende e define uma proposta através de um modelo válido.

O modelo de caso de uso é um diagrama utilizado na análise de requisitos, visando compreender o problema, delimitar o sistema e definir as funcionalidades oferecidas ao usuário, sem nos preocuparmos com a implementação. 

---

# Como fazer um plano de testes baseado em casos de uso.

Os casos de uso como requisitos que identificam o valor que o cliente espera obter da funcionalidade e representam a forma como o sistema será utilizado, permitem identificar todos os caminhos que o usuário pode percorrer para conseguir o que deseja e se podem ocorrer problemas, mostram ao cliente o que esperar do software; ao desenvolvedor, o que codificar; ao testador ou certificados, o que validar para garantir a qualidade dos entregáveis.

Os casos de uso ajudam na certificação e validação dos requisitos implementados, simplificando e sistematizando o processo de teste o software, permitindo ganho de produtividade e ajudando na garantia de que todo o escopo será abrangido pelo teste.

## Como testar a partir do caso de uso

- Selecione o caso de uso que será testado, identifique o fluxo principal e os fluxos alternativos e desenhe um diagrama de atividades, para visualizar, mais facilmente, todos os cenários que o usuário pode utilizar.
- Escrever um caso de teste para cada cenário, detalhando todos os passos do cenário. O testador poderá executar as ações do ator e validar se a resposta do sistema corresponde com o que foi especificado.
- Para iniciar os testes, será necessária a criação de uma base de dados de certificação e identificar os dados de entrada que serão utilizados no teste.
- Tabular o resultado dos testes, como quantidade de acertos, defeitos e correções, e armazenar esta informação, servirá para avaliar a qualidade de cada desenvolvedor da equipe.

---