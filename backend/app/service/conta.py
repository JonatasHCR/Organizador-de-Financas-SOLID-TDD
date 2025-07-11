from sqlalchemy.ext.asyncio import AsyncSession

from app.schema.conta import ContaSchema, ContaOutputSchema
from app.repository.conta import ContaRepository


class ContaService:
    def __init__(self, db: AsyncSession):
        self.repository = ContaRepository(db)

    async def get_by_id(self, conta_id: int) -> ContaOutputSchema:
        busca = await self.repository.get_by_id(conta_id)

        if busca is None:
            raise ValueError(f"Conta com ID = {conta_id} não existe")

        return busca

    async def get_by_nome(self, nome: str) -> ContaOutputSchema:
        busca = await self.repository.get_by_nome(nome)

        if busca is None:
            raise ValueError(f"Conta com NOME = {nome} não existe")

        return busca

    async def get_all(self) -> list[ContaOutputSchema]:
        busca = await self.repository.get_all()

        if busca is None:
            return None

        return busca

    async def create(self, conta_schema: ContaSchema) -> dict[str, str]:
        resposta = await self.repository.create(conta_schema)
        if resposta:
            return {"mensagem": "Conta criado com sucesso!!!"}
        return {"mensagem": "Falha em criar o conta!!!"}

    async def update(self, conta_id: int, conta_schema: ContaSchema) -> dict[str, str]:
        resposta = await self.repository.update(conta_id, conta_schema)
        if resposta:
            return {"mensagem": "Conta modificado com sucesso!!!"}
        return {
            "mensagem": f"Falha em modificar o conta, ID = {conta_id} não encontrado!!!"
        }

    async def delete(self, conta_id: int) -> dict[str, str]:
        resposta = await self.repository.delete(conta_id)
        if resposta:
            return {"mensagem": "Conta deletado com sucesso!!!"}
        return {
            "mensagem": f"Falha em deletar o conta, ID = {conta_id} não encontrado!!!"
        }
