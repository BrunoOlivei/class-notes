[[Manipulando Banco de Dados#Criando a primeira tabela]]

# Criando tabelas a partir de consultas

```MySQL
-- Criando tabelas com base em consultas

CREATE TABLE Professor AS
SELECT NomeCompletoFuncionario, Salario
FROM Funcionario;

INSERT INTO professor (RegistroProfessor, NomeCompletoProfessor)
SELECT RegistroFuncionario, NomeCompletoFuncionario FROM Funcionario;

INSERT INTO Professor (RegistroProfessor, RegistroFuncionario, NomeCompletoProfessor)
SELECT
	1883 AS RegistroProfessor,
    (SELECT MAX(RegistroFuncionario) FROM Funcionario) AS RegistroFuncionario, -- Cria na coluna RegistroFuncionario utilizando o valor máximo da tabela Funcionários
    'Robin Williams' AS NomeCompletoProfessor;
```

# JOIN

A forma mais usada para juntar duas ou mais tabelas diferentes para realizar consultas mais enxutas, porém há mais de uma forma de fazer essa junção:

## CROSS JOIN

A variação menos utilizada, onde cruza os dados da tabela da esquerda para a direita gerando um produto cartesiano basicamente multiplicando o número de linhas de uma tabela pela outra, consumindo muito recurso computacional por exemplo, a realização de um `cross join` de uma tabela com 20 linhas e outra com 115 resulta em uma de 2300 linhas.

```MySQL
SELECT E.NomeCompleto, P.NomeCompleto
FROM Estudante E CROSS JOIN Professor P;
```

No exemplo acima estamos mostrando o nome de todos os professores e todos os alunos como se todos os professores dessem aula para todos os estudantes.

## INNER JOIN

Um dos mais utilizados, retorna os registros de duas ou mais tabelas que satisfaçam uma condição,  ou seja que possuem algo em comum entre elas.

Por padrão o comando `JOIN` já faz esse processo, sem a necessidade de explicitar `INNER`

![[Pasted image 20221106150327.png]]

```MySQL
SELECT P.NomeCompletoProfessor, F.Salario
FROM Professor P INNER JOIN Funcionario F
ON P.RegistroFuncionario = F.RegistroFuncionario;

SELECT P.NomeCompletoProfessor, F.Salario
FROM Professor P JOIN Funcionario F
ON P.RegistroFuncionario = F.RegistroFuncionario
WHERE sALARIO > 1700.00;

SELECT P.NomeCompletoProfessor, D.Descricao, E.NomeCompleto
FROM Professor P JOIN Disciplina D
ON P.RegistroProfessor = D.RegistroFuncionario
JOIN Estudante 
```

## LEFT \[OUTER] JOIN

Enquanto o `INNER JOIN`  foca na parte interna da intersecção entre duas tabelas, como no diagrama de Venn, o `OUTER JOIN` foca na parte externa, pegando mais de uma das entidades do que da outra.

```MySQL
SELECT P.NomeCompletoProfessor, D.Descricao
FROM Professor P
LEFT JOIN Disciplina D
ON P.RegistroProfessor = D.RegistroProfessor;
```

Retorna todos os registros da tabela esquerda e os correspondentes da tabela direita.

```MySQL
SELECT P.NomeCompletoProfessor, D.Descricao
FROM Professor P
LEFT JOIN Disciplina D
ON P.RegistroProfessor = D.RegistroProfessor
WHERE D.RegistroProfessor IS NULL;
```

Quando colocado o `WHERE` com comparação de `NULL`, ele se torna excludente e traz todos os registros da tabela esquerda, exceto os que fazem match com a tabela da direita.

## RIGTH \[OUTER] JOIN

Retorna todos os registros da tabela direita e os correspondentes da tabela esquerda

```MySQL
SELECT E.NomeCompleto, B.Nota1, B.Nota2, B.Nota3
FROM Boletim B
RIGHT JOIN Estudante E
ON B.RegistroAluno = E.RegistroAluno;
```

Quando colocado o where com comparação de null, ele se torna excludente e traz todos os registros da tabela direita, exceto os que fazem match com a tabela esquerda.

```MySQL
SELECT E.NomeCompleto, B.Nota1, B.Nota2, B.Nota3
FROM Boletim B
RIGHT JOIN Estudante E
ON B.RegistroAluno = E.RegistroAluno
WHERE B.RegistroAluno IS NULL;
```

## FULL \[OUTER] JOIN

Trás os dados que estão em ambas as tabelas.

```MySQL
SELECT L.Cidade, V.Quantidade
FROM Lojas L
FULL JOIN Vendas V
ON L.IdLoja = V.IdLoja;
```

Quando utilizado o NULL, ele retorna os dados excludentes, ou seja, os dados que não se relacionam entre as tabelas.

```MySQL
SELECT L.Cidade, V.Quantidade
FROM Lojas L
FULL JOIN Vendas V
ON L.IdLoja = V.IdLoja
WHERE L.IdLoja IS NULL OR V.IdLoja IS NULL;
```

# Operadores

Aritméticos, relacionais, lógicos e auxiliares.

## Aritméticos

| Operador |     Operação      |
|:--------:|:-----------------:|
|    +     |      adição       |
|    -     |     subtração     |
|    *     |   multiplicação   |
|    /     |      divisão      |
|    %     | restro da divisão |

```MySQL
SELECT 1 + 2 + 3 AS SOMA;

SELECT (1 + 2) * 3 AS UmMaisDoisVezesTres;

SELECT Salario + 10
FROM Funcionario;

SELECT Salario * 0,90
FROM Funcionario;

SELECT Nota1, Nota2, Nota3, (Nota1 + Nota2 + Nota3) AS SomaNotas
FROM Boletim
WHERE RegistroAluno = 561257;
```

## Relacionais

| Operador |     Operação     |
|:--------:|:----------------:|
|    >     |    maior que     |
|    <     |    menor que     |
|    =     |     igual a      |
| <> ou != |   diferente de   |
|    >=    | maior ou igual a |
|    <=    | menor ou igual a |

```MySQL
SELECT *
FROM Funcionario
WHERE salario > 1500;

SELECT *
FROM Funcionario
WHERE salario < 1500;

SELECT *
FROM Funcionario
WHERE Cidade = 'Curitiba';

SELECT *
FROM Funcionario
WHERE Cidade <> 'Curitiba';

SELECT *
FROM Funcionario
WHERE salario >= 1500;

SELECT *
FROM Funcionario
WHERE salario <= 1500;
```

## Lógicos

| Operador |    Operação    |
|:--------:|:--------------:|
|   AND    | E (Conjugação) |
|    OR    | OU (Disjunção) |
|   NOT    |    Negação     |

```MySQL
SELECT *
FROM Funcionario
WHERE Cidade = 'Curitiba'
AND Salario = 1500;

SELECT *
FROM Funcionario
WHERE Cidade = 'Curitiba'
OR Salario = 1500;

SELECT *
FROM Funcionario
WHERE NOT Cidade = 'Curitiba';
```

## Auxiliares

| Operador |                    Operação                    |
|:--------:|:----------------------------------------------:|
| IS NULL  |          Verifica se o campo é vazio           |
| BETWEEN  | Verifica se um campo está num range de valores |
|    IN    |      Verifica se o valor existe na tabela      |
|   LIKE   |     Verifica buscando valores semelhantes      |

```MySQL
SELECT *
FROM Funcionario
WHERE Cidade IS NULL;

SELECT *
FROM Funcionario
WHERE Salario BETWEEN 1000 AND 2000;

SELECT *
FROM Funcionario
WHERE Cidade IN ('Curitiba', 'Londrina');

SELECT *
FROM Funcinario
WHERE Cidade NOT IN ('Curitiba', 'Londrina');

SELECT * 
FROM Funcionario
WHERE NomeCompletoFuncionario LIKE 'Maria%'; -- Percentual no final permite procurar o termo em questão no início mesmo que haja outros caracteres na string

SELECT *
FROM Funcionario
WHERE NomeCompletoFuncionario LIKE '%Silva'; -- Percentual no começo permite procurar o termo em questão no final mesmo que haja outros caracteres na string

SELECT *
FROM Funcionario
WHERE NomeCompletoFucionario LIKE '%ada%'; -- Percentual no inicio e fim permite procurar o termo em questão em qualquer local da string.

SELECT *
FROM Funcionario
WHERE NomeCompletoFuncionario = 'Maria%' -- O igual vai consultar os valores que possuem Maria e % na string, ou seja, a busca será literal, e não como no LIKE
```

# Data e Hora

- `GETDATE()`: data atual do sistema
- `DAY()`: dia da data fornecida entre parênteses
- `MONTH()`: mês da data fornecida entre parênteses
- `YEAR()`: ano da data fornecida entre parênteses
- `DATEADD(DAY, 5, <campo>)`: acrescenta 5 dias na data fornecida
- `DATEADD(MONTH, 4, <campo>)`: acrescenta 4 meses na data fornecida
- `DATEADD(YEAR, 7, <campo>)`: acrescenta 7 anos na data fornecida
- `DATEDIFF(DAY, <campo>, GETDATE())`: diferença em dias da data do campo e a data de hoje
- `DATENAME(WEEKDAY, <campo>)`: exibe o nome do dia da semana da data fornecida.

# Funções de agregação
 `COUNT`, `AVG`, `SUM`, `MAX`, `MIN`

## `COUNT` (Contagem)

```MySQL
-- Quantidade de registros existentes
SELECT COUNT(*)
FROM Funcionario;

-- Quantidade de cidades diferentes existentes
SELECT COUNT(DISTINCT Cidade)
FROM Funcionario;

-- Quantidade de registros existentes da cidade de Londrina
SELECT COUNT(*)
FROM Funcionario
WHERE Cidade = 'Londrina';
```

## `AVG` (Média)

```MySQL
-- Média dos salários dos funcionários
SELECT AVG(Salario)
FROM Funcionario;

-- Média dos salários diferentes dos funcionários
SELECT AVG(DISTINCT Salario)
FROM Funcionario;

-- Média dos salários dos funcionários de Londrina
SELECT AVG(Salario)
FROM Funcionario
WHERE Cidade = 'Londrina';
```

## `SUM` (Soma)

```MySQL
-- Soma dos ssalários dos funcionários
SELECT SUM(Salario)
FROM Funcionario;

-- Soma dos salários diferentes dos funcionários
SELECT SUM(DISTINCT Salario)
FROM Funcionario;

-- Soma dos salários dos funcionários de Londrina
SELECT SUM(Salario)
FROM Funcionario
WHERE Cidade = 'Londrina';
```

## `MAX` (Máximo) `MIN` (Mínimo)

```MySQL
-- Maior salário dos funcionarios
SELECT MAX(Salario)
FROM Funcionario;

-- Menor salário dos funcionários
SELECT MIN(Salario)
FROM Funcionario;
```

# Agrupamento de dados

## `GROUP BY`

Usado junto com as funções de agregação

```MySQL
-- Quantidade de funcionários por cidade
SELECT Cidade, COUNT(*)
FROM Funcionario
GROUP BY Cidade;

-- Quantidade de funcionários por cidade que sejam maiores que 7
SELECT Cidade, COUNT(*)
FROM Funcionario
GROUP BY Cidade
HAVING COUNT(*) > 7;
```

