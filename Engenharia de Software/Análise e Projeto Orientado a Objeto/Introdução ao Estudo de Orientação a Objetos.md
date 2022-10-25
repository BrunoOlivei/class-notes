# Introdução

A análise de sistemas é a atividade inicial do processo de desenvolvimento de software. É nessa fase que determinamos e especificamos o que um software deve fazer e verificamos as circunstâncias sob as quais o software deve operar em um esforço colaborativo entre analistas de sistemas e usuários.

Veremos como os métodos surgiram e como aconteceu sua evolução, a partir do primeiro método orientado a objetos, até chegarmos à Unified Modeling Language, UML, que será a linguagem que utilizaremos para as nossas análises e nossos projetos.

A evolução de todos os outros métodos permitiram que chegássemos a uma unificação que, na verdade, apropria-se das melhores características dos demais métodos. 

Conheceremos e entenderemos os conceitos e termos utilizados na análise e no projeto OO e os principais diagramas da UML utilizados na análise e no projeto de softwares.

<aside>
🧠 Sistemas requerem abordagem multidisciplinar e devem ser projetados para durarem muitos anos em um ambiente dinâmico.

</aside>

Podemos identificar três fases nos paradigmas de desenvolvimento:

1. **Definição:** determina viabilidade, requisitos do software, especifica e projeta o sistema.
2. **Desenvolvimento:** implementação, integração e instalação.
3. **Operação:** manutenção, correção e evolução.

---

# Análise e Projeto

O processo de desenvolvimento de um sistema computacional tem, na análise, sua atividade inicial, determinando e especificando o que um sistema deve fazer e as circunstâncias sob as quais ele deve operar, envolvendo um esforço colaborativo entre analistas de sistemas e usuários.

Os analistas procuram obter, a partir dos usuários, em um processo gradual e cumulativo, o maior conhecimento possível acerca do domínio do problema e do respectivo ambiente.

Análise de Sistemas faz parte da Engenharia de Requisitos o que implica em técnicas sistemáticas utilizadas para assegurar que os requisitos do sistema sejam consistentes, relevantes e completos.

A determinação incorreta dos requisitos levará à obtenção e à disponibilização de sistemas computacionais inadequados.

<aside>
🔑 A análise é a solução conceitual dada ao problema, sem considerar detalhes da implementação, tais como a linguagem e o sistema gerenciador de banco de dados a serem utilizados. Preocupa-se com as classes do domínio do problema e suas relações e, também com os casos de uso.

</aside>

Na programação estruturada, havia nitidamente, uma visão sequencial e bem dividida, como programas que executam determinados processos e tratam determinados dados. Na orientação a objetos, passamos a visualizar classes responsáveis por atributos, com operações criadas para tratá-los, e a execução das atividades dos sistemas passa a depender da interação dessas classes.

## Modelagem de Software

1. Analisar UM problema de software.
2. Criar especificação de requisitos funcionais e não-funcionais de software para resolução do problema analisado.
3. Criar modelos propondo soluções para os requisitos especificados de software para o problema analisado.
4. Validar a especificação de requisitos.

---

## Análise e projeto OO

Na década de 80, houve preponderância dos métodos estruturados para o desenvolvimento de software. Atualmente, o paradigma OO é mais forte.

A análise e o projeto estruturados têm, como ênfase, as funções a atuar sobre os dados, todo o processo que se deseja informatizar é compreendido como um conjunto de funções com dados de entrada, processamento e saída.

As principais características são:

- Modularidade e coesão
- Desenvolvimento *top-down* (diferentes níveis de abstração)

Os diagramas que apoiam a análise e o projeto estruturado são:

- Diagrama Entidade e Relacionamento (DER).
- Dicionário de dados.
- Diagrama de Fluxo de Dados (DFD).

O DER é o modelo do sistema, mostra-nos as entidades e seus relacionamentos. Muitos detalhes não são mostrados, ficando a cargo do dicionário de dados os detalhes de nomes de atributos, tipos de dados, comprimento e demais restrições de dados. 

O DFD modela o fluxo destes, mostra os dados em movimento, como ocorre a interação entre as diversas entidades (depósitos) do sistema.

A Orientação a Objetos é uma estratégia de desenvolvimento de software que o organiza como uma coleção de objetos que contém tanto a estrutura dos dados quanto o comportamento deles. Sua principal característica é a forma natural de tratar a realidade.

A proposta da Orientação a Objetos é deslocar o esforço de desenvolvimento para a fase de análise, dando ênfase às estruturas de dados antes das funções, os benefícios são: 

- Reutilização do código (componentes),
- Confiabilidade (objetos encapsulados),
- Aumento da produtividade.

A análise OO apresenta um conjunto de regras e modelos que auxiliam o analista a levantar e a modelar os requisitos dos usuários que o sistema deve atender.

---

# Evolução dos Métodos OO

Um dos primeiros métodos foi o modelo OOSA, proposto por Shlaer e Mellor, em 1988, e o Wirfs-Brock, lançado em 1989 pelo grupo de pesquisa da Smalltalk.

A maior parte dos métodos OO passou a se tornar estável na década de 90, com a fusão das metodologias  de Grady Boock, James Rumbaugh e Ivar Jacobson e a criação da UML.

![1-Linha do tempo OO](1-linha-tempo-oo.png)

1-Linha do tempo OO

A UML sugere, fortemente, a adoção de casos de uso (use cases) como direcionadores de projetos de software, a utilização de diagramas de interação para identificação de objetos e uma série de outros conceitos.

UML abrange as fases de levantamento de requisitos, análise, projeto e implementação. 

<aside>
💡 O intuito do projeto de software é aplicar um conjunto de princípios, conceitos e práticas que levam ao desenvolvimento de um sistema ou produto de alta qualidade. O objetivo do projeto é criar um modelo de software que irá implementar corretamente todos os requisitos do cliente e trazer satisfação àqueles que o usarem.

</aside>

<aside>
🧠 O modelo de projeto engloba quatro elementos distintos; à medida que cada um é desenvolvido, evolui uma visão mais completa do projeto.

</aside>

---

# Conceitos Básicos de OO

## Objeto

Qualquer elemento concreto ou abstrato que existe no mundo real, que pode-se individualizar por possuir comportamentos e características próprios.

<aside>
🧠 Representação virtual de algo real: o seu estado e o seu comportamento.

</aside>

- **Objetos concretos:** caracterizados por objetos que possuem forma física (ex: cadeira, mesa, xícara, garrafa, planta, pessoa, animal, carro, casa, etc.)
- **Objetos abstratos:** caracterizados por objetos que não existem no mundo físico, porém possuem características e operações próprias onde outros objetos, concretos ou abstratos, possam interagir.

## Abstração

Objetos reais com os mesmos comportamentos e características, os quais são classificados como de um mesmo tipo (ex: categorias de aviões, de bolsas, de esportes, pessoas, etc.)

<aside>
🧠 Abstraímos quando definimos um objeto conceitual partindo de objetos reais com os mesmos comportamentos e características, os quais são classificados como do mesmo tipo.

</aside>

## Classe

Representa a abstração de um conjunto de objetos reais que possui comportamentos e características comuns (ex: classe funcionário, possui nome, endereço, telefone, etc).

Tem a função de capturar os atributos e operações dos elementos do problema que são de mesmo tipo. Funciona como um filtro, entre o que existe na realidade e o que nós queremos implementar no computador. Cada classe vai então gerar os objetos no espaço da solução, no mundo virtual. 

É um template que dará forma para cada objeto criado a partir dele, no ambiente virtual, portanto as classes são formadas por:

- Nome
- Atributos
- Funcionalidades

## Instância

É cada uma das ocorrências de um objeto formado a partir da sua classe. Quando um objeto é criado a partir de sua classe, exemplo é criar o objeto funcionário 1 com as informações de nome, telefone e endereço, a partir da classe funcionário.

## Atributo

É uma característica particular que os objetos de uma classe possuem, assumindo valores diferentes para cada objeto instanciado. 

```python
Classe Funcionário
(Possui) Nome
(Possui) Endereço
(Possui) Telefone

Valor:
Nome: Bruno Oliveira
Endereço: Rua 1, 12
Telefone: (11)99999-9999
```

## Operação

É uma ordem que faz um objeto executar uma ação. As operações são tudo o que os objetos de uma classe fazem e nada além do que esses objetos podem fazer.

```python
Classe avião

Objeto: Boing 737
	Atributos:
		Cor: Branco
		Número: 5643

	Operação
		Decolar
		Aterrissar
		Taxiar
		
```

## Mensagem

Representa o mecanismo de chamada de uma operação. É utilizada na solicitação de execução de uma operação. É a maneira como conseguimos que um método seja executado.

```python
Classe Conta Corrente

Objeto contaxxxx-x
	Atributos:
		numero: xxxx-x
		saldo: R$100,00
	Operação:
		Depositar(valor)
		Sacar(valor)
		Transferir(valor, num_conta)

Mensagem:
	Sacar(R$50,00)
```

## Evento

É um tipo de operação que faz com que os objetos mudem de estado (ex: login ou logout, altera o estado, play ou stop.)

## Parâmetro

É um ou mais atributos que são carregados para dentro de uma mensagem

```python
Classe Conta Corrente

Objeto contaxxxx-x
	Atributos:
		numero: xxxx-x
		saldo: R$100,00
	Operação:
		Depositar(valor)
		Sacar(valor)
		Transferir(valor, num_conta)

Mensagem:
	Sacar(parâmetro: R$50,00)
```

## Estado

É a forma de apresentação dos objetos de uma classe em determinado instante (ex: logado ou não)

## Transição de estado:

É quando ocorre a mudança de estado de um objeto de uma classe como resposta a chegada de um evento (ex: o tempo de transição de um semáforo)

## Associação

É a forma como os objetos de uma mesma classe ou de classes diferentes se conectam.

![Untitled](Untitled%201.png)

![Untitled](Untitled%201%201.png)

## Encapsulamento

É a reunião de características e comportamentos de objetos em uma classe, o que pode torná-los públicos ou privados, se privados outros objetos não possuem acesso a eles.

<aside>
🧠 O encapsulamento protege os valores brutos de cada objeto.

</aside>

Exemplo: CPF de um cliente, por ser um valor único não pode ser alterado, ou mesmo que algum atributo possa sofrer alterações, essa é limitada para determinados usuários do sistema.

## Polimorfismo

É a capacidade que objetos de classes diferentes possuem de se comportarem de forma diferente em uma mesma operação. (Ex: Operação CRIAR, pode ser usada para criar um livro, ou um funcionário, ou uma conta bancária, etc.)

## Método

É o algoritmo (conjunto de passos) que um objeto executa quando reage a uma operação. O método é a lógica interna de uma operação.

```python
Classe Conta Corrente

Objeto contaxxxx-x
	Atributos:
		numero: xxxx-x
		saldo: R$100,00
	Operação:
		Depositar(valor)
		Sacar(valor)
		Transferir(valor, num_conta)

Mensagem:
	Sacar(parâmetro: R$50,00)

Método Sacar:
	1º Passo
	2º Passo
	3º Passo
	Resultado
```

## Colaboração

É a troca de mensagens que acontece entre objetos e atores, (ex: usuário informa login e senha)

## Herança

É a propriedade que possibilita que a classe herde características e comportamentos de outra classe (ex: classe pessoa física e pessoa jurídica herda características e comportamentos da classe pessoa) 

---

# Diagramas da UML

A UML 2.5 apresenta diversos diagramas utilizados para documentação de software, eles são classificados em **estruturais** e de **comportamento**.

![2 — Estrutura diagramas da UML 2.5 ](2-diagramas-uml.png)

2 — Estrutura diagramas da UML 2.5 

## Diagramas de Comportamento

Utilizados para descrever o sistema modelado em execução. São utilizados para especificar, visualizar, documentar e construir os aspectos dinâmicos de um sistema.

### Diagrama de casos de uso

Utilizados na análise de requisitos acompanhando o software desde o seu início até a conclusão. Representando através do ator um usuário do sistema ou uma máquina podendo também ser outro software. O ator é quem realiza as atividades e sempre atua sobre um caso de uso.

![3 — Diagrama de casos de uso](3-caso-uso.png)

3 — Diagrama de casos de uso

### Diagrama de sequência

Com objetivo de refinar o diagrama de classes, é um dos diagramas de interação, sua utilidade é estudar as interações entre os objetos, possibilitando a identificação de relação entre as classes.

<aside>
🧠 Diagrama de sequência estabelece micro-fronteiras e a interação entre elas.

</aside>

A partir das informações fornecidas pelo diagrama de sequência, pode-se identificar os métodos associados às classes, além da identificação das relações entre elas.

![4 — Diagrama de Sequência](4-diagrama-sequencia.png)

4 — Diagrama de Sequência

Outra forma de representar esse cenário é pelo diagrama de comunicação (comportamento). Ele contém as mesmas informações que o diagrama de sequência, porém não considera a dimensão temporal.

### Diagrama de Estados

Visa especificar o comportamento das classes mais complexas, utilizando uma máquina de estado.

<aside>
🧠 Autômato finito ou máquina de estados finitos representa a modelagem de comportamentos considerando seu estado. O estado guarda informações sobre o passado do objeto, a transição indica que o objeto está mudando de estado, e uma ação é o detalhamento de uma atividade que deve ser executada em determinado momento.

</aside>

![5 — Diagrama de Estados](5-diagrama-estados.png)

5 — Diagrama de Estados

### Diagrama de comunicação

O diagrama de comunicação permite a identificação das classes mais próximas, e a ordem de envio de mensagens é identificada por números sequenciais. 

<aside>
🧠 Visa identificar quais serão as principais mensagens (informação que deve ser transmitida) passadas entre as classes e a sua ordem cronológica.

</aside>

![6 — Diagrama de Comunicação](6-diagrama-comunicacao.png)

6 — Diagrama de Comunicação

### Diagrama de atividades

É um gráfico de fluxo demonstrando como ocorre o fluxo de controle entre as atividades. Este diagrama é um dos mais detalhistas, dando mais ênfase ao nível de algoritmo.

Podem ser utilizados com vários propósitos, podemos citar a captura do funcionamento interno do objeto, mostrar como pode ser executado um conjunto de ações relacionadas e como elas podem afetar os objetos ao seu redor.

<aside>
🚧 Existe o BPMN (Business Process Model and Notation) que engloba com mais detalhes todas as atividades do projeto de sistemas.

</aside>

![7 — Diagrama de Atividades](7-diagrama-atividades.png)

7 — Diagrama de Atividades

---

## Diagramas de Estrutura

Os diagramas estruturais são utilizados para especificar, visualizar, documentar e construir os aspectos estáticos de um sistema. Envolve a existência e a colocação de itens como classes, pacotes, objetos, componentes e utilização.

### Diagrama de classes

Uma classe é uma estrutura que modela um conjunto de objetos cujas características são similares, por meio dos métodos, modela o comportamento de seus objetos, e os possíveis estados do objeto são modelados por meio dos atributos.

<aside>
🧠 Classe é um template que formaliza os objetos reais.

</aside>

Por meio do diagrama de caso de uso, a classe possibilita a abstração dos objetos mediante os atributos.

![8 — Diagrama de Classes](8-diagrama-classe.png)

8 — Diagrama de Classes

### Diagrama de objetos

Os diagramas de objetos correspondem a um segundo nível de abstração do diagrama de classes. Podem ser uma ótima opção para exemplificar os diagramas de classes mais complexos, pois se trata do **diagrama de classes instanciado**. 

<aside>
🧠 Serve para testar se as classes estão diagramada corretamente.

</aside>

![9 — Diagrama de Objetos](9-diagrama-objeto.png)

9 — Diagrama de Objetos

### Diagrama de componentes

Mostra a organização e dependência entre todos os componentes. Seu objetivo é modelar a visão de implementação dos módulos executáveis do sistema. É um diagrama de alto nível. 

Um componente corresponde a uma parte do código distribuível. Podemos apresentar como exemplos de componentes: executáveis, as tabelas, as bibliotecas, o documento e o arquivo.

![10 — Diagrama de Componente](10-diagrama-componente.png)

10 — Diagrama de Componente

### Diagrama de implantação

São utilizados para modelar a arquitetura física de distribuição em que o software será executado. Mostra os nós e os relacionamentos de comunicação.

Mapeia a arquitetura lógica de classe no nó de processamento e suas dependências. Um nó representa um recurso computacional com memória e processamento, ou seja, um disco rígido, um computador, uma impressora. Quando queremos saber quais computadores e outros hardwares estão conectados, de que modo estão distribuídas as classes e quando a atualização de determinado arquivo resulta na recompilação de outros.

![11 — Diagrama de Implantação](11-diagrama-implantacao.png)

11 — Diagrama de Implantação

### Diagrama de pacotes

O pacote representa um agrupamento de classes. Normalmente, os pacotes apresentam relações em que um depende de outro para o funcionamento.

Um pacote pode representar uma biblioteca, um subsistema, um sistema, entre outros.

 

![12 — Diagrama de Pacotes](12-diagrama-pacote.png)

12 — Diagrama de Pacotes

---