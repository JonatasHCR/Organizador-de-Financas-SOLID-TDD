import pytest

from app.schema.passivo import PassivoSchema
from app.service.passivo import PassivoService


passivo_teste = {
    "nome": "Passivo Teste",
    "referencia": "Emprestado",
    "descricao": None,
    "valor": 100,
    "data": "2025-07-12",
    "eh_fixo": False,
    "frequencia": None,
    "vencimento": None,
    "conta_id": 1,
}


@pytest.mark.asyncio
async def test_service_create(async_db):
    service = PassivoService(async_db)
    resposta = await service.create(PassivoSchema(**passivo_teste))
    assert resposta.passivo.id is not None


@pytest.mark.asyncio
async def test_service_get_by_id(async_db):
    service = PassivoService(async_db)
    await service.create(PassivoSchema(**passivo_teste))

    passivo = await service.get_by_id(1)
    assert passivo.nome == passivo_teste["nome"]


@pytest.mark.asyncio
async def test_service_get_by_conta(async_db):
    service = PassivoService(async_db)
    await service.create(PassivoSchema(**passivo_teste))

    passivo = await service.get_by_conta_id(passivo_teste["conta_id"])
    assert len(passivo) > 0


@pytest.mark.asyncio
async def test_service_get_by_referencia(async_db):
    service = PassivoService(async_db)
    await service.create(PassivoSchema(**passivo_teste))

    passivo = await service.get_by_referencia(passivo_teste["referencia"])
    assert len(passivo) > 0


@pytest.mark.asyncio
async def test_service_get_by_referencia(async_db):
    service = PassivoService(async_db)
    await service.create(PassivoSchema(**passivo_teste))

    passivo = await service.get_by_referencia(passivo_teste["referencia"])
    assert len(passivo) > 0


@pytest.mark.asyncio
async def test_service_update(async_db):
    service = PassivoService(async_db)
    passivo = await service.create(PassivoSchema(**passivo_teste))
    passivo_id = passivo.passivo.id

    passivo_teste["nome"] = "Nome Alterado"
    passivo_teste["descricao"] = "Nova Descrição"

    passivo_alterado = await service.update(passivo_id, PassivoSchema(**passivo_teste))
    assert passivo_alterado.passivo.nome == passivo_teste["nome"]
    assert passivo_alterado.passivo.descricao == passivo_teste["descricao"]


@pytest.mark.asyncio
async def test_service_delete(async_db):
    service = PassivoService(async_db)
    passivo = await service.create(PassivoSchema(**passivo_teste))
    passivo_id = passivo.passivo.id

    passivo_deletado = await service.delete(passivo_id)
    assert passivo_deletado.passivo.id == passivo_id
