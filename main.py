from typing import Dict, List

from fastapi import FastAPI

app = FastAPI()

produtos: List[Dict[str, any]] = [
    {
        "id": 1,
        "nome": "Smartphone",
        "descricao": "Um smartphone de última geração",
        "preco": 1500.00,
    },
    {
        "id": 2,
        "nome": "Notebook",
        "descricao": "Um notebook de última geração",
        "preco": 3500.00,
    },
    {
        "id": 3,
        "nome:": "Tablet",
        "descricao": "Um tablet de última geração",
        "preco": 2000.00,
    },
]


@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá, mundo!"}


@app.get("/produtos")
def listar_produtos():
    return produtos
