USE escola;

CREATE TABLE Estudante (
    RegistroAluno INT NOT NULL,
    NomeCompleto VARCHAR(50) NULL,
    Endereço VARCHAR(100) NULL,
    Cidade VARCHAR(50) NULL,
    DataMatricula DATE NULL,
    NomePai VARCHAR(50) NULL,
    NomeMae VARCHAR(50) NULL,
    PRIMARY KEY(RegistroAluno));

CREATE TABLE Professor (
    RegistroProfessor INT NOT NULL PRIMARY KEY,
    NomeCompletoProfessor VARCHAR(50) NULL,
    Endereço VARCHAR(100) NULL,
    Cidade VARCHAR(50) NULL,
    DataAdmissao DATE NULL);

CREATE TABLE Disciplina (
    RegistroDisciplina INT NOT NULL PRIMARY KEY,
    RegistroProfessor INT NOT NULL,
    Descrição VARCHAR(50) NULL,
    DataCriacao DATE NULL,
    Horário VARCHAR(50) NULL,
    CONSTRAINT fk_RegistroProfessor FOREIGN KEY (RegistroProfessor) REFERENCES professor(RegistroProfessor)
);

ALTER TABLE estudante
ADD Email VARCHAR(100) NULL;

ALTER TABLE estudante
DROP column NomePai;

DROP TABLE inspetores;

INSERT INTO estudante (RegistroAluno, NomeCompleto, Endereço, Cidade, DataMatricula, NomePai, NomeMae)
VALUES (1563881, 'Kaique de Almeida Castro', 'Avenida Paulista 21', 'São Paulo', '2010-09-21', 'Valdemir Francisco Castro', 'Inês de Almeida Castro');

UPDATE estudante
SET Endereço = 'Av Paulista, 790 - Bela Vista'
WHERE RegistroAluno = 1563881;

DELETE FROM estudante
WHERE RegistroAluno = 561257;

SELECT NomeCompleto, Cidade
FROM estudante;

SELECT * FROM estudante;

SELECT * FROM estudante
WHERE Cidade = 'São Paulo';

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
