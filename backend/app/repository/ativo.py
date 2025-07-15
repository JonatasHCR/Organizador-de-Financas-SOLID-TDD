from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.ativo import Ativo
from app.schema.ativo import AtivoSchema, AtivoOutputSchema, AtivoResponseSchema


class AtivoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, ativo_id: int) -> AtivoOutputSchema:
        busca = await self.__db.execute(select(Ativo).where(Ativo.id == ativo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            return ValueError(f"Ativo com ID = {ativo_id} não encontrado")

        return AtivoOutputSchema.model_validate(busca)

    async def _get_by_id(self, ativo_id: int) -> Ativo:
        busca = await self.__db.execute(select(Ativo).where(Ativo.id == ativo_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Ativo com ID = {ativo_id} não encontrado")

        return busca

    async def get_by_conta(self, conta_id: int) -> list[AtivoOutputSchema] | None:
        busca = await self.__db.execute(select(Ativo).where(Ativo.id_conta == conta_id))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [AtivoOutputSchema.model_validate(ativo) for ativo in busca]

    async def get_all(self) -> list[AtivoOutputSchema] | None:
        busca = await self.__db.execute(select(Ativo))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [AtivoOutputSchema.model_validate(ativo) for ativo in busca]

    async def create(self, ativo_schema: AtivoSchema) -> AtivoResponseSchema:
        ativo = Ativo(ativo_schema.model_dump())
        self.__db.add(ativo)
        await self.__db.commit()
        await self.__db.refresh(ativo)

        return AtivoResponseSchema(
            status="Create", ativo=AtivoOutputSchema.model_validate(ativo)
        )

    async def update(
        self, ativo_id: int, ativo_schema: AtivoSchema
    ) -> AtivoResponseSchema:
        ativo = await self._get_by_id(ativo_id)

        ativo_update = ativo_schema.model_dump(exclude_unset=True)
        for key, value in ativo_update.items():
            setattr(ativo, key, value)

        await self.__db.commit()
        await self.__db.refresh(ativo)

        return AtivoResponseSchema(
            status="Update", ativo=AtivoOutputSchema.model_validate(ativo)
        )

    async def delete(self, ativo_id: int) -> AtivoResponseSchema:
        ativo = await self._get_by_id(ativo_id)

        await self.__db.delete(ativo)
        await self.__db.commit()

        return AtivoResponseSchema(
            status="Delete", ativo=AtivoOutputSchema.model_validate(ativo)
        )
