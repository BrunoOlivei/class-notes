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

Retorna todos os registros da tavela direita e os correspondentes da tabela esquerda

```MySQL
SELECT E.NomeCompleto, B.Nota1, B.Nota2, B.Nota3
FROM Boletim B
RIGHT JOIN Estudante E
ON B.RegistroAluno = E.RegistroAluno;
```

Quando colocadoo where com comparação de null, ele se torna excludente e traz todos os registros da tabela direita, exceto os que fazem match com a tabela esquerda.

```MySQL
SELECT E.NomeCompleto, B.Nota1, B.Nota2, B.Nota3
FROM Boletim B
RIGHT JOIN Estudante E
ON B.RegistroAluno = E.RegistroAluno
WHERE B.RegistroAluno IS NULL;
```

## FULL \[OUTER] JOIN

