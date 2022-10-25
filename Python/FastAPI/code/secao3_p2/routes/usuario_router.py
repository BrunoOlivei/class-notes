from fastapi import APIRouter

router = APIRouter()


@router.get("/api/v1/usuarios")
async def get_usuarios():
    return [
        {"id": 1, "nome": "João"},
        {"id": 2, "nome": "Maria"},
        {"id": 3, "nome": "Pedro"},
        {"id": 4, "nome": "José"},
        {"id": 5, "nome": "Paulo"},
        {"id": 6, "nome": "Rafael"},
        {"id": 7, "nome": "André"},
    ]

