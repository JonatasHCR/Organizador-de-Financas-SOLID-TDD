from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.passivo import PassivoSchema, PassivoOutputSchema, PassivoResponseSchema
from app.repository.passivo import PassivoRepository


class PassivoService:
    def __init__(self, db: AsyncSession):
        self.repository = PassivoRepository(db)

    async def get_by_id(self, passivo_id: int) -> PassivoOutputSchema:
        busca = await self.repository.get_by_id(passivo_id)

        return busca

    async def get_by_conta(self, conta_id: int) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_conta(conta_id)

        return busca

    async def get_by_referencia(self, referencia: str) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_referencia(referencia)

        return busca

    async def get_all(self) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, passivo_schema: PassivoSchema) -> PassivoResponseSchema:
        resposta = await self.repository.create(passivo_schema)

        return resposta

    async def update(
        self, passivo_id: int, passivo_schema: PassivoSchema
    ) -> PassivoResponseSchema:
        resposta = await self.repository.update(passivo_id, passivo_schema)

        return resposta

    async def delete(self, passivo_id: int) -> PassivoResponseSchema:
        resposta = await self.repository.delete(passivo_id)

        return resposta
