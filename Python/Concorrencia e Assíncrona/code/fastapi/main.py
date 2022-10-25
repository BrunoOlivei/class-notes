from fastapi import FastAPI
from pydantic import BaseModel


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


app = FastAPI()

produtos = [
    Produto(id=1, nome="Produto 1", preco=10.0, em_oferta=True),
    Produto(id=2, nome="Produto 2", preco=20.0),
    Produto(id=3, nome="Produto 3", preco=30.0, em_oferta=True),
    Produto(id=4, nome="Produto 4", preco=40.0),
    Produto(id=5, nome="Produto 5", preco=50.0, em_oferta=True),
]


@app.get("/")
async def index():
    return produtos


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    for produto in produtos:
        if produto.id == item_id:
            return produto
    return {"message": "Produto não encontrado"}


@app.put("/items/{item_id}")
async def update_item(item_id: int, produto: Produto):
    for produto_atual in produtos:
        if produto_atual.id == item_id:
            produto_atual = produto
            return produto_atual
    return {"message": "Produto não encontrado"}

