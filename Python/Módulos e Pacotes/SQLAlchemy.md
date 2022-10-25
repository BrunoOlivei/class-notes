# SQLAlchemy

[https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html](https://docs.sqlalchemy.org/en/14/tutorial/dbapi_transactions.html)

# Introdução

## Importando as bibliotecas

```python
**from** sqlalchemy **import** create_engine
**from** sqlalchemy **import** text
```

## Versão utilizada

```python
**import** sqlalchemy
sqlalchemy.__version__
```

`'1.4.32'`

## Conexão

```python
engine **=** create_engine("mssql+pyodbc://@"
                    "BRUNO-OLIVEIRA-/"
                    "qyon_bank"
                    "?trusted_connection=yes"
                    "&driver=SQL+Server+Native+Client+11.0")
```

## Trabalhando de forma textual com SQL

**Criando a conexão em um bloco de contexto**

```python
**with** engine.connect() **as** conn:
    result **=** conn.execute(text("select 'hello world'"))
    print(result.all())
```

`[('hello world',)]`

**Criando a tabela e registrando primeiros dados**

```python
**with** engine.connect().execution_options(autocommit**=True**) **as** conn:
    *# Cria um contexto para conexão com o banco de dados*
    conn.execute(text("CREATE TABLE some_table (x int, y int)")) *# Text é usado para criar o script SQL enquanto execute executa os comandos*
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1},
         {"x": 2, "y": 4},
         {"x": 6, "y": 8},
         {"x": 9, "y": 10}] *# Uma lista contendo os valores, são representações das linhas, enquanto os dicionários e suas chaves representam as colunas, os valores dos dicionarios sãos os dados que serão armazenados*
    )

    *# conn.commit() # commit para registrar os dados no banco.*
```

**Consulta**

```python
**with** engine.connect() **as** conn:
    result **=** conn.execute(text("SELECT x, y FROM some_table")) *# o objeto result é um iterável*
    **for** row **in** result: *# o objeto row é uma tupla*
        print(f"x: {row.x}  y: {row.y}")
```

`x: 1  y: 1
x: 2  y: 4
x: 6  y: 8
x: 9  y: 10`

Podemos acessar os dados da linha (row) utilizando notação ponto para acessar cada elemento da tupla, conforme exemplo acima. Outra forma de acessar os dados é através do índice do elemento `row[0]`. Porém a forma mais pythonica é utilizando o desempacotamento da tupla, atribuindo a variáveis cada elemento.

**Envio de parâmetros**

```python
**with** engine.connect() **as** conn:
    result **=** conn.execute(
        text("SELECT x, y FROM some_table WHERE y > :y"),
        {"y": 2} *#* 
    )
    **for** row **in** result:
        print(f"x: {row.x}  y: {row.y}")
```

`x: 2  y: 4
x: 6  y: 8
x: 9  y: 10`

Em SQL

```sql
BEGIN (implicit)
SELECT x, y FROM some_table WHERE y > ?
[...] (2,)

```

**Enviando vários parâmetros**

```python
with engine.connect() as conn:
    conn.execute(
        text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
        [{"x": 11, "y": 12}, {"x": 13, "y": 14}]
    )
    conn.commit()
```

Em SQL

```sql
BEGIN (implicit)
INSERT INTO some_table (x, y) VALUES (?, ?)
[...] ((11, 12), (13, 14))
<sqlalchemy.engine.cursor.CursorResult object at 0x...>
COMMIT
```

**Sessions** são *commit as you go*, portanto precisam do método `.commit`

---

# Consumindo dados com Pandas DataFrame

```python
import sqlalchemy as db

# Criando a engine
engine = db.create_engine("mssql+pyodbc://@"
                          "BRUNO-OLIVEIRA-/"
                          "qyon_bank"
                          "?trusted_connection=yes"
                          "&driver=SQL+Server+Native+Client+11.0")
# Setando os metadados do banco
metadata = db.MetaData(engine)
# Setando a tabela desejada
table = db.Table('ACCOUNT_ACTIVITY', metadata, autoload=True, autoload_with=engine)

# Setando a query
statement = db.select(table).where(table.c.provider_status == 'CLOSED')

# Utilizando bloco de contexto para conexão
with engine.connect() as conn:
    result = conn.execute(statement) # Executando a query
    df = pd.DataFrame(result.fetchall()) # Transformando em um DataFrame do Pandas

```