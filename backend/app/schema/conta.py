from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class ContaSchema(BaseModel):

    nome: str = Field(..., description="Nome do Conta")
    descricao: Optional[str]

    model_config = ConfigDict(from_attributes=True)


class ContaOutputSchema(ContaSchema):
    id: int = Field(..., gt=0)


class ContaResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    conta: ContaOutputSchema = Field(..., description="Conta")
    data_hora: datetime = Field(...,description="Data e hora da resposta")

    model_config = ConfigDict(from_attributes=True)
