from zoneinfo import ZoneInfo
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.investimento import Investimento
from app.schema.investimento import (
    InvestimentoSchema,
    InvestimentoOutputSchema,
    InvestimentoResponseSchema,
)


class InvestimentoRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, investimento_id: int) -> InvestimentoOutputSchema:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        busca = busca.scalar_one_or_none()

        if busca is None:
            return ValueError(f"Investimento com ID = {investimento_id} não encontrado")

        return InvestimentoOutputSchema.model_validate(busca)

    async def _get_by_id(self, investimento_id: int) -> Investimento:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.id == investimento_id)
        )
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Investimento com ID = {investimento_id} não encontrado")

        return busca

    async def get_by_conta(
        self, conta_id: int
    ) -> list[InvestimentoOutputSchema] | None:
        busca = await self.__db.execute(
            select(Investimento).where(Investimento.conta_id == conta_id)
        )
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [
            InvestimentoOutputSchema.model_validate(investimento)
            for investimento in busca
        ]

    async def get_all(self) -> list[InvestimentoOutputSchema] | None:
        busca = await self.__db.execute(select(Investimento))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [
            InvestimentoOutputSchema.model_validate(investimento)
            for investimento in busca
        ]

    async def create(
        self, investimento_schema: InvestimentoSchema
    ) -> InvestimentoResponseSchema:
        investimento = Investimento(**investimento_schema.model_dump())
        self.__db.add(investimento)
        await self.__db.flush()
        await self.__db.refresh(investimento)

        return InvestimentoResponseSchema(
            status="Create",
            investimento=InvestimentoOutputSchema.model_validate(investimento),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def update(
        self, investimento_id: int, investimento_schema: InvestimentoSchema
    ) -> InvestimentoResponseSchema:
        investimento = await self._get_by_id(investimento_id)

        investimento_update = investimento_schema.model_dump(exclude_unset=True)
        for key, value in investimento_update.items():
            setattr(investimento, key, value)

        await self.__db.flush()
        await self.__db.refresh(investimento)

        return InvestimentoResponseSchema(
            status="Update",
            investimento=InvestimentoOutputSchema.model_validate(investimento),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def delete(self, investimento_id: int) -> InvestimentoResponseSchema:
        investimento = await self._get_by_id(investimento_id)

        await self.__db.delete(investimento)
        await self.__db.flush()

        return InvestimentoResponseSchema(
            status="Delete",
            investimento=InvestimentoOutputSchema.model_validate(investimento),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )
