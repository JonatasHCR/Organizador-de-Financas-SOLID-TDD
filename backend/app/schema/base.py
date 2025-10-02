from datetime import date
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class BaseSchema(BaseModel):

    nome: str = Field(
        ...,
    )
    referencia: str = Field(
        ...,
    )
    descricao: Optional[str]
    valor: float = Field(
        ...,
        ge=0,
    )
    data_adquirido: date = Field(
        ...,
    )
    fixo: bool = Field(
        ...,
    )
    data_finalizado: Optional[date]
    conta_id: int = Field(
        ...,
        gt=0,
    )

    model_config = ConfigDict(from_attributes=True)
