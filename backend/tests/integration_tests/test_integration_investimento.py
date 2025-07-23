import pytest


investimento_teste = {
    "nome": "Investimento Teste",
    "descricao": None,
    "valor": 100,
    "tipo": "A",
    "data_adquirido": "2025-07-12",
    "conta_id": 1,
}
conta_teste = {"nome": "Conta Teste", "descricao": None}


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_create_update_get_delete_investimento(async_client):

    response_create_conta = await async_client.post("/conta/create", json=conta_teste)
    assert response_create_conta.status_code == 201
    assert response_create_conta.json()["status"] == "Create"
    assert response_create_conta.json()["conta"]["nome"] == conta_teste["nome"]
    conta_id = response_create_conta.json()["conta"]["id"]
    investimento_teste["conta_id"] = conta_id

    response_create_investimento = await async_client.post(
        "/investimento/create", json=investimento_teste
    )
    assert response_create_investimento.status_code == 201
    assert response_create_investimento.json()["status"] == "Create"
    assert (
        response_create_investimento.json()["investimento"]["nome"]
        == investimento_teste["nome"]
    )
    investimento_id = response_create_investimento.json()["investimento"]["id"]

    investimento_teste["nome"] = "Investimento Teste Alterado"
    response_update_investimento = await async_client.put(
        f"/investimento/update/{investimento_id}", json=investimento_teste
    )
    assert response_update_investimento.status_code == 200
    assert response_update_investimento.json()["status"] == "Update"
    assert (
        response_update_investimento.json()["investimento"]["nome"]
        == investimento_teste["nome"]
    )

    response_get_investimento = await async_client.get(
        f"/investimento/id/{investimento_id}"
    )
    assert response_get_investimento.status_code == 200
    assert response_get_investimento.json()["nome"] == investimento_teste["nome"]

    response_get_by_conta = await async_client.get(f"/investimento/conta/id/{conta_id}")
    assert response_get_by_conta.status_code == 200

    response_delete_investimento = await async_client.delete(
        f"/investimento/delete/{investimento_id}"
    )
    assert response_delete_investimento.status_code == 200
    assert response_delete_investimento.json()["status"] == "Delete"
    assert (
        response_delete_investimento.json()["investimento"]["nome"]
        == investimento_teste["nome"]
    )

    response_delete_conta = await async_client.delete(f"/conta/delete/{conta_id}")
    assert response_delete_conta.status_code == 200
    assert response_delete_conta.json()["status"] == "Delete"
    assert response_delete_conta.json()["conta"]["nome"] == conta_teste["nome"]
