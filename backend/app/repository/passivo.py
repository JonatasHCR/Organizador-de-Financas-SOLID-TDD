from sqlalchemy.ext.asyncio import AsyncSession

from app.model.passivo import Passivo
from app.repository.base import BaseRepository


class PassivoRepository(BaseRepository[Passivo]):
    def __init__(self, db: AsyncSession):
        super().__init__(Passivo, db)

    async def get_by_conta_id(self, conta_id: int) -> list[Passivo]:
        busca = await self.get_by_filter(Passivo.conta_id == conta_id)

        return busca

    async def get_by_referencia(self, referencia: str) -> list[Passivo]:
        busca = await self.get_by_filter(Passivo.referencia == referencia)

        return busca

    async def get_by_frequencia(self, frequencia: str) -> list[Passivo]:
        busca = await self.get_by_filter(Passivo.frequencia == frequencia)

        return busca

    async def get_by_fixo(self, fixo: bool) -> list[Passivo]:
        busca = await self.get_by_filter(Passivo.fixo == fixo)

        return busca
