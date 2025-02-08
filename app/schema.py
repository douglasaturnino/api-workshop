from typing import Optional

from pydantic import BaseModel, PositiveFloat


class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat
