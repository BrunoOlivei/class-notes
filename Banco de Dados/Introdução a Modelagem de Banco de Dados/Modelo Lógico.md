# Modelagem de Dados

O modelo de dados lógico se aproxima mais da parte técnica de um projeto de banco de dados.

As formas de modelagem ER e Relacional permitem estabelecer três tipos de modelos:

- **Conceitual:** elaborado pelo entendimento do negócio, levantamento de requisitos e apresentação aos clientes de negócio.
- **Lógico:** Elaborado para equipe de desenvolvimento, projeto de como o banco de dados será estruturado.
- **Físico:** Implementação do projeto lógico no servidor, baseando-se nas estruturas criadas no modelo lógico.

Existem três abordagens para criação de um modelo lógico, a primeira sendo baseada no modelo conceitual, a segunda é o desenvolvimento do modelo lógico direto, sem a necessidade do conceitual, essa, portanto, requer maior nível de experiência do analista de banco de dados. 

## Etapas do projeto de banco de dados

1. Elicitação dos requisitos através de técnicas de abordagem dos stakeholders do projeto de banco de dados.
2. Documentação dos requisitos
3. Modelagem conceitual a partir dos requisitos levantados
4. Definir a abordagem de banco de dados a ser utilizada (relacional, orientada a objetos, objeto-relacional, não relacional), levantamento de custos, capacidade computacional, e as demais informações que impactam no projeto de banco de dados visando obter uma documentação completa.
5. Aplicar as regras de derivação específicas
6. Implementar as estruturas no SGBD
7. Validar

## Modelo lógico

Um modelo de dados lógico é composto fundamentalmente por:

- Tabelas ou relações;
- Chaves primárias;
- Chaves estrangeiras;
- Atributos.

![21 — Exemplo de Modelo Lógico](4-exemplo-modelo-logico.png)

21 — Exemplo de Modelo Lógico

**Chave primária** é formado por conjunto de caracteres únicos para cada linha de dado registrado, ou seja, cada funcionário no banco de dados possui uma chave primária única que o identifica dos demais. 

**Chave estrangeira** é formado por conjunto de caracteres derivados de outra tabela de dados, que identifica a relação de cada linha com a linha de outra tabela. No caso da chave estrangeira dentro de uma tabela, pode haver repetição. No nosso exemplo, um ou mais funcionários podem estar ligados a um mesmo departamento, isso é representado pelo código departamento. Porém, na tabela que originou a chave secundária, ela seguirá a mesma premissa da chave primária, não havendo repetição de códigos, ou seja, cada linha da tabela original possuí uma chave única. 

## Diferenças entre Modelo Conceitual e Modelo Lógico

| Modelo Conceitual | Modelo Lógico |
| --- | --- |
| Entidade | Tabela (Relação) |
| Instância de Entidade | Linha (Tupla) |
| Atributo | Coluna (Campo) |
| Atributo Multivalorado | Tabela (Auxiliar) |
| Atributo Identificador | Chave |
| Atributo Composto | Várias Colunas |
| Relacionamento | Ligações |

## 💡 Relacionamento NxN

Importante ressaltar que para relacionamentos muitos para muitos (tabela A e tabela B), é necessário criar uma tabela adicional (tabela C) que irá armazenar as chaves estrangeiras das tabelas (A e B) que se relacionam e formar uma chave primária para cada linha de relacionamento (tabela C). Caso existam atributos no relacionamento, alocá-los à tabela (tabela C) criada como campos normais (descritivos).

### **Exemplo 1:**

![22 — Exemplo de Relacionamento N:N](5-exemplo-relacionamento-nn.png)

22 — Exemplo de Relacionamento N:N

**Solução:**

Criar uma terceira tabela (nomeada conforme o relacionamento) que contém os atributos de relacionamento (originais) data inscrição e taxa inscrição, além das chaves primárias das tabelas Aluno e Curso (como chaves estrangeiras).

### Exemplo 2

![23 — Exemplo de Relacionamento N:N](23-exemplo-relacionamento-nn.png)

23 — Exemplo de Relacionamento N:N

**Solução:**

Nesse segundo exemplo também criaremos três tabelas:

1. Analista: contendo os atributos (colunas) código e nome;
2. Projeto: contendo os atributos (colunas) código e título;
3. Atuação contendo as colunas código analista, código projeto, função.

---

## Relacionamentos 1xN

Quando temos um relacionamento um para muitos, acrescenta-se a chave primária da tabela de origem (A) como chave estrangeira na tabela destino (B), ou seja, adicionamos a chave primária do lado 1 na tabela do lado N como chave secundária. 

### Exemplo 1

![24 — Exemplo de Relacionamento 1:N](24-exemplo-relacionamento-1n.png)

24 — Exemplo de Relacionamento 1:N

O exemplo acima nos diz que temos uma relação de que um projeto só pode ter um engenheiro, mas um engenheiro pode ter vários projetos

**Solução:**

Nesse caso a chave primária da tabela engenheiro é inserida como chave estrangeira na tabela projeto. 

Em relacionamentos 1 para N migram-se os atributos do relacionamento (alocado), caso existam, para a tabela do lado N (B), **prática mais comum.**

Pode se criar uma terceira tabela (C) para conter as chaves estrangeiras das tabelas originais (A e B) e alocam-se os atributos do relacionamento (alocado), porém essa prática é pouco usada. 

### Exemplo 2

![25 — Exemplo de Relacionamento 1:N](25-exemplo-relacionamento-1n.png)

25 — Exemplo de Relacionamento 1:N

**Solução:**

Alocar os atributos do relacionamento alocado para a tabela do lado N (projeto) e migrar a chave primária da tabela engenheiro como chave estrangeira na tabela projeto.

### Exemplo 3

![26 — Exemplo Relacionamento 1:N](26-exemplo-relacionamento-1n.png)

26 — Exemplo Relacionamento 1:N

**Solução:**

Seguindo a mesma lógica, nesse caso migraremos o atributo `datalotacao` do relacionamento lotação para a tabela de empregado assim como a chave primária código da tabela departamento, que será uma chave estrangeira na tabela empregado.

| Código Empregado | Nome | Código Departamento | Data Lotação |
| --- | --- | --- | --- |
| 101 | João | 1 | 30/12/1976 |
| 102 | José | 2 | 12/06/2001 |
| 103 | Maria | 1 | 21/03/1987 |

| Código Departamento | Nome |
| --- | --- |
| 1 | Gerência |
| 2 | Vendas |
| 3 | Compras |

---

## Relacionamentos 1x1 ou 0,1x0,1

Quando temos um relacionamento de um e somente um para um podemos acrescentar a chave primária da tabela A para a tabela B como chave secundária e vice-versa.

Alguns aspectos que facilitam a escola:

- Qual tabela nasce antes?
    - Se a tabela A surge primeiro, então, migrar a chave estrangeira de B para A.
- Qual entidade será mais manipulada (nível de acesso)?
    - Se a tabela B será mais manipulada, colocar a chave estrangeira da A na B.
- Qual a maior chave (tamanho de caracteres)?
    - Se a tabela B possuí o menor número de caracteres, deve se migrar a chave estrangeira B para a tabela A

### Exemplo 1

![27 — Exemplo de Relacionamento 1:1](27-exemplo-relacionamento-11.png)

27 — Exemplo de Relacionamento 1:1

**Solução:**

Nesse caso podemos enviar a chave primária da tabela bebê para tabela certidão nascimento como chave secundária.

---

## Auto Relacionamento

Quando temos um uma tabela que possuí relacionamento com ela mesma, exemplo: tabela funcionários, onde um grupo de funcionários é gerenciado por um, nesse caso temos um auto relacionamento.

### Exemplo 1:N

![28 — Exemplo de Auto Relacionamento 1:N](28-exemplo-autorelacionamento.png)

28 — Exemplo de Auto Relacionamento 1:N

**Solução:**

Nesse caso é mais fácil, basta criar um campo a mais na própria tabela (pessoa) que receberá a chave primária para indicar o auto relacionamento. 

### Exemplo N:N

Quando temos, por exemplo, um caso onde, em uma tabela pessoas, um individuo pode representar mais de 1 e o individuo representado por ter mais de 1 representante:

![29 — Exemplo de Auto Relacionamento N:N](29-exemplo-autorelacionemto.png)

29 — Exemplo de Auto Relacionamento N:N

**Solução:**

A solução é criar uma tabela (representa que irá conter os números de CPF da tabela Pessoa como chave estrangeira, porém a tabela representa receberá dois campos, o primeiro com o CPF do representante e o segundo com o CPF do representado. 

### Exemplo N:N relacionamento com atributo

Aqui um exemplo onde o auto relacionamento possui um ou mais atributos:

![30-exemplo-autorelacionamento.png](30-exemplo-autorelacionamento.png)

**Solução:**

Cria-se uma nova tabela chamada composição que receberá a chave primária código peça, essa que também servirá como chave estrangeira para indicar o relacionamento (código peça compõe), além do campo quantidade.

---

# Modelagem

Peguemos um caso para realização da modelagem:

- Deseja-se construir um sistema para gestão de recursos humanos de uma empresa.
- Sabe-se que é importante manter o cadastro dos funcionários, quais os respectivos departamentos e sua evolução na empresa.
- Cada departamento tem uma cidade onde está localizado, e consequentemente uma regional, que, está localizada em um dos países.
- Para controle territorial, é necessário definir qual continente cada filial está localizada.
- Deve-se manter o histórico de todos os cargos que cada funcionário já ocupou.
- Informações importantes que devem ser armazenadas:
    - Nome, sobrenome, e-mail e data de admissão dos funcionários;
    - Qual é o gerente de cada funcionário;
    - Qual é o cargo atual de cada funcionário;
    - Quais cargos cada funcionário já ocupou;
    - Qual é o departamento que cada funcionário está vinculado;
    - Qual localidade cada departamento se encontra, bem como seu endereço;
    - Países e continentes de cada departamento.

---

[modelagem_recursos_humanos.pdf](modelagem_recursos_humanos.pdf)