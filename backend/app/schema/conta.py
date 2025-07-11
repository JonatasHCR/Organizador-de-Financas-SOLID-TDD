from pydantic import BaseModel, Field


class ContaSchema(BaseModel):

    nome: str = Field(..., description="Nome do Conta")
    descricao: str


class ContaOutputSchema(ContaSchema):
    id: int = Field(..., ge=0)
