from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.conta import ContaSchema, ContaOutputSchema, ContaResponseSchema
from app.repository.conta import ContaRepository


class ContaService:
    def __init__(self, db: AsyncSession):
        self.repository = ContaRepository(db)

    async def get_by_id(self, conta_id: int) -> ContaOutputSchema:
        busca = await self.repository.get_by_id(conta_id)

        return busca

    async def get_by_nome(self, conta_nome: str) -> ContaOutputSchema:
        busca = await self.repository.get_by_nome(conta_nome)

        return busca

    async def get_all(self) -> list[ContaOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, conta_schema: ContaSchema) -> ContaResponseSchema:
        resposta = await self.repository.create(conta_schema)

        return resposta

    async def update(
        self, conta_id: int, conta_schema: ContaSchema
    ) -> ContaResponseSchema:
        resposta = await self.repository.update(conta_id, conta_schema)

        return resposta

    async def delete(self, conta_id: int) -> ContaResponseSchema:
        resposta = await self.repository.delete(conta_id)

        return resposta
