# Introdução

Quando pensamos em qualidade, geramos muitas preocupações relacionadas com o gerenciamento de qualidade que podem ser resumidas em elementos que contribuem para organizá-la, assim como os padrões e normas de qualidade e os testes de software. 

Portanto, estudiosos e institutos preocupados, não só com a qualidade de seus produtos e serviços mas também em garantir maior segurança para os usuários criaram diversos padrões e normas de qualidade, como, por exemplo, CMMI e MPSBR.

# Introdução à Qualidade de Software

A qualidade, em software, refere-se às características dos produtos que atendem os requisitos de funcionalidade. Esses requisitos estão ligados diretamente com a área de utilização do programa. 

Tais requisitos são: 

- Funcionalidade;
- Confiabilidade;
- Usabilidade;
- Eficiência;
- Manutenibilidade;
- Portabilidade;
- Estabilidade.

Esses requisitos fazem parte da qualidade do software de forma que cada produto, cada programa, possa atender as necessidades tecnológicas, econômicas, sociais, intelectuais e práticas do setor ao qual se destinam, observando as especificidades de cada área onde o produto é utilizado. 

A qualidade visa apresentar um produto completo, que atenda todas as necessidades do setor ao qual se destina.

O termo qualidade possui várias definições, as quais variam conforme a abordagem utilizada:

- **Conformidade com as especificações**: o gerenciamento da qualidade deve ser feito desde o início do desenvolvimento, para evitar defeitos e diminuir o retrabalho (levantamento de requisitos e modelagem).
- **Adequação ao uso:** significa que as expectativas do cliente são atendidas. Aqui há dois fatores a considerar, a qualidade obrigatória, em que o produto cumpre o que devia fazer, e a qualidade atrativa, onde o produto vai além do que ele devia fazer.
- **NBR ISO 8402:** qualidade é a totalidade das características de uma entidade que lhe confere a capacidade de satisfazer às necessidades explícitas e implícitas.
    - **Entidade:** é o produto do qual estamos falando.
    - **Necessidades explícitas:** são expressas na definição de requisitos, são as condições em que o produto deve ser utilizado, seus objetivos, funções e qual vai ser o seu desempenho esperado.
    - **Necessidades implícitas:** não são expressas em documentos, mas são necessárias para o usuário durante o manuseio do produto no seu dia a dia.

No início da década de 70 Bohem e McCall propuseram uma classificação para os fatores que afetam a qualidade de um produto de software, surgindo então os primeiros padrões para garantia de qualidade. 

Dessa forma programas de melhoria de qualidade bem-sucedidos propiciam um aumento de produtividade, redução no número de defeitos no software, maior previsão e visibilidade dos processos definidos, além do cumprimento das metas de custo, prazo, funcionalidade e aumento na motivação da equipe desenvolvedora.

---

## Fatores de Qualidade

McCall, Richards e Walters criaram uma proposta de categorização dos fatores que afetam a qualidade de software. Eles se concentram em três importantes aspectos: r**evisão, a transição e a operação do produto de software:**

![56.fatores-qualidade-software.png](56.fatores-qualidade-software.png)

| Fator | Descrição |
| --- | --- |
| Correção | O quanto um programa satisfaz a sua especificação e atende aos objetivos da missão do cliente. |
| Confiabilidade | O quanto se pode esperar que um programa realize a função pretendida com a precisão exigida. |
| Integridade | O quanto o acesso ao software ou dados por pessoas não autorizadas pode ser controlado. |
| Usabilidade | Esforço necessário para aprender, operar, preparar a entrada de dados e interpretar a saída de um programa |
| Facilidade de Manutenção | Esforço necessário para localizar e corrigir um erro em um programa e fazer a manutenção. |
| Flexibilidade | Esforço necessário para modificar um programa em operação, exemplo adicionar alguma funcionalidade, campo ou coluna. |
| Testabilidade | Esforço necessário para testar um programa, de modo a garantir que ele desempenhe a função destinada. |
| Portabilidade | Esforço necessário para transferir um programa de um ambiente de hardware e/ou software para outro. |
| Reusabilidade | O quanto um programa [ou partes de um] pode ser reutilizado em outras aplicações relacionadas ao empacotamento e o escopo das funções que o programa executa |
| Interoperabilidade | Esforço necessário para integrar um sistema a outro. Um sistema de ERP integrando com um sistema de emissão de NF, por exemplo. |

---

## Elementos de Garantia da Qualidade de Software

Quando pensamos em garantir a qualidade de software, temos muitas preocupações e atividades relacionadas com a gestão da qualidade:

| Elemento | Descrição |
| --- | --- |
| Padrões | O IEEE, a ISO e outras organizações de padronização produziram uma ampla gama de padrões para engenharia de software e seus respectivos documentos. Os padrões podem ser adotados voluntariamente por uma organização de engenharia de software ou impostos pelo cliente ou outros interessados. |
| Revisões e Auditorias | As revisões técnicas são uma atividade de controle de qualidade realizada por engenheiros de software. Seu intuito é o de revelar erros. |
| Testes | Os testes de software são uma função de controle de qualidade com um objetivo principal: o de descobrir erros e também verificar se o que foi desenvolvido está em conformidade com o que o cliente solicitou. |
| Coleta e Análise de Erros/Defeitos | A única forma de melhorar e medir o nosso desempenho. Assim, deve-se reunir e analisar dados de erros e defeitos para melhor compreender como os erros são introduzidos e quais atividades de engenharia de software melhor se adéquam para sua eliminação. |
| Administração da Segurança | Com o aumento dos crimes cibernéticos e novas regulamentações governamentais referentes à privacidade, toda organização de software deve instituir políticas que protejam os dados em todos os níveis, estabelecer proteção através de firewalls para as aplicações da Internet (WebApps) e garantir que o software não tenha sido alterado internamente, sem autorização. |
| Proteção | O fato de o software ser quase sempre um componente fundamental de sistemas que envolvem vidas humanas (por exemplo, aplicações na indústria automotiva ou aeronáutica), o impacto de defeitos ocultos pode ser catastrófico. Devemos avaliar o impacto de falhas de software e por iniciar as etapas necessárias para redução de riscos. |

---

## Normas e Modelos de Padrões de Qualidade de Software

As normas e modelos de padrões de qualidade de software são a principal chave para a garantia da qualidade. Muitos são aplicados na empresa na totalidade, mas há também empresas que optam por adotar somente em um projeto, também pode ser uma exigência do cliente. São elas quem definem as características que todos os componentes de software devem possuir e como o processo de software deve ser condizido, para assegurar a qualidade do produto de software. Existem diversas normas e modelos criados, um delas é a CMMI e a MPSBr.

---

### CMMI

O CMMI (Capability Maturity Model Integration ou Modelo integrado de Maturidade e Capacitação), foi desenvolvido pelo SEI (Software Engineering Institute), é o modelo desenvolvido para a melhoria da maturidade dos processos de desenvolvimento de software na empresa. 

É um modelo para avaliar e melhorar a capacitação das empresas que desenvolvem software, propondo etapas que levam a instituição a se aprimorar continuamente em busca de soluções para o seu crescimento com qualidade.

Os objetivos principais do CMMI envolvem:

- Auxiliar as empresas a se conhecerem. A partir disso, espera-se que elas melhorem seus processos de desenvolvimento e a manutenção do software.
- Fornecer, às empresas, um controle de seus processos através de uma estrutura conceitual e, com isso, obter a melhoria contínua de seus produtos de software.

<aside>
🚨 O modelo não diz como implementar determinadas práticas, ele apenas indica o que deve ser feito.

</aside>

Existem duas representações, uma contínua e outra em estágios, nas quais os modelos CMMI podem variar conforme a representação e o corpo de conhecimento escolhido pela empresa.

**Representação contínua**: é caracterizada pelos níveis de capacidade. O modelo descreve um caminho de melhoria de maturidade através de cinco níveis distintos, cada um com características individuais, as quais determinam qual é a capacitação do processo. Quanto maior o nível, maior é a maturidade dos processos de desenvolvimento de software de uma empresa.

A etapa do nível 1, a empresa precisa se conhecer melhor, avaliando seu nível de gerenciamento e controle. 

![57-niveis-cmmi.png](57-niveis-cmmi.png)

**Representação em estágio:** foca nas melhores práticas que uma empresa pode utilizar. A maturidade é medida por um conjunto de processos.

![58.representacao-estagio.png](58.representacao-estagio.png)

O quadro acima nos mostra que cada nível de maturidade é composto por várias área-chaves de processo, as quais possuem objetivos específicos e genéricos. Cada objetivo específico é alcançado através de algumas práticas bem definidas. Cada objetivo genérico especifica várias funcionalidades comuns, as quais estão ligadas as práticas genéricas. Essas práticas são os detalhes operacionais que devem ser abordados pelo processo ou pela metodologia  de desenvolvimento usado na empresa.

O modelo CMMI fornece orientação para melhorias nos processos e nas habilidades organizacionais. Ele também inclui o ciclo de vida de produtos e serviços de um software, o qual abrange as fases de: concepção, desenvolvimento, aquisição, entrega e manutenção.

Este modelo se tornou conhecido pela riqueza de detalhes e pela sua completa descrição do processo de software, influenciando outros modelos criados, como o MPSBr.

---

### MPSBr

O MPSBr é um modelo de qualidade de processos de software voltado para características das empresas brasileiras, baseado no padrão CMMI, nas normas ISO/IEC 12207 e SPICE. Principal vantagem é seu custo reduzido de certificação.

Ele está dividido em três componentes:

- Modelo de Referência (MR-MPS): para serviço e gestão de pessoas
- Método de Avaliação (MA-MPS)
- Modelo de Negócio (MN-MPS)

![59 — Componentes do Modelo MPSBr](59-MPSBr.png)

59 — Componentes do Modelo MPSBr

O MR-MPS é um modelo de referência para a melhoria do processo de software e apresenta sete níveis de maturidade, que são:

- **Nível G — Parcialmente gerenciado:** primeiro nível do modelo, é composto pelos processos de gerência de projeto e gerência de requisitos.
- **Nível F — Gerenciado:** composto pelo nível G acrescido dos processos de gerência de configuração, garantia da qualidade, medição e aquisição.
- **Nível E — Parcialmente Definido:** composto pelo nível F acrescido dos processos de treinamento, definição do processo organizacional, avaliação e melhoria do processo organizacional e adaptação do processo para gerência de projetos.
- **Nível D — Largamente Definido:** composto pelo nível E, acrescido dos processos de desenvolvimento de requisitos, solução técnica, validação, verificação, integração de produto, instalação de produto e liberação de produto.
- **Nível C — Definido:** composto pelo nível D, acrescido dos processos de gerência de riscos e análise de decisão e resolução.
- **Nível B — Gerenciado Quantitativamente:** é composto pelo nível C, acrescido dos processos de desempenho do processo organizacional e gerência quantitativa de projeto.
- **Nível A — Em Otimização:** nível mais elevado do modelo, composto pelo nível B e acrescido dos processos de inovação e implantação na organização, análise e resolução de causas.

Cada nível de maturidade possui suas áreas de processo, nas quais são analisados os:

- **Processos fundamentais:** aquisição, gerência de requisitos, desenvolvimento de requisitos, solução técnica, integração, instalação e liberação de produto.
- **Processos organizacionais:** gerência de projeto, adaptação do processo para gerência de projeto, análise de decisão e resolução, gerência de riscos, avaliação e melhoria do processo organizacional, definição do processo organizacional, desempenho do processo organizacional, gerência quantitativa do projeto, análise e resolução de causas, inovação e implantação na organização.
- **Processo de apoio:** garantia de qualidade, gerência de configuração, validação, medição, verificação e treinamento.

Em seguida, apresentam-se os níveis de capacidade, nos quais são obtidos os resultados dos processos analisados:

- AP 1.1 — O processo é executado.
- AP 1.2 — O processo é gerenciado.
- AP 2.2 — O produto de trabalho do processo gerenciados.
- AP 3.1 — O processo é definido.
- AP 3.2 — O processo está implementado.

O MA-MPS é um método de avaliação para melhoria do processo de software e o seu objetivo é o de orientar a realização de avaliações, em conformidade com a norma ISO/IEC 15504, em empresas que já implementaram o MR-MPS.

Já o MN-MPS é um modelo de negócio para melhoria do processo de software. 

---

# Teste de Software

A qualidade de software é determinada pela qualidade dos processos usados durante a fase de desenvolvimento do software. 

Todo software deve sofrer um nível mínimo de teste. Quanto maior o nível de complexidade do software, mais testes e técnicas se tornam necessários.

Há alguns axiomas e conceitos que podem ser usados no processo de teste:

- Não é possível testar um programa completamente.
- Teste de software é um exercício baseado em risco.
- Teste não mostra que bugs não existem, mas sim, o contrário.
- Quanto mais bugs são encontrados, mais bugs poderão aparecer.

O teste de software tem, como objetivo, mostrar que um sistema corresponde com as especificações descritas no documento de requisitos e atende as expectativas do cliente comprador do sistema. A maior parte dos custos de validação é observada depois da implementação, quando o sistema é testado pelo usuário final. 

Os testes de software não podem provar que um produto funciona, mas apenas encontrar defeitos, geralmente possuem dois objetivos principais:

- Encontrar defeitos no software, para eles poderem ser corrigidos ou minimizados.
- Fornecer uma avaliação geral de qualidade e uma estimativa das possíveis falhas.

### Por que testar?

- Quando um código defeituoso é executado, falhas ocorrem.
- Um sistema com falhas gera insatisfação, ferimentos ou até a morte dos clientes e usuários.

### Testamos para:

- Verificar se o sistema está fazendo o que foi solicitado pelo cliente, com base nos requisitos levantados.
- Garantir que o negócio não vai correr riscos provocados por defeitos em produção.
- Assegurar qualidade do sistema.

<aside>
💡 Os desenvolvedores querem provar que "**algo funciona**".

</aside>

<aside>
🚨 Os testadores querem provar que "**algo NÃO funciona**".

</aside>

> Analisando o esforço dos testes podemos perceber que é mais fácil provar que "algo funciona" do que provar que "algo não funciona".
> 

---

## Conceitos Básicos de Teste de Software

Um dos conceitos que devem ser vistos é a diferença entre erro e defeito. 

Defeitos são considerados parte do universo físico, são provocados por pessoas e podem ocasionar erros em um software. Um defeito pode ocorrer em função de desvios do que foi levantado na análise de requisitos.

O teste de software é muitas vezes conhecido como verificação e validação. A verificação diz respeito ao conjunto de tarefas que visa garantir que o software teve suas funções específicas implementadas corretamente. A validação se constitui como um conjunto de tarefas que objetiva assegurar que o software foi criado e pode ser verificado com base nos requisitos do cliente.

<aside>
💡 **Verificação:** "Estamos construindo corretamente o sistema?"
**Validação:** "Estamos construindo o sistema correto?"

A primeira questão diz respeito ao que foi construído, enquanto a segunda se refere ao entendimento do que era para ser construído.

</aside>

---

## Técnicas de Teste de Software e Tipos de Testes

As técnicas de teste são procedimentos técnicos e gerenciais que ajudam na avaliação e nas melhorias do processo de software. Podem ser utilizadas para classificar:

- Diferentes conceitos de testes de software.
- Técnicas que envolvem o design de testes e suas situações.
- Técnicas de execução de teste e organizações de testes de software.

A fase de testes de software pode ser dividida em duas técnicas: funcional e estrutura.

### Testes funcionais

Garantem o atendimento aos requisitos do sistema, ou seja, que os requisitos estão corretamente codificados. São conhecidos como testes de caixa preta

Utilizam as especificações do documento de análise de requisitos e de projetos para definir os testes a serem realizados, sem considerar o seu comportamento interno, apenas o resultado produzido.

Esse teste pode encontrar funções incorretas ou que estejam faltando, erros de interface, erros em estruturas de dados ou acesso à base de dados externas, erros de comportamento ou de desempenho e, por último, erros de inicialização e término.

<aside>
🚨 Se o tipo de saída não ocorre, então houve uma situação de defeito.

</aside>

### Testes estruturais

Garantem que os sistemas sejam estruturalmente sólidos e que funcionem no contexto técnico em que serão instalados. São conhecidos como testes de caixa branca.

Essa técnica não é desenhada para garantir que o sistema esteja funcionalmente correto, mas para ele ser estruturalmente robusto, estabelecendo os objetivos do teste com base em uma determinada implementação, analisando os detalhes do código-fonte. Todas as variações originadas por estruturas de condições/repetições do código são testadas.

Portanto, essa categoria de teste, visa garantir que todos os caminhos independentes de um módulo sejam executados pelo menos uma vez, exercitando todas as decisões lógicas nos seus estados verdadeiro e falso, executando todas as decisões lógicas nos seus estados verdadeiro e falso, executando todos os ciclos em seus limites e dentro de suas fronteiras operacionais, por último, exercitando estruturas de dados internas para assegurar a sua validade.

A seguir uma lista com algumas categorias de testes que podem ser utilizados:

- **Teste de Unidade:** Teste em um nível de componente ou classe. É o teste cujo objetivo é um "pedaço de código".
- **Teste de Integração:** Garante que um ou mais componentes combinados (ou unidades) funcionam. Podemos dizer que um teste de integração é composto por diversos testes de unidade.
- **Teste Positivo-Negativo:** Garante que a aplicação vai funcionar no "caminho feliz" de sua execução e funcionará no seu fluxo de exceção.
- **Teste de Interface:** Verifica se a navegabilidade e os objetivos da tela funcionam assim como foram especificados e se atendem da melhor forma ao usuário.
- **Teste de Aceitação do Usuário:** Testa se a solução será bem vista pelo usuário. Ex: caso exista um botão pequeno demais para executar uma função, isso deve ser criticado em fase de testes (aqui cabem quesitos fora da interface também).
- **Teste de Volume:** Testa a quantidade de dados envolvidos (pode ser pouca, normal, grande ou além de grande).
- **Testes de Configuração:** Testa se a aplicação funciona corretamente em diferentes ambientes de hardware ou de software.
- **Testes de Instalação:** Testa se a instalação da aplicação foi bem sucedida.
- **Testes de Sistemas:** Testa a execução do sistema na totalidade, de modo a validar a exatidão e perfeição na execução de suas funções.
- **Teste de Usabilidade:** Testa e simula as condições de utilização do software sob a perspectiva do usuário final. Esses testes focalizam a facilidade de navegação entre as telas, clareza dos textos e as mensagens apresentadas ao usuário, dentre outros aspectos da interface do sistema.
- **Testes de Progressão:** Testa apenas as funcionalidades (ou requisitos não funcionais) especificadas para a versão.
- **Teste de Fumaça:** Teste o qual acontece rapidamente, executando as principais funcionalidades do sistema sem se preocupar com as condições de erro. É o mesmo que o teste do "caminho feliz".

Existe na literatura a definição de uma técnica de teste chamada "caixa cinza", a qual mescla as técnicas de caixa preta com a caixa branca.

O sistema de software comercial tem de passar por três estágios de teste:

1. Testes em desenvolvimento, em que o sistema é testado durante o desenvolvimento para descobrir bugs e defeitos. Projetistas de sistemas e programadores podem estar envolvidos no processo de teste.
2. Testes de release, em que uma equipe de teste independente testa uma versão completa do sistema antes que ele seja liberado para os usuários.
3. Testes de usuário, em que os usuários ou potenciais usuários de um sistema testam o sistema em seu próprio ambiente.
4. Os testes de aceitação são uma categoria de teste de usuário onde o cliente testa formalmente o sistema para decidir se ele deve ser aceite por parte do fornecedor do sistema ou se é necessário um desenvolvimento adicional.

---

# Evolução de Software

Depois que o software é posto em funcionamento, com certeza ocorrerão mudanças. Essas mudanças podem ser para correção de erros não detectados durante a etapa de validação do software, quando há adaptação a um novo ambiente, quando o cliente solicita novas características ou funções, ou, ainda, quando a aplicação passa por um processo de reengenharia para proporcionar benefício em um contexto moderno. 

Normalmente, os custos de manutenção são maiores que os custos de desenvolvimento inicial e considerados menos desafiadores.

Atualmente, os estágios de desenvolvimento e manutenção têm sido considerados integrados e contínuos. 

![60-Evolução do Software](60-evolucao-software.png)

60-Evolução do Software

---

## Manutenção de Software

Após a implantação de um sistema, é inevitável que ocorram mudanças, seja para pequenos ajustes após a implantação, para melhorias substanciais, por força da legislação, para atender novos requisitos dos usuários, ou por, finalmente, estar com erros.

Cerca de dois terços dos custos de software estão relacionados com a evolução do software, além do consumo alto de tempo por parte da equipe de desenvolvimento em relação à manutenção e todas as implicações que essa etapa carrega. 

Uma das razões para o problema acerca da manutenção de software se dá na troca das pessoas que compõem as equipes de desenvolvimento, possivelmente a equipe que desenvolveu o software inicialmente já não se encontre mais por perto, ou ainda, que ninguém esteja trabalhando atualmente na empresa. Nesse caso,  se o sistema desenvolvido estiver bem documentado e, em seu desenvolvimento, tenham sido seguidos os preceitos da engenharia de software, com certeza, sua alteração se tornará mais fácil e é possível afirmar que o sistema apresenta uma alta manutenibilidade. 

A manutenção do software é importante, visto que o mundo muda rapidamente, demandadas por tecnologia de informação que suportem essas mudanças e exigências no mercado impõem um ritmo de enorme pressão competitiva a todas as organizações comerciais. Portanto, o software deve ser mantido continuamente, ou seja, deve passar por manutenções constantemente. 

Existem três tipos diferentes de manutenção:

1. **Correção de defeitos:** erros de codificação são relativamente baratos para serem corrigidos e erros de projeto são mais caros, pois podem implicar na reescrita de vários componentes de programa. Erros de requisitos são os mais caros para se corrigir, devido ao retrabalho (reprojeto) de sistema que pode ser necessário.
2. **Adaptação ambiental:** essa categoria manutenção é necessário quando algum aspecto do ambiente do sistema, como o hardware, a plataforma do sistema operacional ou outro software de apoio, sofre uma mudança. O sistema de aplicação deve ser modificado para se adaptar a essas mudanças de ambiente.
3. **Adição de funcionalidade:** essa categoria de manutenção é necessário quando os requisitos de sistema mudam em resposta às mudanças organizacionais ou de negócios. A escala de mudanças necessárias para o software é, frequentemente, muito maior do que para as outras categorias de manutenção.

Uma pesquisa realizada em empresas de desenvolvimento mostram que a manutenção de software ocupa dois terços do orçamento de desenvolvimento. A pesquisa também mostra que se gasta mais do orçamento na implementação de novos requisitos do que na correção de bugs.

![61-Distribuição do esforço de manutenção](61-distribuicao-esforco-manutencao.png)

61-Distribuição do esforço de manutenção

---

# Configuração de Software

O Gerenciamento de Configuração de Software (SCM — *Software Configuration Management*) ou GCS é uma atividade de apoio, do tipo "guarda-chuva aplicada no decorrer de toda a gestão de qualidade, destinada a gerenciar as mudanças, identificando os artefatos que precisam ser alterados, as relações entre eles e o controle de versão desses artefatos, controlando essas mudanças, auditando e relatando todas as alterações feitas no software.

As mudanças podem ocorrer em qualquer instante, por isso, as atividades de SCM são desenvolvidas para:

- Identificar a alteração feita.
- Controlar a alteração que está sendo feita.
- Assegurar que a alteração esteja sendo implementada corretamente no software.
- Relatar as alterações aos membros da equipe.

São descritas quatro atividades de Gerenciamento de Configuração de Software:

1. **Gerenciamento de mudanças:** envolve manter o acompanhamento das solicitações dos clientes e desenvolvedores por mudanças no software, definir os custos e o impacto de fazer tais mudanças, bem como decidir se e quando as mudanças devem ser implementadas.
2. **Gerenciamento de versões:** envolve manter o acompanhamento de várias versões de componentes do sistema e assegurar que as mudanças nos componentes, realizadas por diferentes desenvolvedores, não interferem uma nas outras.
3. **Construção do sistema:** é o processo de montagem de componentes de programas, dados e bibliotecas e, em seguida, compilação e ligação destes, para criar um sistema executável.
4. **Gerenciamento de releases:** envolve a preparação de software para o release externo e manter o acompanhamento das versões de sistema liberadas para uso do cliente.

<aside>
💡 Qual a diferença de suporte de software e gerenciamento de configuração de software?

</aside>

> **Suporte** é um conjunto de atividades de engenharia que ocorrem depois que o software foi fornecido ao cliente e posto em operação. 

**Gestão** **de configuração** é um conjunto de atividades de rastreamento e controle iniciadas quando um projeto de engenharia de software começa e termina apenas quando o software sai de operação.
> 

![62-Atividades gerenciamento de configuração de software](62-atividades-gerenciamento-configuracao-software.png)

62-Atividades gerenciamento de configuração de software

A SCM possui um conjunto de atividades desenvolvidas para controlar as mudanças que podem ocorrer ao longo do ciclo de vida de um software. Pode ser entendida como uma atividade de garantia de qualidade do sistema e pode ser aplicada em todo o processo do software. 

As informações resultantes do processo de software podem ser divididas em três categorias:

- Aplicações (forma de código-fonte ou executável).
- Produtos que descrevem os softwares (focado em vários interessados do sistema — analistas, desenvolvedores, testadores, suporte, etc.).
- Dados ou conteúdo (contidos nos sistemas ou externos a eles).

Os itens que compõem todas as informações produzidas como parte do processo de software são chamados coletivamente de configuração de software. Conforme se avança no desenvolvimento do sistema, cria-se uma hierarquia dos itens de configuração de software.

Um dos problemas do gerenciamento de configuração, é que muitas empresas falam sobre os mesmos conceitos usando termos diferentes:

| Termo | Descrição |
| --- | --- |
| Item de configuração u item de configuração de software (SCI, Software Configuration Item) | Qualquer coisa associada a um projeto de software (projeto, código, dados de teste, documentos, etc) que tenha sido colocado sob controle de configuração. Muitas vezes, existem diferentes versões de um item de configuração. Itens de configuração têm um nome único.  |
| Controle de Configuração | O processo de garantia de que versões de sistemas e componentes sejam registradas e mantidas para que as mudanças sejam gerenciadas e todas as versões de componentes sejam identificadas e armazenadas por todo o tempo de vida do sistema. |
| Versão | Uma instância de um item de configuração que difere de alguma forma, de outras instâncias deste item. As versões sempre têm um identificador único, o qual é geralmente composto pelo nome do item de configuração mais um número de versão. |
| Baseline | Uma baseline é uma coleção de versões de componentes que compõem um sistema. As baselines são controladas, o que significa que as versões dos componentes que constituem o sistema, não podem ser alteradas. Isso significa que deveria sempre ser possível recriar uma baseline a partir de seus componentes. |
| Codeline | Uma codeline é um conjunto de versões de um componente de software e outros itens de configuração dos quais esse componente depende. |
| Mainline | Trata-se de uma sequência de baselines que representam diferentes versões de um sistema.  |
| Release | Uma versão de um sistema liberada para os clientes (ou outros usuários em uma organização) para uso. |
| Branching | Trata-se da criação de uma nova codeline de uma versão em uma codeline existente. A nova codeline e uma codeline podem, então, ser desenvolvidas independentemente. |
| Merging | Trata-se da criação de uma nova versão de um componente de software, fundindo versões separadas em diferentes codelines. Essas codelines podem ter sido criadas por um branch anterior de uma das codelines envolvidas. |

---