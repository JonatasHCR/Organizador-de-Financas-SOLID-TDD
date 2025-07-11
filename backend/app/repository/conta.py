from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.conta import Conta
from app.schema.conta import ContaSchema, ContaOutputSchema


class ContaRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, conta_id: int) -> ContaOutputSchema | None:
        busca = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return ContaOutputSchema.model_validate(busca)

    async def _get_by_id(self, conta_id: int) -> Conta | None:
        busca = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return busca

    async def get_by_nome(self, nome: str) -> ContaOutputSchema:
        busca = await self.__db.execute(select(Conta).where(Conta.nome == nome))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return ContaOutputSchema.model_validate(busca)

    async def get_all(self) -> list[ContaOutputSchema]:
        busca = await self.__db.execute(select(Conta))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [ContaOutputSchema.model_validate(conta) for conta in busca]

    async def create(self, conta_schema: ContaSchema) -> bool:
        conta = conta(conta_schema.model_dump())
        self.__db.add(conta)
        await self.__db.commit()
        return True

    async def update(self, conta_id: int, conta_schema: ContaSchema) -> bool:
        conta = await self._get_by_id(conta_id)

        if conta is None:
            return False

        conta_update = conta_schema.model_dump(exclude_unset=True)
        for key, value in conta_update.items():
            setattr(conta, key, value)

        await self.__db.commit()
        return True

    async def delete(self, conta_id: int) -> bool:
        conta = await self._get_by_id(conta_id)

        if conta is None:
            return False

        await self.__db.delete(conta)
        await self.__db.commit()
        return True
