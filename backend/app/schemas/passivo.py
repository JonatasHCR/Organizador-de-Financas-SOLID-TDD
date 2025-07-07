from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, Field


class PassivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do passivo")
    descricao: str
    valor: float = Field(..., ge=0, description="Valor do passivo")
    referente: str = Field(..., description="A associação do passivo, ex: Saúde, Lazer, Boleto")
    data: date = Field(..., description="Data que foi adquirido o passivo")
    fixo: Literal["S", "N"]
    vencimento: date
    plano: Optional[Literal["D", "M", "S"]]
    id_conta: int = Field(..., ge=0, description="Conta que está relacionado")


class PassivoCreateSchema(PassivoSchema):
    pass


class PassivoOutputSchema(PassivoSchema):
    id: int = Field(..., ge=0)


class PassivoUpdateSchema(PassivoSchema):
    pass
