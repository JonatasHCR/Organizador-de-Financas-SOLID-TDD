from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.passivo import Passivo
from app.schemas.passivo import PassivoCreateSchema, PassivoUpdateSchema


class PassivoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, passivo_id: int) -> Passivo:
        busca = await self.__db.execute(select(Passivo).where(Passivo.id == passivo_id))
        return busca.scalar_one_or_none()

    async def create(self, passivo_schema: PassivoCreateSchema) -> Passivo:
        passivo = Passivo(passivo_schema.model_dump())
        self.__db.add(passivo)
        await self.__db.commit()
        await self.__db.refresh(passivo)
        return passivo

    async def update(
        self, passivo_id: int, passivo_schema: PassivoUpdateSchema
    ) -> Passivo:
        passivo = await self.__db.execute(
            select(Passivo).where(Passivo.id == passivo_id)
        )
        passivo = passivo.scalar_one_or_none()

        if passivo is None:
            return None

        passivo_update = passivo_schema.model_dump(exclude_unset=True)
        for key, value in passivo_update.items():
            setattr(passivo, key, value)

        await self.__db.commit()
        await self.__db.refresh(passivo)
        return passivo

    async def delete(self, passivo_id: int) -> bool:
        passivo = await self.__db.execute(
            select(Passivo).where(Passivo.id == passivo_id)
        )
        passivo = passivo.scalar_one_or_none()

        await self.__db.delete(passivo)
        await self.__db.commit()
        return True
