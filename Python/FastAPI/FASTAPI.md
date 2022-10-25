# Instalação

```powershell
> pip install fastapi uvicorn
```

# Primeira API

```python
**from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}**
```

## Iniciando aplicação

```powershell
> uvicorn main:app

INFO:     Started server process [9520]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

## Para utilizar o python para executar:

```python
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="info")
```

Dessa forma podemos executar o comando `python <nome do arquivo.py>` para executar

## Acesso remoto para usuários na mesma rede

```python
if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
```

Dessa maneira podemos passar o IP da máquina que está localizado o arquivo e em execução com a porta 8000 para qualquer pessoa  que esteja conectada na mesma rede wifi ter acesso a aplicação

## Básico Deploy

A forma como é realizado o deploy é um pouco diferente, basicamente precisamos instalar o pacote `gunicorn`

Com esse pacote instalado podemos executar o comando:

```python
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

O `-w 4` refere-se a quantos servidores (workers) queremos que ele inicie. O `-k uvicorn.workers.UvicornWorker` indica qual a classe que ele execute.

# CRUD básico

Utilizando a memória local na aplicação:

```python
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import Response
from models import Curso

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação para Leigos",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmos e Lógica de Programação",
        "aulas": 87,
        "horas": 67
    }
}

@app.get("/cursos")
async def get_cursos():
    return cursos

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int):  # typehints para o parâmetro indica que o input deve ser um inteiro
    # Tenta acessar o curso com ID informado
    try:
        curso = cursos[curso_id]
    # Se não encontrar, retorna erro 404 (Not Found) com mensagem "Curso não encontrado"
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso

@app.post("/cursos", status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

@app.put("/cursos/{curso_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

# Limitando o range de parâmetros passados da URI

Utilizando o exemplo acima, de uma aplicação para uma escola de programação, suponhamos que desejamos limitar o range do parâmetro id, ou seja, se tivermos até 2 cursos, limitar para receber apenas 1 ou 2. 

O *path parameter* é o parâmetro passado na URI

```python
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from models import Curso

from fastapi import Path # Lib necessária para o path parameters

@app.get("/cursos/{curso_id}")
async def get_curso(curso_id: int = Path(default=None, 
                                         title="ID do curso", 
                                         description="Deve ser entre 1 e 2", 
                                         gt=0, 
                                         lt=3)):
# A classe Path possui como parametro obrigatório o default,   
    # Tenta acessar o curso com ID informado
    try:
        curso = cursos[curso_id]
    # Se não encontrar, retorna erro 404 (Not Found) com mensagem "Curso não encontrado"
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

    return curso
```

Passando ID 3 (não existe) como parâmetro na URI recebemos como resultado:

```json
{
    "detail": [
        {
            "loc": [
                "path",
                "curso_id" # Title
            ],
            "msg": "ensure this value is less than 3", # Retorno do lt
            "type": "value_error.number.not_lt",
            "ctx": {
                "limit_value": 3
            }
        }
    ]
}
```