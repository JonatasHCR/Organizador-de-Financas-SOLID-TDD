from datetime import date, datetime
from zoneinfo import ZoneInfo
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class InvestimentoSchema(BaseModel):

    nome: str = Field(..., description="Nome do investimento")
    descricao: str
    valor: float = Field(..., ge=0, description="Valor do investimento")
    data: date = Field(..., description="Data que foi adquirido o investimento")
    fixo: Literal["S", "N"]
    tipo_remuneracao: Optional[Literal["Q", "M", "S"]]
    id_conta: int = Field(..., ge=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class InvestimentoOutputSchema(InvestimentoSchema):
    id: int = Field(..., ge=0)


class InvestimentoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    ativo: InvestimentoOutputSchema = Field(..., description="Investimento")
    data: datetime = Field(
        datetime.now(ZoneInfo("America/Bahia")), description="Data e hora da resposta"
    )

    model_config = ConfigDict(from_attributes=True)
