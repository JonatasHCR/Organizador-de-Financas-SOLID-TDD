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
conta_teste = {"nome": "Conta Teste", "descricao": None}

URL_ATIVO = "/ativos/"
URL_CONTA = "/contas/"


@pytest.mark.asyncio
@pytest.mark.integration
async def test_integration_create_update_get_delete_ativo(async_client):

    response_create_conta = await async_client.post(URL_CONTA, json=conta_teste)
    assert response_create_conta.status_code == 201
    assert response_create_conta.json()["status"] == "Create"
    assert response_create_conta.json()["conta"]["nome"] == conta_teste["nome"]
    conta_id = response_create_conta.json()["conta"]["id"]
    ativo_teste["conta_id"] = conta_id

    response_create_ativo = await async_client.post(URL_ATIVO, json=ativo_teste)
    assert response_create_ativo.status_code == 201
    assert response_create_ativo.json()["status"] == "Create"
    assert response_create_ativo.json()["ativo"]["nome"] == ativo_teste["nome"]
    ativo_id = response_create_ativo.json()["ativo"]["id"]

    ativo_teste["nome"] = "Ativo Teste Alterado"
    response_update_ativo = await async_client.put(
        f"{URL_ATIVO}{ativo_id}", json=ativo_teste
    )
    assert response_update_ativo.status_code == 200
    assert response_update_ativo.json()["status"] == "Update"
    assert response_update_ativo.json()["ativo"]["nome"] == ativo_teste["nome"]

    response_get_ativo = await async_client.get(f"{URL_ATIVO}{ativo_id}")
    assert response_get_ativo.status_code == 200
    assert response_get_ativo.json()["nome"] == ativo_teste["nome"]

    response_get_by_conta = await async_client.get(f"{URL_ATIVO}conta/{conta_id}")
    assert response_get_by_conta.status_code == 200

    response_delete_ativo = await async_client.delete(f"{URL_ATIVO}{ativo_id}")
    assert response_delete_ativo.status_code == 200
    assert response_delete_ativo.json()["status"] == "Delete"
    assert response_delete_ativo.json()["ativo"]["nome"] == ativo_teste["nome"]

    response_delete_conta = await async_client.delete(f"{URL_CONTA}{conta_id}")
    assert response_delete_conta.status_code == 200
    assert response_delete_conta.json()["status"] == "Delete"
    assert response_delete_conta.json()["conta"]["nome"] == conta_teste["nome"]
