-- Crie uma base de dados chamada Campenonato
CREATE DATABASE CAMPEONATO;

USE CAMPEONATO;

-- Crie uma tabela chamada Players, com as seguintes colunas
CREATE TABLE Players (
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(50) NOT NULL,
    date_registration DATE NULL,
    date_last_access DATE NULL,
    salary DECIMAL(10,2) NULL,
    PRIMARY KEY(Id));

-- Insira 6 jogadores na tabela Players
INSERT INTO Players
VALUES 
	(1, 'Camila de Almeida Campos', '2022-09-08', '2022-10-25', 1450.79), 
	(2, 'Oswaldo Cruz de Melo Santos', '2022-09-09', '2022-10-25', 1450.79),
    (3, 'Gabriel dos Santos Silva', '2022-06-22', '2022-10-25', 10204.50),
    (4, 'João Neto Aparecido dos Santos', '2022-04-22', '2022-10-25', 5789.50),
    (5, 'Melanie Vanessa Duarte', '2022-10-22', '2022-10-25', 7655.50),
    (6, 'Guilherme Amaral', '2022-10-22', '2022-10-25', 5000);

-- Mostre todos os jogadores cadastrados.
SELECT * FROM players;

-- Mostre todos os jogadores cadastrados por ordem alfabética de nome
SELECT * FROM players ORDER BY name;

-- Mostre os salários e quantos jogadores possuem aquele salário
SELECT salary, COUNT(*)
FROM players
GROUP BY salary;

-- Mostre apenas os salários duplicados
SELECT salary
FROM players
GROUP BY salary
HAVING COUNT(*) > 1;

-- Traga as informações do jogador com maior salário
WITH max_salary AS (
	SELECT MAX(salary) as salary
    FROM players
    ) SELECT * FROM players WHERE salary = (SELECT salary FROM max_salary);

-- Traga os salários distintos dos jogadores
SELECT DISTINCT(salary)
FROM players;

-- Traga o nome dos funcionários com o salário acima da média.
WITH avg_salary AS (
	SELECT AVG(salary) AS salary
    FROM players
    ) SELECT name
	FROM players
    WHERE salary > (
		SELECT salary
		FROM avg_salary);
        
