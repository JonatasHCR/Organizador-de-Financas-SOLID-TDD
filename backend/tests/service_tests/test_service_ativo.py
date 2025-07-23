import pytest

from app.schema.ativo import AtivoSchema
from app.service.ativo import AtivoService


ativo_teste = {
    "nome": "Ativo Teste",
    "referencia": "Emprestado",
    "descricao": None,
    "valor": 100,
    "data_adquirido": "2025-07-12",
    "eh_fixo": True,
    "tipo_remuneracao": "M",
    "data_finalizado": None,
    "conta_id": 1,
}


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_create(async_db):
    service = AtivoService(async_db)
    resposta = await service.create(AtivoSchema(**ativo_teste))
    assert resposta.ativo.id is not None


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_id(async_db):
    service = AtivoService(async_db)
    teste_id = await service.create(AtivoSchema(**ativo_teste))

    ativo = await service.get_by_id(teste_id.ativo.id)
    assert ativo.nome == ativo_teste["nome"]


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_conta_id(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativos = await service.get_by_conta_id(ativo_teste["conta_id"])
    assert len(ativos) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_referencia(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativos = await service.get_by_referencia(ativo_teste["referencia"])
    assert len(ativos) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_by_fixo(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativos = await service.get_eh_fixo(ativo_teste["eh_fixo"])
    assert len(ativos) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_tipo_remuneracao(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativos = await service.get_by_tipo_remuneracao(ativo_teste["tipo_remuneracao"])
    assert len(ativos) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_get_all(async_db):
    service = AtivoService(async_db)
    await service.create(AtivoSchema(**ativo_teste))

    ativos = await service.get_all()
    assert len(ativos) > 0


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_update(async_db):
    service = AtivoService(async_db)
    ativo = await service.create(AtivoSchema(**ativo_teste))
    ativo_id = ativo.ativo.id

    ativo_teste["nome"] = "Nome Alterado"
    ativo_teste["descricao"] = "Nova Descrição"

    ativo_alterado = await service.update(ativo_id, AtivoSchema(**ativo_teste))
    assert ativo_alterado.ativo.nome == ativo_teste["nome"]
    assert ativo_alterado.ativo.descricao == ativo_teste["descricao"]


@pytest.mark.asyncio
@pytest.mark.service
async def test_service_delete(async_db):
    service = AtivoService(async_db)
    ativo = await service.create(AtivoSchema(**ativo_teste))
    ativo_id = ativo.ativo.id

    ativo_deletado = await service.delete(ativo_id)
    assert ativo_deletado.ativo.id == ativo_id
