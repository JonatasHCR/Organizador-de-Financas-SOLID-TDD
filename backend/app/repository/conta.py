from zoneinfo import ZoneInfo
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from app.model.conta import Conta
from app.schema.conta import ContaSchema, ContaOutputSchema, ContaResponseSchema


class ContaRepository:
    def __init__(self, db: AsyncSession):
        self.__db = db

    async def get_by_id(self, conta_id: int) -> ContaOutputSchema:
        busca = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Conta com o ID = {conta_id} não encontrada")

        return ContaOutputSchema.model_validate(busca)

    async def _get_by_id(self, conta_id: int) -> Conta:
        busca = await self.__db.execute(select(Conta).where(Conta.id == conta_id))
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Conta com o ID = {conta_id} não encontrada")

        return busca

    async def get_by_nome(self, nome: str) -> ContaOutputSchema:
        busca = await self.__db.execute(select(Conta).where(Conta.nome == nome))
        busca = busca.scalar_one_or_none()

        if busca is None:
            raise ValueError(f"Conta com o NOME = {nome} não encontrada")

        return ContaOutputSchema.model_validate(busca)

    async def get_all(self) -> list[ContaOutputSchema] | None:
        busca = await self.__db.execute(select(Conta))
        busca = busca.scalars().all()

        if busca is None:
            return None

        return [ContaOutputSchema.model_validate(conta) for conta in busca]

    async def create(self, conta_schema: ContaSchema) -> ContaResponseSchema:
        conta = Conta(**conta_schema.model_dump())

        self.__db.add(conta)
        await self.__db.flush()
        await self.__db.refresh(conta)

        return ContaResponseSchema(
            status="Create",
            conta=ContaOutputSchema.model_validate(conta),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def update(
        self, conta_id: int, conta_schema: ContaSchema
    ) -> ContaResponseSchema:
        conta = await self._get_by_id(conta_id)

        conta_update = conta_schema.model_dump(exclude_unset=True)
        for key, value in conta_update.items():
            setattr(conta, key, value)

        await self.__db.flush()
        await self.__db.refresh(conta)

        return ContaResponseSchema(
            status="Update",
            conta=ContaOutputSchema.model_validate(conta),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )

    async def delete(self, conta_id: int) -> ContaResponseSchema:
        conta = await self._get_by_id(conta_id)

        await self.__db.delete(conta)
        await self.__db.flush()

        return ContaResponseSchema(
            status="Delete",
            conta=ContaOutputSchema.model_validate(conta),
            data_hora=datetime.now(ZoneInfo("America/Bahia")),
        )
