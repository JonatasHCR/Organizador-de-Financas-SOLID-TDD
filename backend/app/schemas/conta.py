from pydantic import BaseModel, Field


class ContaSchema(BaseModel):

    nome: str = Field(..., description="Nome do Conta")
    descricao: str


class ContaCreateSchema(ContaSchema):
    pass


class ContaOutputSchema(ContaSchema):
    id: int = Field(..., ge=0)


class ContaUpdateSchema(ContaSchema):
    pass
