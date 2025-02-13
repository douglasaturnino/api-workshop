from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config import get_db
from app.model import Produto
from app.schema import ProdutosSchema

router = APIRouter()
produtos = Produto()


@router.get("/")
def ola_mundo():
    return {"mensagem": "Olá, mundo!"}


@router.get("/produtos", response_model=List[ProdutosSchema])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(Produto).all()


@router.get("/produtos/{produto_id}", response_model=ProdutosSchema)
def buscar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    return produto


@router.post("/produtos", response_model=ProdutosSchema, status_code=201)
def adicionar_produto(produto: ProdutosSchema, db: Session = Depends(get_db)):
    db_produto = Produto(**produto.model_dump())
    db.add(db_produto)
    db.commit()
    db.refresh(db_produto)
    return db_produto


@router.delete("/produtos/{produto_id}", status_code=204)
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()
    return produto


@router.put("/produtos/{produto_id}", response_model=ProdutosSchema)
def atualizar_produto(
    produto_id: int,
    produto_data: ProdutosSchema,
    db: Session = Depends(get_db),
):
    db_produto = db.query(Produto).filter(Produto.id == produto_id).first()
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    for key, value in produto_data.model_dump().items():
        setattr(db_produto, key, value) if value else None

    db.commit()
    db.refresh(db_produto)
    return db_produto
