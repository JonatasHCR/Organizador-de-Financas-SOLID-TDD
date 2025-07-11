from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.investimento import InvestimentoSchema, InvestimentoOutputSchema
from app.repository.investimento import InvestimentoRepository


class InvestimentoService:
    def __init__(self, db: AsyncSession):
        self.repository = InvestimentoRepository(db)

    async def get_by_id(self, investimento_id: int) -> InvestimentoOutputSchema:
        busca = await self.repository.get_by_id(investimento_id)

        if busca is None:
            raise ValueError(f"Investimento com ID = {investimento_id} não existe")

        return busca

    async def get_by_conta(self, conta_id: int) -> list[InvestimentoOutputSchema]:
        busca = await self.repository.get_by_conta(conta_id)

        if busca is None:
            raise ValueError(f"Conta com ID = {conta_id} não existe")

        return busca

    async def get_all(self) -> list[InvestimentoOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, investimento_schema: InvestimentoSchema) -> dict[str, str]:
        resposta = await self.repository.create(investimento_schema)
        if resposta:
            return {"mensagem": "Investimento criado com sucesso!!!"}
        return {"mensagem": "Falha em criar o investimento!!!"}

    async def update(
        self, investimento_id: int, investimento_schema: InvestimentoSchema
    ) -> dict[str, str]:
        resposta = await self.repository.update(investimento_id, investimento_schema)
        if resposta:
            return {"mensagem": "Investimento modificado com sucesso!!!"}
        return {
            "mensagem": f"Falha em modificar o investimento, ID = {investimento_id} não encontrado!!!"
        }

    async def delete(self, investimento_id: int) -> dict[str, str]:
        resposta = await self.repository.delete(investimento_id)
        if resposta:
            return {"mensagem": "Investimento deletado com sucesso!!!"}
        return {
            "mensagem": f"Falha em deletar o investimento, ID = {investimento_id} não encontrado!!!"
        }
