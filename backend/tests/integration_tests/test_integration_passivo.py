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
conta_teste = {"nome": "Conta Teste", "descricao": None}

URL_PASSIVO = "/passivos/"
URL_CONTA = "/contas/"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_create_update_get_delete_passivo(async_client):

    response_create_conta = await async_client.post(URL_CONTA, json=conta_teste)
    assert response_create_conta.status_code == 201
    assert response_create_conta.json()["status"] == "Create"
    assert response_create_conta.json()["conta"]["nome"] == conta_teste["nome"]
    conta_id = response_create_conta.json()["conta"]["id"]
    passivo_teste["conta_id"] = conta_id

    response_create_passivo = await async_client.post(URL_PASSIVO, json=passivo_teste)
    assert response_create_passivo.status_code == 201
    assert response_create_passivo.json()["status"] == "Create"
    assert response_create_passivo.json()["passivo"]["nome"] == passivo_teste["nome"]
    passivo_id = response_create_passivo.json()["passivo"]["id"]

    passivo_teste["nome"] = "Passivo Teste Alterado"
    response_update_passivo = await async_client.put(
        f"{URL_PASSIVO}{passivo_id}", json=passivo_teste
    )
    assert response_update_passivo.status_code == 200
    assert response_update_passivo.json()["status"] == "Update"
    assert response_update_passivo.json()["passivo"]["nome"] == passivo_teste["nome"]

    response_get_passivo = await async_client.get(f"{URL_PASSIVO}{passivo_id}")
    assert response_get_passivo.status_code == 200
    assert response_get_passivo.json()["nome"] == passivo_teste["nome"]

    response_get_by_conta = await async_client.get(f"{URL_PASSIVO}conta/{conta_id}")
    assert response_get_by_conta.status_code == 200

    response_delete_passivo = await async_client.delete(f"{URL_PASSIVO}{passivo_id}")
    assert response_delete_passivo.status_code == 200
    assert response_delete_passivo.json()["status"] == "Delete"
    assert response_delete_passivo.json()["passivo"]["nome"] == passivo_teste["nome"]

    response_delete_conta = await async_client.delete(f"{URL_CONTA}{conta_id}")
    assert response_delete_conta.status_code == 200
    assert response_delete_conta.json()["status"] == "Delete"
    assert response_delete_conta.json()["conta"]["nome"] == conta_teste["nome"]
