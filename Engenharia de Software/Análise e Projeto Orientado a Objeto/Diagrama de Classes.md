# Introdução

Estudaremos a notação UML para diagrama de classes, além das convenções para os nomes das classes, atributos e métodos, as várias formas de notação para o diagrama de classes.

Uma classe tem a função de individualizar o objeto através de suas características e comportamentos. 

Existem várias formas de associações de classes, e tais associações fazem surgir o conceito de multiplicidade.

---

# Diagrama de Classes

O diagrama de classes mostra a estrutura estática do sistema. A classe representa a abstração de um conjunto de objetos do mundo real, que possui tipos, características e comportamento comuns. A abstração ocorre quando definimos um objeto conceitual a partir de objetos do mundo real que possuam as mesmas características. 

<aside>
🗣 Visão estática de como as classes estão organizadas, sua estrutura lógica e suas relações.

</aside>

O objeto é qualquer elemento concreto ou abstrato com existência perceptível no mundo real e possa ser individualizado por possuir características e comportamento próprio. 

![30 — Objetos do mundo real](30-objetos.png)

30 — Objetos do mundo real

Uma classe é uma estrutura que modela um conjunto de objetos cujas características sejam similares. A classe, por meio dos métodos, modela o comportamento de seus objetos, e os possíveis estados do objeto são modelados mediantes atributos.

---

# Notação para Classes

Uma classe é representada por um retângulo com seu nome (esteriótipo). Todo nome deve começar com uma letra maiúscula e não pode conter caracteres de língua de origem latina, como caracteres acentuados, e especiais. Caso o nome de uma classe seja composto por mais de uma palavra, a primeira letra de cada uma delas deve ser maiúscula. 

Uma classe é dividida em mais dois compartimentos, o segundo representa os atributos com o tipo de dados, o terceiro representa os métodos (operações).

![31 — Representação Classe](31-classe.png)

31 — Representação Classe

## Atributos

O atributo é uma característica que define a estrutura de uma classe, também são denominados variáveis de classe.

A sintaxe para declaração de um atributo em UML é:

```
[<visibilidade>]<nome>:[<tipo>][=<valor inicial>]
```

### `<visibilidade>`

A visibilidade nos informa quais são as classes que podem ver o atributo que recebe a sinalização, as opções de visibilidade são:

| Notação | Nome | Significado |
| --- | --- | --- |
| + | Público | Todas as classes têm acesso. |
| - | Privado | Somente métodos definidos na classe podem vê-lo. |
| # | Protegido | Métodos definidos na classe e nas classes derivadas podem vê-lo. |
| ~ | Pacote | Visível nas classes do pacote. |

### `<nome>`

O nome do atributo deve obedecer algumas regras:

- Começar com letras.
- Não conter caracteres de lingual de origem latina.
- Não começar por números.
- Caso o nome de um atributo seja composto por mais de uma palavra, a primeira letra de cada uma delas deve ser uma maiúscula ou as separar as palavras com underline (_).

### `<tipo>`

Tipos de linguagem de programação, sendo:

![32 — Tipos de dados primitivos](32-tipos-dados-primitivos.png)

32 — Tipos de dados primitivos

### `<valor inicial>`

Valor inicial para o atributo que respeite o tipo de dado.

## Métodos

Um método é uma ação, de acordo com certos princípios, que determina um comportamento dos objetos de uma classe e são semelhantes às funções ou aos procedimentos da programação estruturada. 

Os métodos, quando em tempo de execução, possuem acesso aos dados armazenados em um objeto e são, dessa forma, capazes de controlar o estado objeto.

A sintaxe para declaração de um método segue a seguinte ordem:

```
[<visibilidade>]<nome>(<lista argumentos>):[<retorno>]
```

### `<visibilidade>`

### `<nome>`

O nome do método deve obedecer algumas regras:

- Começar com letras.
- Não conter caracteres de lingual de origem latina.
- Não começar por números.
- Caso o nome de um método seja composto por mais de uma palavra, a primeira letra de cada uma delas deve ser uma maiúscula.

### `<lista de argumentos>`

Argumentos são os meios que utilizaremos para passar dados aos métodos que trabalharão, especificamente, em cima destas informações.

![33 — Argumento do método](33-argumentos.png)

33 — Argumento do método

### `<retorno>`

Tipo do dado retornado pelo argumento seguindo os tipos de dados da linguagem.

![34 — Retorno do método](34-tipo-dado-retorno.png)

34 — Retorno do método

---

# Multiplicidade entre as Associações de Classes

A associação é uma relação entre duas classes, significando que os seus objetos possuem uma ligação. 

A multiplicidade especifica quantas instâncias de uma classe relacionam-se a uma única instância de uma classe associada.

| Representação | Significado |
| --- | --- |
| 1 | Exatamente um. |
| 0..* | Zero ou mais. |
| * | Zero ou mais. |
| 1..* | Um ou mais. |
| m..n | Intervalo específico (5..8) - (5, 6, 7 ou 8)  |
| m..n,o | Combinação (4..7,9) - (4, 5, 6, 7, ou 9) |

Para exemplificar, segue o relacionamento entre classes de Alunos e Disciplina. Para definir a multiplicidade do relacionamento, fazemos as seguintes perguntas:

- Realizando a leitura do diagrama da esquerda para a direita:
    - Um aluno pode cursar quantas disciplinas?
    - A resposta será a multiplicidade que deverá ser informado ao lado da classe disciplina.
- Realizando a leitura do diagrama da direita para a esquerda:
    - Uma disciplina pode ser cursada por quantos alunos?
    - A resposta será a multiplicidade que deverá ser informada ao lado da classe aluno.

![35 — Exemplo de Multiplicidade](35-exemplo-multiplicidade.png)

35 — Exemplo de Multiplicidade

Dessa forma podemos fazer a seguinte leitura para o diagrama de classes acima:

- Da esquerda para a direita →
    - Um aluno pode cursar somente uma disciplina.
- Da direita para a esquerda ←
    - Uma disciplina pode ser cursada somente por um aluno.

![36 — Exemplo de Multiplicidade](36-exemplo-multiplicidade.png)

36 — Exemplo de Multiplicidade

No exemplo acima temos:

- Da esquerda para a direita →
    - Um aluno pode cursar uma ou muitas disciplinas.
- Da direita para a esquerda ←
    - Uma disciplina pode ser cursada nenhum ou muitos alunos.

---

# Tipos de Associação entre Classes

## Associação unária

Em uma associação unária, uma classe se associa com ela mesma.

![37 — Associação Unária](37-associacao-unaria.png)

37 — Associação Unária

Um funcionário pode ser gerenciado por nenhum ou apenas um chefe, enquanto o chefe pode gerenciar nenhum ou muitos funcionários. 

## Associação binária

As associações binárias são as mais comuns e acontecem entre duas classes.

![38 — Associação Binária](38-associacao-binaria.png)

38 — Associação Binária

Um cliente pode fazer varias compras, mas uma compra só pode ser de um único cliente.

## Associação ternária

Associação de três classes, a notação é dada por um losango, fazendo a ligação entre as três classes.

![39 — Associação Ternária](39-associacao-ternaria.png)

39 — Associação Ternária

Um cliente pode ter nenhum ou vários contratos, um contrato pode ser de um ou vários clientes. Enquanto um contrato pode ter uma ou várias regras, consequentemente um cliente pode ter uma ou várias regras de contrato.

## Classe associativa

Quando uma associação possuir atributos próprios. Estas classes são úteis quando queremos armazenar o histórico de uma associação (relacionamentos que ocorrem e interessam ser salvos).

- São comuns em associações de multiplicidade *..* (muitos para muitos).
- A linha que representa a associação não é nomeada, o nome da classe associativa deve ser suficiente para identificar a associação.
- Classes associativas podem estar relacionadas a outras classes.

![40 — Classe associativa](40-classe-associativa.png)

40 — Classe associativa

Uma venda pode vender vários produtos e um produto pode ser vendido em várias vendas.

## Agregação

A agregação é um caso especial de associação, utilizado para representar relacionamentos de pertinência "parte-todo" ou "uma parte de". Permite representar que um objeto ou mais objetos de uma classe parte de um objeto de outra classe. 

### Agregação regular

É representada por um losango vazado, a classe B é "uma parte" da classe A, porém as instâncias de objetos da classe B existem sem o objeto associado na classe A.

![41 — Agregação regular](41-agregacao-regular.png)

41 — Agregação regular

Um quadro pode ter uma ou várias figuras, uma figura é uma parte do quadro, com a notação do losango vazado indicando que uma figura também existe sem o quadro.

### Agregação de composição

A agregação de composição é uma agregação de fato, em que o todo é composto pelas partes. Existe uma relação forte entre ambos, pois quando o todo é destruído, as partes também serão.

Representada por um losango preenchido, a classe B é "parte-todo" da classe A, as instâncias de objetos da classe B não existem sem um objeto associado na classe A. A destruição da instância de objeto de A implica a destruição da instância de objeto associado da classe B.

![42 — Agregação de composição](42-agregacao-composicao.png)

42 — Agregação de composição

Um orçamento tem muitos itens, porém os itens de um orçamento não existirão sem o orçamento.

## Generalização

Uma generalização é uma associação hierárquica que indica um relacionamento entre a classe de mais alto nível, denominada superclasse, e outra de mais baixo nível, denominada subclasse (classe mãe e classe filha), também conhecida como especialização ou herança.

O elemento mais específico possui toas as características do elemento geral e contém, ainda, mais particularidades.

Existem alguns tipos de generalização:

- Normal
- Restrita

As generalizações restritas se dividem em generalização de sobreposição, exclusiva, total ou parcial. 

Na generalização, é enfatizado o conceito de herança, que tem como característica a reutilização de atributos e métodos definidos nas classes mais gerais (superclasse) por classes mais específicas (subclasses).

As subclasses, que representam as classes mais especializadas, herdam atributos, métodos e associações da superclasse. A notação é uma seta em branco apontando sempre para a superclasse.

![43 — Generalização](43-generalizacao.png)

43 — Generalização

### Cobertura total

A generalização apresenta um conceito importante: a cobertura. A notação para a cobertura é uma linha tracejada com o tipo de cobertura entre chaves.

A cobertura total (completa) quando cada elemento da classe genérica (superclasse) é mapeado para, pelo menos, um elemento das classes especializadas (subclasse).

![44 — Generalização com Cobertura Total](44-generalizacao-cobertura-total.png)

44 — Generalização com Cobertura Total

A cobertura da generalização acima é total, portanto, significa que uma pessoa obrigatoriamente tem que ser homem ou mulher. 

### Exclusiva

A cobertura de uma generalização é exclusiva  se cada elemento da classe genérica é mapeado para, no máximo um elemento das subclasses.

![45 — Generalização com Cobertura Total e Exclusiva](45-generalizacao-cobertura-tota-exclusiva.png)

45 — Generalização com Cobertura Total e Exclusiva

Uma pessoa será, obrigatoriamente, um homem ou mulher, não podendo ser os dois.

### Parcial

A cobertura é parcial ou incompleta se existe algum elemento da classe genérica que não é mapeado para nenhum elemento das subclasses.

![46 — Generalização com Cobertura Parcial](46-generalizacao-cobertura-parcial.png)

46 — Generalização com Cobertura Parcial

Um veículo pode ser um carro ou uma bicicleta, podendo não ser nenhum dos dois.

### Sobreposição

A cobertura de uma generalização é de sobreposição se existe algum elemento da classe genérica que é mapeado para elementos de duas ou mais subclasses diferentes.

![47 — Generalização com Cobertura de Sobreposição](47-generalizacao-cobertura-sobreposicao.png)

47 — Generalização com Cobertura de Sobreposição

Uma pessoa pode ser aluno ou professor, podendo ser os dois. 

As coberturas podem ser combinadas da seguinte forma:

- Total, exclusiva: nesta combinação uma classe genérica deve ser mapeada para uma única subclasse.
- Total, sobreposição: nesta combinação, uma classe genérica deve ser mapeada para uma ou várias subclasses.
- Parcial, exclusiva: nesta combinação, uma classe genérica pode ser mapeada para uma única subclasse ou para nenhuma.
- Parcial, sobreposição: nesta combinação de cobertura, uma classe genérica pode ser mapeada para uma ou mais subclasses, ou para nenhuma.

---

# Herança Múltipla

Na herança múltipla, uma classe (subclasse) é derivada de mais de uma classe base (superclasse). Uma superclasse não representa um caso geral completo da subclasse, ou seja, a superclasse representa uma parte do conceito representado na subclasse.

![48 — Herança Múltipla](48-heranca-multipla.png)

48 — Herança Múltipla

A herança múltipla permite a concatenação (mesclagem) de informações de duas ou mais origens. A vantagem da herança múltipla é ter mais capacidade de especificação de classes e mais oportunidade de reutilização. A desvantagem é a perda em simplicidade conceitual e de implementação.

<aside>
📌 Herança múltipla dá-se quando uma subclasse herda atributos e operações de duas ou mais superclasses. Este tipo de situação deve ser evitado, pois, introduz possibilidades de difícil solução.

</aside>

---

# Conclusão

O diagrama de classes mostra a estrutura estática do domínio das abstrações (classes) do sistema, descreve as categorias de objetos no sistema e os vários tipos de relacionamentos estáticos que existem entre eles, sendo o diagrama de maior importância na engenharia de software. 

Através da sua estrutura, especificando os atributos que, definem a estrutura de uma classe, representando uma característica dos objetos instanciados, os métodos que determinam o comportamento dos objetos de uma classe e são semelhantes às funções ou aos procedimentos da programação estruturada.

A multiplicidade entre as associações de classes especificam quantas instâncias de uma classe se relacionam a uma única instância de uma classe associada.

---