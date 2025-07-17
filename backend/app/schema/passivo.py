from datetime import date, datetime
from zoneinfo import ZoneInfo
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class PassivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do passivo")
    descricao: Optional[str]
    valor: float = Field(..., ge=0, description="Valor do passivo")
    referente: str = Field(
        ..., description="A associação do passivo, ex: Saúde, Lazer, Boleto"
    )
    data: date = Field(..., description="Data que foi adquirido o passivo")
    fixo: Literal["S", "N"]
    vencimento: Optional[date]
    plano: Optional[Literal["D", "M", "S"]]
    id_conta: int = Field(..., gt=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class PassivoOutputSchema(PassivoSchema):
    id: int = Field(..., gt=0)


class PassivoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    passivo: PassivoOutputSchema = Field(..., description="Passivo")
    data: datetime = Field(
        datetime.now(ZoneInfo("America/Bahia")), description="Data e hora da resposta"
    )

    model_config = ConfigDict(from_attributes=True)
