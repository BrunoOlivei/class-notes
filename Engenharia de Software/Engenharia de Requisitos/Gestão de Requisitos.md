# Introdução

A construção de um sistema não é algo físico, não é palpável, não é como construir uma casa, ou um computador, exige interpretação, envolve dedução. Pesquisas e estudos indicam como principal fator pelas falhas em projetos o inadequado gerenciamento de requisito.

Gerenciamento de requisitos deve iniciar durante o levantamento dos requisitos, ali as políticas de gestão dos requisitos devem ser definidas, considerando as características e necessidades do sistema a ser desenvolvido, permanecer ativo durante todo o ciclo de vida de um produto de software e perpertuar-se na fase de manutenção.

O PMI apresenta pesquisas demonstrando que, dos projetos que fracassam, 47% deles têm como causa base uma gestão de requisitos mal feita.

O primeiro passo é definir quais são os objetivos e criar políticas de identificação, controle e rastreamento das informações necessárias para atingi-los.

A gestão de requisitos começa com a identificação, um atributo responsável por identificar cada requisito de forma única. Tabelas de rastreamento podem ser desenvolvidas os relacionamentos com um ou mais aspectos do sistema ou seu ambiente.

---

# Evolução dos Requisitos

Requisitos mudam, essa é uma certeza no desenvolvimento de software. A evolução é uma característica inerente aos sistemas computacionais. 

Alterações no macrosistema afetam os sistemas de software, que ou evoluem para se adaptarem ou se tornarão inúteis. Outros fatores de mudanças são:

- Especificações mal descritas ou erradas de requisitos,
- Mais conhecimento adquirido pelo cliente ou usuário com o decorrer do projeto
- Mudanças de prioridade do cliente
- Mudança de tecnologia
- Mudança de leis, políticas e processos internos ou externos a organização vinculada ao projeto.

Ainda, existem duas classificações de requisitos a partir da perspectiva evolutiva:

- Requisitos permanentes: são os requisitos criados a partir do domínio da aplicação, são relativamente estáveis, mudam mais lentamente.
- Requisitos voláteis: são requisitos que irão mudar durante o tempo de desenvolvimento do sistema, provavelmente, depois, quando já estiverem em operação.
    - Mutáveis: são os requisitos que se modificam devido às mudanças no ambiente em que a organização está inserida.
    - Emergentes: são os requisitos que surgem conforme a compreensão do cliente referente ao sistema evolui e/ou requisitos que o processo do projeto revela.
    - Consequentes: são os requisitos que surgem após a inserção do sistema na organização. São as solicitações de adaptações ou criação de novas rotinas desencadeadas pelo uso do sistema até sua perfeita adaptação às rotinas da organização.
    - Compatibilidade: são os requisitos que dependem de outro sistema, equipamento ou processo. Conforme esse sistema, equipamento ou processo evoluem os requisitos também mudam.

---

# Rastreabilidade

Gerir requisitos é o primeiro passo para um processo de desenvolvimento de software maduro e que garanta um produto final de qualidade.

Um processo de controle de mudanças conciso e um atributo de rastreabilidade bem definido, são aspectos fundamentais para um gerenciamento de requisitos bem executado.

Rastreabilidade pode ser definida como o conjunto de ligações entre os requisitos, com as fontes dos requisitos, com eles mesmos e com outros artefatos.

A condição de rastreamento deve ser atribuída ao requisito no momento do seu levantamento e ela deverá refletir a facilidade de se encontrar os requisitos relacionados. Existem três tipos de rastreabilidade:

1. Por stakeholder: vincula o requisito ao stakeholder que propôs.
2. Requisitos dependentes: quando o requisito é vinculado a outro requisito na sua concepção, essa informação pode ser utilizada para avaliar quantos requisitos serão afetados pela mudança proposta e a extensão das mudanças consequentes dela que serão necessárias.
3. Modelos de projeto: vincula o requisito ao modelo de projeto onde foi implementado. 

Para acompanhar e descrever a vida de um sistema são utilizadas matrizes de rastreabilidade que podem ser implementadas através de uma ferramenta simples, como um editor de textos ou uma planilha eletrônica.

![23 — Exemplo de Matriz de Rastreabilidade por Requisito e Caso de Teste](23-exemplo-matriz-rastreabilidade.png)

23 — Exemplo de Matriz de Rastreabilidade por Requisito e Caso de Teste

A matriz deverá ser preenchida com os requisitos, expressos em linguagem natural e numerados sequencialmente. As colunas subsequentes representam os documentos gerados durante o desenvolvimento do software.

![26 — Exemplo de Matriz de Rastreabilidade por Requisitos Funcionais e Não Funcionais](26-matriz-rastreabilidade-requisitos.png)

26 — Exemplo de Matriz de Rastreabilidade por Requisitos Funcionais e Não Funcionais

Alguns exemplos de matriz de rastreabilidade:

- Rastreamento das fontes de requisitos (relaciona o requisito, stakeholders e documento de requisito).
- Rastreamento da razão dos requisitos (relaciona o requisito com a descrição do porquê o requisito foi especificado).
- Rastreamento requisitos-requisitos (relaciona requisitos com outros requisitos que são dependentes uns dos outros).
- Rastreamento requisitos-arquitetura (relaciona os requisitos com os sub-sistemas onde foram implementados).
- Rastreamento requisitos-projeto (relaciona os requisitos com o hardware específico ou componentes de software que são usados para implementá-los)
- Rastreamento requisitos-interface (relaciona os requisitos com a interface do sistema que será usada para apresentar os requisitos).

Vários caminhos de rastreamento são possíveis:

- Rastreamento Backward-From: vincula requisitos a suas fontes em outros documentos ou stakeholders.
- Rastreamento Forward-From: vincula requisitos ao projeto e componentes de implementação.
- Rastreamento Backward-To: vincula o projeto e os componentes de implementação aos requisitos.
- Rastreamento Forward-To: vincula outros documentos (que possam ter precedido o documento de requisitos) aos requisitos relevantes.

Existem, no mercado, várias ferramentas para o gerenciamento de requisitos, proprietárias e livres. Por exemplo: IBM Rational, EasyRM Version 1.06, Caliber, DotProject e outros.

Para sistemas de pequeno porte, geralmente, o rastreamento é suportado por ferramentas simples, como processadores de texto e planilhas de cálculo.

---