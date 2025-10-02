from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.ativo import AtivoSchema, AtivoOutputSchema
from app.repository.ativo import AtivoRepository
from app.service.base import BaseService


class AtivoService(BaseService[AtivoRepository, AtivoSchema, AtivoOutputSchema]):
    def __init__(self, db: AsyncSession):
        super().__init__(AtivoRepository, AtivoOutputSchema, db)

    async def get_by_conta_id(self, conta_id: int) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_conta_id(conta_id)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_referencia(self, referencia: str) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_referencia(referencia)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_fixo(self, fixo: bool) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_fixo(fixo)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_frequencia(
        self, frequencia: str
    ) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_frequencia(frequencia)

        return [self.output_schema.model_validate(objeto) for objeto in busca]
