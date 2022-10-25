# Introdução

A partir do documento de requisitos, realizamos a modelagem de um sistema, esse sendo o processo de elaboração de modelos abstratos de um sistema. 

É representada através de um diagrama, em que cada um desses modelos apresenta uma visão ou perspectiva diferente do sistema, são normalmente elaborados utilizando uma notação gráfica.

Um dos meios é a UML, os diagramas UML auxiliam os desenvolvedores de ‘software’ a construírem o ‘software’.

A versão 2.0 da UML, define treze categorias de diagramas para uso de modelagem de ‘software’, um dos principais é o **diagrama de casos de uso**, o qual ajuda a determinar a funcionalidade e as características do sistema do ponto de vista do usuário, além de ser um dos diagramas mais gerais e informais da UML. Deve ser utilizada uma linguagem simples e de fácil acesso. 

Este diagrama (Diagrama de casos de uso) é muito importante e um dos mais utilizados da UML, pois serve de apoio para a construção de grande parte de outros diagramas. 

# Introdução à UML

A UML (*Unified Modeling Language*) ou Linguagem de Modelagem Unificada) é uma linguagem-padrão para a elaboração da estrutura de projetos de ‘software’. Pode ser utilizada para **visualização**, **especificação**, **construção** e **documentação** de artefatos que usem sistemas complexos de ‘software’, por meio do paradigma de orientação a objetos.

<aside>
📌 Linguagem de representação de um modelo para especificação de sistemas.

</aside>

Pode ser utilizado para diversas categorias de sistemas. Exemplo:

- Sistemas de informação;
- ‘Software’ embutido;
- Aplicação mobile;
- Entre outros.

UML **é uma linguagem de modelagem** que tem, como meta, auxiliar os engenheiros de ‘software’ a definirem as características do ‘software’, como seus requisitos, comportamentos, estrutura lógica, dinâmica de seus processos, necessidades físicas em relação ao equipamento em que o sistema deverá ser implantado. É independente do ‘software’ e pode ser utilizada em qualquer modelo de processo de ‘software’.

A notação UML é independente de processo de ‘software’, visto que pode ser utilizada em modelo cascata, desenvolvimento evolucionário, ou qualquer outro processo que esteja sendo utilizado para o desenvolvimento de ‘software’. Utiliza diversos **símbolos gráficos**, existindo uma semântica bem definida para cada um deles, o que permite elaborar diversos modelos. No entanto, ela não se limita à modelagem de ‘software’, dado que pode modelar sistemas, tais como fluxo de trabalho no sistema legal, a estrutura e o comportamento de sistemas de saúde e o projeto de equipamento físico.

## Ferramentas CASE Baseadas na Linguagem UML

As ferramentas CASE (*Computer-Aided Software Enfineering* — Engenharia de Software Auxiliada por Computador) são ‘softwares’ que, de alguma forma, colaboram para a realização de uma ou de mais atividades realizadas durante o processo de desenvolvimento de sistemas, como a engenharia de requisitos, o projeto, o desenvolvimento de programa e os testes. As ferramentas CASE podem incluir editores de projeto, dicionários de dados, compiladores, depuradores, ferramentas de construção de sistemas entre outros. 

<aside>
📌 São ferramentas que auxiliam na automatização de alguma técnica da engenharia de ‘software’.

</aside>

Exemplos de ferramentas de modelagem:

- Rational Rose;
- Astah Professional;
- Visual Paradgm for UML;
- Enterprise Architect.

Alguns exemplos de atividades que podem ser automatizadas utilizando a CASE:

1. Desenvolvimento de modelos gráficos de sistemas
2. A compreensão de um projeto utilizando um dicionário de dados que carrega informações sobre as entidades e sua relação em um projeto;
3. A geração de ‘interfaces’ com usuário;
4. Depuração de programas pelo fornecimento de informações sobre um programa em execução;
5. A tradução automatizada de programa a partir de uma antiga versão de uma linguagem de programação.

# Ferramentas CASE

Como a engenharia de requisitos, o projeto, o desenvolvimento de programa e os testes. Podem incluir editores de projeto, dicionários de dados, compiladores, depuradores, ferramentas de construção de sistemas e entre outros. 

Alguns exemplos de atividades que podem ser automatizadas utilizando a CASE:

1. O desenvolvimento de modelos gráficos de sistema;
2. A compreensão de um projeto utilizando um dicionário de dados que carrega informações sobre as entidades e sua relação em um projeto;
3. A geração de ‘interfaces’ com usuários;
4. A depuração de programas;
5. A tradução automatizada de programas a partir de uma antiga versão de uma linguagem de programação.

Existem basicamente, duas formas de classificação geral para as ferramentas CASE. A primeira delas divide-se em:

- ***Upper* CASE ou U-CASE ou *Front-End*:** são ferramentas que estão voltadas para as primeiras fases do processo de desenvolvimento de sistemas, como a análise de requisitos, projeto lógico e documentação.
- ***Lower* CASE ou L-CASE ou *Back-End*:** oferecem suporte nas últimas fases do desenvolvimento, como a codificação, os testes e a manutenção.
- ***Integrated*** **CASE ou I-CASE:** além de englobar as características das *Upper* e *Lower* CASE's, ainda oferecem outras características, como controle de versão, por exemplo. Somente são utilizadas em projetos de desenvolvimento muito grandes.
- ***Best in Class*** **ou Kit de Ferramenta**: assemelha-se às I-CASE, os ‘kits’ de ferramenta também acompanham todo o ciclo de desenvolvimento. Entretanto, possuem a propriedade de conjugar sua capacidade a outras ferramentas externas complementares, as quais viriam conforme as necessidades do usuário. São mais usadas para desenvolvimento corporativo, apresentando controle de acesso, versão, repositórios de dados, entre outras características.

A segunda forma divide as ferramentas CASE em orientadas a função e orientadas a atividade:

- **Orientadas a função:** seriam as *Upper* CASE e *Lower* CASE. Baseiam-se na funcionalidade das ferramentas.
- **Orientadas a atividade:** seriam as *Best in Class* e as I-CASE, as quais processam atividades, tais como especificações, modelagem e implementação.

# Modelagem de Sistemas

Processo de desenvolvimento de modelos abstratos de um sistema, em que cada modelo apresenta uma visão ou perspectiva, diferente do sistema.

Os modelos são usados durante o processo de engenharia de requisitos para **ajudar a extrair os requisitos do sistema durante o processo de projeto.**

**Modelagem de sistemas**, é a atividade de construção de modelo que expliquem/ilustrem a forma de funcionamento de um ‘software’.

Os modelos podem ser aproveitados em todas as atividades da engenharia de software, desde a modelagem da interface até a modelagem de banco de dados, além de servir como a documentação do sistema. 

Com a modelagem alcançamos alguns objetivos:

- Os modelos ajudam a visualizar o sistema como ele é ou como desejamos que seja;
- Os modelos permitem especificar a estrutura ou o **comportamento de um sistema,** por exemplo, uma tela de clientes, quais comportamentos teremos nessa tela, exclusão, visualização, alteração, pesquisa, etc.;
- Os modelos proporcionam **um guia para a construção** **do sistema,** principalmente para a fase de implementação, incluindo até a fase de manutenção**;**
- Os modelos documentam o sistema

<aside>
⚠️ Construímos modelos para compreender melhor o que estamos desenvolvendo.

</aside>

Modelagem visual significa modelar com a utilização de notações padrão, a UML é a linguagem padrão mais popular no momento, utilizada para:

- Visualização
- Especificar
- Construção de modelos e diagramas
- Documentação

Um modelo pode ser entendido como uma representação idealizada de um sistema a ser construído. 

A modelagem de sistemas de ‘software’ baseia-se na utilização de notações gráficas e textuais com o objetivo de construir modelos que representem as partes essenciais de um sistema. Algumas das razões para se utilizar modelos na construção de sistemas.

1. No desenvolvimento do ‘software’, usamos desenhos gráficos denominados diagramas, de modo a representar o comportamento do sistema. Esses diagramas seguem um padrão lógico e possuem uma série de elementos gráficos que carregam um significado pré-definido.
2. Adiciona informações em forma de texto, com o objetivo de explicar ou definis certas partes. A modelagem de um sistema em forma de diagrama, em conjunto com a informação textual, forma a documentação de um sistema de ‘software’.
3. O rápido crescimento da capacidade computacional das máquinas resultou na demanda por sistemas de software cada vez mais complexos e que tirassem aproveito de tal capacidade, gerando a necessidade de reavaliação na forma de desenvolver sistemas, as técnicas para a construção de sistemas têm evoluído para suprir as necessidades do desenvolvimento de software.

Os modelos construídos na fase de análise devem ser cuidadosamente validados e verificados. O objetivo da validação é o de assegurar que as necessidades do cliente estão sendo atendidas sendo apresentado os modelos criados para representar o sistema aos futuros usuários.

A verificação objetiva analisar se os modelos construídos estão em conformidade com os requisitos definidos, sendo analisadas a exatidão de cada modelo, separadamente, bem como a consistência entre os modelos.

# Diagrama de Casos de Uso

O diagrama de casos de uso (*use case diagram*) é um diagrama UML abstrato, flexível e informal, utilizado no início da modelagem do sistema, a partir do documento de requisitos, podendo ser modificado durante o processo de engenharia, além de servir de base para a modelagem de outros diagramas. 

Seu principal objetivo é modelar as funcionalidades e serviços oferecidos pelo sistema, ou seja, o comportamento e as funções que o sistema executará, utilizando linguagem simples, demonstrar o comportamento externo do sistema a partir da perspectiva do usuário, incorporando o conjunto de requisitos funcionais. Os requisitos não funcionais não aparecem no diagrama de casos de uso, pois não constituem o foco da modelagem.

O diagrama de casos de uso é composto por atores, casos de uso e seus relacionamentos. 

<aside>
📌 IMPORTANTE:
Ter uma clara visão de como as telas do sistema serão, para se ter uma boa ideia de como serão as funcionalidades do sistema.
Os Use Cases serão reflexo das funcionalidades do sistema, e na grande maioria das vezes serão representados em uma tela.

</aside>

## Atores

Um ator representa um papel que um ser humano, um dispositivo de 'hardware' ou até mesmo outro sistema, ou seja, qualquer elemento externo que interaja com o ‘software’. O nome do ator identifica qual é o papel assumido por ele no diagrama. Um estudo de caso de uso é sempre iniciado por um estímulo de um ator, podendo outros atores participar também. 

![4-atores.jpg](4-atores.jpg)

## Casos de Uso

Um caso de uso especifica o comportamento de um sistema ou de parte de um, referindo-se a serviços, tarefas ou funções que podem ser utilizadas de alguma maneira pelos usuários do sistema, como cadastrar funcionário, por exemplo.

<aside>
📌 Representados na forma de elipses com texto interno, descrevendo a que serviço/tarefa/função o caso de uso se refere, o texto é utilizado um verbo + substantivo (indicando ação) como nome do caso de uso. Exemplo: abrir conta, comprar produtos, efetuar login.

</aside>

É indicado que cada caso de uso seja documentado, demonstrando qual é o comportamento pretendido para o caso de uso em questão e quais funções ele executará quando for solicitado, conforme o documento de requisitos. 

![14-exemplo-relacionamento.jpg](14-exemplo-relacionamento.jpg)

## Relacionamento entre Casos de Uso e Atores

Os casos de uso representam conjuntos bem definidos de funcionalidades do sistema, os quais precisam se relacionar com outros casos de uso e com atores que enviaram e receberam mensagens deles. Podemos ter os relacionamentos de **associação, generalização, extensão e inclusão**: 

Os relacionamentos de casos de uso de extensão e inclusão, são chamados esteriótipos. 

- Para relacionamentos entre atores e casos de uso: somente associação.
- Para relacionamentos de atores entre si: somente generalização
- Para relacionamentos de casos de uso entre si: generalização, extensão e inclusão.

### Associação

A associação é o único relacionamento possível entre ator e caso de uso e sempre é binária, ou seja, envolve apenas dois elementos, a comunicação através de envio e recebimento de mensagens. 

Um relacionamento de associação demonstra que o ator utiliza a funcionalidade representada pelo caso de uso. É representado por uma reta ligando o ator ao caso de uso e vice-versa, podendo conter uma seta na extremidade, a depender do fluxo de informação.

![5-associação.jpg](5-associao.jpg)

![6-associação.jpg](6-associao.jpg)

![7-associação.jpg](7-associao.jpg)

### Generalização

Generalização entre casos de uso pode ocorrer quando existirem dois ou mais casos de usos com características semelhantes, apresentando pequenas diferenças entre si.

Quando isso acontece, define-se um caso de uso geral, o qual deverá possuir as características compartilhadas por todos os casos de uso em questão. Toda a estrutura de um caso de uso generalizado é herdada pelos casos de uso especializados, incluindo quaisquer possíveis associações que o caso de uso generalizado possua. A associação é representada por uma reta com uma seta mais grossa, partindo dos casos de uso especializado até atingir o caso de uso geral.

![8-generalização.jpg](8-generalizao.jpg)

Em um banco existem três opções de abertura de contas: abertura de conta comum, de conta especial e de conta poupança, cada uma representada por um caso de uso diferente.

As aberturas de conta especial e de conta poupança possuem todas as características e requisitos da abertura de conta comum, mas cada uma delas possui algumas características e requisitos próprios, o que justifica elencá-las como especializações do caso de uso abertura de conta comum, detalhando-se as particularidades de cada caso de uso especializado em sua própria documentação

O relacionamento de generalização também pode ser aplicado entre atores. 

![9-generalização.jpg](9-generalizao.jpg)

### Inclusão

Essa categoria de relacionamento é possível somente entre casos de uso sendo utilizado quando existem ações comuns a mais de um caso de uso. Quando isso ocorre, a documentação dessas ações é colocada em um caso de uso específico, permitindo que outros casos se utilizem dessas ações, evitando a descrição de uma mesma sequência de passos em vários casos de uso.

Um relacionamento de inclusão entre casos de uso significa que o caso de uso base incorpora explicitamente o comportamento de outro.

O relacionamento de inclusão pode ser comparado com a chamada sub-rotina. Portanto, indica uma obrigatoriedade, ou seja, quando um caso de uso base possui um relacionamento de inclusão com outro caso de uso, a execução do primeiro obriga, também, a execução do segundo.

A representação é feita através de uma reta tracejada que contém uma seta em uma de suas extremidades rotulada com a palavra-chave <<include>>. A seta deve sempre apontar para o caso de uso a ser incluído.

<aside>
📌 Exemplo: Quando um caso de uso A possui relacionamento de inclusão com outro caso de uso B, a execução de A implica na execução de B.

</aside>

![10-inclusão.jpg](10-incluso.jpg)

Sempre que um saque ou depósito ocorrer, ele deve ser registrado para fins de histórico bancário. Como as rotinas para registro de um saque ou um depósito são extremamente semelhantes, colocou-se a rotina de registro em um caso de uso à parte, chamado registro movimento, que será executado, obrigatoriamente, sempre que os casos de uso como realizar depósito ou saque forem executados. Assim, só é preciso descrever os passos para registrar um movimento no caso de uso incluído.

![11-inclusão.jpg](11-incluso.jpg)

### Extensão

O relacionamento de extensão também é possível somente entre casos de uso sendo utilizado para modelar as rotinas opcionais de um sistema que ocorrerão somente se uma determinada condição for satisfeita.

As associações de extensão possuem uma representação muito semelhante à das associações de inclusão, as quais também são representadas por uma reta tracejada, diferenciando-se por possuir um estereótipo com o texto “<<extend>>” e pelo fato de que a seta aponta para o caso de uso que estende, ou seja, nesse caso, a seta aponta para o caso de uso base.

<aside>
📌 Extensão: relacionamento com outro caso de uso que pode ou não ser executado.

</aside>

![12-extensão.jpg](12-extenso.jpg)

![15-restrição-associação-extenção.jpg](15-restrio-associao-exteno.jpg)

### Resumo de relacionamento entre caso de uso e ator

![13-relacionamento.jpg](13-relacionamento.jpg)

Considerando que, estamos trabalhando com um sistema que irá controlar o acesso dos usuários a diversos programas.

Na tela de cadastro de módulo, há opções de pesquisa, cadastro e alteração de dados de módulos. 

### Extend

Na tela de `Consulta de Programas` temos um botão chamado NOVO que pode ser usado para cadastrar novos programas. Nesse caso, podemos entrar na `Consulta de Programas`, executar uma pesquisa e sair. A opção de NOVO nesse caso é somente uma opção, não sendo obrigatória aplica-se o esteriótipo **<<*extend*>>**.

Ainda na tela de `Consulta de Programa`, temos a opção de consultar os módulos cadastrados, porém ao executar esta opção a tela de `Cadastro de Módulo` é aberta, disponibilizando então as opções de consulta, cadastro e alteração de módulos. Assim a `Consulta de Programa` pode **estender** para a tela de `Cadastro de Módulo`. 

### Include

No momento de cadastro de um novo programa, é exigido que se informe a qual módulo ela pertence. Nesse caso ao cadastrar o programa, o usuário será levado a tela `Consulta de Módulo` para poder selecionar a qual módulo o programa que está sendo cadastrado fará parte, assim o esteriótipo de inclusão se aplica. 

![54-aula-vivo-05.png](54-aula-vivo-05.png)

<aside>
📌 Toda chamada a uma determinada funcionalidade em que esta for obrigatória, o esteriótipo usado é o de inclusão <<include>>, quando não há obrigatoriedade o esteriótipo é de extensão <<extend>>.

</aside>

<aside>
⚠️ Os esteriótipos <<include>> e <<extend>> ocorrem apenas entre casos de uso.

</aside>

---

# Conceitos Básicos de Orientação a Objeto

A UML é totalmente baseada no paradigma de Orientação a Objetos (OO).

## Objetos

Um objeto é qualquer coisa, em forma concreta ou abstrata, que exista física ou apenas conceitualmente no mundo real, em que se pode individualizá-la por possuir comportamentos e características próprias. São exemplos de objetos: cliente, professor, carteira, caneta, carro, disciplina, curso, caixa de diálogo, etc. Além disso, os objetos possuem características e comportamentos. 

![21-exemplos-objetos.jpg](21-exemplos-objetos.jpg)

          Objetos concretos

         Objetos abstratos

### Abstração

Abstraímos quando definimos um objeto conceitual partindo de **objetos** do mundo real com os mesmos comportamentos e características, os quais são classificados como de um mesmo tipo. Ao ter um problema muito grande para resolver, se quebra o problema em pequenas partes, classificando pequenos os pequenos problemas e criando pequenos objetos. 

Exemplo: aviões podem ser desmembrados em diversos tipos de aviões, porém todos possuem a mesma característica, por exemplo, duas asas, duas turbinas, porém divididos em tipos diferentes, aviões de cargas, aviões de guerra, aviões de passageiros, aviões de manobras, etc. 

![22-exemplos-abstração.jpg](22-exemplos-abstrao.jpg)

### Classes

Uma classe é uma abstração de um conjunto de objetos que possuem as mesmas características e comportamentos, sendo representada por um retângulo que pode ter até três divisões. A primeira divisão armazena o nome da classe; a segunda, os atributos (características, enquanto a terceira carrega os métodos. 

> É a abstração de algo que exista de forma concreta ou conceitualmente no mundo real.
> 

![16-exemplo-classe.jpg](16-exemplo-classe.jpg)

É possível encontrar classes que contenham apenas uma dessas características ou até mesmo nenhuma, quando se trata de classes abstratas.

O momento inicial para a identificação de classes em um documento de requisitos é assinalar os substantivos. Substantivos podem representar objetos físicos (livros, cliente, computador) ou objetos conceituais (reserva, cronograma, norma). Em seguida, é preciso identificar somente os objetos que possuem importância para o sistema, verificando o que realmente consiste em ser objeto e o que consiste em ser atributo. Também é preciso fazer uma nova análise dos requisitos para identificar as classes implícitas no contexto trabalhado, excluir classes parecidas ou juntar duas classes em uma única classe.

### Instância

Criação de objeto baseado no modelo, através das características declaradas.   

### **Atributos**

Atributos representam as suas características e informações, as quais costumam variar de objeto para objeto, como nome de um objeto da classe cliente ou a cor em um objeto da classe carro, por exemplo. Tais aspectos são os responsáveis por diferenciar um objeto de outro da mesma classe.

Cada atributo deve possuir um nome e, eventualmente, o tipo de dado que armazena, por exemplo, *intefer*, *float* ou *char*.

Em relação ao objeto, este corresponde a uma instância de uma classe em um determinado momento.

![17-atributos-classe.jpg](17-atributos-classe.jpg)

Ao instanciar um objeto da classe criada, devemos informar os valores para cata atributo da classe, por exemplo nome: Márcia, sexo: feminino, data_nascimento: 22/03/1969. Dessa forma trabalhamos com as instâncias (objetos) de uma classe, pois os valores de cada atributo são carregados nas instâncias (objetos).

### **Métodos**

São processos ou serviços realizados por uma classe, devem ficar armazenados na terceira divisão da classe. Os métodos são as atividades que uma instância de uma classe pode executar.

Um método pode receber, ou não, parâmetros (valores utilizados durante a execução do método), bem como pode, também, retornar valores, os quais podem representar o resultado da operação executada ou somente indicar se o processo foi concluído com sucesso. 

Um método representa um conjunto de instruções executadas quando o método é chamado. 

![18-metodos-classe.jpg](18-metodos-classe.jpg)

### **Visibilidade**

A visibilidade é um símbolo que antecede um atributo ou método e é utilizada para indicar o seu nível de acessibilidade. Existem basicamente, três modos de visibilidade: **público, protegido e privado.**

- Símbolo de mais **(+)** indica visibilidade **pública**, ou seja, significa que o atributo ou o método pode ser utilizado por objetos de qualquer classe.
- Símbolo de sustenido **(#)** indica que a visibilidade é **protegida**, ou seja, determina que apensas objetos da classe possuidora do atributo ou método ou de suas subclasses podem acessá-lo
- Símbolo de menos **(-)** indica que a visibilidade é **privada**, ou seja, somente os objetos da classe possuidora do atributo ou método poderão utilizá-lo.

### **Herança (Generalização/Especialização)**

A herança permite que as classes de um sistema compartilhem atributos e métodos, otimizando, assim o tempo de desenvolvimento, com a diminuição de linhas de código, facilitando futuras manutenções. A herança (generalização/especialização) acontece entre classes gerais (**superclasses** ou **classes-mãe**) e classes específicas (**subclasses** ou **classes-filha**). 

A herança significa que os objetos da subclasse podem ser utilizados em qualquer local em que a superclasse ocorra, mas não vice-versa. A subclasse herda as propriedades da mãe, ou seja, seus atributos e métodos, bem como pode possuir atributos e métodos próprios, além dos herdados.

Sua representação gráfica na UML é uma linha com um triangulo no final, apontando a classe mãe:

![19-herança.jpg](19-herana.jpg)

### Polimorfismo

O conceito de polimorfismo está associado com a herança, pois trabalha com a redeclaração de métodos previamente herdados por uma classe. Esses métodos, embora parecidos, diferem-se, de alguma forma, da implementação utilizada na superclasse, sendo preciso implementá-los novamente na subclasse.

Polimorfismo é o princípio em que classes devidas (as subclasses) e uma mesma superclasse podem chamar métodos que têm o mesmo nome (ou a mesma assinatura), mas possuem comportamentos diferentes em cada subclasse.

Podem existir dois ou mais métodos com a mesma nomenclatura, diferenciando-se na maneira como foram implementados. O sistema é o responsável por verificar se a classe da instância em questão possui o método declarado nela própria ou se o herda de uma superclasse.

![20-polimorfismo.jpg](20-polimorfismo.jpg)

---