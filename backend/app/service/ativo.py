from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.ativo import AtivoSchema, AtivoOutputSchema, AtivoResponseSchema
from app.repository.ativo import AtivoRepository


class AtivoService:
    def __init__(self, db: AsyncSession):
        self.repository = AtivoRepository(db)

    async def get_by_id(self, ativo_id: int) -> AtivoOutputSchema:
        busca = await self.repository.get_by_id(ativo_id)

        return busca

    async def get_by_conta(self, conta_id: int) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_conta(conta_id)

        return busca

    async def get_all(self) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, ativo_schema: AtivoSchema) -> AtivoResponseSchema:
        resposta = await self.repository.create(ativo_schema)

        return resposta

    async def update(
        self, ativo_id: int, ativo_schema: AtivoSchema
    ) -> AtivoResponseSchema:
        resposta = await self.repository.update(ativo_id, ativo_schema)

        return resposta

    async def delete(self, ativo_id: int) -> AtivoResponseSchema:
        resposta = await self.repository.delete(ativo_id)

        return resposta
