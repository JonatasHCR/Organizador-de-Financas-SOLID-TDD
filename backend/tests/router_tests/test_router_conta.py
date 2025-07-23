import pytest


conta_teste = {"nome": "Conta Teste", "descricao": None}


@pytest.mark.asyncio
@pytest.mark.routers
async def test_get_contas_all(async_client):
    response = await async_client.get("/conta/")
    assert response.status_code == 200
