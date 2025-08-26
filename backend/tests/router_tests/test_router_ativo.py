import pytest


ativo_teste = {
    "nome": "Ativo Teste Rotas",
    "referencia": "Emprestado",
    "descricao": None,
    "valor": 100,
    "data_adquirido": "2025-07-12",
    "eh_fixo": True,
    "tipo_remuneracao": "M",
    "data_finalizado": None,
    "conta_id": 1,
}

URL_ATIVO = "/ativos/"


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_ativos_all(async_client):
    response = await async_client.get(URL_ATIVO)
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_ativo_by_tipo_remuneracao(async_client):
    response = await async_client.get(
        f"{URL_ATIVO}remuneracao/{ativo_teste['tipo_remuneracao']}"
    )
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_ativo_by_referencia(async_client):
    response = await async_client.get(
        f"{URL_ATIVO}referencia/{ativo_teste['referencia']}"
    )
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_ativo_eh_fixo(async_client):
    response = await async_client.get(
        f"{URL_ATIVO}eh/fixo", params={"eh_fixo": ativo_teste["eh_fixo"]}
    )
    assert response.status_code == 200
