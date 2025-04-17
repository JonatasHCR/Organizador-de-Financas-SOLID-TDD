from datetime import date

from app.models.model_ativo import ModelAtivo
from app.models.model_passivo import ModelPassivo
from app.models.model_investimento import ModelInvestimento


class TestModels:
    def test_model_ativo(self):
        id_teste = 1
        nome_teste = "salario"
        descricao_teste = "teste"
        valor_teste = 50.0
        data_teste = date.today()
        fixo_teste = "N"
        tipo_renumeracao_teste = "M"
        try:
            modelo_teste = ModelAtivo(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                valor=valor_teste,
                data=data_teste,
                fixo=fixo_teste,
                tipo_remuneracao=tipo_renumeracao_teste,
            )
            assert True
        except Exception as error:
            print(error)
            assert False

    def test_model_passivo(self):
        id_teste = 1
        nome_teste = "despesa"
        descricao_teste = "teste"
        valor_teste = 50.0
        data_teste = date.today()
        fixo_teste = "N"
        vencimento_teste = date.today()
        plano_pagamento_teste = "M"
        try:
            modelo_teste = ModelPassivo(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                valor=valor_teste,
                data=data_teste,
                fixo=fixo_teste,
                vencimento=vencimento_teste,
                plano=plano_pagamento_teste,
            )
            assert True
        except Exception as error:
            print(error)
            assert False

    def test_model_investimento(self):
        id_teste = 1
        nome_teste = "despesa"
        descricao_teste = "teste"
        tipo_investimento_teste = "A"
        valor_teste = 50.0
        data_teste = date.today()
        try:
            modelo_teste = ModelInvestimento(
                id=id_teste,
                nome=nome_teste,
                descricao=descricao_teste,
                tipo=tipo_investimento_teste,
                valor=valor_teste,
                data=data_teste,
            )
            assert True
        except Exception as error:
            print(error)
            assert False
