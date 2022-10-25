from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/cursos")
async def get_cursos():
    return [
        {"id": 1, "nome": "Python"},
        {"id": 2, "nome": "Java"},
        {"id": 3, "nome": "C#"},
        {"id": 4, "nome": "C++"},
        {"id": 5, "nome": "PHP"},
        {"id": 6, "nome": "JavaScript"},
        {"id": 7, "nome": "C"},
        {"id": 8, "nome": "Cobol"},
        {"id": 9, "nome": "Assembly"}
    ]

