from datetime import date, datetime
from zoneinfo import ZoneInfo
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class InvestimentoSchema(BaseModel):

    nome: str = Field(..., description="Nome do investimento")
    descricao: Optional[str]
    tipo: Literal["A", "FII", "C", "ETF", "ETFI", "AI", "TD", "RF"] = Field(
        ..., description="Tipo de investimento"
    )
    valor: float = Field(..., ge=0, description="Valor do investimento")
    data_adquirido: date = Field(
        ..., description="Data que foi adquirido o investimento"
    )
    conta_id: int = Field(..., gt=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class InvestimentoOutputSchema(InvestimentoSchema):
    id: int = Field(..., gt=0)


class InvestimentoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    investimento: InvestimentoOutputSchema = Field(..., description="Investimento")
    data_hora: datetime = Field(..., description="Data e hora da resposta")

    model_config = ConfigDict(from_attributes=True)
