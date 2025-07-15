from datetime import datetime
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field, ConfigDict


class ContaSchema(BaseModel):

    nome: str = Field(..., description="Nome do Conta")
    descricao: str

    model_config = ConfigDict(from_attributes=True)


class ContaOutputSchema(ContaSchema):
    id: int = Field(..., ge=0)


class ContaResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    conta: ContaOutputSchema = Field(..., description="Conta")
    data: datetime = Field(
        datetime.now(ZoneInfo("America/Bahia")), description="Data e hora da resposta"
    )

    model_config = ConfigDict(from_attributes=True)
