from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.passivo import Passivo
from app.schemas.passivo import PassivoSchema, PassivoOutputSchema


class PassivoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, passivo_id: int) -> PassivoOutputSchema | None:
        busca = await self.__db.execute(select(Passivo).where(Passivo.id == passivo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return PassivoOutputSchema.model_validate(busca)

    async def _get_by_id(self, passivo_id: int) -> Passivo | None:
        busca = await self.__db.execute(select(Passivo).where(Passivo.id == passivo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return busca

    async def get_by_conta(self, conta_id: int) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(
            select(Passivo).where(Passivo.id_conta == conta_id)
        )
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def get_all(self):
        busca = await self.__db.execute(select(Passivo))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def create(self, passivo_schema: PassivoSchema) -> bool:
        passivo = Passivo(passivo_schema.model_dump())
        self.__db.add(passivo)
        await self.__db.commit()
        return True

    async def update(self, passivo_id: int, passivo_schema: PassivoSchema) -> bool:
        passivo = await self._get_by_id(passivo_id)

        if passivo is None:
            return False

        passivo_update = passivo_schema.model_dump(exclude_unset=True)
        for key, value in passivo_update.items():
            setattr(passivo, key, value)

        await self.__db.commit()
        return True

    async def delete(self, passivo_id: int) -> bool:
        passivo = await self._get_by_id(passivo_id)

        if passivo is None:
            return False

        await self.__db.delete(passivo)
        await self.__db.commit()
        return True
