from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.passivo import PassivoSchema, PassivoOutputSchema
from app.repository.passivo import PassivoRepository


class PassivoService:
    def __init__(self, db: AsyncSession):
        self.repository = PassivoRepository(db)

    async def get_by_id(self, passivo_id: int) -> PassivoOutputSchema:
        busca = await self.repository.get_by_id(passivo_id)

        if busca is None:
            raise ValueError(f"Passivo com ID = {passivo_id} não existe")

        return busca

    async def get_by_conta(self, conta_id: int) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_by_conta(conta_id)

        if busca is None:
            raise ValueError(f"Conta com ID = {conta_id} não existe")

        return busca

    async def get_all(self) -> list[PassivoOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, passivo_schema: PassivoSchema) -> dict[str, str]:
        resposta = await self.repository.create(passivo_schema)
        if resposta:
            return {"mensagem": "Passivo criado com sucesso!!!"}
        return {"mensagem": "Falha em criar o passivo!!!"}

    async def update(
        self, passivo_id: int, passivo_schema: PassivoSchema
    ) -> dict[str, str]:
        resposta = await self.repository.update(passivo_id, passivo_schema)
        if resposta:
            return {"mensagem": "Passivo modificado com sucesso!!!"}
        return {
            "mensagem": f"Falha em modificar o passivo, ID = {passivo_id} não encontrado!!!"
        }

    async def delete(self, passivo_id: int) -> dict[str, str]:
        resposta = await self.repository.delete(passivo_id)
        if resposta:
            return {"mensagem": "Passivo deletado com sucesso!!!"}
        return {
            "mensagem": f"Falha em deletar o passivo, ID = {passivo_id} não encontrado!!!"
        }
