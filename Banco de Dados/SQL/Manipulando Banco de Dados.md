# Criando um banco de dados

[MySQL :: MySQL 8.0 Reference Manual :: 13.1.12 CREATE DATABASE Statement](https://dev.mysql.com/doc/refman/8.0/en/create-database.html)

```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name;
```

Onde `db_name`, será o nome do banco de dados. Ainda podemos adicionar algumas informações de metadados, como, por exemplo, o padrão de linguagem UTF-8.

```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name CHARACTER SET [=] charset_name;
```

```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name COLLATE [=] collation_name;
```

Também temos a opção de criptografia, basta adicionar o comando `ENCRYPTION` seguido do caractere entre aspas simples Y

```sql
CREATE {DATABASE | SCHEMA} [IF NOT EXISTS] db_name ENCRYPTION [=] {'Y' | 'N'}
```

## Localizando o banco de dados nos diretórios

`C:\ProgramData\MySQL\MySQL Server 8.0\Data`

---

# Deletando banco de dados

[MySQL :: MySQL 8.0 Reference Manual :: 13.1.24 DROP DATABASE Statement](https://dev.mysql.com/doc/refman/8.0/en/drop-database.html)

```sql
DROP {DATABASE | SCHEMA} [IF EXISTS] db_name
```

---

# TIPOS DE DADOS

[MySQL :: MySQL 8.0 Reference Manual :: 11 Data Types](https://dev.mysql.com/doc/refman/8.0/en/data-types.html)

## Tipos de Dados Numéricos

| Tipo | Valor em Bytes | Menor Valor (com sinal) - Signed | Menor Valor (sem sinal) - Unsigned | Maior Valor (com sinal) - Signed | Maior Valor (com sinal) - Unsigned |
| --- | --- | --- | --- | --- | --- |
| TINYINT | 1 | -128 | 0 | 127 | 255 |
| SMALLINT | 2 | -32768 | 0 | 32767 | 65535 |
| MEDIUMINT | 3 | -8388608 | 0 | 8388607 | 16777215 |
| INT | 4 | -2147483648 | 0 | 2147483647 | 4294967295 |
| BIGINT | 8 | -2xE63 | 0 | 2xE63 - 1 | 2xE64 - 1 |

## Ponto Flutuante

`FLOAT`: precisão simples (4 bytes)

`DOUBLE`: precisão dupla (8 bytes)

Basicamente o `FLOAT` faz um arredondamento das casas decimais, se precisarmos de números com mais precisão, ou seja, mais casas decimais, utilizamos o `DOUBLE`.

### Decimais Fixos

`DECIMAL`

`NUMERIC`

Ambos possuem tamanho de até 65 dígitos. Nesses dois casos se declararmos um campo com DECIMAL (5,2) ou seja, 5 dígitos sendo 2 antes da vírgula, só poderemos armazenar os números - 999,99 a 999,99. 

### Bit

Armazena valores de até 64 bits. Exemplos:

BIT(1) só pode armazenar 1 ou 0.

BIT(2) só pode armazenar 01, 10, 00 ou 11.

### Atributos dos Campos Numéricos

`SIGNED` ou `UNSIGNED`: se o número possuí sinal (+ | -) no número.

`ZEROFILL`: preenche com Zeros os espaços, exemplo, se armazenarmos como INT(4) = 5 será gravado 0005.

`AUTO_INCREMENT`: sequencia auto incrementada, exemplo: 1, 2, 3, 4, 5, ...

### Erros `OUT OF RANGE`

Vão ocorrer quando tentamos preencher um valor numérico maior que está permitido dentro do campo através da especificação do tipo de dado. 

---

## Tipos de Dados de Tempo

`DATE`: 1000-01-01 até 9999-12-31

`DATETIME`: 1000-01-01 00:00:00 até 9999-12-31 23:59:59

`TIMESTAMP`: 1970-01-01 00:00:01 UTC até 2038-01-19 UTC

`TIME`: -838:59:59 até 839:59:59

`YEAR`: 1901 até 2155 (podendo ser expresso no formato de 2 ou 4 dígitos)

---

## Tipos de Dados Texto

### Strings

`CHAR`: cadeia de caracteres com valor fixo (de 0 a 255).

`VARCHAR`: cadeia de caracteres com valor variado (de 0 a 255).

O tipo `CHAR` cria reserva no disco espaço para o total de caracteres que se deseja armazenar, por exemplo: se quisermos armazenar somente as letras 'aa' num campo `CHAR(4)` o banco irá armazenar '  aa'. Já o `VARCHAR` armazena utiliza espaço conforme a necessidade, por exemplo: armazenando as mesmas letras num campo `VARCHAR(4)` temos 'aa' registrado na memória.  

### Strings Binárias

Armazena não os caracteres mas os bites.

`BINARY`: cadeia de caracteres com valor fixo (de 0 a 255) expressos em binários.

`VARBINARY`: cadeia de caracteres com valor variado (de 0 a 255) expressos em binários.

### `TEXT`

Utilizado para armazenar texto e diferem em tamanho reservado pelo banco de dados no disco:

- `TINYTEXT`
- `TEXT`
- `MEDIUMTEXT`
- `LONGTEXT`

### `ENUM`

Esse tipo é utilizado para armazenar valores pré-definidos, por exemplo, uma lista de opções de tamanho para um determinado produto.

Exemplo: Tamanho `ENUM` ('pequeno', 'medio', 'grande', extra_grande')

### Atributos dos campos tipo texto

- `SET` e `COLLATE` são utilizados para estabelecer qual conjunto de caracteres será permitido armazenar, por exemplo, UTF-8. Ou se preferirmos armazenar um alfabeto específico como o árabe ou o russo.

---

## Tipos de dados Binários

### `BLOB` (binário)

Utilizado para armazenar a representação binária de uma foto, por exemplo, e dividido por alguns tipos que diferem no tamanho possível para armazenamento:

- `TINYBLOB`
- `BLOB`
- `MEDIUMBLOB`
- `LONGBLOB`

---

## Tipos de dados espaciais

- GEOMETRY
- POINT
- LINESTRING
- POLYGON

---

# Criando a primeira tabela

[MySQL :: MySQL 5.6 Reference Manual :: 13.1.17 CREATE TABLE Statement](https://dev.mysql.com/doc/refman/5.6/en/create-table.html)

---

```MySQL
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
```

