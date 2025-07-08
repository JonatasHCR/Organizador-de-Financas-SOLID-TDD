from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.conta import Conta
from app.schemas.conta import ContaCreateSchema, ContaUpdateSchema


class ContaRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, conta_id: int) -> Conta:
        busca = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        return busca.scalar_one_or_none()

    async def create(self, conta_schema: ContaCreateSchema) -> Conta:
        conta = Conta(conta_schema.model_dump())
        self.__db.add(conta)
        await self.__db.commit()
        await self.__db.refresh(conta)
        return conta

    async def update(self, conta_id: int, conta_schema: ContaUpdateSchema) -> Conta:
        conta = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        conta = conta.scalar_one_or_none()

        if conta is None:
            return None

        conta_update = conta_schema.model_dump(exclude_unset=True)
        for key, value in conta_update.items():
            setattr(conta, key, value)

        await self.__db.commit()
        await self.__db.refresh(conta)
        return conta

    async def delete(self, conta_id: int) -> bool:
        conta = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        conta = conta.scalar_one_or_none()

        await self.__db.delete(conta)
        await self.__db.commit()
        return True
