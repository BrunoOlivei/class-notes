# Introdução

Iremos conhecer os processos e atividades responsáveis por garantir a especificação de um bom requisito.

A engenharia de requisitos tem o objetivo de fornecer a todos os envolvidos no projeto de desenvolvimento de software um artefato escrito que promova o entendimento do que se deseja produzir. Para ter certeza de que esse artefato reproduz, de fato, o produto final desejado, ele deve ser revisado e validado com os stakeholders.

A literatura dispõe um conjunto de atividades que nos auxiliam na construção do documento que será o ponto-chave, o produto final.

O primeiro passo é o levantamento de requisitos, deve ter características que o torne conciso, claro, completo em sua unidade. Para isso ocorrer, várias técnicas e elicitação podem ser utilizadas. 

É importante analisar o que foi especificado e, então, corrigir, caso não se tenha escrito exatamente o que era esperado. Esse processo da engenharia de requisitos é denominado análise do requisito. Na sequência, vem a etapa da negociação de requisitos com os stakeholders.

Os processos de levantamento, análise e negociação devem andar juntos e permanecer durante todo o ciclo de vida do projeto, o que irá dar garantias da elaboração de um bom Documento de Requisitos.

---

# Processos da Engenharia de Requisitos

Processo da engenharia de requisitos podem variar muito em função das características do projeto e, até mesmo, das organizações.

Independente do nome dado a cada fase, é extremamente recomendável que o processo contemple, no mínimo, dois grupos de atividades:

- **Especificação de requisitos:** que representa todas as atividades realizadas para **identificar**, **analisar**, **especificar** e **definir** as necessidades que o sistema deverá prover para solução do problema levantado.
- **Gestão de requisitos:** atividades responsáveis pela **documentação**, **versionamento**, **controle de mudanças** e **qualidade** dos requisitos levantados na fase de especificação de requisitos.

Com base na mescla dos principais autores sobre engenharia de requisitos e as práticas no mercado, temos os seguintes processos:

1. Levantamento e Análise;
2. Negociação;
3. Documentação;
4. Validação;
5. Especificação;
6. Gerenciamento de requisitos.

![11 — Processo da Engenharia de Requisitos](11-processo-engenharia-requisitos.png)

11 — Processo da Engenharia de Requisitos

---

# Levantamento e Análise de Requisitos

Esta etapa inicia o processo de engenharia de requisitos. Nesse ponto, já temos identificados os *stakeholders*, considerando seu grau de interesse, poder e influência, aqueles que conhecem a regra de negócio e sejam capazes de auxiliar nas atividades de levantamento de requisitos. Essa fase também é conhecida como **elicitação de requisitos**.

<aside>
🗣 Processo de transformar ideias na mente dos stakeholders em um documento que formaliza os requisitos de software.

</aside>

A definição do escopo geral deve ser feita em uma fase anterior à de Levantamento e Análise, intitulada Estudo de Viabilidade, nessa fase, o engenheiro de requisitos reúne-se com os clientes e usuários — patrocinadores e usuários finais do sistema — para obter a noção geral sobre as funcionalidades do sistema a ser desenvolvido ou mantido e, a partir dessa noção, define-se o escopo geral e se existe viabilidade para o desenvolvimento do software.

<aside>
📌 O levantamento de requisito é o ir a campo e compreender o que o cliente deseja e como será desenhada a proposta para atender às expectativas dele.

</aside>

Processo genérico de levantamento e análise:

1. **Compreensão do domínio:** os engenheiros de requisitos devem desenvolver sua compreensão do domínio (ambiente) da aplicação para que a transcrição seja eficiente e clara para os demais profissionais envolvidos no processo.
2. **Coleta de requisitos:** é o processo de interagir com os *stakeholders* do sistema para descobrir seus requisitos.
3. **Classificação:** organização dos requisitos em grupos coerentes, por exemplo, pela complexidade, funcionais ou não funcionais, etc.
4. **Resolução de conflitos:** os requisitos são apresentados a partir do ponto de vista de cada *stakeholder* diferente, podendo conflitar uns com os outros, nessa fase, o engenheiro de requisitos irá categorizar todas as informações para, posteriormente decidir pelo conjunto de requisitos mais consistente.
5. **Definição de prioridades:** com os *stakeholder* tomadores de decisão, são definidos os requisitos mais importantes.
6. **Verificação de requisitos:** os requisitos são verificados para descobrir se estão completos e consistentes e se estão em concordância com o que os *stakeholders* desejam do sistema.

A obtenção de requisitos não é um processo formal, o engenheiro deve contar com técnicas de entrevista, questionário, mapeamento, entendimento do processo-alvo, etc.

---

## Técnicas para coleta de requisitos

O objetivo é reunir-se com os *stakeholders* e conquistá-los, trazê-los para o projeto e fazê-los entender serem coautores, e não meros participantes ou telespectadores. Existem diversas técnicas que visam auxiliar a comunicação e a elicitação dos requisitos como: entrevistas, cenários, estórias de usuários, *shadowing*, prototipação, etc. As características do projeto e do cliente determinarão a técnica mais adequada para coleta de requisitos. 

![17 — Modelo espiral da interação entre levantamento e análise de requisito.](17-ciclo-interacao-engenharia-requisito.png)

17 — Modelo espiral da interação entre levantamento e análise de requisito.

Alguns procedimentos a serem estabelecidos durante o levantamento de requisitos que independem da técnica adotada para a coleta:

**Antes:**

1. Identificar as áreas envolvidas; 
2. Explicar a finalidade;
3. Obter aprovação das gerências apropriadas.
4. Obter nome e função dos *stakeholders* chaves que participarão da coleta. 
5. Confirmar e solicitar concordância quanto a papéis, responsabilidades e disponibilidades previstas.

**Durante:**

1. Familiarizar-se com o local de trabalho que está sendo estudado.
2. Coletar amostras de documentos e procedimentos escritos.
3. Acumular informações estatísticas a respeito das tarefas: frequência com que ocorrem, estimativas de volume, tempo de duração para cada tarefa e assim por diante.
4. Ser objetivo e não comentar as formas de trabalho de maneira não construtiva.
5. Além das operações normais de negócio, identificar, também, as exceções.
6. Levantamento completado, agradecer às pessoas pelo apoio.

**Após:**

1. Documentar os requisitos e consolidar os resultados.
2. Caso seja necessário, contatar os próprios informantes para esclarecer dúvidas.
3. Rever os resultados consolidados com os próprios informantes e/ou superiores.
4. Atribuir uma prioridade para cada requisito identificado.

Existem inúmeras técnicas para interagir com os *stakeholders* de modo a coletar dados e informações. A metodologia a ser usada deve ser considerada o projeto. 

---

### Entrevista

As entrevistas acontecem em reuniões para sanar dúvidas, levantar problema e buscar soluções. Normalmente é utilizada quando a equipe de desenvolvimento não conhece os problemas do cliente ou da organização.

Deve se fazer uma preparação prévia para realização da entrevista:

**Antes:**

- Algumas questões devem ser consideradas:
    - O que se deseja saber?
    - O que se aceita saber? (Mínimo necessário).
    - Quem será o entrevistado?
    - Quais perguntas serão feitas?
    - Qual é a sequência de execução das perguntas?
    - Quando finalizar?
- Divulgue com antecedência a agenda e pauta da entrevista com todos os envolvidos.
- Agendar a entrevista/reunião em um horário conveniente para o entrevistado.

**Durante a entrevista:**

- Ter em mente que pode haver resistência às mudanças e que seu trabalho pode ser considerado uma ameaça pelo entrevistado.
- Ouvir e responder de forma cordial às perguntas do entrevistado.
- Tomar notas.
- Não ser tendencioso.
- Determinar quem ficará responsável pelas atividades a serem realizadas e o respectivo prazo de conclusão.

Quanto a categoria de pergunta, elas podem ser abertas (subjetivas) ou fechadas (objetivas).

A estrutura da entrevista pode ser organizada das seguintes formas:

- **Estrutura Pirâmide:** começa com questões detalhadas (objetivas) e termina com questões mais gerais (subjetivas).
- **Estrutura Funil:** começa com questões mais gerais (subjetivas) e termina com questões mais detalhadas (objetivas).
- **Estrutura Diamante:** agrega a estrutura funil mais a pirâmide. Começa com questões específicas, avança para questões mais gerais e finaliza com as específicas novamente.
- **Não-Estruturada:** não há uma sequência de como as questões serão abordadas, porém, as questões são definidas com antecedência.

---

### Brainstorming

O *brainstorming* é uma dinâmica de grupo usada para desenvolver novas ideias ou projetos, para juntar informação e para estimular o pensamento criativo. Propõe que um grupo de pessoas se reúna para expor seus pensamentos e ideias sobre um determinado problema onde o foco é na quantidade de ideias geradas.

Os procedimentos para implantação do *brainstorming* é composto pelas seguintes etapas:

- Definição do tema: defina o problema e saiba qual resultado almeja-se.
- Escolha da equipe: representantes de várias áreas diferentes.
- Defina o tipo de brainstorming
- Geração das ideias
- Seleção das ideias

![12 — Etapas brainstorming](12-etapas-brainstorming.png)

12 — Etapas brainstorming

Algumas regras básicas para uma sessão de brainstorming:

- Garantir que todos compreendam o objetivo do brainstorming antes de iniciá-lo.
- Decidir o método de brainstorming
- Grupos máximos de 12 participantes
- Garantir igualdade de participação
- É proibido debates e críticas às ideias apresentadas, a discussão deve começar depois que o brainstorming acabar.
- Nenhuma ideia deve ser desprezada.
- Modificação ou combinação de ideias.
- Deve-se garantir igualdade de oportunidade. Todos os participantes devem ter chance de expor suas ideias.

Existem várias formas de promover o brainstorming, pode ser estruturado ou não estruturado, utilizar anotações anônimas para divulgação de ideias. No brainstorming estruturado, cada membro deve dar uma ideia sobre o tema escolhido a cada rodada, já no não estruturado, qualquer participante lança ideias à medida que vão surgindo.

![22 — Double Diamonds](22-brainstormin-double-dimonds.png)

22 — Double Diamonds

---

### Técnica de Grupo Nominal (TGN)

A técnica de grupo nominal adiciona ao processo de brainstorming uma etapa de votação para ordenar as melhores ideias e priorizá-las.

As etapas para realização da TGN:

- Gere ideias: cada participante escreve suas ideias em um papel.
- Recolha o material e registre cada ideia gerada de forma pública.
- Reveja e discuta as ideias.
- Priorize as ideias através da votação.

---

### Técnica Delphi

<aside>
📌 Técnica coletiva de definição da lista de requisitos através de interações.

</aside>

O método consiste em um inquérito efetuado a especialistas e realizado em dois ou mais ciclos. Em cada ciclo os participantes têm acesso aos resultados do ciclo anterior, suas respostas podem ser mantidas ou alteradas para incorporar o conhecimento e as opiniões expressas pelos demais.

É uma técnica não interativa e utilizada como meio de alcançar um consenso quando há dificuldade em reunir os participantes.

Utilizando o método Delphi para levantamento dos requisitos, podemos organizar os processos da seguinte forma:

1. Designa-se um facilitador e escolhem-se os participantes. 
2. Conforme o problema, um questionário é elaborado e distribuído aos participantes. Apenas o facilitador tem acesso sobre os participantes e suas respostas.
3. O facilitador distribui as informações sobre o projeto e solicita aos participantes que respondam ao questionário e gerem uma lista de requisitos individual e anonimamente.
4. O facilitador consolida as diversas listas em uma única e redistribui para os participantes revisarem/complementarem. 
5. A nova lista é devolvida ao facilitador que, novamente a consolida.

Esse processo pode se repetir quantas vezes forem necessárias.

![13 — Processo método Delphi](13-metodo-delphi.png)

13 — Processo método Delphi

---

### Oficinas

As oficinas reúnem partes interessadas multifuncionais para definir os requisitos do produto a ser desenvolvido ou melhorado. Visam acionar o trabalho em equipe. Deve existir sempre um facilitador para conduzir a equipe e promover a discussão entre os vários stakeholders. As tomadas de decisão são baseadas em processos bem definidos e com objetivo de obter um processo de negociação, mediado pelo facilitador. Algumas abordagens podem ser usadas:

- **QFD — quality function deployment**: Método desdobramento da função de qualidade visa permitir que a equipe de desenvolvimento do produto incorpore as reais necessidades do cliente. Em geral, o QFD obedece a quatro fases: planejamento do produto, desenvolvimento dos componentes, planejamento do processo e planejamento da produção.
    
    ![14 — Matriz QFD](14-matriz-qfd.png)
    
    14 — Matriz QFD
    
- **JAD — joint application design**. É a metodologia para definição de requisitos criada pela IBM do Canadá em 1977. Busca promover que todos os participantes compartilhem uma mesma visão do produto, todos os participantes são coautores da solução. A técnica se divide em duas etapas: dados sobre o projeto e resultados revisados. Cada etapa possui três fases:
    - Adaptação: preparar o material que será utilizado durante as reuniões, alocar e convidar os participantes selecionados para as reuniões, adaptar o processo JAD ao produto que será desenvolvido.
    - Sessão: são as reuniões onde os requisitos são desenvolvidos e documentados.
    - Finalização: converter os requisitos extraídos em um documento de especificação de requisitos.
    
    Os quatro princípios do método JAD são:
    
    1. Dinâmica de grupo
    2. Recursos visuais — usar técnicas visuais que facilitam a comunicação e o entendimento.
    3. Processo organizado e racional — o JAD emprega análise top-down com atividades bem definidas.
    4. Documentação padrão — cada sessão JAD possui um documento de saída padrão que tem como objetivo registrar formalmente os resultados do processo para que todos os participantes entendam as decisões tomadas.
    
    ![15 — Visão geral do JAD](15-jad.png)
    
    15 — Visão geral do JAD
    
- **História do usuário (user stories):** são descrições textuais de uma funcionalidade requerida escrita do ponto de vista do usuário. Deriva da metodologia ágil que focam mais na comunicação do que na documentação. O foco do user stories é a discussão em torno dos itens. São descrições curtas de uma funcionalidade de um sistema. Os requisitos tratados como histórias devem ser pensados sempre ao nível de negócio. O cliente deve focar nos objetivos do negócio. "Por que você quer que seja realizada essa história?" — deve ser a pergunta da equipe ao tentar determinar o objetivo da história. É recomendado que cada história seja composta, no mínimo, por um ator, uma ação e uma funcionalidade.
    - Ator: é o proprietário da história de usuário, interessado naquela funcionalidade.
    - Ação: representa o que o ator quer fazer.
    - Funcionalidade: é o resultado esperado após a execução da ação.
    
    ![16 — User Story](16-user-stories.png)
    
    16 — User Story
    

---

### Questionários

O uso de questionário é indicado quando há diversos grupos de usuários que podem estar em diferentes locais.

Na fase de preparação do questionário, deve ser indicado o tipo de informação que se deseja obter. O questionário deve ser acompanhado por uma carta explicativa, redigida por um alto executivo, para enfatizar a importância dessa pesquisa para a organização.

A distribuição deve ocorrer com instruções detalhadas sobre como preenchê-lo e o prazo para devolução do questionário. Ao analisar as respostas é feita uma consolidação das informações documentando as principais descobertas e enviando uma cópia com essas informações para o participante.

Alguns procedimentos que podem garantir uma aplicação eficiente do questionário:

**Antes:**

- Definir objetivos do questionário.
- Decidir o que é preciso saber para atingir os objetivos.
- Expor os objetivos e a importância da contribuição.
- Desenvolver perguntas representativas e objetivas, evitar as discursivas.
- Definir método de tabulação para respostas.
- Validar o questionário em piloto com usuário de fácil acesso.

**Durante:**

- Distribuir o questionário com prazo suficiente.
- Estar disponível para dirimir eventuais dúvidas.
- Monitorar o recebimento do questionário.

**Após:**

- Tabular os dados.
- Analisar os resultados da tabulação.
- Remeter os dados tabulados para cada participante que respondeu ao questionário.

---

### Pesquisas

Pesquisas em documentos organizacionais podem ser uma maneira de conseguir identificar os requisitos necessários. **Exemplos** de documentos incluem plano de negócio, registro de marketing, acordos, requisições de propostas, fluxo de negócio, modelos lógicos de dados, repositório de regras de negócio, documentação, processos de negócio, casos de uso, registro de questões públicas, políticas, procedimentos, leis, códigos, etc.

---

### Etnografia

É uma técnica de observação usada para compreender os requisitos sociais e organizacionais. O engenheiro de requisitos se insere no ambiente de trabalho onde o sistema será usado, observando o trabalho do dia a dia e anotando as tarefas nas quais os participantes estão envolvidos. Essa técnica muitas vezes possibilita encontrar requisitos que não seriam observáveis usando técnicas convencionais.

Também conhecida como Shadowing ou Operação Sombra. Esse procedimento, as pessoas não explicam seu trabalho e fatores sociais e organizacionais de importância podem ser observados. 

---

## Próximos passos

Uma vez levantado os requisitos, passamos para a atividade de análise. Nessa etapa, os requisitos levantados são usados para a modelagem do sistema. Na atividade de análise, os requisitos podem ser detalhados de maneira mais técnica, utilizando diversos tipos de modelos que utilizam representação gráfica.

A modelagem, nessa fase, é dita conceitual, pois se preocupa com o domínio do problema. Esse é o momento onde a equipe de desenvolvimento irá interpretar as necessidades do cliente e desenhar o sistema.

Todas as atividades do processo, na prática, ocorrem em paralelo. Durante o levantamento uma análise e uma especificação já estarão sendo executadas de maneira indireta e alguns problemas são identificados e tratados.

O levantamento é o ato de identificar as necessidades do usuário. A análise trata da constante observação e dos elementos do ambiente onde o software será implantado, checando todas as atividades que serão envolvidas no sistema: quem faz, por que faz, e se existem outras formas de ser feito, considerando os dados e informações gerados por essas atividades.

A especificação é a descrição sistemática e abstrata do que o sistema deve fazer a partir dos requisitos levantados. Ela apresenta a solução de como os problemas levantados na análise devem ser resolvidos pelo software em desenvolvimento, fechando o primeiro ciclo da engenharia de requisitos com a produção do Documento de Requisitos e da Matriz de Rastreabilidade de Requisito. Naturalmente, os requisitos passarão por uma negociação e uma prévia validação tanto dos stakeholders do lado do cliente quanto da equipe de desenvolvimento.

---

# Negociação

Com a lista geral de requisitos começa a fase de negociação e priorização dos requisitos junto aos *stakeholders* do lado do cliente.

É muito comum que clientes e usuários peçam mais do que pode ser conseguido, e também diferentes clientes ou usuários proponham requisitos conflitantes. Restrições de prazo, custos e recursos vêm de encontro aos requisitos.

Alguns pontos devem ser considerados e discutidos, para garantir que o produto final atinja seu objetivo, as restrições de prazo, custos e recursos. Nesse ponto a equipe de desenvolvimento deve deixar as limitações de projeto claras e iniciar um processo de negociação, com o intuito de acordar entre as partes, quanto aos requisitos que serão considerados prioritários e quais participarão do escopo do projeto.

O que se sugere é que os riscos associados a cada requisito sejam identificados e analisados para, então, elaborar estimativas de esforço de desenvolvimento, para avaliar o impacto de cada requisito no custo do projeto e no prazo de entrega, podendo requisitos serem eliminados, combinados ou modificados para se alcançar o consenso entre cliente e equipe de desenvolvimento.

Existem várias técnicas para priorização dos requisitos:

- **Atribuição numérica:** propõe uma escala de notas para cada requisito.
- **Árvores de Busca Binária (BSTs):** algoritmo comumente usado em busca de informações e pode ser facilmente adaptado para priorizar uma abundância de requisitos.
- **Analytic Herarchy Process (AHP):** é uma técnica de tomada de decisões em situações de múltiplos objetivos. Provê um índice de consistência utilizado para verificar a fidelidade dos resultados. Calcula conforme o número de requisitos e com os valores atribuídos em uma matriz. É uma técnica complexa e de difícil rastreabilidade dos resultados.
- **Abordagem Custo-Valor (Cost-Value Approach):** prioriza os requisitos de acordo com seus custos e valores relativos. Une a precisão da AHP com resultados mais transparentes o que a torna muito custosa conforme o número de requisitos aumenta.
- **Value-Oriented Priorization (VOP):** avalia e ordena requisitos conforme o impacto que eles terão em valores de negócios específicos da organização, a partir daí, escolhem-se quais requisitos serão mais benéficos para toda a organização. Para a priorização, são atribuídos pesos a cada área da organização de acordo com seu nível de importância, pode-se também atribuir pesos para os riscos dos requisitos e considerá-los no resultado.

A negociação deve ser seguida até a satisfação de todas as partes envolvidas, sendo um processo influenciado não só pela lógica e argumentos técnicos, mas também pela política da organização e pela personalidade dos *stakeholders*.

---

# Validação dos Requisitos

Após levantados e negociados os requisitos, chegou o momento de revisar tudo quanto à ambiguidade, às omissões e às inconsistências. Esse processo garante que a necessidade real do usuário esteja descrita corretamente no Documento de Requisitos.

<aside>
📌 Análise e Negociação respondem à pergunta: foram elicitados os requisitos corretos? A validação responde: os requisitos foram elicitados corretamente?

</aside>

Um primeiro momento o engenheiro de requisitos irá certificar se todos os requisitos que devem ser considerados foram realmente, garantindo a completude do sistema que será desenvolvido. A segunda validação é a correção.

O objetivo é descobrir erros nos requisitos documentados. Um erro de requisito descoberto quando o sistema já está em produção ou em operação exige revisão de todos os artefatos: código-fonte, artefatos de teste e descrições de arquitetura, o que implica custos significativos.

**Revisões técnicas, prototipação e geração de casos de teste** são algumas das técnicas para revisão dos requisitos.

A **revisão técnica** de requisito pode ser **formal** ou **informal**, a **formal** é o principal mecanismo para validação de requisitos, trata-se de um processo onde uma equipe formada por engenheiros de software, clientes, usuários ou outros interessados examinam as especificações, procurando por erro de registro ou interpretação, requisitos que precisem de mais esclarecimento ou aqueles que são conflitantes e/ou intangíveis.

Já a **informal** é um debate que ocorre entre equipe técnica e cliente com objetivo de identificar problema e propor soluções.

Na **prototipação** os requisitos são apresentados de maneira mais lúdica, por exemplo, no formato de telas para o usuário.

A técnica de **geração de casos de teste** verifica se o requisito é implementável, ou seja, fácil de ser interpretado e codificado.

**Nas metodologias ágeis os requisitos são expressos em cenários** (user stories). Partindo das informações adquiridas, a equipe de desenvolvimento estima o esforço e recursos necessários para a implementação e o cliente atribui uma prioridade para cada história.

A **técnica checklist** deve ser usada durante a revisão técnica formal de requisitos e tem como objetivos:

- **Descobrir erros de função, de lógica ou de implementação** para qualquer representação do software.
- Verificar que o software em questão **atende aos requisitos especificados.**
- Garantir que o software foi  **representado de acordo com padrões pré-definidos.**
- Garantir que o software seja **desenvolvido de maneira uniforme.**
- Desenvolver **projetos mais gerenciáveis.**

Segue uma lista de verificação proposta por Sommerville (2008):

1. **Verificação de validade:** nessa validação a equipe irá identificar se certas funções citadas como necessárias por um usuário são, realmente, indispensáveis para o todo.
2. **Verificação de consistência:** identifica se existem requisitos que dizem a mesma coisa de formas diferentes.
3. **Verificação de completeza:** o documento de requisito deve descrever todas as funções e todas as restrições exigidas pelos usuários do sistema.
4. **Verificação de realismo:** validar se existe tecnologia para a implementação dos requisitos, também considera os custos e prazos determinados para o desenvolvimento do sistema.
5. **Facilidade de verificação:** observa se os requisitos estão escritos de forma compreensível para todas as partes envolvidas.

![18 — Modelo Checklist de Validação de Requisitos](18-modelo-checklist-validacao-requisito.png)

18 — Modelo Checklist de Validação de Requisitos

O processo abaixo demonstra o que seriam as possíveis **entradas e saídas da etapa de validação:**

![19 — Entradas e Saídas do Processo de Validação de Requisitos](19-entradas-saidas-processo-validacao.png)

19 — Entradas e Saídas do Processo de Validação de Requisitos

A entrada Especificações de Requisitos deve ser uma versão completa do Documento de Requisitos.

O Conhecimento da Organização é onde as pessoas envolvidas na validação de requisitos devem participar por deterem o conhecimento sobre as terminologias particulares, a execução prática das rotinas que serão automatizadas pelo novo sistema e, principalmente, o perfil dos usuários que ofereceram as informações.

Padrões Organizacionais, garante que a validação irá considerar que todos os padrões relevantes para o documento de requisitos devem ser entrada para o processo de validação.

Como saídas do processo, teremos a Lista de Problemas que podem ser inconsistências, requisitos incompletos, intangíveis, etc. A Lista de Ações representa as atividades em resposta aos problemas listados, acordada com os envolvidos no processo.

No final da validação, temos praticamente o documento de requisitos pronto que corresponde à entrega final da engenharia de requisitos.

---

# Especificação de Requisitos

O documento de requisitos contém a estrutura, que consequentemente precisa ser representada de forma gráfica, sejam ela pela escrita ou por diagramas como usado na UML. Para isso precisamos, primeiro, considerar o público-alvo dos requisitos, a quem se destinam, quem serão os leitores e quais serão os propósitos da leitura:

- Clientes: leem para validar.
- Gerentes: utilizam para solicitar uma proposta e para planejar o processo de desenvolvimento.
- Programadores: utilizam para entender o que deve ser desenvolvido.
- Testes: utilizam para planejar os testes de validação do sistema.
- Manutenção: utiliza para compreender o sistema e suas relações.

Assim que escrito o requisito deve o engenheiro aplicar um rápido teste para verificar se os critérios foram atingidos:

- Necessidade: após escrito, pergunte qual será a pior coisa que poderá acontecer se esse requisito não for incluído, se não encontrarmos nenhum problema, então, é porque, provavelmente, não precisamos do requisito.
- Verificável: se está entendível para todos os leitores.
- Realizável: o engenheiro de requisitos deve observar se o que foi registrado pode ser desenvolvido em relação à tecnologia disponível, orçamento e prazo.
- Claro: cada requisito deve expressar uma única ideia.

A linguagem natural, para especificação, deve seguir algumas regras básicas:

1. Crie um formato padrão para a escrita e garanta que todos os requisitos serão escritos seguindo esse padrão.
2. Utilize uma linguagem coerente, use variações de tempo de verbos para indicar o que é obrigatório ser feito e o que é desejável. Por exemplo, a utilização do verbo deve para requisitos obrigatórios, e sua variação deveria para aqueles desejáveis.
3. Destaque as partes mais importantes da descrição do requisito.
4. Não utilize jargões de informática ou da regra de negócio.
5. Procure especificar as ações em sua sequência e registre, sempre que possível, uma ação por requisito.

A linguagem natural possuí uma ambiguidade intrínseca, por tanto sugere-se que a especificação de requisitos de sistema sigam algumas linguagens padronizadas.

- **Linguagem natural estruturada:** os requisitos são escritos em linguagem natural em um formulário padrão ou template.
- **Linguagem de descrição de projeto:** essa abordagem usa uma linguagem como de programação, mas com características mais abstratas para especificar os requisitos, definindo um modelo operacional do sistema.
- **Notações gráficas:** para definições de requisitos funcionais do sistema.
- **Especificações matemáticas:** essas notações são baseadas em conceitos matemáticos, como máquinas de estado finito ou conjuntos.

Quando um formulário padrão é usado para especificar os requisitos funcionais, as seguintes informações devem ser consideradas:

- Descrição da função ou entidade.
- Descrição de suas entradas e de onde elas vieram.
- Descrição de suas saídas e para onde elas irão.
- Informações sobre os dados necessários para o processamento e outras entidades usadas.
- Descrição da ação a ser tomada.
- Condições pré e pós.
- Os efeitos colaterais (se houver) da função.

![20-formulario-padrao-especificao-requisito.png](20-formulario-padrao-especificao-requisito.png)

- **Função:** identifica a função do requisito.
- **RF:** identificação do requisito (RF001).
- **UC:** representa o Caso de Uso, pode ser utilizada para auxiliar na especificação de requisitos mais complexos e de difícil compreensão.
- **PR:** representa a prioridade estipulada pelo stakeholder.
- **Descrição/Ação:** campo destinado à especificação da função do requisito e da ação a ser tomada.
- **Entrada:** entradas necessárias para o processamento da função.
- **Saída:** saídas/resultados produzidos com a realização da função do requisito.
- **Pré-condições:** o que já deve ter ocorrido ou estar disponível antes da execução do requisito.
- **Pós-condições:** que devem ser verdadeiras quando a execução do requisito se completar
- **Stakeholder**

![21 — Modelo de Especificação de Requisito](21-modelo-especificacao-requisito%201.png)

21 — Modelo de Especificação de Requisito

Ao ter pouco acesso ou informação nenhuma sobre o que se deseja desenvolver/produzir, busque-as. Para o caso de não existir nenhuma informação, registre suas hipóteses associadas a cada requisito, isso ajudará nas etapas de negociação e validação.

Outra dica para escrever seus requisitos: **separe funcionalidade de implementação**. As especificações devem referir o que é necessário para o sistema e não como vai ser disponibilizado ou programado. Para evitar a especificação de implementações, pergunte-se: por que precisamos deste requisito?

Sempre pergunte ao requisito para que precisamos dele e verifique se a resposta remete para uma ou mais necessidades. Se isso ocorrer, refine o requisito, separando a necessidade da implementação, senão você tem a garantia de que definiu a função da maneira correta.

Os atributos de qualidade aplicados nos requisitos são, basicamente, os mesmos aplicados na fase de validação:

1. Não Ambiguidade: cada requisito deve possuir, apenas, uma interpretação.
2. Completude: é a capacidade de cada requisito especificar claramente seu assunto, objetivo.
3. Consistência: é a capacidade de cada requisito não ser contraditório a outro.
4. Correção/Exatidão: é a capacidade de o requisito de estar correto.

---

# Conclusão

Requisitos bem especificados favorecem todas as outras atividades do processo de desenvolvimento de software, garantindo, ainda, que seja realizado no custo e prazo estabelecido e, mais importante, que satisfaça a necessidade do cliente.

São quatro as principais atividades para realização da engenharia de requisito. A primeira delas é o levantamento de requisito, o momento onde o cliente declara sua expectativa e a equipe de desenvolvimento levanta os requisitos funcionais e suas restrições. A entrevista é uma das técnicas utilizadas na fase de levantamento de requisito. Em seguida, as fases de negociação e validação do requisito garantem que sejam coesos, claros, não ambíguos e rastreáveis. Na última etapa é a de especificação do requisito no Documento devendo ser descritos de uma maneira que possibilite que sejam verificados e em uma linguagem ou padronização que possa ser compreendida por leitores técnicos e não técnicos.

---