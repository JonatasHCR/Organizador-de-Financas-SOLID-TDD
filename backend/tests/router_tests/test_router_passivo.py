import pytest


passivo_teste = {
    "nome": "Passivo Teste",
    "referencia": "Emprestado",
    "descricao": None,
    "valor": 100,
    "data": "2025-07-12",
    "eh_fixo": True,
    "frequencia": "M",
    "vencimento": None,
    "conta_id": 1,
}


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_passivos_all(async_client):
    response = await async_client.get("/passivo/")
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_passivo_by_frequencia(async_client):
    response = await async_client.get(
        f"/passivo/frequencia/{passivo_teste['frequencia']}"
    )
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_passivo_by_referencia(async_client):
    response = await async_client.get(
        f"/passivo/referencia/{passivo_teste['referencia']}"
    )
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_passivo_eh_fixo(async_client):
    response = await async_client.get(
        "/passivo/eh/fixo", params={"eh_fixo": passivo_teste["eh_fixo"]}
    )
    assert response.status_code == 200
