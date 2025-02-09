from fastapi import FastAPI

from app.data import Produto
from app.schema import ProdutosSchema

app = FastAPI()
produtos = Produto()


@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá, mundo!"}


@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return produtos.listar_produtos()


@app.get("/produtos/{id}", response_model=ProdutosSchema)
def buscar_produto(id: int):
    return produtos.buscar_produto(id)


@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return produtos.adicionar_produto(produto.model_dump())
