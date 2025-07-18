from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.ativo import AtivoSchema, AtivoOutputSchema, AtivoResponseSchema
from app.repository.ativo import AtivoRepository


class AtivoService:
    def __init__(self, db: AsyncSession):
        self.repository = AtivoRepository(db)

    async def get_by_id(self, ativo_id: int) -> AtivoOutputSchema:
        busca = await self.repository.get_by_id(ativo_id)

        return busca

    async def get_by_conta_id(self, conta_id: int) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_conta_id(conta_id)

        return busca

    async def get_by_referencia(self, referencia: str) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_referencia(referencia)

        return busca

    async def get_eh_fixo(self, eh_fixo: bool) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_eh_fixo(eh_fixo)

        return busca

    async def get_by_tipo_remuneracao(
        self, tipo_remuneracao: str
    ) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_tipo_remuneracao(tipo_remuneracao)

        return busca

    async def get_all(self) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_all()

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
