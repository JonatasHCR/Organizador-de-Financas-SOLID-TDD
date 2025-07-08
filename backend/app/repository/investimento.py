from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.models.investimento import Investimento
from app.schemas.investimento import InvestimentoCreateSchema, InvestimentoUpdateSchema


class InvestimentoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, investimento_id: int) -> Investimento:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        return busca.scalar_one_or_none()

    async def create(
        self, investimento_schema: InvestimentoCreateSchema
    ) -> Investimento:
        investimento = Investimento(investimento_schema.model_dump())
        self.__db.add(investimento)
        await self.__db.commit()
        await self.__db.refresh(investimento)
        return investimento

    async def update(
        self, investimento_id: int, investimento_schema: InvestimentoUpdateSchema
    ) -> Investimento:
        investimento = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        investimento = investimento.scalar_one_or_none()

        if investimento is None:
            return None

        investimento_update = investimento_schema.model_dump(exclude_unset=True)
        for key, value in investimento_update.items():
            setattr(investimento, key, value)

        await self.__db.commit()
        await self.__db.refresh(investimento)
        return investimento

    async def delete(self, investimento_id: int) -> bool:
        investimento = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        investimento = investimento.scalar_one_or_none()

        await self.__db.delete(investimento)
        await self.__db.commit()
        return True
