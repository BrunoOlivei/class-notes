# Requisitos de Software

# Introdução

Uma das tarefas mais difíceis que os desenvolvedores enfrentam é a de entenderem os requisitos de um problema. Os requisitos definirão o que o sistema deve fazer, suas propriedades emergentes desejáveis e essenciais, bem como as restrições quanto à operação do sistema. Essa definição de requisitos somente é possível com a comunicação entre os clientes, os usuários e os desenvolvedores de software.

Os **requisitos funcionais** representam as descrições das diversas funções que o cliente e usuários querem ou precisam que o software ofereça. Um exemplo é a possibilidade de cadastramento dos dados pessoais dos pacientes. Já os **requisitos não funcionais** declaram as restrições ou atributos de qualidade para um software, como precisão, manutenibilidade, usabilidade e entre outros.

# Requisitos de Software

As descrições das funções e das restrições são os **requisitos para o sistema,** enquanto o processo de descobrir, analisar, documentar e verificar essas funções e restrições é chamado de **engenharia de requisitos**.

>[!note]
>📌 Define o que o software deve fazer. É extremamente importante para o sucesso do desenvolvimento. Um ator importantíssimo é o usuário final e a habilidade mais importante do analista de software é a comunicação.

O requisito é visto como uma declaração abstrata, em outras ele é uma definição detalhada e formal de uma função do sistema.

É muito importante que seja claro o que o sistema não vai fazer.

Alguns problemas que surgem durante a especificação de requisitos é fazer uma separação clara entre os diferentes níveis de descrição e os dos requisitos. A literatura propõe uma distinção entre esses níveis por meio do uso do termo **requisitos de usuário**, para expressar os requisitos abstratos de alto nível, e **requisitos de sistema**, para expressar a descrição detalhada que o sistema deve fazer. 

## Requisitos Funcionais e Não Funcionais

Os requisitos dizem respeito as necessidades dos usuários para um sistema que deve atender um determinado objetivo, como cadastrar um pedido de venda ou emitir um relatório. A engenharia de requisitos engloba as atividades que são necessárias para criar e manter um documento de requisitos de sistema. Essas atividades sendo: estudo de viabilidade, levantamento e analise de requisitos, especificação de requisitos e a validação desses requisitos.

1. Requisitos Funcionais: definem as funções que o sistema deve fornecer, sobre como o sistema deve reagir a entradas específicas e sobre como se comportar em determinadas situações. Em alguns casos, podem também, declarar o que o sistema não deve fazer.
2. Requisitos Não Funcionais: são os requisitos relacionados com a utilização do software em termos de desempenho, confiabilidade, segurança, usabilidade e portabilidade entre outros.

A diferenciação entre esses dois tipos de requisitos não é tão clara como sugere as definições apresentadas. Portanto embora interessante a divisão entre funcionais e não funcionais, devemos nos atentar que, na verdade, é uma distinção artificial. O mais importante é que os requisitos, sejam eles funcionais ou não, sejam declarados.

### Requisitos Funcionais

Devem descrever detalhadamente os serviços e a funcionalidade que deve ser fornecida pelo sistema, indicando suas entradas e saídas, exceções, etc.

Elas devem ser completas e consistentes, ou seja, que todas as funções requeridas pelo usuário devem estar definidas e sem definições contraditórias.

**Exemplos:**

**[RF001]** O sistema deve cadastrar médicos profissionais (entrada)

**[RF002]** O sistema deve emitir um relatório de clientes (saída)

**[RF003]** O sistema deve passar um cliente da situação "em consulta" para "consultado" quando o cliente terminar de ser atendido (mudança de Estado)

**[RF004]** O cliente pode consultar seus dados no sistema.

### Requisitos Não Funcionais

Podem estar relacionados a propriedades, tais como confiabilidade, tempo de resposta e espaço em disco, por exemplo. Também podem definir restrições para o sistema, como a capacidade dos dispositivos E/S (entrada/saída) e as representações de dados utilizadas nas interfaces de sistema.

Surgem conforme a necessidade dos usuários, em razão de restrições de orçamento, políticas organizacionais, pela necessidade de interoperabilidade com outros sistemas de software ou hardware ou devido a fatores externos como regulamentos de segurança e legislações sobre privacidade, por exemplo.

Há na literatura uma classificação:

1. **Requisitos de produto:** especificam o comportamento do produto e podem ser subdivididos em requisitos de usabilidade, de eficiência, de confiança e de proteção.
2. **Requisitos organizacionais:** derivados das políticas dos procedimentos da organização do cliente e do desenvolvedor, são subdivididos em ambientais, operacionais e de desenvolvimento.
3. **Requisitos externos:** procedem de fatores externos ao sistema e seu processo de desenvolvimento, subdivididos em reguladores, éticos e legais. 

Há uma necessidade de fazer a diferenciação de requisitos funcionais e não funcionais nos documentos, porém, na prática, não é fácil fazer a distinção. Se em documentos separados por exemplo, os funcionais e não funcionais, pode ser difícil entender a relação entre eles. Se declarados juntos e sem distinção também fica difícil a identificação dos requisitos que correspondem ao sistema como um todo, sendo assim é preciso encontrar um equilíbrio adequado.

**Exemplos:**

**[RNF001]** O sistema deve imprimir o relatório em até 5 segundos;

**[RNF002]** Todos os relatórios devem seguir o padrão de relatórios especificado pelo setor XYZ.

**[RNF003]** O sistema deve ser implementado em Java.

**[RNF004]** O sistema deve ser protegido para o acesso de usuários.

### Requisitos de domínio/negócio:

Requisitos derivados do domínio da aplicação e descrevem características do sistema e qualidades que refletem o domínio (regra do negócio).

**Exemplo:** 

**[RD001]** O calculo da média final de cada aluno é dado pela fórmula: (Nota1 *2 + Nota2 * 3)/5.

**[RD002]** O valor do IPI é calculado em relação ao valor da nota fiscal da mercadoria despachada, que pode eventualmente incluir valores sobre o frete e despesas acessórias (juros, taxas e outras).

**[RD003]** O cálculo de comissão dos vendedores é de 15% sore o total líquido das vendas no mês.

### Requisitos de Usuário

Devem descrever os requisitos funcionais e não funcionais, de forma detalhada e de fácil entendimento, especificando o comportamento externo do sistema, pois é destinado às pessoas envolvidas no uso e aquisição do sistema.

### Requisitos de Sistema

Os requisitos de sistema são as descrições mais detalhadas dos requisitos do usuário, devem ser uma especificação completa e consistente de todo sistema.

Antes de qualquer coisa, os requisitos de sistema deveriam definir o que o sistema deveria fazer, e não como ele teria de ser implementado. Todavia é quase impossível excluir todas as informações de projeto. Há, pelo menos, duas razões para isso:

1. Uma arquitetura inicial dos sistema pode ser definida para ajudar a estruturar a especificação de requisitos.
2. Na maioria dos casos, os sistemas devem interoperar com outros sistemas existentes, restringindo, assim, o projeto em desenvolvimento e, muitas vezes, essas restrições geram requisitos para o novo sistema.

Os requisitos devem ser escritos em níveis diferentes de detalhamento, para que diferentes leitores possam usá-lo de formas distintas.

### Requisitos de Projeto (especificação do projeto)

É a definição do projeto de software em nível mais técnico - modelagem.

# Documento de Requisitos

É um documento de acordo (entre quem solicita e quem desenvolve). Estabelece o escopo do software, garante uma rastreabilidade mínima, serve como documento de referência.

É a declaração oficial do que é exigido dos desenvolvedores de sistema, deve incluir os requisitos de usuários para um sistema e uma especificação detalhada dos requisitos de sistema. Em alguns casos, os requisitos de usuário e de sistema podem ser integrados em uma única descrição, em outros, os requisitos de usuário são definidos em uma introdução para a especificação dos requisitos de sistema. Se houver um grande número de requisitos, os requisitos detalhados de sistema poderão ser apresentados como documentos separados.

O documento de requisitos serve como um termo de consenso entre a equipe técnica (desenvolvedores) e o cliente, bem como constitui a base para atividades subsequentes do desenvolvimento do sistema, fornecendo um ponto de referência para qualquer validação futura do software construído.

Existem diversos modelos sugeridos, o **RUP** (Processo Unificado da Rational) sugere modelos para documento de requisitos mais complexo. O guia **PMBOK** tem uma sugestão para a documentação de requisitos.

Abaixo uma tabela com base na norma IEEE (Institute of Eletrical and Electronics Engineers) para documentos de requisitos:

![Estrutura de documento de requisitos](2-IEEE.jpg)

Estrutura de documento de requisitos

Qual o nível certo de documentação? Primeiro o documento deve ser capaz de garantir o entendimento dos stakeholders. Segundo a equipe técnica deve estar ciente de que este documento é a única garantia que atende as solicitação do cliente. Em outras palavras, o documento de requisitos garante a empresa desenvolvedora que tudo que foi solicitado e acordado previamente foi realizado e entregue.

### Requisitos de Qualidade

Quanto mais rígidos forem os requisitos de qualidade e mais complexo for o software a ser desenvolvido, aumenta-se a necessidade de se aplicar teorias e ferramentas que garantam que esses requisitos sejam satisfeitos. A **Norma ISO** (*The International Organization for Standardization*) / **IEC** (*The International Electrotechnical Commission*) **9126** define seis características de qualidade de software que devem ser avaliadas:

- **Funcionalidade:** capacidade de um software em fornecer funcionalidades que atendam às necessidades explícitas e implícitas dos usuários, dentro de um determinado contexto de uso.
- **Usabilidade:** conjunto de atributos que evidenciam o esforço necessário para a utilização do software.
- **Confiabilidade:** indica a capacidade do software em manter seu nível de desempenho sob determinadas condições durante um período de tempo estabelecido.
- **Eficiência:** indica que o tempo de execução e os recursos envolvidos são compatíveis com o nível de desempenho de software.
- **Manutenibilidade:** conjunto de atributos que evidenciam o esforço necessário para fazer modificações especificadas no software, incluindo tanto as melhorias/extensões de funcionalidades quanto as correções de defeitos, falhas ou erros.
- **Portabilidade:** indica a capacidade do software em ser transferido de um ambiente para outro.

# Engenharia de Requisitos

É um processo que envolve todas as atividades necessárias para a criação e manutenção de um documento de requisitos de software. Existem quatro atividades genéricas do processo de engenharia de requisitos que são de alto nível:

1. O estudo de viabilidade do sistema;
2. O levantamento e análise de requisitos;
3. A especificação de requisitos e sua documentação;
4. A validação desses requisitos.

![Processo de engenharia de requisitos](3-Processo-Engenharia-Requisitos.jpg)

Processo de engenharia de requisitos

A figura acima demonstra as atividades de engenharia de requisitos básicas, porém é importante pontuar que em praticamente todos os sistemas:

1. Os requisitos se modificam;
2. As pessoas interessadas desenvolvem uma melhor compreensão do que elas querem que o software faça;
3. A organização compradora do sistema sofre modificações;
4. São feitas alterações no hardware, no software e no ambiente organizacional do sistema.

## Estudo de Viabilidade

Para todos os sistemas novos, o processo de engenharia de requisitos de sistemas deve ser iniciado com um estudo de viabilidade ou licitação de requisitos. Um estudo sobre descrição geral do sistema e de como ele será utilizado dentro de uma organização. O resultado desse estudo deve ser um relatório que recomenda a viabilidade, ou não, do processo de realização do processo de engenharia de requisitos e processo de desenvolvimento de sistemas.

Um estudo de viabilidade é rápido, direcionado e destinado a responder a algumas perguntas:

1. O sistema contribui para os objetivos gerais da organização?
2. O sistema pode ser implementado com a utilização da tecnologia atual dentro das restrições de custo e prazo?
3. O sistema pode ser integrado com os outros sistemas já em operação?

Preparar um estudo de viabilidade envolve avaliar e coletar informações. Alguns exemplos das perguntas que devem ser feitas:

1. Como a organização se comportaria se esse sistema não fosse implementado?
2. Quais são os problemas com os processos atuais e como um novo sistema ajudaria a diminuir esses problemas?
3. Que contribuição direta o sistema trará para os objetivos da empresa?
4. As informações podem ser transferidas para outros sistemas organizacionais e podem ser recebidas a partir deles?
5. O sistema requer alguma tecnologia que já não tenha sido utilizada na organização?
6. O que precisa e o que não precisa ser compatível com o sistema?

Entre as fontes de informação estão os *stakeholders* (gerentes de departamentos, engenheiros de software, peritos em tecnologia, usuários finais do sistema, entre outros).

## Levantamento e Análise de Requisitos

Nessa atividade, os membros da equipe técnica de desenvolvimento de software trabalham com o cliente e os usuários finais do sistema para descobrir mais informações sobre o domínio da aplicação, quais serviços o sistema deve fornecer, o desempenho exigido do sistema, as restrições de hardware e assim por diante.

O levantamento e a análise de requisitos podem envolver diferentes tipos de pessoas em uma organização. Esse processo pode enfrentar as possíveis dificuldades:

1. Exceto em termos gerais, os *stakeholder* não costumam saber o que querem de um sistema, não tendo conhecimento do que é viável ou não, podem fazer exigências inviáveis.
2. *Stakeholder* expressam requisitos nos seus próprios termos e com conhecimento implícito de seu próprio trabalho. Engenheiros de requisitos podem não entender esses requisitos.
3. Diferentes *stakeholders* têm requisitos diferentes e podem expressar essas diferenças de várias maneiras. Engenheiros de requisitos precisam descobrir todas as potenciais fontes de requisitos e descobrir as semelhanças e conflitos. 
4. Fatores políticos podem influenciar os requisitos de um sistema. Os gerentes podem exigir requisitos específicos, porque estes lhes permitirão aumentar sua influência na organização.
5. O ambiente econômico e empresarial no qual a análise ocorre é dinâmico. A importância dos requisitos específicos pode mudar e novos requisitos podem surgir a partir de novos *stakeholder* que não foram inicialmente consultados. 

## Entrevista

As entrevistas formais ou informais com os *stakeholders*, são a fonte mais importante para o levantamento dos requisitos.

A sumarização durante e no final da entrevista é necessária, primeiro, para garantir que toda informação apresentada foi anotada e, segundo que foi corretamente entendida.

Antes de tentar uma entrevista, o engenheiro de software deve prepará-la, algumas dicas a serem seguidas para que haja tal preparação:

1. **Comece por definir os objetivos:** verifique a documentação formal e desenvolva um esquema do sistema existente ou proposto. Identifique questões, partes omitidas e ambíguas. 
2. **Selecionar a pessoa ou grupo a ser entrevistado:** Podemos encontrar a melhor pessoa para responder sobre o assunto, a partir do organograma, analisando o fluxo de trabalho ou uma lista de distribuição de relatórios. 
3. **Ler a documentação relevante:** conheça a posição e as responsabilidades do entrevistado, bem como os procedimentos e os documentos relevantes.
4. **Prepare questões específicas:** selecione questões específicas que podem ser respondidas. 

A **entrevista** é composta por três partes: 

1. **Abertura:** o objetivo-chave é estabelecer (concordância), começando pela identificação, apresentando o tópico pretendido e o propósito da entrevista.
2. **Corpo:** nessa fase o engenheiro de software deve:
    1. Mostrar que conhece as responsabilidades e deveres do trabalho do entrevistado.
    2. Ter conhecimento das decisões que o entrevistado toma (quais são, como são tomadas, quais informações necessárias e se são satisfatórias, qual o tempo necessário para tomada de decisão)
    3. Procurar respostas quantitativas.
    4. Pedir ideias, sugestões e exemplos.
3. **Encerramento:** Realizar um sumário de todos os pontos principais.

 Além disso vários pontos devem ser aprendidos e esclarecidos na entrevista:

1. Organização da empresa (ambiente de trabalho): Como é organizado o pessoal?
2. Os objetivos e exigências do sistema (declarados nos manuais de procedimentos) devem ser reafirmados e esclarecidos na entrevista: avaliar se os objetivos e exigências declarados nos manuais, são os mesmos que os representantes enxergam na execução de suas tarefas.
3. Fluxo funcional: para cada função importante, é necessário determinar as etapas exigidas e descrever o significado delas.
4. Exigências de recursos: determinar quais são os recursos aplicados pela organização para executar o trabalho. Quais são os recursos humanos (treinamento especializado, experiência exigida) equipamento e material necessário. 
5. Relação de tempo: como o trabalho executado se relaciona com períodos específicos do ano ou outros ciclos comerciais. Existe pico? Qual é o atual volume de trabalho?
6. Formulários, procedimentos e relatórios: quais são utilizados? Inclua um exemplo de cada formulário.
7. Funções desejáveis e não existentes: registre a opinião das pessoas sobre o sistema, como ele existe e como poderia ser. Atribua atenção para as opiniões mais subjetivas do que as objetivas.
8. Flexibilidade dos procedimentos.
9. Capacidade: o sistema atual consegue manipular volumes maiores do que aqueles que resultam do crescimento normal?

## Especificação de Requisitos

O produto do levantamento de requisitos é o documento de requisitos ou especificação de requisitos, o qual declara os diversos tipos de requisitos do sistema.

## Validação de Requisitos

A validação de requisitos tem, como objetivo, mostrar que os requisitos realmente definem o sistema que o cliente deseja. A validação deve se ocupar da elaboração de um esboço completo do documento de requisitos. É importante, pois a ocorrência de erros em um documento de requisitos pode acarretar em grande custo relacionado ao retrabalho.

É proposto que diferentes tipos de verificação devam ser realizados sobre os requisitos:

1. **Verificações de validade:** um usuário pode considerar que um sistema é necessário para realizar certas funções. No entanto, mais estudos e análises podem identificar funções adicionais ou diferentes as quais são exigidas, a solução é conciliar entre a comunidade de usuários.
2. **Verificações de consistência:** os requisitos, em um documento, não devem ser conflitantes, não devendo existir descrições diferentes para uma mesma função do sistema.
3. **Verificações de completeza:** o documento de requisitos deve incluir os requisitos que definam todas as funções e restrições exigidas pelos usuários do sistema.
4. **Verificação de realismo:** utilizando o conhecimento acerca da tecnologia existente, os requisitos devem ser verificados, a fim de assegurar que eles realmente podem ser implementados, levando-se em consideração o orçamento e os prazos para o desenvolvimento do sistema.
5. **Facilidade de verificação:** para diminuir as possíveis divergências entre cliente e fornecedor, os requisitos do sistema devem sempre ser escritos de modo que possam ser verificados.

A seguir algumas **técnicas de validação** de requisitos que podem ser utilizadas em conjunto ou individualmente:

1. **Revisões de requisitos:** os requisitos são analisados sistematicamente por uma equipe de revisores, a fim de eliminar erros e inconsistências.
2. **Prototipação:** um modelo executável do sistema é mostrado aos usuários finais e clientes, possibilitando que eles experimentem o modelo para verificar se atende às necessidades.
3. **Geração de casos de teste:** como modelo ideal, os requisitos deveriam ser testáveis. Se os testes criados como parte do processo de validação revelam problemas com os requisitos ou, até mesmo, se o teste é difícil ou impossível de ser projetado, significa que os requisitos serão de difícil implementação e talvez devam ser reconsiderados. 

---
