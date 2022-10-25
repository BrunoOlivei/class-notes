from typing import Optional
from pydantic import BaseModel, validator


# Cria um objeto modelo para representar um curso e validar o dado no momento da criação
class Curso(BaseModel):
    id: Optional[int] = None  # ID do curso é opcional
    titulo: str  # Título do curso
    aulas: int  # Número de aulas
    horas: int  # Número de horas

    @validator('titulo')
    def titulo_validator(cls, valor: str):
        palavras = valor.split(" ")
        if len(palavras) < 3:
            raise ValueError("Título deve conter pelo menos 3 palavras")

        return valor
