# Introdução ao MySQL
A entidade maior é o próprio banco de dados, ele é um repósitório que armazena dados e podem ser recuperados. Os dados ficam armazenados no disco rígido, ou seja, ocupa espaço no disco. 

No banco de dados há diversas **entidades** que são estruturas que organizam como os dados são armazenados. Uma das principais entidades é a **tabela**, podendo conter várias no mesmo banco de dados. 

Uma tabela é análoga a uma planilha do Excel, que contém colunas e linhas. Mas, diferente da planilha, que permite inserir dados de qualquer tipo em suas células, no banco de dados é preciso estabelecer **definições** do que ela abrangerá. 

Uma das definições básicas na criação de uma tabela é a quantidade de campos e quais os tipos de dados de cada campo. O **campo** é a **coluna**.

Os valores de cada campo não podem ser diferentes do que foi definido na criação.

Cada linha da tabela é chamado de **registro**, irrestrito.

Outro conceito básico é a chamada **chave primária**, ao criar uma nova tabela podemos definir ou não. A chave primária define que no campo que foi configurado a combinação de caracteres não podem se repetir, exemplo são códigos de identificação como CPF. 

> [!attention] 
> Tabelas com chave primária definida proibem que haja mais de um registro com a mesma chave primária.

**Chaves primária composta**, são dois ou mais campos definidos cujo a combinação dos seus valores não podem repetir entre os registros.

A **chave estrangeira** cria uma ligação (relacionamento) entre duas ou mais tabelas, por exemplo, uma tabela de cadastro de clientes e uma tabela de vendas, cujo o campo CPF indica para qual cliente cada venda foi feita. O valor de um CPF na tabela de vendas precisa ser necessáriamente pré-cadastrado na tabela de clientes.

As tabelas contam também com **índice** que é um instrumento que facilita a localização de cada registro. 

Quando temos uma chave estrangeira, automaticamente o banco de dados cria índices nos campos que se interrelacionam, para que seja viável, por exemplo, ao cadastrar um cliente na `tabela_vendas` o banco de dados, internamente, verifique se o cliente consta na `tabela_cadastro_clientes` e para encontrar rápido é proveitoso que a tabela original já possua índice.

Um grupo de tabelas são chamados de **esquemas (Schemas)** é o conjunto de tabelas que representam o mesmo assunto. As tabelas de esquemas diferentes podem se relacionar, o esquema está mais relacionado a organização.

O banco de dados também possui a **View (visão)** que é um agrupamento de tabelas utilizando uma query (consulta) que retorna não só informações de uma determinada tabela, mas de duas ou mais através das chaves estrangeiras. Apos conseguir unir duas ou mais tabelas e gerar um resultado para essa consulta, podemos transforma-lá em uma view.

>[!info]
>Isso significa que a view possui um comportamento similar a tabela, mas que por trás dela já há uma consulta estabelecida com as regras de negócio para agrupar as informações solicitadas.

Temos no SQL **comandos de consultas (queries)** ao realizar consultas precisamos definir em quais tabelas gostariamos de buscar determinadas informações. 

Internamente o banco de dados também possui as **procedures** que permite criar comandos SQL para fazer algum tipo de lógica etruturada com `if`, `while` entre outros comandos de repetição por exemplo. Também dentro das procedures podemos ter as **funções**. Essas são cálculos montados com campos que podem usar dentro de um comando de consulta. 

O SQL já possui algumas funções nativas para diversos tipos de tarefas, como por exemplo, exluir espaços em branco, cálulos entre datas ou numéricos entre outros. Porém o SQL permite que construamos as nossas próprias funções.

No banco de dados também temos o **trigger**, que é um aviso programado caso algo ocorra no banco de dados ou tabela. Esse trigger pode executar uma função, uma procedure ou um único comando SQL quando uma condição for satisfeita.

---

