from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class PassivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do passivo")
    referencia: str = Field(
        ..., description="A associação do passivo, ex: Saúde, Lazer, Boleto"
    )
    descricao: Optional[str]
    valor: float = Field(..., ge=0, description="Valor do passivo")
    data: date = Field(..., description="Data que foi adquirido o passivo")
    eh_fixo: bool = Field(..., description="O passivo ocorre de maneira constante?")
    frequencia: Optional[Literal["D", "M", "S"]]
    vencimento: Optional[date]
    conta_id: int = Field(..., gt=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class PassivoOutputSchema(PassivoSchema):
    id: int = Field(..., gt=0)


class PassivoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    passivo: PassivoOutputSchema = Field(..., description="Passivo")
    data_hora: datetime = Field(..., description="Data e hora da resposta")

    model_config = ConfigDict(from_attributes=True)
