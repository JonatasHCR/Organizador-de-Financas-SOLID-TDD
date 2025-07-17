import pytest

from app.schema.investimento import InvestimentoSchema
from app.service.investimento import InvestimentoService


investimento_teste = {
    "nome": "Investimento Teste",
    "descricao": None,
    "valor": 100,
    "tipo": "A",
    "data_adquirido": "2025-07-12",
    "conta_id": 1,
}


@pytest.mark.asyncio
async def test_service_create(async_db):
    service = InvestimentoService(async_db)
    resposta = await service.create(InvestimentoSchema(**investimento_teste))
    assert resposta.investimento.id is not None


@pytest.mark.asyncio
async def test_service_get_by_id(async_db):
    service = InvestimentoService(async_db)
    await service.create(InvestimentoSchema(**investimento_teste))

    investimento = await service.get_by_id(1)
    assert investimento.nome == investimento_teste["nome"]


@pytest.mark.asyncio
async def test_service_get_by_conta(async_db):
    service = InvestimentoService(async_db)
    await service.create(InvestimentoSchema(**investimento_teste))

    investimento = await service.get_by_conta(investimento_teste["conta_id"])
    assert len(investimento) > 0


@pytest.mark.asyncio
async def test_service_update(async_db):
    service = InvestimentoService(async_db)
    investimento = await service.create(InvestimentoSchema(**investimento_teste))
    investimento_id = investimento.investimento.id

    investimento_teste["nome"] = "Nome Alterado"
    investimento_teste["descricao"] = "Nova Descrição"

    investimento_alterado = await service.update(
        investimento_id, InvestimentoSchema(**investimento_teste)
    )
    assert investimento_alterado.investimento.nome == investimento_teste["nome"]
    assert (
        investimento_alterado.investimento.descricao == investimento_teste["descricao"]
    )


@pytest.mark.asyncio
async def test_service_delete(async_db):
    service = InvestimentoService(async_db)
    investimento = await service.create(InvestimentoSchema(**investimento_teste))
    investimento_id = investimento.investimento.id

    investimento_deletado = await service.delete(investimento_id)
    assert investimento_deletado.investimento.id == investimento_id
