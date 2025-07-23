import pytest


investimento_teste = {
    "nome": "Investimento Teste",
    "descricao": None,
    "valor": 100,
    "tipo": "A",
    "data_adquirido": "2025-07-12",
    "conta_id": 1,
}


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_investimentos_all(async_client):
    response = await async_client.get("/investimento/")
    assert response.status_code == 200


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_investimento_by_tipo(async_client):
    response = await async_client.get(
        f"/investimento/tipo/{investimento_teste['tipo']}"
    )
    assert response.status_code == 200
