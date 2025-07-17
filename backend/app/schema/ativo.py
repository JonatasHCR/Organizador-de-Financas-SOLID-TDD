from datetime import date, datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field, ConfigDict


class AtivoSchema(BaseModel):

    nome: str = Field(..., description="Nome do ativo")
    referencia: str = Field(
        ..., description="A associação do ativo, ex: Salario, Freelancer, Empréstimo"
    )
    descricao: Optional[str]
    valor: float = Field(..., ge=0, description="Valor do ativo")
    data_adquirido: date = Field(..., description="Data que foi adquirido o ativo")
    eh_fixo: bool = Field(..., description="O ativo ocorre de maneira constante?")
    tipo_remuneracao: Optional[Literal["Q", "M", "S"]]
    data_finalizado: Optional[date]
    conta_id: int = Field(..., gt=0, description="Conta que está relacionado")

    model_config = ConfigDict(from_attributes=True)


class AtivoOutputSchema(AtivoSchema):
    id: int = Field(..., gt=0)


class AtivoResponseSchema(BaseModel):
    status: str = Field(..., description="Status da resposta")
    ativo: AtivoOutputSchema = Field(..., description="Ativo")
    data_hora: datetime = Field(..., description="Data e hora da resposta")

    model_config = ConfigDict(from_attributes=True)
