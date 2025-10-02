from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.conta import ContaOutputSchema
from app.repository.conta import ContaRepository


class ContaService:
    def __init__(self, db: AsyncSession):
        self.repository = ContaRepository(db)

    async def get_by_nome(self, conta_nome: str) -> ContaOutputSchema:
        busca = await self.repository.get_by_nome(conta_nome)

        return ContaOutputSchema.model_validate(busca)
