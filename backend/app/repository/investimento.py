from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.investimento import Investimento
from app.schemas.investimento import InvestimentoSchema, InvestimentoOutputSchema


class InvestimentoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, investimento_id: int) -> InvestimentoOutputSchema | None:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return InvestimentoOutputSchema.model_validate(busca)

    async def _get_by_id(self, investimento_id: int) -> Investimento | None:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        busca = busca.scalar_one_or_none()

        if busca is None:
            return None

        return busca

    async def get_by_conta(self, conta_id: int) -> list[InvestimentoOutputSchema]:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id_conta == conta_id)
        )
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [
            InvestimentoOutputSchema.model_validate(investimento)
            for investimento in busca
        ]

    async def get_all(self):
        busca = await self.__db.execute(select(Investimento))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [
            InvestimentoOutputSchema.model_validate(investimento)
            for investimento in busca
        ]

    async def create(self, investimento_schema: InvestimentoSchema) -> bool:
        investimento = Investimento(investimento_schema.model_dump())
        self.__db.add(investimento)
        await self.__db.commit()
        return True

    async def update(
        self, investimento_id: int, investimento_schema: InvestimentoSchema
    ) -> bool:
        investimento = await self._get_by_id(investimento_id)

        if investimento is None:
            return False

        investimento_update = investimento_schema.model_dump(exclude_unset=True)
        for key, value in investimento_update.items():
            setattr(investimento, key, value)

        await self.__db.commit()
        return True

    async def delete(self, investimento_id: int) -> bool:
        investimento = await self._get_by_id(investimento_id)

        if investimento is None:
            return False

        await self.__db.delete(investimento)
        await self.__db.commit()
        return True
