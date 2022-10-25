from time import sleep
from models import Curso
from typing import Optional, Any, Dict
from fastapi import FastAPI, Request, status, Response, HTTPException, Path, Query, Header, Depends
from fastapi.responses import JSONResponse


def fake_db():
    try:
        print("Abrindo conxão com banco de dados...")
        sleep(1)
    finally:
        print("Fechando conxão com banco de dados...")
        sleep(1)


app = FastAPI(
    title="Curso FastAPI", description="Curso de FastAPI", version="0.1.0")

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


@app.get("/cursos",
         description="Retorna todos os cursos",
         summary="Retorna todos os cursos",
         response_model=Dict[int, Curso])
async def get_cursos(db: Any = Depends(fake_db)):
    return cursos


@app.get("/cursos/{curso_id}")
async def get_curso(request: Request, curso_id: int = Path(default=None,
                                         title="ID do curso",
                                         description="Deve ser entre 1 e 2",
                                         gt=0,
                                         lt=5), db: Any = Depends(fake_db)):
    # Tenta acessar o curso com ID informado
    try:
        curso = cursos[curso_id]
    # Se não encontrar, retorna erro 404 (Not Found) com mensagem "Curso não encontrado"
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
    # Se encontrar, retorna o curso
    else:
        return curso


@app.post("/cursos", status_code=status.HTTP_201_CREATED, response_model=Curso)
async def post_curso(curso: Curso, db: Any = Depends(fake_db)):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso


@app.put("/cursos/{curso_id}", status_code=status.HTTP_202_ACCEPTED)
async def put_curso(curso_id: int, curso: Curso, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        cursos[curso_id] = curso
        del curso.id

        return curso
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.delete("/cursos/{curso_id}")
async def delete_curso(curso_id: int, db: Any = Depends(fake_db)):
    if curso_id in cursos:
        del cursos[curso_id]
        # return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@app.get('/calculador')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=10), x_geek: str = Header(default=None), c: Optional[int] = None):
    soma: int = a + b
    if c:
        soma += c
    print("x_geek:", x_geek)
    return {'resultado': soma}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
