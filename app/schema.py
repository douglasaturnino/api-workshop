from typing import Optional

from pydantic import BaseModel, ConfigDict, PositiveFloat


class ProdutosSchema(BaseModel):
    id: Optional[int] = None
    nome: str
    descricao: Optional[str] = None
    preco: PositiveFloat

    model_config = ConfigDict(from_attributes=True)
