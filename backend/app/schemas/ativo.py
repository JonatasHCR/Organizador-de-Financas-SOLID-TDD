from datetime import date
from typing import Literal, Optional

from pydantic import BaseModel, Field


class AtivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do ativo")
    descricao: str
    valor: float = Field(..., ge=0, description="Valor do ativo")
    referente: str = Field(..., description="A associação do ativo, ex: Salario, Freelancer, Empréstimo")
    data: date = Field(..., description="Data que foi adquirido o ativo")
    fixo: Literal["S", "N"]
    tipo_remuneracao: Optional[Literal["Q", "M", "S"]]
    finalizado: date
    id_conta: int = Field(..., ge=0, description="Conta que está relacionado")


class AtivoCreateSchema(AtivoSchema):
    pass


class AtivoOutputSchema(AtivoSchema):
    id: int = Field(..., ge=0)


class AtivoUpdateSchema(AtivoSchema):
    pass
