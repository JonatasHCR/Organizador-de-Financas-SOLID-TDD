from sqlalchemy.ext.asyncio import AsyncSession

from app.model.conta import Conta
from app.repository.base import BaseRepository


class ContaRepository(BaseRepository[Conta]):
    def __init__(self, db: AsyncSession):
        super().__init__(Conta, db)

    async def get_by_nome(self, nome: str) -> Conta:
        busca = await self.get_by_filter(Conta.nome == nome)
        busca = busca[0] if busca else None

        if busca is None:
            raise ValueError(f"Conta com o NOME = {nome} não encontrada")

        return busca
