from sqlalchemy.ext.asyncio import AsyncSession

from app.model.ativo import Ativo
from app.repository.base import BaseRepository


class AtivoRepository(BaseRepository[Ativo]):
    def __init__(self, db: AsyncSession):
        super().__init__(Ativo, db)

    async def get_by_conta_id(self, conta_id: int) -> list[Ativo]:
        busca = await self.get_by_filter(Ativo.conta_id == conta_id)

        return busca

    async def get_by_referencia(self, referencia: str) -> list[Ativo]:
        busca = await self.get_by_filter(Ativo.referencia == referencia)

        return busca

    async def get_by_frequencia(self, frequencia: str) -> list[Ativo]:
        busca = await self.get_by_filter(Ativo.frequencia == frequencia)

        return busca

    async def get_by_fixo(self, fixo: bool) -> list[Ativo]:
        busca = await self.get_by_filter(Ativo.fixo == fixo)

        return busca
