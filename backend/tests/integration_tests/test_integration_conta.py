import pytest


conta_teste = {"nome": "Conta Teste", "descricao": None}

URL_CONTA = "/contas/"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_create_update_get_delete_conta(async_client):

    response_create_conta = await async_client.post(URL_CONTA, json=conta_teste)
    assert response_create_conta.status_code == 201
    assert response_create_conta.json()["status"] == "Create"
    assert response_create_conta.json()["conta"]["nome"] == conta_teste["nome"]
    conta_id = response_create_conta.json()["conta"]["id"]
    conta_teste["conta_id"] = conta_id

    conta_teste["nome"] = "conta Teste Alterado"
    response_update_conta = await async_client.put(
        f"{URL_CONTA}{conta_id}", json=conta_teste
    )
    assert response_update_conta.status_code == 200
    assert response_update_conta.json()["status"] == "Update"
    assert response_update_conta.json()["conta"]["nome"] == conta_teste["nome"]

    response_get_by_id = await async_client.get(f"{URL_CONTA}id/{conta_id}")
    assert response_get_by_id.status_code == 200
    assert response_get_by_id.json()["nome"] == conta_teste["nome"]

    response_get_by_name = await async_client.get(
        f"{URL_CONTA}name/{conta_teste['nome']}"
    )
    assert response_get_by_name.status_code == 200
    assert response_get_by_name.json()["id"] == conta_id

    response_delete_conta = await async_client.delete(f"{URL_CONTA}{conta_id}")
    assert response_delete_conta.status_code == 200
    assert response_delete_conta.json()["status"] == "Delete"
    assert response_delete_conta.json()["conta"]["nome"] == conta_teste["nome"]
