from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.ativo import AtivoSchema, AtivoOutputSchema
from app.repository.ativo import AtivoRepository


class AtivoService:
    def __init__(self, db: AsyncSession):
        self.repository = AtivoRepository(db)

    async def get_by_id(self, ativo_id: int) -> AtivoOutputSchema:
        busca = await self.repository.get_by_id(ativo_id)

        if busca is None:
            raise ValueError(f"Ativo com ID = {ativo_id} não existe")

        return busca

    async def get_by_conta(self, conta_id: int) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_by_conta(conta_id)

        if busca is None:
            raise ValueError(f"Conta com ID = {conta_id} não existe")

        return busca

    async def get_all(self) -> list[AtivoOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, ativo_schema: AtivoSchema) -> dict[str, str]:
        resposta = await self.repository.create(ativo_schema)
        if resposta:
            return {"mensagem": "Ativo criado com sucesso!!!"}
        return {"mensagem": "Falha em criar o ativo!!!"}

    async def update(self, ativo_id: int, ativo_schema: AtivoSchema) -> dict[str, str]:
        resposta = await self.repository.update(ativo_id, ativo_schema)
        if resposta:
            return {"mensagem": "Ativo modificado com sucesso!!!"}
        return {
            "mensagem": f"Falha em modificar o ativo, ID = {ativo_id} não encontrado!!!"
        }

    async def delete(self, ativo_id: int) -> dict[str, str]:
        resposta = await self.repository.delete(ativo_id)
        if resposta:
            return {"mensagem": "Ativo deletado com sucesso!!!"}
        return {
            "mensagem": f"Falha em deletar o ativo, ID = {ativo_id} não encontrado!!!"
        }
