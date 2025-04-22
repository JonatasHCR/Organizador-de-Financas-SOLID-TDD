from sys import path
from os import getenv
from datetime import date

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = getenv("PROJECT_ROOT")
path.insert(0, PROJECT_ROOT)

from app.models.model_passivo import ModelPassivo
import config.config


class TestModelsPassivo:
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
            assert len(modelo_teste.to_list()) == 8
        except Exception as error:
            print("Tipo do erro:", type(error).__name__)
            print("Mensagem:", str(error))
            assert False
