from zoneinfo import ZoneInfo
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.passivo import Passivo
from app.schema.passivo import PassivoSchema, PassivoOutputSchema, PassivoResponseSchema


class PassivoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, passivo_id: int) -> PassivoOutputSchema:
        busca = await self.__db.execute(select(Passivo).where(Passivo.id == passivo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return ValueError(f"Passivo com ID = {passivo_id} não encontrado")

        return PassivoOutputSchema.model_validate(busca)

    async def _get_by_id(self, passivo_id: int) -> Passivo:
        busca = await self.__db.execute(select(Passivo).where(Passivo.id == passivo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Passivo com ID = {passivo_id} não encontrado")

        return busca

    async def get_by_referencia(self, referencia: str) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(
            select(Passivo).where(Passivo.referencia == referencia)
        )
        busca = busca.scalars().all()

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def get_by_frequencia(self, frequencia: str) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(
            select(Passivo).where(Passivo.frequencia == frequencia)
        )
        busca = busca.scalars().all()

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def get_eh_fixo(self, eh_fixo: bool) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(
            select(Passivo).where(Passivo.eh_fixo == eh_fixo)
        )
        busca = busca.scalars().all()

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def get_by_conta_id(self, conta_id: int) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(
            select(Passivo).where(Passivo.conta_id == conta_id)
        )
        busca = busca.scalars().all()

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def get_all(self) -> list[PassivoOutputSchema]:
        busca = await self.__db.execute(select(Passivo))
        busca = busca.scalars().all()

        return [PassivoOutputSchema.model_validate(passivo) for passivo in busca]

    async def create(self, passivo_schema: PassivoSchema) -> PassivoResponseSchema:
        passivo = Passivo(**passivo_schema.model_dump())
        self.__db.add(passivo)
        await self.__db.flush()
        await self.__db.refresh(passivo)

        return PassivoResponseSchema(
            status="Create",
            passivo=PassivoOutputSchema.model_validate(passivo),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def update(
        self, passivo_id: int, passivo_schema: PassivoSchema
    ) -> PassivoResponseSchema:
        passivo = await self._get_by_id(passivo_id)

        passivo_update = passivo_schema.model_dump(exclude_unset=True)
        for key, value in passivo_update.items():
            setattr(passivo, key, value)

        await self.__db.flush()
        await self.__db.refresh(passivo)

        return PassivoResponseSchema(
            status="Update",
            passivo=PassivoOutputSchema.model_validate(passivo),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def delete(self, passivo_id: int) -> PassivoResponseSchema:
        passivo = await self._get_by_id(passivo_id)

        await self.__db.delete(passivo)
        await self.__db.flush()

        return PassivoResponseSchema(
            status="Delete",
            passivo=PassivoOutputSchema.model_validate(passivo),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )
