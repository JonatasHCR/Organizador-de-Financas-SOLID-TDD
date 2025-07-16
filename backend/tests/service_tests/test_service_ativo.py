import pytest

from app.schema.ativo import AtivoSchema
from app.service.ativo import AtivoService


ativo_teste = {
    "nome": "Ativo Teste",
    "descricao": "Descrição Teste",
    "valor": 100,
    "referente": "Emprestado",
    "data": "2025-07-12",
    "fixo": "N",
    "tipo_remuneracao": None,
    "finalizado": None,
    "id_conta": 1,
}


@pytest.mark.asyncio
async def test_service_create(async_db):
    service = AtivoService(async_db)
    resposta = await service.create(AtivoSchema(**ativo_teste))
    assert resposta.ativo.id is not None


@pytest.mark.asyncio
async def test_service_get_by_id(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativo = await service.get_by_id(1)
    assert ativo.nome == ativo_teste["nome"]


@pytest.mark.asyncio
async def test_service_get_by_conta(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativo = await service.get_by_conta(1)
    assert len(ativo) > 0


@pytest.mark.asyncio
async def test_service_update(async_db):
    service = AtivoService(async_db)
    ativo = await service.create(AtivoSchema(**ativo_teste))
    ativo_id = ativo.ativo.id

    ativo_teste["nome"] = "Nome Alterado"

    ativo_alterado = await service.update(ativo_id, AtivoSchema(**ativo_teste))
    assert ativo_alterado.ativo.nome == ativo_teste["nome"]


@pytest.mark.asyncio
async def test_service_delete(async_db):
    service = AtivoService(async_db)
    ativo = await service.create(AtivoSchema(**ativo_teste))
    ativo_id = ativo.ativo.id

    ativo_deletado = await service.delete(ativo_id)
    assert ativo_deletado.ativo.id == ativo_id
