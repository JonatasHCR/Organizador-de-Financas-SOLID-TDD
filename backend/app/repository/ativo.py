from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.ativo import Ativo
from app.schemas.ativo import AtivoCreateSchema, AtivoUpdateSchema


class AtivoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, ativo_id: int) -> Ativo:
        busca = await self.__db.execute(select(Ativo).where(Ativo.id == ativo_id))
        return busca.scalar_one_or_none()

    async def create(self, ativo_schema: AtivoCreateSchema) -> Ativo:
        ativo = Ativo(ativo_schema.model_dump())
        self.__db.add(ativo)
        await self.__db.commit()
        await self.__db.refresh(ativo)
        return ativo

    async def update(self, ativo_id: int, ativo_schema: AtivoUpdateSchema) -> Ativo:
        ativo = await self.__db.execute(select(Ativo).where(Ativo.id == ativo_id))
        ativo = ativo.scalar_one_or_none()

        if ativo is None:
            return None

        ativo_update = ativo_schema.model_dump(exclude_unset=True)
        for key, value in ativo_update.items():
            setattr(ativo, key, value)

        await self.__db.commit()
        await self.__db.refresh(ativo)
        return ativo

    async def delete(self, ativo_id: int) -> bool:
        ativo = await self.__db.execute(select(Ativo).where(Ativo.id == ativo_id))
        ativo = ativo.scalar_one_or_none()

        await self.__db.delete(ativo)
        await self.__db.commit()
        return True
