from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, Field


class InvestimentoSchema(BaseModel):

    nome: str = Field(..., description="Nome do investimento")
    descricao: str
    valor: float = Field(..., ge=0, description="Valor do investimento")
    data: date = Field(..., description="Data que foi adquirido o investimento")
    fixo: Literal["S", "N"]
    tipo_remuneracao: Optional[Literal["Q", "M", "S"]]
    id_conta: int = Field(..., ge=0, description="Conta que está relacionado")


class InvestimentoOutputSchema(InvestimentoSchema):
    id: int = Field(..., ge=0)
