from datetime import date, datetime
from zoneinfo import ZoneInfo
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class AtivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do ativo")
    descricao:  Optional[str]
    valor: float = Field(..., ge=0, description="Valor do ativo")
    referente: str = Field(
        ..., description="A associação do ativo, ex: Salario, Freelancer, Empréstimo"
    )
    data: date = Field(..., description="Data que foi adquirido o ativo")
    fixo: Literal["S", "N"]
    tipo_remuneracao: Optional[Literal["Q", "M", "S"]]
    finalizado:  Optional[date]
    id_conta: int = Field(..., gt=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class AtivoOutputSchema(AtivoSchema):
    id: int = Field(..., gt=0)


class AtivoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    ativo: AtivoOutputSchema = Field(..., description="Ativo")
    data: datetime = Field(
        datetime.now(ZoneInfo("America/Bahia")), description="Data e hora da resposta"
    )

    model_config = ConfigDict(from_attributes=True)
