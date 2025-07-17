import pytest

from app.schema.passivo import PassivoSchema
from app.service.passivo import PassivoService


passivo_teste = {
    "nome": "Passivo Teste",
    "descricao": None,
    "valor": 100,
    "referente": "Emprestado",
    "data": "2025-07-12",
    "fixo": "N",
    "vencimento": None,
    "plano": None,
    "id_conta": 1,
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

    passivo = await service.get_by_conta(1)
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
