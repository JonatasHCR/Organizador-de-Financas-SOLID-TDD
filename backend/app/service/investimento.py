from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.investimento import (
    InvestimentoSchema,
    InvestimentoOutputSchema,
    InvestimentoResponseSchema,
)
from app.repository.investimento import InvestimentoRepository


class InvestimentoService:
    def __init__(self, db: AsyncSession):
        self.repository = InvestimentoRepository(db)

    async def get_by_id(self, investimento_id: int) -> InvestimentoOutputSchema:
        busca = await self.repository.get_by_id(investimento_id)

        return busca

    async def get_by_conta_id(self, conta_id: int) -> list[InvestimentoOutputSchema]:
        busca = await self.repository.get_by_conta_id(conta_id)

        return busca

    async def get_all(self) -> list[InvestimentoOutputSchema]:
        busca = await self.repository.get_all()

        return busca

    async def create(
        self, investimento_schema: InvestimentoSchema
    ) -> InvestimentoResponseSchema:
        resposta = await self.repository.create(investimento_schema)

        return resposta

    async def update(
        self, investimento_id: int, investimento_schema: InvestimentoSchema
    ) -> InvestimentoResponseSchema:
        resposta = await self.repository.update(investimento_id, investimento_schema)

        return resposta

    async def delete(self, investimento_id: int) -> InvestimentoResponseSchema:
        resposta = await self.repository.delete(investimento_id)

        return resposta
