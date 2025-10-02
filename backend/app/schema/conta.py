from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ContaSchema(BaseModel):

    nome: str = Field(..., description="Nome do Conta")
    descricao: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class ContaOutputSchema(ContaSchema):
    id: int = Field(..., gt=0)
