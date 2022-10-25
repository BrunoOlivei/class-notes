# O que é um SGBD

Sistema Gerenciador de Banco de Dados

É um sistema que facilita o acesso e gerenciamento das informações em um banco de dados. 

Coleção de dados inter-relacionados e um conjunto de programas para acessar esses dados. 

# O que são dados

Dados são chamados de fatos conhecidos que podem ser registrados e possuem um significado implícito, exemplo: nome, telefone, CPF, etc. 

É a menor unidade de uma informação que pode ser armazenada em um banco de dados. 

# O que são Banco de Dados

É uma coleção de informações relevantes armazenadas em algum local e podem ser recuperadas posteriormente. 

Bancos de dados possuem uma ligação com o mundo real, com a fonte que gera as informações, usuários, algum ator que futuramente possa necessitar das informações armazenadas. Geralmente essas entidades reais são representadas em locais bem definidos no banco de dados. 

# SGBD's x Banco de Dados

Os SGBD's são sistemas projetados para gerir os volumes de informações armazenados em um banco de dados, fornecendo mecanismos de inserção, recuperação, alteração e remoção (CRUD) de todas as informações do banco de dados.

Exemplos de SGBD's:

- Oracle
- SQL Server
- MySQL
- PostgreeSQL
- DB2

## Redundância e Inconsistência

Sendo assim a finalidade de um SGBD é reduzir a redundância e inconsistência nos dados, ou seja, a garantia que uma determinada informação esteja armazenada em apenas um local e que as alterações nos dados sejam controladas e automaticamente propagadas a todos os usuários que acessam a informação.

## Recuperação de dados eficiente

Além disso, os SGBD's fornecem linguagens e mecanismos eficientes para que determinada informação seja encontrada, através de algoritmos que façam, por exemplo, buscas em um volume de dados.

## Isolamento

O SGBD precisa garantir isolamento das informações, garantido que os dados gravados, mesmo ocorrendo acesso concorrente onde possa vir a ter alterações, o SGBD gerencia as informações alteradas não sejam perdidas.

## Integridade

Outro aspecto importante são relacionadas a lógica do negócio, onde o SGBD provê formas mais fáceis de garantir a integridade das informações através de restrições e regras estabelecidas, por exemplo, alunos de uma instituição de ensino precisam estar devidamente cadastrados em um curso para poderem cursar as disciplinas. 

## Atomicidade

O SGBD deve garantir todas as operações atômicas, resolvendo problemas de atomicidade, que referi-se as operações realizadas em determinado dado, permitindo que todas essas operações sejam realizadas, caso ocorra alguma falha todas as alterações são desfeitas. Um exemplo é uma transferência bancária, onde para se realizar a transferência precisamente a conta que irá transferir um valor precisa ter um saldo positivo, se essa condição for satisfeita, o valor sai da conta de origem e é adicionado a conta de destino, sem antes checar o saldo para que a adição seja feita corretamente. Caso alguma condição não seja satisfeita, por exemplo, algum dado referente a conta de destino esteja incorreto, toda a operação é desfeita sem nenhum prejuízo as informações.  

## Segurança

Por fim o SGBD necessariamente precisa resolver problemas de segurança, através de usuários e perfis de acesso, de modo que nem todos os usuários têm acesso a todas as informações.

# Abstração de dados

Muitos usuários de uma corporação possuem a necessidade de acessar e compreender como os dados estão armazenados e distribuídos no banco de dados, mas muitos deles não são especialistas em computação.

Portanto, existem maneiras diferentes de abstrair os dados, de forma que todos os usuários possam compreender o banco de dados:

- **Nível Conceitual**
    
    Nível mais alto, próximo da linguagem natural humana, descreve apenas parte do banco de dados, exibe apenas a parte do sistema que o usuário necessita ver, de forma simplificada. Descrevendo as principais entidades do sistema e quais são os níveis de relacionamento, não entrando no mérito de hardware ou tipo de dado, por exemplo.
    
- **Nível Lógico**
    
    É o nível intermediário, neste nível é possível representar todo o banco de dados, com suas estruturas e relacionamentos, mas sem a preocupação de como o dado será gravado no disco, tipos de dados, atributos, identificadores, índices para pesquisa. Basicamente desenhando como será implementado ao nível técnico o projeto de banco de dados.
    
- **Nível Físico**
    
    Nível de abstração mais baixo, ou seja, demonstra como os dados serão armazenados fisicamente no disco.
    

---

🆙 [Índice](https://www.notion.so/Introdu-o-a-Modelagem-de-Dados-8c48cbaf9e8f44c6972869b37d26d9e2)

# Modelo de dados

O modelo de dados é a forma pela qual descrevemos o projeto de banco de dados. Representa todos os dados, como se dados se relacionam e as possíveis restrições. 

![1.modelo-de-dados.png](1.modelo-de-dados.png)

## Elementos

São subdivididos em três categorias:

- Entidades: conjunto de elementos que possuem características próprias, exemplo um sistema para frota de veículos de aluguel, onde o veículo, o atendente, o cliente são exemplos de entidade.
- Atributos: representam as características de uma entidade, exemplos são características do cliente como nome, endereço, CPF, bandeira do cartão de crédito, placa do veículo, cor, modelo, etc.
- Relacionamentos: vínculos ou associações entre entidades, exemplo o relacionamento de locação de um veículo por um cliente.

### Entidade

Principal item de um modelo de dados, o primeiro detalhe que um analista de banco de dados deve listar. As características que indicam uma entidade dentro de requisitos levantado com o cliente do sistema de banco de dados são:

- Objetos sobre os quais é preciso armazenar informação
- Conjunto de vários elementos (mais que 1).
- Conjunto de elementos distinguíveis que aceitam um código para diferenciá-los.
- Seus atributos NÃO dependem de outras entidades.
- Exemplos: pessoas, locais, objetos, documentos, etc.

Representação de uma entidade na modelagem é feita pelo retângulo contendo o nome da entidade no centro. As linhas indicam os atributos da entidade. 

![2 — Exemplos de Entidades](2-entidades.png)

2 — Exemplos de Entidades

## Atributos

São informações úteis que caracterizam uma entidade ou relacionamento. Os atributos de uma entidade permanecem constantes para todos os relacionamentos. Os atributos de uma entidade são independentes das demais entidades. 

Representado por uma linha, ligada a entidade (retângulo), com um círculo no final e o nome do atributo. Existem três tipos de atributos:

- **Chave**
    - Seu valor representa um elemento da entidade.
    - Seu valor é único para a entidade
    - Deve ser sublinhado
    - Exemplos: código, matrícula, número de série, etc.
- **Composto**
    - Necessita ser dividido em sub-atributos para que seu significado seja melhor compreendido.
    - Exemplo: endereço, telefone, etc.
- Multi-valorado
    - Pode assumir mais do que um valor para cada entidade.
    - Exemplo: Telefone, onde tem os telefones residenciais, celulares e comerciais.

![3 — Exemplo de Atributos](3-atributos.png)

3 — Exemplo de Atributos

![4 — Exemplo de Atributo Composto](4-atributo-composto.png)

4 — Exemplo de Atributo Composto

![5 — Exemplo Atributo Multi-valorado](5-atributo-multivalorado.png)

5 — Exemplo Atributo Multi-valorado

![6 — Exemplo de Atributo Multi-valorado e Composto](6-caso-atributos-multivalorados-compostos.png)

6 — Exemplo de Atributo Multi-valorado e Composto

## Entidades Fracas

São entidades que dependem de uma outra entidade, sua existência só pode ser determinada a partir da existência de uma "entidade forte". Entidade Fraca é representada por:

- Dependência de Existência

Utilizado em casos que uma entidade só pode existir se outra entidade existe. Exemplo: dependente de um funcionário.

![7 - Entidade Fraca](7-entidade-fraca.png)

7 - Entidade Fraca

![8 — Exemplo de Entidade Fraca - Dependência de Existência](8-entidade-fraca.png)

8 — Exemplo de Entidade Fraca - Dependência de Existência

- Dependência de Identificador.

Utilizada quando uma entidade precisa de atributos de outra entidade. Exemplo: declaração de IR, que possui seus próprios atributos, mas só pertence a 1 contribuinte. 

![9 — Exemplo de Entidade Fraca - Dependência de Identificador](9-entidade-fraca-dependencia-indentificador.png)

9 — Exemplo de Entidade Fraca - Dependência de Identificador

---

🆙 [Índice](https://www.notion.so/Introdu-o-a-Modelagem-de-Dados-8c48cbaf9e8f44c6972869b37d26d9e2)

# Relacionamento

Representa a associação entre entidades, representam os vínculos que existem entre as entidades no mundo real. 

São representados por losangos.

Exemplo: Um sistema de controle acadêmico o relacionamento MATRÍCULA, vincula um ALUNO a uma DISCIPLINA.

Os relacionamentos são divididos em graus que é igual à quantidade de entidades vinculadas na relação. 

![10 — Grau de Relacionamento](10-grau-relacionamento.png)

10 — Grau de Relacionamento

## Classe ou Cardinalidade

Identifica quantas vezes cada instância de uma entidade pode participar do relacionamento. Para relacionamentos binários temos classes:

- 1:1 (Um para um)
- 1:N (Um para N ou muitos)
- N:N (N para N ou muitos para muitos)

![11 — Exemplo de Classe ou Cardinalidade](11-classe-cardinalidade.png)

11 — Exemplo de Classe ou Cardinalidade

![12 — Exemplo de Classe 1:1 (um para um)](12-classe-1-1.png)

12 — Exemplo de Classe 1:1 (um para um)

![13 — Exemplo de Classe 1:N (um para muitos)](13-classe-1-N.png)

13 — Exemplo de Classe 1:N (um para muitos)

![14 — Exemplo de Classe N:1 (muitos para um)](14-classe-N-1.png)

14 — Exemplo de Classe N:1 (muitos para um)

![15 — Exemplo de Classe 1:N (um para muitos)](15-exemplo-classe-1-N.png)

15 — Exemplo de Classe 1:N (um para muitos)

![16 — Exemplo de Classe N:N (muitos para muitos)](16-classe-N-N.png)

16 — Exemplo de Classe N:N (muitos para muitos)

![17 — Exemplo de Classe N:N (muitos para muitos)](17-classe-N-N.png)

17 — Exemplo de Classe N:N (muitos para muitos)

## Atributos de Relacionamentos

Pouco utilizado, uma vez que duranta a análise e modelagem de banco de dados, os atributos de relacionamento acabam sendo consolidados em uma entidade própria.

Por exemplo: um fornecedor pode vender vários produtos, assim como um produto pode ser vendido por vários fornecedores, nesse caso os atributos preço, quantidade e prazo, pertencerão a qual entidade? 

![18 — Exemplo Atributos de Relacionamentos](18-atributos-relacionamento.png)

18 — Exemplo Atributos de Relacionamentos

Analisando o caso, atribuir preço, quantidade e prazo aos produtos não é possível visto que a entidade produtos se relaciona muitos produtos se relacionam com diversos fornecedores (N:N) e cada fornecedor pode vender o mesmo produto por valores diferentes, por exemplo. Além de que, um produto pode sofrer alterações sazonais no preço, prazos e condições de pagamento.

A mesma lógica se aplica ao fornecedor caso os atributos sejam parte desta entidade. 

A solução é levar os atributos para a relação, sendo assim, a cada relacionamento de venda ou compra, são registrados os valores dos atributos. 

![19 — Exemplo de Atributos de Relacionamentos](19-exemplo-atributo-relacionamento.png)

19 — Exemplo de Atributos de Relacionamentos

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

# Identificando as entidades e seus atributos

1. Empregados
    1. Nome
    2. E-mail
    3. Data_admissão
    4. Sobrenome
2. Departamentos
    1. Nome Departamento
3. Cargos
    1. Nome cargo
4. Localidades
    1. Endereço
    2. Cidade
    3. Estado
5. Países
    1. Nome país
6. Regiões
    1. Nome região
7. Histórico Cargo
    1. Data início
    2. Data fim

![3-modelo-conceitual.png](3-modelo-conceitual.png)

---
#modelagem #bancodedados
