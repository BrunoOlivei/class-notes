# Introdução

A modelagem de sistema é o processo de elaboração de modelos abstratos de um sistema, normalmente representado através de um diagrama. Cada um desses apresenta uma visão ou perspectiva diferente do sistema.

# Diagrama de Classe

Visa permitir a visualização das classes utilizadas pelo sistema e como elas se relacionam, apresentando uma visão estática de como estão organizadas, preocupando apenas em definir sua estrutura lógica. 

Diagrama de Classes serve de apoio para a maioria dos demais diagramas. Define a estrutura das classes identificadas para o sistema, mostrando os atributos e métodos possuídos por cada uma das classes, como se relacionam e trocam informações entre si, além de detalhes de implementação (código), essa estrutura é usada para representar algum objeto real.

- Classe a entidade que representa algo em um mundo real.
- Atributos são as características daquilo que existe no mundo real e se deseja representar.
- Método, também chamado operações, são ações que o objeto pode executar no mundo real.
- Multiplicidade é a quantidade de ocorrências que uma classe tem em relação a outra classe.

## Classe

Descrição de uma coleção de objetos que possuem propriedades semelhantes (atributos, método, associações).

Sua estrutura se dá através de um retângulo, dividido em três partes, a primeira sendo o nome da classe, a segunda os atributos e categoria de dados (inteiro, string, float, etc.) e a terceira os métodos

- **Atributos:** são as informações associadas a um objeto, por exemplo: nome, idade, cor, tamanho, código, endereço, etc.
- **Método:** são as operações que podem ser executadas sobre um objeto, por exemplo: abrir conta, consultar conta, mover, adicionar, extrair, deletar, encerrar, sacar, etc.

## Relacionamentos

As classes colaboram umas com as outras, através de relacionamento. Os relacionamentos possuem:

- Nome: sendo a descrição, geralmente utilizam-se verbos, dada ao relacionamento (ex: faz, tem, possui, etc.);
- Sentido de leitura: que basicamente é determinar quais dados serão lidos de uma determinada classe;
- Multiplicidade: que determinam as restrições dos relacionamentos entre as classes (0..1, 0..*, 1..1, 1..*, *, 2..3, etc.);
- Tipo
    - Associação (que pode ser unária ou binária)
    - Generalização
    - Agregação

## Associação

A associação é um relacionamento que conecta duas ou mais classes, demonstrando a colaboração entre as instâncias de classe. Pode-se também, haver um relacionamento de uma classe com ela mesma e, nesse caso, tem-se uma associação unária ou reflexiva. Representado por uma linha sólida conectando duas classes.

![23-associação](23-associacao.png)

23-associação

## Associação Unária ou Reflexiva

Ocorre quando existe um relacionamento de uma instância de uma classe com instâncias da mesma classe.

![24-associação-reflexiva](24-associacao-reflexiva.png)

24-associação-reflexiva

## Associação Binária

Conecta duas classes através de uma reta que liga uma classe a outra.

![25-associação](25-associacao-binaria.png)

25-associação

## Agregação

Uma agregação pode ocorrer somente entre duas classes. É identificável a partir da notação de uma linha sólida entre duas classes: a classe denominada todo-agregado recebe um diamante vazio, enquanto a outra ponta da linha é ligada à classe chamada parte-constituinte. Ambas as classes podem "viver" de forma independente, mas ambas são parte de um único todo. 

<aside>
📌 Informa que uma classe faz parte de outra classe, mas não de forma exclusiva, a classe "todo" vive sem a classe "parte", e vice-versa.

</aside>

Para sabermos se um relacionamento é de agregação, basta questionarmos:

1. **O relacionamento comporta uma estrutura todo-parte?** 
    
    **Exemplo:** em um problema que trata sobre apartamentos e condomínio, cada apartamento possuí um depósito, quando nos referimos ao depósito podemos perguntar a qual apartamento ele pertence. 
    
2. **O objeto constituinte-parte "vive" sem o objeto agregado?**
    
    **Exemplo:** Porém, podemos ter a situação em que o proprietário do apartamento e, consequentemente, do depósito tenha vendido o depósito, para alguém que sequer mora no prédio. Assim temos os dois objetos vivendo separadamente. 
    

## Composição

Composição ocorre quando os objetos da classe parte não podem "viver" quando o todo é destruído. Essa categoria de relacionamento é identificável pela notação de uma linha sólida entre duas classes:

<aside>
📌 Informa que a classe faz parte de outra classe de forma exclusiva, não podendo existir sem a dependência.

</aside>

- A classe denominada todo-composta, onde recebe um diamante preenchido;
- A classe denominada parte-componente, que recebe a outra ponta da linha que liga com a classe toda-composta

Ambas as classes "vivem" unidas de uma forma dependente. Os objetos-parte não podem ser destruídos por um objeto diferente do objeto-todo ao qual estão relacionados.

Para sabermos se um relacionamento é de composição, basta questionarmos:

1. É cabido a estrutura todo-parte?
    
    Exemplo: Pensando um prédio com conjunto de apartamentos, nesse domínio de problema, precisamos pensar no prédio como o **todo** e os apartamentos sendo a **parte**.
    
2. O objeto parte "vive" sem o objeto todo?
    
    Exemplo: No caso do condomínio de apartamentos, um apartamento não existe sem o prédio, um endereço (ex. atributo) não existe sem o prédio, afinal o endereço é do prédio o apartamento é apenas um complemento ao endereço. 
    

![26-composição](26-composicao.png)

26-composição

## Generalização/Especialização

A associação identifica as classes-mãe (superclasse), as quais são chamadas gerais, e as classes-filhas (subclasses), as chamadas especializadas, demonstrando a ocorrência de herança e, possivelmente, de métodos polimórficos nas classes especializadas.

![27-generalização](27-generalizacao.png)

27-generalização

## Multiplicidade

A multiplicidade específica o nível de dependência de um objeto e o número mínimo e máximo de instâncias envolvidas em cada uma das extremidades da associação e o nível de dependência de um objeto com os outros. 

Existem situações em que é necessário restringir o número de objetos associados através de uma associação a um objeto determinado (restringir a cardinalidade).

Quando não existe multiplicidade explícita, entende-se que a multiplicidade é "1..1".

Exemplos de multiplicidades:

- `**0..1`: no mínimo zero (nenhum) e no máximo um.**
    
    Indica que os objetos das classes associadas não precisam obrigatoriamente estar relacionadas, mas se houver relacionamento indica que apenas UMA instância da classe se relaciona com as instâncias da outra classe. 
    
- `**1..1`: um e somente um.**
    
    Indica que apenas um objeto da classe se relaciona com os objetos da outra classe. 
    
- `**0..*`: no mínimo nenhum e no máximo muitos.**
    
    Indica que pode ou não haver instância da classe participando do relacionamento. Podendo haver muitos objetos envolvidos.
    
- `***`: muitos**
    
    Indica que muitos objetos da classe estão envolvidos no relacionamento.
    
- `**1..*`: no mínimo 1 e no máximo muitos.**
    
    Indica haver pelo menos UM objeto envolvido no relacionamento, podendo haver muitos objetos envolvidos. 
    
- `**2..5`: no mínimo 2 e no máximo 5.**
    
    Indica que existe pelo menos DUAS instâncias envolvidas no relacionamento e pode ser TRÊS, QUATRO ou CINCO as instâncias envolvidas, mas não mais do que isso. 
    

As associações que possuem multiplicidade do tipo muitos (*), em qualquer de suas extremidades, forçam a transmissão do atributo-chave contido na classe da outra extremidade da associação. Entretanto, esse atributo-chave não aparece desenhado na classe.

## Classe Associativa

Quando um relacionamento possui uma multiplicidade de muitos em ambas extremidades, é necessário criar uma classe associativa para guardar os objetos envolvidos nessa associação. Na classe associativa, são definidos o conjunto de atributos que participam da associação. 

Pelo menos os atributos-chave devem fazer parte da classe associativa, lembrando que esses não são representados no diagrama, enquanto a classe associativa também pode possuir atributos próprios. 

Uma classe associativa é representada por uma reta tracejada que parte do meio da associação e atinge uma classe. 

![28-associação](28-associacao.png)

28-associação

As classes associativas podem ser substituídas por classes normais, que, nesse caso, são chamadas classes intermediárias, mas que desempenham a mesma função das classes associativas. 

![29-associação](29-associacao.png)

29-associação

⬆️ [Retornar ao Índice](https://www.notion.so/Diagramas-de-Sistema-452ca0987bf84125a38ff563c3c38d01)

# Diagrama de Sequência

Procura determinar a sequência de eventos que ocorrem em um determinado processo, identificando quais mensagens devem ser disparadas entre os elementos envolvidos e em que ordem.

Pode ser baseado no diagrama de caso de uso e no diagrama de classes:

- **Diagrama de caso de uso:** cada uso especificado refere-se a um processo disparado por um ator.
- **Diagrama de classe:** as classes contidas nele se tornam objetos no diagrama de sequência.

## Atores

Os atores são usuários ou pessoas do meio externo que possuem algum papel no sistema. Pode ser aproveitado do diagrama de casos de uso, gerando, assim, eventos iniciais dos processos. A representação se dá através de bonecos, contendo uma linha de vida logo abaixo.

![30-atores](30-atores.png)

30-atores

## Linha de vida (lifelines)

Representa o tempo que um objeto existe durante um processo, objeto podendo ser um ator, uma classe, etc. Pode estar, também, ligada a outros objetos e composta por uma instância de uma classe que participa de uma interação. 

Quando é necessário destruir um objeto, a linha da vida é interrompida por um X.

![32-lifeline](31-lifeline.png)

32-lifeline

## Foco de controle ou ativação

Utilizado para representar os momentos ativos em que um objeto está executando um ou mais métodos. Sua representação se dá por uma linha mais grossa sobre a linha pontilhada.

![32-foco-controle](32-foco-controle.png)

32-foco-controle

## Mensagens

Têm o objetivo de mostrar a ocorrência de eventos, normalmente forçando a chamada de um método entre os objetos envolvidos no processo.

![33-mensagens](33-mensagens.png)

33-mensagens

![34-mensagens](34-mensagens.png)

34-mensagens

## Mensagens de Retorno

A função da mensagem de retorno é simbolizar o retorno das informações do método que a solicitou. Pode simbolizar os valores ou se o método foi executado com sucesso ou não. A representação da mensagem de retorno se dá através de uma linha tracejada a qual contém uma ponta fina que aponta para o objeto que recebe o resultado. 

![35-mensagem-retorno](35-mensagem-retorno.png)

35-mensagem-retorno

## Tipos de Mensagens

1. **Mensagens Síncronas**
    
    No momento em que um objeto (chamador) realizar o envio de uma mensagem síncrona, o objeto deverá aguardar que ela seja finalizada para ser continuado o fluxo. A representação é uma flecha com o desenho da ponta preenchido.
    

![36-mensagem-síncrona](36-menssagem-sincrona.png)

36-mensagem-síncrona

1. **Mensagens Assíncronas**
    
    São utilizadas para indicar que a execução ocorre em paralelo aos outros processos e ela poder ter um processamento contínuo. Representada por uma seta tipo "pé de galinha".
    

![37-mensagem-assíncrona](37-mensagem-assincrona.png)

37-mensagem-assíncrona

1. **Autochamadas ou autodelegações**
    
    São mensagens que o objeto envia para si mesmo. Parte da linha da vida e retorna ao próprio objeto.
    

![38-autochamadas](38-autochamadas.png)

38-autochamadas

1. **Estereótipo <<*boundary*>>**
    
    Utilizado para identificação de uma classe que comunica os atores externos e o próprio sistema. O uso de classes *<<boundary>>* é feito quando se quer definir uma ‘interface’ para o sistema. 
    

![39-boundary](39-boundary.png)

39-boundary

1. **Estereótipo <<*control*>>**
    
    Trata-se de uma classe intermediária entre as classes <<*boundary*>> e as demais. Objetivo de realizar uma interpretação de eventos realizados pelo objeto <<*boundary*>>, como ações do mouse e a execução de botões, por exemplo, o que permite retransmitir ações aos demais objetos do sistema. 
    
    ![40-control](40-control.png)
    
    40-control
    

⬆️ [Retornar ao Índice](https://www.notion.so/Diagramas-de-Sistema-452ca0987bf84125a38ff563c3c38d01)

# Diagrama de Máquina de Estados

O diagrama de máquina de estados é um diagrama de comportamentos, usado para especificar o comportamento de vários elementos, seja uma instância de uma classe ou um diagrama de caso de uso, por exemplo.

## Estado

Representa, no diagrama, os momentos em que um componente (objeto) está ou pode vir a estar. Podemos ter um ou vários estados ocorrendo de forma simultânea. Representado na UML por um retângulo.

![41-estado](41-estado.png)

41-estado

### Atividades Internas

Na parte inferior do retângulo pode-se (não é obrigatório) descrever as atividades internas relativas ao estado descrito. As atividades internas podem haver as seguintes variações:

![42-atividades-internas](42-atividades-internas.png)

42-atividades-internas

- **Entry:** Determina que a atividade descrita será executada no momento em que o objeto entra em um estado.
- **Exit**: Determina que a atividade descrita será executada no momento em que o objeto sai de um estado.
- **Do**: Determina que a atividade descrita será executada no período em que o estado for executado.

## Transições

Ocorrem para evidenciar uma alteração no estado entre um objeto e outro, de modo a permitir a geração de um novo estado. Sua representação se dá através de uma flecha, que pode, ou não, conter uma descrição a respeito. 

![43-transições](43-transicoes.png)

43-transições

## Estado Inicial

Para simbolizar que o processo está começando a ser modelado, usa-se o estado inicial, o qual é constituído por um círculo preenchido.

![44-estado-inicial](44-estado-inicial.png)

44-estado-inicial

## Estado Final

Para simbolizar que a modelagem do processo chegou ao fim. Representado por um círculo preto preenchido envolto de outro círculo não preenchido.

![45-estado-final](45-estado-final.png)

45-estado-final

## Pseudoestado de Escolha

Utiliza-se símbolo de losango para representar uma tomada de decisão, ou seja, uma condição que decidirá o próximo estado.

![46-pseudoestado-escolha](46-pseudoestado-escolha.png)

46-pseudoestado-escolha

⬆️ [Retornar ao Índice](https://www.notion.so/Diagramas-de-Sistema-452ca0987bf84125a38ff563c3c38d01)

# Diagrama de Atividades

Este diagrama ajuda na modelagem de atividades que podem ser um método, ou um algoritmo, ou mesmo um processo completo. Está ligado também a descrição de computação procedural, a modelagem organizacional para engenharia de processos e ao *workflow*.

## Atividade

Representado por um retângulo com bordas arredondadas, uma atividade pode receber várias categorias de comportamentos, tais como ocorrências de funções aritméticas, comportamento de atividade, ações de comunicação, leitura e gravação de atributos ou até mesmo a instanciação. 

![47-atividade](47-atividade.png)

47-atividade

## Nó de Ação

Um nó de ação representa um passo, uma etapa que deve ser executada em uma atividade, não podendo ser decomposto. Sua representação é parecida com a da atividade, porém, o retângulo é um pouco menor

![48-no-ação](48-no-acao.png)

48-no-ação

## Fluxo de Controle

Representado por uma seta que realiza  a ligação entre dois nós, local onde passam sinais de controle do nó antigo apontando para o novo. O fluxo de controle, pode-se, também, descrever a condição ou restrição.

![49-fluxo-controle](49-fluxo-controle.png)

49-fluxo-controle

## Nó Inicial

Representado por um círculo preenchido, o nó inicial visa demonstrar o início do fluxo da atividade invocada. Temos o nó inicial sempre acoplado a um fluxo de um sistema. 

![50-no-inicial](50-no-inicial.png)

50-no-inicial

## Nó de Final de Atividade

Representa que o fim do fluxo acabou, através de um círculo preenchido por outro.

![51-no-final](51-no-final.png)

51-no-final

# Nó de Decisão

Através de losangolo, simboliza as possíveis condições ou percussos que aquele ponto do sistema oferece. Simbolizado por um losangolo.

![52-no-decisão](52-no-decisao.png)

52-no-decisão

## Partição de Atividade

Em alguns casos, faz-se necessário representar por onde passa o fluxo de um processo. Utilizamos o desenho de retângulos com o nome do setor, departamento ou até mesmo de um processo que pode ser manipulado entre atores. Os retângulos podem ser dispostos na horizontal ou vertical. 

![53-particao.png](53-particao.png)

⬆️ [Retornar ao Índice](https://www.notion.so/Diagramas-de-Sistema-452ca0987bf84125a38ff563c3c38d01)