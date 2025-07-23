import pytest

from app.schema.conta import ContaSchema
from app.service.conta import ContaService


conta_teste = {"nome": "Conta Teste", "descricao": None}


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_create(async_db):
    service = ContaService(async_db)
    resposta = await service.create(ContaSchema(**conta_teste))
    assert resposta.conta.id is not None


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_id(async_db):
    service = ContaService(async_db)
    teste_id = await service.create(ContaSchema(**conta_teste))

    conta = await service.get_by_id(teste_id.conta.id)
    assert conta.nome == conta_teste["nome"]


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_nome(async_db):
    service = ContaService(async_db)
    await service.create(ContaSchema(**conta_teste))

    conta = await service.get_by_nome(conta_teste["nome"])
    assert conta.id is not None


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_all(async_db):
    service = ContaService(async_db)
    await service.create(ContaSchema(**conta_teste))

    contas = await service.get_all()
    assert len(contas) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_update(async_db):
    service = ContaService(async_db)
    conta = await service.create(ContaSchema(**conta_teste))
    conta_id = conta.conta.id

    conta_teste["nome"] = "Nome Alterado"
    conta_teste["descricao"] = "Nova Descrição"

    conta_alterado = await service.update(conta_id, ContaSchema(**conta_teste))
    assert conta_alterado.conta.nome == conta_teste["nome"]
    assert conta_alterado.conta.descricao == conta_teste["descricao"]


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_delete(async_db):
    service = ContaService(async_db)
    conta = await service.create(ContaSchema(**conta_teste))
    conta_id = conta.conta.id

    conta_deletado = await service.delete(conta_id)
    assert conta_deletado.conta.id == conta_id
