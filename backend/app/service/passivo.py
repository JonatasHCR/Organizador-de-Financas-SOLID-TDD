from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.passivo import PassivoSchema, PassivoOutputSchema
from app.repository.passivo import PassivoRepository
from app.service.base import BaseService


class PassivoService(BaseService[PassivoRepository, PassivoSchema, PassivoOutputSchema]):
    def __init__(self, db: AsyncSession):
        super().__init__(PassivoRepository, PassivoOutputSchema, db)

    async def get_by_conta_id(self, conta_id: int) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_conta_id(conta_id)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_referencia(self, referencia: str) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_referencia(referencia)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_fixo(self, fixo: bool) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_fixo(fixo)

        return [self.output_schema.model_validate(objeto) for objeto in busca]

    async def get_by_tipo_remuneracao(
        self, tipo_remuneracao: str
    ) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_tipo_remuneracao(tipo_remuneracao)

        return [self.output_schema.model_validate(objeto) for objeto in busca]
